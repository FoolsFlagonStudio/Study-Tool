"""Attempt and session history, stored in SQLite.

Every checked answer is logged (with how long it took) so the app can show
progress per topic and steer adaptive quizzes toward weak spots. Every
finished quiz is logged as a session, so practice exams can be compared on
both score and completion time.
"""

from __future__ import annotations

import json
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
    created_at TEXT NOT NULL,
    seconds REAL
);
CREATE INDEX IF NOT EXISTS attempts_topic ON attempts (topic, id);

CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kind TEXT NOT NULL,
    finished_at TEXT NOT NULL,
    question_count INTEGER NOT NULL,
    answered INTEGER NOT NULL,
    correct INTEGER NOT NULL,
    duration_seconds REAL NOT NULL,
    time_limit_seconds REAL,
    timed_out INTEGER NOT NULL DEFAULT 0,
    topics TEXT NOT NULL
);
"""


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class History:
    def __init__(self, path: str | Path):
        if str(path) != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        self._db = sqlite3.connect(str(path), check_same_thread=False)
        self._db.row_factory = sqlite3.Row
        self._lock = threading.Lock()
        with self._lock:
            self._db.executescript(SCHEMA)
            self._migrate()

    def _migrate(self) -> None:
        """Bring databases created by earlier versions up to date."""
        columns = {row["name"] for row in self._db.execute("PRAGMA table_info(attempts)")}
        if "seconds" not in columns:
            self._db.execute("ALTER TABLE attempts ADD COLUMN seconds REAL")
            self._db.commit()

    # ------------------------------------------------------------ attempts

    def record(self, problem_id: str, topic: str, fmt: str, correct: bool, seconds: float | None = None) -> None:
        with self._lock, self._db:
            self._db.execute(
                "INSERT INTO attempts (problem_id, topic, format, correct, created_at, seconds) VALUES (?, ?, ?, ?, ?, ?)",
                (problem_id, topic, fmt, int(correct), _now(), seconds),
            )

    def topic_stats(self) -> dict[str, dict]:
        with self._lock:
            rows = self._db.execute("SELECT topic, format, correct, created_at, seconds FROM attempts ORDER BY id").fetchall()
        stats: dict[str, dict] = {}
        for row in rows:
            entry = stats.setdefault(
                row["topic"], {"attempts": 0, "correct": 0, "recent": [], "times": [], "by_format": {}, "last_seen": None}
            )
            entry["attempts"] += 1
            entry["correct"] += row["correct"]
            entry["recent"] = (entry["recent"] + [row["correct"]])[-RECENT_WINDOW:]
            if row["seconds"] is not None:
                entry["times"] = (entry["times"] + [row["seconds"]])[-RECENT_WINDOW:]
            fmt = entry["by_format"].setdefault(row["format"], {"attempts": 0, "correct": 0})
            fmt["attempts"] += 1
            fmt["correct"] += row["correct"]
            entry["last_seen"] = row["created_at"]
        for entry in stats.values():
            recent = entry.pop("recent")
            times = entry.pop("times")
            entry["accuracy"] = entry["correct"] / entry["attempts"]
            entry["recent_accuracy"] = sum(recent) / len(recent)
            entry["avg_seconds"] = sum(times) / len(times) if times else None
        return stats

    def days_studied(self) -> list[str]:
        with self._lock:
            rows = self._db.execute("SELECT DISTINCT substr(created_at, 1, 10) AS day FROM attempts ORDER BY day").fetchall()
        return [row["day"] for row in rows]

    # ------------------------------------------------------------ sessions

    def record_session(
        self,
        kind: str,
        topics: list[str],
        question_count: int,
        answered: int,
        correct: int,
        duration_seconds: float,
        time_limit_seconds: float | None = None,
        timed_out: bool = False,
    ) -> int:
        with self._lock, self._db:
            cur = self._db.execute(
                """INSERT INTO sessions (kind, finished_at, question_count, answered, correct, duration_seconds,
                   time_limit_seconds, timed_out, topics) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (kind, _now(), question_count, answered, correct, duration_seconds, time_limit_seconds, int(timed_out), json.dumps(topics)),
            )
            return cur.lastrowid

    def sessions(self, kind: str | None = None, limit: int = 30) -> list[dict]:
        query = "SELECT * FROM sessions"
        params: tuple = ()
        if kind:
            query += " WHERE kind = ?"
            params = (kind,)
        query += " ORDER BY id DESC LIMIT ?"
        with self._lock:
            rows = self._db.execute(query, (*params, limit)).fetchall()
        out = []
        for row in rows:
            item = dict(row)
            item["topics"] = json.loads(item["topics"])
            item["timed_out"] = bool(item["timed_out"])
            item["score"] = item["correct"] / item["question_count"] if item["question_count"] else 0
            out.append(item)
        return out

    def reset(self) -> None:
        with self._lock, self._db:
            self._db.execute("DELETE FROM attempts")
            self._db.execute("DELETE FROM sessions")
