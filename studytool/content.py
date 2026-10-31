"""Course outline and lesson content.

Courses live in ``content/<course>/course.json`` with markdown lessons next to
it. The outline maps every topic to the lesson section that teaches it and
(through its id) to the generator that drills it.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from . import generators  # noqa: F401  (registers generators before topics are resolved)
from .core.problem import REGISTRY

CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"
DEFAULT_COURSE = "precalc"


@lru_cache
def load_course(course_id: str = DEFAULT_COURSE) -> dict:
    path = CONTENT_DIR / course_id / "course.json"
    course = json.loads(path.read_text())
    for section in course["sections"]:
        for module in section["modules"]:
            module["section"] = section["id"]
            for topic in module["topics"]:
                generator = REGISTRY.get(topic["id"])
                topic["title"] = topic.get("title") or (generator.title if generator else topic["id"])
                topic["has_generator"] = generator is not None
                topic["module"] = module["id"]
    return course


def modules(course_id: str = DEFAULT_COURSE) -> list[dict]:
    return [m for s in load_course(course_id)["sections"] for m in s["modules"]]


def topics(course_id: str = DEFAULT_COURSE) -> dict[str, dict]:
    return {t["id"]: t for m in modules(course_id) for t in m["topics"]}


def module_markdown(module_id: str, course_id: str = DEFAULT_COURSE) -> str:
    for module in modules(course_id):
        if module["id"] == module_id:
            return (CONTENT_DIR / course_id / module["file"]).read_text()
    raise KeyError(module_id)
