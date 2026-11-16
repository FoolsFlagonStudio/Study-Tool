"""Answer forms added for factoring and vertex form, and ± inside an expression."""

import pytest

from studytool.core.checker import FORMS, parse_expression, parse_numbers, preview


def form_problem(form, text):
    return FORMS[form](text, parse_expression(text))


@pytest.mark.parametrize(
    "form, text, ok",
    [
        ("gcf", "6x^2(3x - 2)", True),
        ("gcf", "-5x(2x + 5)", True),
        ("gcf", "5(x - 1)(x - 3)", True),
        ("gcf", "2x(9x^2 - 6x)", False),  # 3x is still common inside
        ("gcf", "18x^3 - 12x^2", False),  # not factored at all
        ("factored", "4(2x - 3)(2x + 3)", True),
        ("factored", "(x - 3)(x + 3)(x^2 + 9)", True),
        ("factored", "(3y - z)(3y + z)(9y^2 + z^2)", True),
        ("factored", "(4x - 6)(4x + 6)", False),  # each factor still has a 2
        ("factored", "(x^2 - 9)(x^2 + 9)", False),  # x^2 - 9 factors again
        ("vertex", "3(x + 2)^2 - 20", True),
        ("vertex", "-(x - 3)^2 + 5", True),
        ("vertex", "(x + 3/2)^2 - 5/4", True),
        ("vertex", "3x^2 + 12x - 8", False),
        ("vertex", "(2x + 4)^2 - 20", False),
        ("vertex", "3(x + 2)^2 - 12 - 8", False),
    ],
)
def test_forms(form, text, ok):
    assert (form_problem(form, text) is None) == ok


def test_plus_minus_inside_expression():
    values = parse_numbers("(3 ± √57)/8")
    assert len(values) == 2 and abs(float(sum(values)) - 0.75) < 1e-9
    assert len(parse_numbers("x = 2 +- sqrt(5)")) == 2
    assert preview("(3±sqrt(57))/8") == "\\frac{3 \\pm \\sqrt{57}}{8}"
