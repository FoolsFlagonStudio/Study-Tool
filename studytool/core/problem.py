"""The Problem model and the generator registry.

A generator is a function that takes a seeded ``random.Random`` and returns a
``Spec``. The registry turns that into a ``Problem`` with a stable id of the
form ``"<topic>:<seed>"``. Because generation is deterministic, the server
never has to store a quiz: to check an answer it simply regenerates the
problem from its id.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Any, Callable

KINDS = ("expr", "numbers", "choice")


@dataclass
class Spec:
    """What a generator returns.

    kind:
        ``expr``    - the answer is an algebraic expression (``expected`` is a SymPy expr)
        ``numbers`` - the answer is one or more numbers (``expected`` is a list)
        ``choice``  - multiple choice only (``answer`` is the correct choice text)
    answer:       display text of the correct answer (markdown + $latex$)
    distractors:  display text of wrong answers, ideally built from real mistakes
    form:         extra requirement on typed answers, see ``checker.FORMS``
    choices:      a fixed, ordered list of choices (e.g. Yes / No); the answer
                  must be one of them and distractors are ignored
    """

    prompt: str
    answer: str
    kind: str
    expected: Any = None
    distractors: list[str] = field(default_factory=list)
    explanation: str = ""
    form: str | None = None
    tolerance: float = 0.0
    input_hint: str = ""
    choices: list[str] | None = None
    allow_input: bool = True
    tex_options: dict = field(default_factory=dict)  # passed to sympy.latex for distractors
    ordered: bool = False  # numbers answer is an ordered pair/tuple, e.g. (x, y), not a set


@dataclass
class Problem:
    id: str
    topic: str
    spec: Spec
    choices: list[str]  # final ordered choices for multiple choice ([] if unavailable)

    @property
    def supports_mc(self) -> bool:
        return len(self.choices) >= 2

    @property
    def supports_input(self) -> bool:
        return self.spec.kind != "choice" and self.spec.allow_input

    def formats(self) -> list[str]:
        out = []
        if self.supports_mc:
            out.append("mc")
        if self.supports_input:
            out.append("input")
        return out


@dataclass
class Topic:
    id: str
    title: str
    generator: Callable[[random.Random], Spec]


REGISTRY: dict[str, Topic] = {}


def generator(topic_id: str, title: str):
    """Decorator registering a generator for a topic id."""

    def wrap(fn: Callable[[random.Random], Spec]):
        if topic_id in REGISTRY:
            raise ValueError(f"duplicate generator for topic {topic_id!r}")
        REGISTRY[topic_id] = Topic(topic_id, title, fn)
        return fn

    return wrap


def make_problem(topic_id: str, seed: int) -> Problem:
    from . import checker  # local import avoids a cycle

    topic = REGISTRY[topic_id]
    rng = random.Random(f"{topic_id}:{seed}")
    spec = topic.generator(rng)
    if spec.kind not in KINDS:
        raise ValueError(f"{topic_id}: unknown kind {spec.kind!r}")

    if spec.choices is not None:
        choices = list(spec.choices)
        if spec.answer not in choices:
            raise ValueError(f"{topic_id}: answer {spec.answer!r} not in fixed choices")
    else:
        wrong: list[str] = []
        using_fallbacks = False
        for option in [*spec.distractors, None, *_fallbacks(spec)]:
            if option is None:  # end of the generator's own distractors
                using_fallbacks = True
            elif _finite(option) and not checker.same_answer(spec, option):
                option = display(option, spec.tex_options)
                if option != spec.answer and option not in wrong:
                    wrong.append(option)
            if using_fallbacks and len(wrong) >= 3:
                break
        if len(wrong) >= 3:
            choices = [spec.answer, *rng.sample(wrong, 3)]
            rng.shuffle(choices)
        else:
            choices = []  # not enough distinct distractors: typed answer only

    return Problem(id=f"{topic_id}:{seed}", topic=topic_id, spec=spec, choices=choices)


def _finite(option) -> bool:
    """False for distractors like 1/0 that a generator produced by accident."""
    import sympy as sp

    values = option if isinstance(option, (list, tuple)) else [option]
    return not any(isinstance(v, sp.Basic) and (v.has(sp.zoo, sp.oo, -sp.oo, sp.nan)) for v in values)


def _fallbacks(spec: Spec) -> list:
    """Generic near-misses, used only when a generator's own distractors
    collapse into fewer than three distinct wrong answers."""
    if spec.kind == "expr":
        e = spec.expected
        return [e + 1, e - 1, -e, 2 * e, e + 2]
    if spec.kind == "numbers":
        vals = list(spec.expected)
        kind = tuple if spec.ordered else list
        options = [[v + 1 for v in vals], [v - 1 for v in vals], [-v for v in vals], [v + 2 for v in vals], [2 * v for v in vals]]
        if spec.ordered and len(vals) == 2:
            options = [vals[::-1], [vals[0], -vals[1]], [-vals[0], vals[1]], *options]
        return [kind(o) for o in options]
    return []


def display(option, tex_options: dict | None = None) -> str:
    """Display text for a distractor given as text, a SymPy expression, a list of
    numbers (shown as a set of answers) or a tuple (shown as an ordered pair)."""
    import sympy as sp

    from .symbols import show_numbers, show_pair, tex

    if isinstance(option, sp.Basic):
        return tex(option, **(tex_options or {}))
    if isinstance(option, tuple):
        return show_pair(option)
    if isinstance(option, list):
        return show_numbers(option)
    return str(option)


def parse_problem_id(problem_id: str) -> tuple[str, int]:
    topic_id, _, seed = problem_id.rpartition(":")
    if topic_id not in REGISTRY or not seed.isdigit():
        raise KeyError(problem_id)
    return topic_id, int(seed)


def get_problem(problem_id: str) -> Problem:
    return make_problem(*parse_problem_id(problem_id))
