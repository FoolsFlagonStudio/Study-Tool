"""Every generator, over many seeds: the right answer must be accepted (typed and
multiple choice), wrong choices must be rejected, and generation must be
deterministic so a problem can be rebuilt from its id."""

import pytest

import studytool.generators  # noqa: F401  (registers generators)
from studytool.core.checker import check
from studytool.core.problem import REGISTRY, get_problem, make_problem

SEEDS = range(80)


def typed(problem) -> str:
    spec = problem.spec
    if spec.kind == "numbers":
        return ", ".join(str(val) for val in spec.expected)
    return str(spec.expected)


@pytest.mark.parametrize("topic", sorted(REGISTRY))
def test_generator(topic):
    mc_count = 0
    for seed in SEEDS:
        problem = make_problem(topic, seed)
        spec = problem.spec
        assert problem.formats(), f"{problem.id} has no answer format"
        assert spec.prompt and spec.explanation and spec.answer

        if problem.supports_mc:
            mc_count += 1
            assert problem.choices.count(spec.answer) == 1, problem.id
            assert len(set(problem.choices)) == len(problem.choices), problem.id
            for choice in problem.choices:
                assert check(problem, "mc", choice).correct == (choice == spec.answer)

        if problem.supports_input:
            result = check(problem, "input", typed(problem))
            assert result.correct, f"{problem.id}: typed {typed(problem)!r} rejected ({result.feedback}) | {spec.prompt}"

        again = make_problem(topic, seed)
        assert (again.spec.prompt, again.choices) == (spec.prompt, problem.choices)
        assert get_problem(problem.id).spec.prompt == spec.prompt

    assert mc_count >= len(SEEDS) // 2, f"{topic}: multiple choice available for only {mc_count} seeds"
