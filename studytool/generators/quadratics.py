"""Section 2, Module 6 - Quadratic Functions."""

from __future__ import annotations

import math
import random

import sympy as sp

from ..core.problem import Spec, generator
from ..core.symbols import coef_tex, join_terms, nice_number, nonzero, show_numbers, show_pair, x, y
from .functions import YES_NO

PAIR_HINT = "Type the ordered pair, e.g. (2, -3)"
NUMBER_HINT = "Number only, e.g. -4 or 1.5"
DIRECTIONS = ["Opens up", "Opens down"]
EXTREMES = ["Maximum", "Minimum"]
COUNTS = ["None", "One", "Two"]


def quad(a, b, c, var=x):
    return a * var**2 + b * var + c


def qtex(a, b, c, var=x) -> str:
    return sp.latex(sp.expand(quad(a, b, c, var)))


def num(val) -> str:
    return f"${nice_number(val)}$"


def num_options(correct, wrongs) -> list[str]:
    """Display text for single-number distractors, in the same style as the answer
    (terminating decimals, otherwise fractions), skipping repeats of the answer."""
    correct = sp.nsimplify(correct)
    out = []
    for val in wrongs:
        val = sp.nsimplify(val)
        if val != correct and num(val) not in out:
            out.append(num(val))
    return out


def vf_tex(a, h, k) -> str:
    """LaTeX for a(x - h)^2 + k, written the way the course writes vertex form."""
    a, h, k = (sp.nsimplify(v) for v in (a, h, k))
    inner = "x" if h == 0 else sp.latex(x - h)
    body = f"{coef_tex(a)}{inner}^2" if h == 0 else f"{coef_tex(a)}({inner})^2"
    if k > 0:
        body += f" + {sp.latex(k)}"
    elif k < 0:
        body += f" - {sp.latex(-k)}"
    return body


def vf_expr(a, h, k):
    """Vertex form as an unevaluated SymPy expression (so it prints in that form)."""
    square = sp.Pow(x - h, 2, evaluate=False)
    term = square if a == 1 else sp.Mul(a, square, evaluate=False)
    return term if k == 0 else sp.Add(term, k, evaluate=False)


def product(*factors):
    return sp.Mul(*map(sp.sympify, factors), evaluate=False)


def factors_tex(*factors) -> str:
    """'6x^2(3x - 2)' or '(x - 3)(x + 3)': a leading monomial, then each sum in parentheses."""
    out = ""
    for f in map(sp.sympify, factors):
        if f.is_Add:
            out += f"({sp.latex(f)})"
        else:
            out += coef_tex(f) if f.is_Number else sp.latex(f)
    return out


def vertex_of(a, b, c):
    h = sp.Rational(-b, 2 * a)
    return h, quad(a, b, c).subs(x, h)


# ---------------------------------------------------------------- 1. parabola features


@generator("parabola-features", "Parabola features")
def parabola_features(rng: random.Random) -> Spec:
    a = nonzero(rng, -5, 5)
    b, c = rng.randint(-9, 9), nonzero(rng, -12, 12)
    terms = [t for t in (a * x**2, b * x, sp.Integer(c)) if t != 0]
    if rng.random() < 0.3:
        rng.shuffle(terms)
    shown = f"f(x) = {join_terms(terms)}"
    up = a > 0
    variant = rng.choice(["direction", "extreme", "y-intercept", "y-intercept", "match", "match"])

    if variant == "direction":
        return Spec(
            prompt=f"Does the graph of ${shown}$ open upward or downward?",
            answer=DIRECTIONS[0 if up else 1],
            kind="choice",
            choices=DIRECTIONS,
            explanation=f"The coefficient of $x^2$ is $a = {a}$. {'Positive' if up else 'Negative'} $a$ means the parabola opens {'up' if up else 'down'}.",
        )
    if variant == "extreme":
        return Spec(
            prompt=f"Does ${shown}$ have a maximum or a minimum?",
            answer=EXTREMES[1 if up else 0],
            kind="choice",
            choices=EXTREMES,
            explanation=(
                f"$a = {a}$ is {'positive' if up else 'negative'}, so the parabola opens {'up' if up else 'down'} "
                f"and its vertex is the {'lowest' if up else 'highest'} point - a **{'minimum' if up else 'maximum'}**."
            ),
        )
    if variant == "y-intercept":
        return Spec(
            prompt=f"What is the $y$-intercept of ${shown}$?",
            answer=num(c),
            kind="numbers",
            expected=[sp.Integer(c)],
            distractors=num_options(c, [a, b, -c, a + b + c]),
            input_hint="The y-value, e.g. -4",
            explanation=f"Let $x = 0$: every term with an $x$ disappears, leaving $f(0) = {c}$. The $y$-intercept is $(0, {c})$.",
        )

    k = rng.randint(1, 9)
    sign = rng.choice([1, -1])
    choices = [f"$y = x^2 + {k}$", f"$y = -x^2 + {k}$", f"$y = x^2 - {k}$", f"$y = -x^2 - {k}$"]
    answer = f"$y = {'' if up else '-'}x^2 {'+' if sign > 0 else '-'} {k}$"
    return Spec(
        prompt=f"A parabola opens {'upward' if up else 'downward'} and crosses the $y$-axis at $(0, {sign * k})$. Which equation matches?",
        answer=answer,
        kind="choice",
        choices=choices,
        explanation=(
            f"Opens {'up' if up else 'down'}, so the $x^2$ term is {'positive' if up else 'negative'}. "
            f"Letting $x = 0$ must give $y = {sign * k}$, so the constant is ${sign * k}$."
        ),
    )


# ---------------------------------------------------------------- 2. domain and range


def interval_up(k) -> str:
    return f"$[{nice_number(k)}, \\infty)$"


def interval_down(k) -> str:
    return f"$(-\\infty, {nice_number(k)}]$"


@generator("quadratic-domain-range", "Domain and range of quadratics")
def quadratic_domain_range(rng: random.Random) -> Spec:
    a = rng.choice([1, 1, 2, 3, -1, -1, -2, -3, 4, -4])
    h = rng.choice([0, 0, *range(-5, 6)])
    k = rng.randint(-10, 12)
    b, c = -2 * a * h, a * h * h + k
    shown = f"f(x) = {qtex(a, b, c)}"
    up = a > 0
    why_vertex = (
        f"The vertex is at $x = -\\frac{{b}}{{2a}} = {h}$, and $f({h}) = {k}$, so the vertex is $({h}, {k})$."
        if b != 0
        else f"There's no $x$ term, so the vertex is at $x = 0$: $(0, {k})$."
    )
    direction = f"$a = {a}$ is {'positive' if up else 'negative'}, so it opens {'up' if up else 'down'} and ${k}$ is the {'minimum' if up else 'maximum'}."
    variant = rng.choice(["interval", "interval", "inequality", "domain", "value"])

    if variant == "interval":
        right, wrong_dir = (interval_up, interval_down) if up else (interval_down, interval_up)
        open_end = f"$({k}, \\infty)$" if up else f"$(-\\infty, {k})$"
        wrong = [wrong_dir(k), open_end, "$(-\\infty, \\infty)$", right(h), right(-k), wrong_dir(h)]
        return Spec(
            prompt=f"What is the range of ${shown}$ in interval notation?",
            answer=right(k),
            kind="choice",
            distractors=wrong,
            explanation=f"{why_vertex} {direction} The range uses a bracket at ${k}$ because the vertex is on the graph: {right(k)}.",
        )
    if variant == "inequality":
        sym = "\\ge" if up else "\\le"
        flip = "\\le" if up else "\\ge"
        answer = f"$y {sym} {k}$"
        wrong = [f"$y {flip} {k}$", f"$x {sym} {h}$", f"$y {sym} {h}$", f"$y {sym} {-k}$", "$\\mathbb{R}$", f"$x {sym} {k}$"]
        return Spec(
            prompt=f"Give the range of ${shown}$ algebraically. ($\\mathbb{{R}}$ means all real numbers.)",
            answer=answer,
            kind="choice",
            distractors=wrong,
            explanation=f"{why_vertex} {direction} So $y$ can be ${k}$ or anything {'above' if up else 'below'} it: {answer}.",
        )
    if variant == "domain":
        return Spec(
            prompt=f"What is the domain of ${shown}$?",
            answer="$(-\\infty, \\infty)$",
            kind="choice",
            distractors=[interval_up(k), interval_down(k), interval_up(h), f"$(-\\infty, {h}]$", f"$[{-abs(k) - 1}, {abs(k) + 1}]$"],
            explanation="Any real number can be squared, multiplied, and added, so every $x$ works. The domain of every quadratic is all real numbers, $(-\\infty, \\infty)$. (It's the **range** that depends on the vertex.)",
        )
    return Spec(
        prompt=f"What is the {'minimum' if up else 'maximum'} value of ${shown}$?",
        answer=num(k),
        kind="numbers",
        expected=[sp.Integer(k)],
        distractors=num_options(k, [h, -k, c, -h]),
        input_hint=NUMBER_HINT,
        explanation=f"{why_vertex} The {'minimum' if up else 'maximum'} value is the vertex's $y$-coordinate, ${k}$ - not its $x$-coordinate.",
    )


# ---------------------------------------------------------------- 3. GCF


def _primitive_inner(rng: random.Random):
    """A polynomial in x with a constant term (so no x is common) and no common number."""
    while True:
        degree = rng.choice([1, 1, 2, 2])
        coeffs = [rng.randint(1, 9)] + [rng.randint(-9, 9) for _ in range(degree - 1)] + [nonzero(rng, -9, 9)]
        inner = sum(co * x ** (degree - i) for i, co in enumerate(coeffs))
        if math.gcd(*coeffs) == 1 and len(sp.Add.make_args(inner)) >= 2:
            return inner


@generator("gcf-factoring", "Factoring out the GCF")
def gcf_factoring(rng: random.Random) -> Spec:
    n = rng.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
    m = rng.choice([0, 1, 1, 2])
    gcf = n * x**m * (-1 if rng.random() < 0.2 else 1)
    inner = _primitive_inner(rng)
    whole = sp.expand(gcf * inner)
    terms = sp.Add.make_args(inner)

    if rng.random() < 0.3:
        wrong = [n, n * x ** (m + 1), sp.Rational(n, min(p for p in range(2, n + 1) if n % p == 0)) * x**m, n * x ** max(m - 1, 0), 2 * x**m]
        wrong = [w for w in wrong if w != gcf and w != -gcf]
        return Spec(
            prompt=f"What is the greatest common factor of ${sp.latex(whole)}$?",
            answer=f"${sp.latex(abs(gcf.as_coeff_Mul()[0]) * gcf.as_coeff_Mul()[1])}$",
            kind="expr",
            expected=abs(gcf.as_coeff_Mul()[0]) * gcf.as_coeff_Mul()[1],
            distractors=wrong,
            input_hint="e.g. 4x or 8",
            form="monomial",
            explanation=(
                f"The largest number dividing every coefficient is ${n}$. "
                + (f"Every term has at least $x^{{{m}}}$, " if m > 1 else "Every term has at least one $x$, " if m == 1 else "Not every term has an $x$, ")
                + f"so the GCF is ${sp.latex(n * x**m)}$."
            ),
        )

    answer = factors_tex(gcf, inner)
    wrong = []
    for p in (2, 3, 5, 7):
        if n % p == 0 and n != p:
            wrong.append(factors_tex(gcf / p, sp.expand(p * inner)))
            break
    if m:
        wrong.append(factors_tex(gcf / x, sp.expand(x * inner)))
    const = terms[0] if terms[0].is_Number else [t for t in terms if t.is_Number][0]
    wrong.append(factors_tex(gcf, sp.expand(inner - const + const * n)))  # forgot to divide the constant
    lead = sp.LT(inner, x)
    wrong.append(factors_tex(gcf, sp.expand(inner - lead + lead * x)))  # exponent slip on the first term
    wrong.append(factors_tex(gcf, sp.expand(2 * lead - inner)))  # sign slip on the rest
    wrong = [w for w in wrong if w != answer]
    return Spec(
        prompt=f"Factor out the greatest common factor: ${sp.latex(whole)}$",
        answer=f"${answer}$",
        kind="expr",
        expected=product(gcf, inner),
        distractors=[f"${w}$" for w in wrong],
        input_hint="e.g. 4x(5x + 4)",
        form="gcf",
        explanation=(
            f"The GCF is ${sp.latex(gcf)}$ (largest number ${n}$"
            + (f", smallest power of $x$: ${sp.latex(x**m)}$" if m else ", and not every term has an $x$")
            + f"). Divide each term by it: ${answer}$. Check by distributing back."
        ),
    )


# ---------------------------------------------------------------- 4. difference of squares


def _coprime_pair(rng: random.Random, hi_p: int, hi_q: int):
    while True:
        p, q = rng.randint(1, hi_p), rng.randint(1, hi_q)
        if math.gcd(p, q) == 1 and (p, q) != (1, 1):
            return p, q


@generator("difference-of-squares", "Difference of squares")
def difference_of_squares(rng: random.Random) -> Spec:
    var = rng.choice([x, x, x, y])
    variant = rng.choice(["basic", "basic", "gcf", "fourth", "check"])

    if variant == "check":
        p, q = _coprime_pair(rng, 9, 11)
        kind = rng.choice(["yes", "sum", "not-square", "not-square-const"])
        if kind == "yes":
            shown, ok, why = f"{p * p}{sp.latex(var)}^2 - {q * q}", "Yes", f"$({p if p > 1 else ''}{sp.latex(var)})^2 - {q}^2$: both are perfect squares and they're subtracted."
        elif kind == "sum":
            shown, ok, why = f"{p * p if p > 1 else ''}{sp.latex(var)}^2 + {q * q}", "No", "It's a **sum** of squares. Only a difference $a^2 - b^2$ factors this way."
        elif kind == "not-square":
            co = rng.choice([2, 3, 5, 6, 7, 8, 10, 12, 14, 15, 18, 20])
            shown, ok, why = f"{co}{sp.latex(var)}^2 - {q * q}", "No", f"${co}$ isn't a perfect square, so ${co}{sp.latex(var)}^2$ isn't one either."
        else:
            co = rng.choice([2, 3, 5, 7, 8, 10, 11, 12, 15, 17])
            shown, ok, why = f"{p * p if p > 1 else ''}{sp.latex(var)}^2 - {co}", "No", f"${co}$ isn't a perfect square."
        return Spec(
            prompt=f"Can ${shown}$ be factored as a difference of perfect squares?",
            answer=ok,
            kind="choice",
            choices=YES_NO,
            explanation=why,
        )

    if variant == "fourth":
        p, q = _coprime_pair(rng, 3, 3)
        whole = p**4 * var**4 - q**4
        factors = (p * var - q, p * var + q, p * p * var**2 + q * q)
        why = (
            f"$({sp.latex(p * p * var**2)})^2 - ({q * q})^2 = ({sp.latex(p * p * var**2 - q * q)})({sp.latex(p * p * var**2 + q * q)})$. "
            f"The first factor is **another** difference of squares: $({sp.latex(p * var - q)})({sp.latex(p * var + q)})$. "
            f"The sum ${sp.latex(p * p * var**2 + q * q)}$ doesn't factor."
        )
        wrong = [
            factors_tex(p * p * var**2 - q * q, p * p * var**2 + q * q),
            factors_tex(p * var - q, p * var + q, p * p * var**2 - q * q),
            f"({sp.latex(p * var - q)})^2({sp.latex(p * var + q)})^2",
            factors_tex(p * var - q, p * var + q) + f"({sp.latex(p * var + q)})^2",
        ]
    else:
        p, q = _coprime_pair(rng, 9, 11)
        g = rng.randint(2, 6) if variant == "gcf" else 1
        whole = sp.expand(g * (p * p * var**2 - q * q))
        factors = ((g,) if g > 1 else ()) + (p * var - q, p * var + q)
        sq = f"({sp.latex(p * var)})^2 - {q}^2"
        why = (f"Take out the GCF first: ${g}({sp.latex(p * p * var**2 - q * q)})$. Then " if g > 1 else "") + (
            f"${sp.latex(p * p * var**2 - q * q)} = {sq}$, so $a = {sp.latex(p * var)}$ and $b = {q}$: "
            f"$(a - b)(a + b) = {factors_tex(p * var - q, p * var + q)}$."
        )
        rest = ((g,) if g > 1 else ())
        wrong = [
            factors_tex(*rest) + f"({sp.latex(p * var - q)})^2",
            factors_tex(*rest) + f"({sp.latex(p * var + q)})^2",
            factors_tex(*rest, p * var - q * q, p * var + q * q),
            factors_tex(*rest, p * p * var - q, p * p * var + q),
        ]
        if g > 1:
            wrong.append(factors_tex(p * var - q, p * var + q))
        if p > 1:
            wrong.append(factors_tex(*rest, var - q, var + q))

    answer = factors_tex(*factors)
    wrong = [w for w in dict.fromkeys(wrong) if w != answer]
    return Spec(
        prompt=f"Factor completely: ${sp.latex(whole)}$",
        answer=f"${answer}$",
        kind="expr",
        expected=product(*factors),
        distractors=[f"${w}$" for w in wrong],
        input_hint="e.g. (5x - 7)(5x + 7)",
        form="factored",
        explanation=why + f" Answer: ${answer}$.",
    )


# ---------------------------------------------------------------- 5. grouping


@generator("factoring-by-grouping", "Factoring by grouping")
def factoring_by_grouping(rng: random.Random) -> Spec:
    while True:
        p, q = rng.choice([1, 1, 2, 3, 5]), nonzero(rng, -9, 9)
        r, s = rng.choice([1, 1, 2, 3, 4]), nonzero(rng, -8, 8)
        left, right = r * x + s, p * x**2 + q
        if math.gcd(p, q) == 1 and math.gcd(r, s) == 1 and len(sp.factor_list(right)[1]) == 1:
            break
    g = rng.choice([2, 3]) if rng.random() < 0.15 else 1
    whole = sp.expand(g * left * right)
    pr, ps, qr, qs = p * r, p * s, q * r, q * s
    inner = sp.expand(left * right)
    why = (f"Every term shares ${g}$, so take it out first: ${g}({sp.latex(inner)})$. " if g > 1 else "") + (
        f"Group the first two terms: ${sp.latex(pr * x**3 + ps * x**2)} = {factors_tex(p * x**2, left)}$. "
        f"Group the last two: ${join_terms([qr * x, sp.Integer(qs)])} = {factors_tex(q, left)}$"
        + (" (take out a negative so the binomials match)" if q < 0 else "")
        + f". Both contain $({sp.latex(left)})$, so factor it out."
    )
    rest = (g,) if g > 1 else ()
    answer = factors_tex(*rest, left, right)
    wrong = [
        factors_tex(*rest, left, p * x**2 - q),
        factors_tex(*rest, r * x - s, right),
        factors_tex(*rest, r * x - s, p * x**2 - q),
        factors_tex(*rest, p * x + s, r * x**2 + q),
        factors_tex(*rest, left, p * x + q),
    ]
    if g > 1:
        wrong.append(factors_tex(left, right))
    wrong = [w for w in dict.fromkeys(wrong) if w != answer]
    return Spec(
        prompt=f"Factor by grouping: ${sp.latex(whole)}$",
        answer=f"${answer}$",
        kind="expr",
        expected=product(*rest, left, right),
        distractors=[f"${w}$" for w in wrong],
        input_hint="e.g. (x - 5)(x^2 + 3)",
        form="factored",
        explanation=why + f" Answer: ${answer}$.",
    )


# ---------------------------------------------------------------- 6. graphing with a table


@generator("graphing-quadratics", "Tables of values for quadratics")
def graphing_quadratics(rng: random.Random) -> Spec:
    a = rng.choice([1, 1, 1, -1, -1, 2, -2])
    b, c = rng.randint(-6, 6), rng.randint(-9, 9)
    f = quad(a, b, c)
    start = rng.randint(-3, 0)
    xs = list(range(start, start + 4))
    hidden = rng.choice([v for v in xs if v < 0] or xs)
    val = f.subs(x, hidden)
    row = " | ".join("?" if v == hidden else f"${f.subs(x, v)}$" for v in xs)
    table = "| $x$ | " + " | ".join(f"${v}$" for v in xs) + " |\n|---|" + "---|" * len(xs) + f"\n| $y$ | {row} |"
    wrong = [
        a * -(hidden**2) + b * hidden + c,  # (-3)^2 treated as -9
        a * hidden**2 - b * hidden + c,  # sign slip on bx
        -a * hidden**2 + b * hidden + c,  # -x^2 squared to a positive
        hidden**2 + b * hidden + c,  # dropped a
        a * (2 * hidden) + b * hidden + c,  # squared as doubling
    ]
    first = f"{a}({hidden})^2" if a not in (1, -1) else ("-" if a == -1 else "") + f"({hidden})^2"
    return Spec(
        prompt=f"Complete the table for $y = {qtex(a, b, c)}$. What is the missing $y$-value?\n\n{table}",
        answer=num(val),
        kind="numbers",
        expected=[val],
        distractors=num_options(val, wrong),
        input_hint=NUMBER_HINT,
        explanation=(
            f"Substitute $x = {hidden}$" + (", with the negative in parentheses" if hidden < 0 else "") + f": $y = {first}"
            + (f" {'+' if b > 0 else '-'} {abs(b)}({hidden})" if b else "")
            + (f" {'+' if c > 0 else '-'} {abs(c)}" if c else "")
            + f" = {val}$. Square first: $({hidden})^2 = {hidden**2}$."
        ),
    )


# ---------------------------------------------------------------- 7. vertex and axis of symmetry


@generator("vertex-and-axis", "Vertex and axis of symmetry")
def vertex_and_axis(rng: random.Random) -> Spec:
    a = rng.choice([1, 1, 2, 2, 3, 4, 5, -1, -1, -2, -3, -4, -6])
    if rng.random() < 0.6:
        h = rng.randint(-5, 5)
        b = -2 * a * h
    else:
        a = rng.choice([1, 1, -1, 2, -2, 3, 4])
        b = nonzero(rng, -12, 12)
    c = rng.randint(-12, 15)
    h, k = vertex_of(a, b, c)
    shown = f"f(x) = {qtex(a, b, c)}"
    up = a > 0
    find_x = f"$x = -\\frac{{b}}{{2a}} = -\\frac{{{b}}}{{2({a})}} = {sp.latex(h)}$"
    find_y = f"$f\\left({sp.latex(h)}\\right) = {sp.latex(k)}$"
    variant = rng.choice(["vertex", "vertex", "axis", "value"])

    if variant == "axis":
        return Spec(
            prompt=f"What is the axis of symmetry of ${shown}$? Give the value of $x$.",
            answer=num(h),
            kind="numbers",
            expected=[h],
            distractors=num_options(h, [-h, sp.Rational(-b, a), sp.Rational(b, a), k, 2 * h]),
            input_hint="The x-value, e.g. -2 or 0.5",
            explanation=f"With $a = {a}$ and $b = {b}$: {find_x}. The axis of symmetry is the vertical line $x = {sp.latex(h)}$.",
        )
    if variant == "value":
        return Spec(
            prompt=f"What is the {'minimum' if up else 'maximum'} value of ${shown}$?",
            answer=num(k),
            kind="numbers",
            expected=[k],
            distractors=num_options(k, [h, -k, c, quad(a, b, c).subs(x, -h)]),
            input_hint=NUMBER_HINT,
            explanation=f"{find_x}, then {find_y}. The {'min' if up else 'max'} **value** is the $y$-coordinate, ${sp.latex(k)}$ ($a {'>' if up else '<'} 0$, so it's a {'minimum' if up else 'maximum'}).",
        )
    return Spec(
        prompt=f"Find the vertex of ${shown}$.",
        answer=show_pair((h, k)),
        kind="numbers",
        expected=(h, k),
        ordered=True,
        distractors=[(-h, quad(a, b, c).subs(x, -h)), (h, -k), (k, h), (sp.Rational(-b, a), quad(a, b, c).subs(x, sp.Rational(-b, a)))],
        input_hint=PAIR_HINT + " - decimals or fractions are fine",
        explanation=f"{find_x}. Substitute it back in: {find_y}. The vertex is {show_pair((h, k))}.",
    )


# ---------------------------------------------------------------- 8. vertex form


@generator("vertex-form", "Vertex form")
def vertex_form(rng: random.Random) -> Spec:
    a = rng.choice([1, 1, 2, 3, 5, -1, -1, -2, -3])
    h = nonzero(rng, -8, 8)
    variant = rng.choice(["vertex", "vertex", "y-intercept", "x-intercepts", "x-intercepts", "count"])
    if variant == "x-intercepts":
        r = rng.randint(1, 5)
        k = -a * r * r
    else:
        k = rng.randint(-20, 20)
    shown = f"f(x) = {vf_tex(a, h, k)}"
    read = f"Compare with $a(x - h)^2 + k$: $({sp.latex(x - h)})$ means $h = {h}$, and $k = {k}$."

    if variant == "vertex":
        return Spec(
            prompt=f"What is the vertex of ${shown}$?",
            answer=show_pair((h, k)),
            kind="numbers",
            expected=(sp.Integer(h), sp.Integer(k)),
            ordered=True,
            distractors=[(-h, k), (h, -k), (-h, -k), (k, h)],
            input_hint=PAIR_HINT,
            explanation=f"{read} The vertex is $(h, k) = ({h}, {k})$. Watch the sign: the form has $x - h$.",
        )
    if variant == "y-intercept":
        val = a * h * h + k
        return Spec(
            prompt=f"What is the $y$-intercept of ${shown}$?",
            answer=num(val),
            kind="numbers",
            expected=[sp.Integer(val)],
            distractors=num_options(val, [k, -a * h + k, (a * h) ** 2 + k, h * h + k, a * h * h - k]),
            input_hint="The y-value, e.g. 75",
            explanation=f"Let $x = 0$: $f(0) = {coef_tex(a)}({-h})^2 {'+' if k >= 0 else '-'} {abs(k)} = {a}({h * h}) {'+' if k >= 0 else '-'} {abs(k)} = {val}$.",
        )
    if variant == "count":
        count = "One" if k == 0 else ("None" if (a > 0) == (k > 0) else "Two")
        where = "on" if k == 0 else ("above" if k > 0 else "below")
        return Spec(
            prompt=f"How many $x$-intercepts does ${shown}$ have?",
            answer=count,
            kind="choice",
            choices=COUNTS,
            explanation=(
                f"The vertex $({h}, {k})$ is {where} the $x$-axis and the parabola opens {'up' if a > 0 else 'down'}. "
                + {
                    "One": "The vertex touches the axis, so there's exactly one.",
                    "None": f"Setting $f(x) = 0$ gives $(x {'-' if h > 0 else '+'} {abs(h)})^2 = {sp.latex(sp.Rational(-k, a))}$ - a square can't be negative, so it never crosses.",
                    "Two": f"It heads toward the axis and crosses it twice: $(x {'-' if h > 0 else '+'} {abs(h)})^2 = {sp.latex(sp.Rational(-k, a))}$ has two solutions.",
                }[count]
            ),
        )
    r = int(math.isqrt(-k // a))
    roots = [sp.Integer(h - r), sp.Integer(h + r)]
    return Spec(
        prompt=f"Find the $x$-intercepts of ${shown}$.",
        answer=show_numbers(roots),
        kind="numbers",
        expected=roots,
        distractors=[[-h - r, -h + r], [h - r * r, h + r * r], [h + r], [h - k, h + k] if abs(k) != r else [h - 2 * r, h + 2 * r]],
        input_hint="Both x-values, e.g. 3, 7",
        explanation=(
            f"Set $f(x) = 0$: " + (f"${vf_tex(a, h, 0)} = {-k}$, so " if a != 1 else "")
            + f"$({sp.latex(x - h)})^2 = {r * r}$. "
            f"Square root both sides **with** $\\pm$: $x {'-' if h > 0 else '+'} {abs(h)} = \\pm {r}$, so $x = {h - r}$ or $x = {h + r}$."
        ),
    )


# ---------------------------------------------------------------- 9. completing the square


@generator("completing-the-square", "Completing the square")
def completing_the_square(rng: random.Random) -> Spec:
    if rng.random() < 0.25:
        b = nonzero(rng, -14, 14)
        add = sp.Rational(b, 2) ** 2
        c = rng.randint(-15, 15)
        return Spec(
            prompt=f"To complete the square for $f(x) = {qtex(1, b, c)}$, what number do you add and subtract?",
            answer=num(add),
            kind="numbers",
            expected=[add],
            distractors=num_options(add, [sp.Rational(b, 2), b * b, 2 * b, sp.Rational(b * b, 2), abs(b)]),
            input_hint=NUMBER_HINT,
            explanation=f"Half of ${b}$ is ${sp.latex(sp.Rational(b, 2))}$, and squaring it gives ${sp.latex(add)}$.",
        )

    if rng.random() < 0.6:
        a = 1
        h = sp.Rational(nonzero(rng, -13, 13), 2) if rng.random() < 0.3 else sp.Integer(nonzero(rng, -7, 7))
    else:
        a = rng.choice([2, 3, 4, 5, -1, -2, -3, -5])
        h = sp.Integer(nonzero(rng, -5, 5))
    b = -2 * a * h
    c = rng.randint(-15, 20)
    k = c - a * h * h
    half = -h
    answer = vf_tex(a, h, k)
    if a == 1:
        why = (
            f"Half of ${sp.latex(b)}$ is ${sp.latex(half)}$, and $({sp.latex(half)})^2 = {sp.latex(h * h)}$. "
            f"Add and subtract it: $f(x) = (x^2 {'+' if b > 0 else '-'} {sp.latex(abs(b))}x + {sp.latex(h * h)}) - {sp.latex(h * h)} {'+' if c >= 0 else '-'} {abs(c)}$. "
            f"Factor the perfect square and combine: ${answer}$."
        )
    else:
        inner_b = b / a
        why = (
            f"Factor ${a}$ out of the first two terms: $f(x) = {a}(x^2 {'+' if inner_b > 0 else '-'} {sp.latex(abs(inner_b))}x) {'+' if c >= 0 else '-'} {abs(c)}$. "
            f"Half of ${sp.latex(inner_b)}$ is ${sp.latex(half)}$; squared, ${sp.latex(h * h)}$. "
            f"$f(x) = {a}[({sp.latex(x - h)})^2 - {sp.latex(h * h)}] {'+' if c >= 0 else '-'} {abs(c)}$. "
            f"Distribute the ${a}$ to the ${-h * h}$ - it becomes ${-a * h * h}$ - and combine: ${answer}$."
        )
    wrong = [vf_tex(a, -h, k), vf_tex(a, h, c - h * h), vf_tex(a, h, c + a * h * h), vf_tex(a, h, -k), vf_tex(a, h / 2, c - a * h * h / 4)]
    wrong = [w for w in dict.fromkeys(wrong) if w != answer]
    return Spec(
        prompt=f"Write $f(x) = {qtex(a, b, c)}$ in vertex form by completing the square.",
        answer=f"$f(x) = {answer}$",
        kind="expr",
        expected=vf_expr(a, h, k),
        distractors=[f"$f(x) = {w}$" for w in wrong],
        input_hint="e.g. 3(x + 2)^2 - 20",
        form="vertex",
        explanation=why + f" The vertex is {show_pair((h, k))}.",
    )


# ---------------------------------------------------------------- 10. quadratic formula


def roots_tex(nb, disc, den) -> tuple[str, bool] | None:
    """Display text for x = (nb ± sqrt(disc)) / den, fully simplified. Returns
    (text, rational?) or None if there are no real roots."""
    if disc < 0 or den == 0:
        return None
    root = sp.sqrt(disc)
    if root.is_Rational:
        vals = [sp.Rational(nb, den) + root / den, sp.Rational(nb, den) - root / den]
        return show_numbers(vals), True
    m, rest = root.as_coeff_Mul()
    m, n = int(m), int(rest**2)
    g = math.gcd(math.gcd(int(nb), m), int(den))
    nb, m, den = nb // g, m // g, den // g
    if den < 0:
        nb, den = -nb, -den
    rad = f"{m if m != 1 else ''}\\sqrt{{{n}}}"
    top = f"{nb} \\pm {rad}" if nb else f"\\pm {rad}"
    return (f"$x = {top}$" if den == 1 else f"$x = \\frac{{{top}}}{{{den}}}$"), False


@generator("quadratic-formula", "The quadratic formula")
def quadratic_formula(rng: random.Random) -> Spec:
    if rng.random() < 0.45:
        while True:
            p, r = rng.randint(1, 3), rng.randint(1, 3)
            q, s = rng.randint(-6, 6), rng.randint(-6, 6)
            a, b, c = p * r, -(p * s + q * r), q * s
            g = math.gcd(math.gcd(a, b), c) or 1
            a, b, c = a // g, b // g, c // g
            if c != 0 and b * b - 4 * a * c > 0:
                break
    else:
        while True:
            a, b, c = rng.randint(1, 6), rng.randint(-9, 9), nonzero(rng, -9, 9)
            disc = b * b - 4 * a * c
            if disc > 0 and not sp.sqrt(disc).is_Rational and math.gcd(math.gcd(a, b), c) == 1:
                break
    disc = b * b - 4 * a * c

    style = rng.choice(["standard", "standard", "move-c", "move-bx", "distribute"])
    if style == "move-c":
        shown = f"{sp.latex(a * x**2 + b * x)} = {-c}" if b else f"{sp.latex(a * x**2)} = {-c}"
    elif style == "move-bx" and b:
        shown = f"{sp.latex(a * x**2)} = {sp.latex(-b * x - c)}"
    elif style == "distribute" and b and a == 1:
        shown = f"x({sp.latex(x + b)}) = {-c}"
    else:
        style, shown = "standard", f"{qtex(a, b, c)} = 0"
    rewrite = "" if style == "standard" else f"Rewrite with 0 on one side: ${qtex(a, b, c)} = 0$. "

    if style != "standard" and rng.random() < 0.35:
        return Spec(
            prompt=f"To use the quadratic formula on ${shown}$, write it as $ax^2 + bx + c = 0$ with $a > 0$. What are $a$, $b$, and $c$?",
            answer=show_pair((a, b, c)),
            kind="numbers",
            expected=(sp.Integer(a), sp.Integer(b), sp.Integer(c)),
            ordered=True,
            distractors=[(a, -b, c), (a, b, -c), (a, -b, -c), (b, a, c)],
            input_hint="a, b, c - e.g. 2, -7, 5",
            explanation=rewrite + f"So $a = {a}$, $b = {b}$, $c = {c}$. Moving a term across the equals sign flips its sign.",
        )

    answer, rational = roots_tex(-b, disc, 2 * a)
    root = sp.sqrt(disc)
    vals = [(-b + root) / (2 * a), (-b - root) / (2 * a)]
    candidates = [
        (b, disc, 2 * a),  # forgot the minus in -b
        (-b, b * b + 4 * a * c, 2 * a),  # sign slip in -4ac
        (-b, disc, a),  # divided by a instead of 2a
        (-b, b * b - 2 * a * c, 2 * a),  # 2ac instead of 4ac
        (b, b * b + 4 * a * c, 2 * a),
        (-b, disc, 2),  # forgot the a in 2a
        (-b, disc, 4 * a),
    ]
    wrong = []
    for cand in candidates:
        shown_roots = roots_tex(*cand)
        if shown_roots and shown_roots[1] == rational and shown_roots[0] != answer and shown_roots[0] not in wrong:
            wrong.append(shown_roots[0])
    return Spec(
        prompt=f"Use the quadratic formula to solve ${shown}$.",
        answer=answer,
        kind="numbers",
        expected=vals,
        distractors=wrong,
        input_hint="e.g. (3 ± sqrt(57))/8, or 1, -1/3",
        explanation=(
            rewrite
            + f"$a = {a}$, $b = {b}$, $c = {c}$. "
            + f"$b^2 - 4ac = ({b})^2 - 4({a})({c}) = {disc}$. "
            + f"$x = \\frac{{-({b}) \\pm \\sqrt{{{disc}}}}}{{2({a})}}$, which simplifies to "
            + answer.replace("$x = ", "$")
            + "."
        ),
    )


# ---------------------------------------------------------------- 11. height functions

FEET_STORIES = [
    "A ball is thrown straight up at {v} feet per second {start}.",
    "A model rocket is launched straight up at {v} feet per second {start}.",
    "A kicker sends a football straight up at {v} feet per second {start}.",
    "A juggler tosses a pin straight up at {v} feet per second {start}.",
]
METER_STORIES = [
    "A ball is thrown straight up at {v} meters per second {start}.",
    "A rocket is launched vertically at {v} meters per second {start}.",
    "A diver jumps up at {v} meters per second {start}.",
    "A basketball is launched straight up at {v} meters per second {start}.",
]


@generator("height-functions", "Projectile height problems")
def height_functions(rng: random.Random) -> Spec:
    if rng.random() < 0.5:
        g, unit, other_g = 16, "feet", 5
        v0 = rng.choice([32, 48, 64, 80, 96, 112, 128, 144, 160])
        h0 = sp.Integer(rng.choice([0, 4, 5, 6, 20, 25, 30, 48, 64, 80, 96, 128, 144, -16]))
        story = rng.choice(FEET_STORIES)
    else:
        g, unit, other_g = 5, "meters", 16
        v0 = rng.choice([10, 15, 20, 25, 30, 40, 50, 60, 230])
        h0 = rng.choice([sp.Integer(0), sp.Rational(3, 2), sp.Integer(2), sp.Integer(5), sp.Integer(10), sp.Integer(20), sp.Integer(30), sp.Integer(-20)])
        story = rng.choice(METER_STORIES)
    one = "foot" if unit == "feet" else "meter"
    start = "from the ground" if h0 == 0 else (
        f"from the bottom of a {nice_number(-h0)}-{one} pit" if h0 < 0 else
        f"from {nice_number(h0)} {unit} above the ground" if h0 < 10 else f"from the top of a {nice_number(h0)}-{one} building"
    )
    text = story.format(v=v0, start=start)
    T = sp.Rational(v0, 2 * g)
    H = -g * T**2 + v0 * T + h0
    model = f"h(t) = -{g}t^2 + {v0}t" + ("" if h0 == 0 else f" + {nice_number(h0)}" if h0 > 0 else f" - {nice_number(-h0)}")
    find_t = f"$t = -\\frac{{b}}{{2a}} = -\\frac{{{v0}}}{{2(-{g})}} = {nice_number(T)}$ second{'' if T == 1 else 's'}"
    T_other = sp.Rational(v0, 2 * other_g)
    variant = rng.choice(["height", "height", "time", "model"])

    if variant == "model":
        wrong = [
            f"$h(t) = -{other_g}t^2 + {v0}t" + ("" if h0 == 0 else f" + {nice_number(h0)}" if h0 > 0 else f" - {nice_number(-h0)}") + "$",
            f"$h(t) = {g}t^2 + {v0}t" + ("" if h0 == 0 else f" + {nice_number(h0)}" if h0 > 0 else f" - {nice_number(-h0)}") + "$",
            f"$h(t) = -{g}t^2 + {nice_number(h0) if h0 else 0}t + {v0}$",
            f"$h(t) = -{g}t^2 - {v0}t" + ("" if h0 == 0 else f" + {nice_number(h0)}" if h0 > 0 else f" - {nice_number(-h0)}") + "$",
        ]
        return Spec(
            prompt=f"{text} Which function gives its height after $t$ seconds?",
            answer=f"${model}$",
            kind="choice",
            distractors=wrong,
            explanation=(
                f"The units are {unit}, so use $h(t) = -{g}t^2 + v_0t + h_0$ with $v_0 = {v0}$ and $h_0 = {nice_number(h0)}$"
                + (" (negative because it starts below ground)" if h0 < 0 else "")
                + f": ${model}$."
            ),
        )
    if variant == "time":
        return Spec(
            prompt=f"{text} When does it reach its maximum height?",
            answer=f"${nice_number(T)}$ seconds",
            kind="numbers",
            expected=[T],
            distractors=[f"{o} seconds" for o in num_options(T, [H, sp.Rational(v0, g), T_other, 2 * T])],
            input_hint="Seconds, e.g. 1.5",
            explanation=f"${model}$ opens down, so the top is the vertex: {find_t}.",
        )
    wrong = [T, H - h0, -other_g * T_other**2 + v0 * T_other + h0, v0 * T + h0, -g * T**2 + v0 * T]
    return Spec(
        prompt=f"{text} What is its maximum height, in {unit}?",
        answer=f"${nice_number(H)}$ {unit}",
        kind="numbers",
        expected=[H],
        distractors=[f"{o} {unit}" for o in num_options(H, [w for w in wrong[:3] + [2 * H, H + h0 if h0 else H + v0] if (w * 100).is_Integer])],
        input_hint=f"Height in {unit}, e.g. 41",
        explanation=(
            f"${model}$. The vertex is the maximum: {find_t}. "
            f"Then $h({nice_number(T)}) = -{g}({nice_number(T)})^2 + {v0}({nice_number(T)})"
            + ("" if h0 == 0 else f" + {nice_number(h0)}" if h0 > 0 else f" - {nice_number(-h0)}")
            + f" = {nice_number(H)}$ {unit}. (The ${nice_number(T)}$ is the **time**, not the height.)"
        ),
    )
