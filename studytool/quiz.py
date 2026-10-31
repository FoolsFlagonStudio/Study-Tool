"""Building quizzes: picking topics, seeds and answer formats."""

from __future__ import annotations

import random
from dataclasses import dataclass

from .core.problem import REGISTRY, Problem, make_problem

MODES = ("mixed", "mc", "input")
NEW_TOPIC_WEIGHT = 2.5


@dataclass
class QuizItem:
    problem: Problem
    format: str


def topic_weights(topic_ids: list[str], stats: dict[str, dict]) -> dict[str, float]:
    """Adaptive weighting: topics you miss come up more, new topics get a boost,
    and topics you've mastered still appear now and then so they don't fade."""
    weights = {}
    for topic in topic_ids:
        entry = stats.get(topic)
        if not entry:
            weights[topic] = NEW_TOPIC_WEIGHT
        else:
            weights[topic] = 1 + 3 * (1 - entry["recent_accuracy"])
    return weights


def choose_topics(topic_ids: list[str], count: int, rng: random.Random, weights: dict[str, float] | None) -> list[str]:
    if weights:
        picks = rng.choices(topic_ids, weights=[weights[t] for t in topic_ids], k=count)
    else:
        picks = []
        while len(picks) < count:
            batch = list(topic_ids)
            rng.shuffle(batch)
            picks.extend(batch)
        picks = picks[:count]
    return picks


def choose_format(problem: Problem, mode: str, rng: random.Random) -> str:
    formats = problem.formats()
    if mode in formats:
        return mode
    return rng.choice(formats)


def build_quiz(
    topic_ids: list[str],
    count: int,
    mode: str = "mixed",
    weights: dict[str, float] | None = None,
    rng: random.Random | None = None,
) -> list[QuizItem]:
    rng = rng or random.Random()
    topic_ids = [t for t in topic_ids if t in REGISTRY]
    if not topic_ids:
        return []
    items, seen = [], set()
    for topic in choose_topics(topic_ids, count, rng, weights):
        for _ in range(5):  # avoid repeating the exact same problem in one quiz
            problem = make_problem(topic, rng.randrange(10**9))
            if problem.spec.prompt not in seen:
                break
        seen.add(problem.spec.prompt)
        items.append(QuizItem(problem, choose_format(problem, mode, rng)))
    return items
