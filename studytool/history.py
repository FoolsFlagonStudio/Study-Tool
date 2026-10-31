"""Attempt history, stored in SQLite.

Every checked answer is logged so the app can show progress per topic and
steer adaptive quizzes toward weak spots.
"""

from __future__ import annotations

import sqlite3
import threading
from datetime import datetime, timezone
from pathlib import Path

RECENT_WINDOW = 20

SCHEMA = """
CREATE TABLE IF NOT EXISTS attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    problem_id TEXT NOT NULL,
    topic TEXT NOT NULL,
    format TEXT NOT NULL,
    correct INTEGER NOT NULL,
    created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS attempts_topic ON attempts (topic, id);
"""


class History:
    def __init__(self, path: str | Path):
        if str(path) != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        self._db = sqlite3.connect(str(path), check_same_thread=False)
        self._db.row_factory = sqlite3.Row
        self._lock = threading.Lock()
        with self._lock:
            self._db.executescript(SCHEMA)

    def record(self, problem_id: str, topic: str, fmt: str, correct: bool) -> None:
        now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        with self._lock, self._db:
            self._db.execute(
                "INSERT INTO attempts (problem_id, topic, format, correct, created_at) VALUES (?, ?, ?, ?, ?)",
                (problem_id, topic, fmt, int(correct), now),
            )

    def topic_stats(self) -> dict[str, dict]:
        with self._lock:
            rows = self._db.execute("SELECT topic, format, correct, created_at FROM attempts ORDER BY id").fetchall()
        stats: dict[str, dict] = {}
        for row in rows:
            entry = stats.setdefault(row["topic"], {"attempts": 0, "correct": 0, "recent": [], "by_format": {}, "last_seen": None})
            entry["attempts"] += 1
            entry["correct"] += row["correct"]
            entry["recent"] = (entry["recent"] + [row["correct"]])[-RECENT_WINDOW:]
            fmt = entry["by_format"].setdefault(row["format"], {"attempts": 0, "correct": 0})
            fmt["attempts"] += 1
            fmt["correct"] += row["correct"]
            entry["last_seen"] = row["created_at"]
        for entry in stats.values():
            recent = entry.pop("recent")
            entry["accuracy"] = entry["correct"] / entry["attempts"]
            entry["recent_accuracy"] = sum(recent) / len(recent)
        return stats

    def days_studied(self) -> list[str]:
        with self._lock:
            rows = self._db.execute("SELECT DISTINCT substr(created_at, 1, 10) AS day FROM attempts ORDER BY day").fetchall()
        return [row["day"] for row in rows]

    def reset(self) -> None:
        with self._lock, self._db:
            self._db.execute("DELETE FROM attempts")
