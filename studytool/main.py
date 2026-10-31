"""FastAPI app: serves the API and the web frontend.

Run with:  uvicorn studytool.main:app --reload
"""

from __future__ import annotations

import os
import random
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from . import content
from . import generators  # noqa: F401  (registers every generator)
from .core import checker
from .core.problem import Problem, get_problem
from .history import History
from .quiz import MODES, build_quiz, topic_weights

WEB_DIR = Path(__file__).resolve().parent / "web"

app = FastAPI(title="Study Tool", version="0.1.0", description="Generated practice quizzes with notes, by topic.")
history = History(os.environ.get("STUDYTOOL_DB", "data/history.db"))


# ---------------------------------------------------------------- models


class CheckRequest(BaseModel):
    problem_id: str
    format: str = Field(pattern="^(mc|input)$")
    response: str = Field(max_length=300)
    record: bool = True


class PreviewRequest(BaseModel):
    text: str = Field(max_length=300)


def public_problem(problem: Problem, fmt: str) -> dict:
    """What the browser gets - everything except the answer."""
    topics = content.topics()
    return {
        "id": problem.id,
        "topic": problem.topic,
        "topic_title": topics.get(problem.topic, {}).get("title", problem.topic),
        "module": topics.get(problem.topic, {}).get("module"),
        "format": fmt,
        "formats": problem.formats(),
        "prompt": problem.spec.prompt,
        "choices": problem.choices if fmt == "mc" else [],
        "input_hint": problem.spec.input_hint if fmt == "input" else "",
    }


# ---------------------------------------------------------------- routes


@app.get("/api/course")
def course():
    return content.load_course()


@app.get("/api/modules/{module_id}/content", response_class=PlainTextResponse)
def module_content(module_id: str):
    try:
        return content.module_markdown(module_id)
    except KeyError:
        raise HTTPException(404, f"Unknown module {module_id!r}") from None


@app.get("/api/quiz")
def quiz(
    topics: str = Query(..., description="Comma-separated topic ids"),
    count: int = Query(10, ge=1, le=50),
    mode: str = Query("mixed"),
    adaptive: bool = False,
    seed: int | None = None,
):
    if mode not in MODES:
        raise HTTPException(422, f"mode must be one of {MODES}")
    topic_ids = [t for t in topics.split(",") if t]
    unknown = [t for t in topic_ids if t not in content.topics()]
    if unknown:
        raise HTTPException(422, f"Unknown topics: {', '.join(unknown)}")
    weights = topic_weights(topic_ids, history.topic_stats()) if adaptive else None
    items = build_quiz(topic_ids, count, mode, weights, random.Random(seed))
    return {"problems": [public_problem(item.problem, item.format) for item in items]}


@app.post("/api/check")
def check(req: CheckRequest):
    try:
        problem = get_problem(req.problem_id)
    except (KeyError, ValueError):
        raise HTTPException(404, "Unknown problem") from None
    if req.format not in problem.formats():
        raise HTTPException(422, f"This problem doesn't support {req.format!r} answers")
    result = checker.check(problem, req.format, req.response)
    if result.valid and req.record:
        history.record(problem.id, problem.topic, req.format, result.correct)
    return {
        "correct": result.correct,
        "valid": result.valid,
        "feedback": result.feedback,
        "answer": problem.spec.answer if result.valid else None,
        "explanation": problem.spec.explanation if result.valid else None,
    }


@app.post("/api/preview")
def preview(req: PreviewRequest):
    try:
        return {"latex": checker.preview(req.text), "error": None}
    except checker.InputError as err:
        return {"latex": None, "error": str(err)}


@app.get("/api/stats")
def stats():
    per_topic = history.topic_stats()
    topics = content.topics()
    rows = []
    for topic_id, topic in topics.items():
        entry = per_topic.get(topic_id)
        rows.append({"topic": topic_id, "title": topic["title"], "module": topic["module"], **(entry or {"attempts": 0})})
    attempts = sum(e["attempts"] for e in per_topic.values())
    correct = sum(e["correct"] for e in per_topic.values())
    return {
        "topics": rows,
        "attempts": attempts,
        "accuracy": correct / attempts if attempts else None,
        "days_studied": history.days_studied(),
    }


@app.delete("/api/stats")
def reset_stats():
    history.reset()
    return {"ok": True}


app.mount("/", StaticFiles(directory=WEB_DIR, html=True), name="web")
