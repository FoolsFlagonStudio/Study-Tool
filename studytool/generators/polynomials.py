"""Section 1, Module 1 - Polynomials and Exponents."""

from __future__ import annotations

import math
import random

import sympy as sp

from ..core.problem import Spec, generator
from ..core.symbols import SYMS, coef_tex, join_terms, mono, nonzero, ordinal, show_numbers, tex, x, y

VARS = [x, y, SYMS["a"], SYMS["m"], SYMS["n"]]

DEGREE_NAMES = {0: "constant", 1: "linear", 2: "quadratic", 3: "cubic", 4: "quartic"}
TERM_NAMES = {1: "monomial", 2: "binomial", 3: "trinomial"}

EXPONENT_HINT = "Use ^ for exponents, e.g. 6x^7y^2"
FRACTION_HINT = "Use / for fractions, e.g. y^5/(4x^5)"


def degree_name(deg: int) -> str:
    return DEGREE_NAMES.get(deg, f"{ordinal(deg)} degree")


def terms_name(count: int) -> str:
    return TERM_NAMES.get(count, f"{count}-term polynomial")


def poly_terms(expr) -> list:
    """Terms of a polynomial, highest power first."""
    return list(sp.Add.make_args(sp.expand(expr)))[::-1] if expr != 0 else []


def random_poly(rng: random.Random, var, max_deg: int = 3, count: int = 3):
    exps = sorted(rng.sample(range(0, max_deg + 1), count), reverse=True)
    return [nonzero(rng) * var**e for e in exps]


def flip_one(rng: random.Random, expr):
    """The expression with the sign of one term flipped - a classic slip."""
    terms = sp.Add.make_args(sp.expand(expr))
    term = rng.choice(terms)
    return sp.expand(expr - 2 * term)


# ---------------------------------------------------------------- 1. polynomial basics

BASICS_CHOICES = [
    "Yes, it's a polynomial",
    "No - a variable has a negative exponent",
    "No - a variable has a fractional exponent",
    "No - a variable is in a denominator",
]


@generator("polynomial-basics", "Is it a polynomial?")
def polynomial_basics(rng: random.Random) -> Spec:
    var = rng.choice(["x", "y", "a", "m"])
    sym = SYMS[var]
    kind = rng.choice(["yes", "yes", "neg", "frac", "denom"])
    terms: list = [nonzero(rng) * sym**e for e in rng.sample(range(0, 5), 2)]
    coef = nonzero(rng, -7, 7)
    power = rng.randint(1, 4)

    if kind == "yes":
        special = rng.choice(
            [
                sp.sqrt(rng.choice([2, 3, 5])) * sym**power,
                sp.Rational(nonzero(rng, -5, 5), rng.choice([2, 3, 4, 7])) * sym**power,
                coef * sym * SYMS["b"] ** rng.randint(1, 3),
            ]
        )
        answer = BASICS_CHOICES[0]
        why = (
            "Every variable has a whole-number exponent and none are in a denominator. "
            "Fractions, roots, or multiple variables in the *coefficients* are fine."
        )
    elif kind == "neg":
        special = mono(coef, (var, -power))
        answer = BASICS_CHOICES[1]
        why = f"${special}$ has a negative exponent on ${var}$, so it can't be part of a polynomial."
    elif kind == "frac":
        q = rng.choice([2, 3, 4])
        prefix = coef_tex(coef)
        special = rng.choice([f"{prefix}{var}^{{\\frac{{1}}{{{q}}}}}", f"{prefix}\\sqrt{{{var}}}"])
        answer = BASICS_CHOICES[2]
        why = (
            f"${special}$ has a fractional exponent on ${var}$ "
            f"(remember $\\sqrt{{{var}}} = {var}^{{\\frac{{1}}{{2}}}}$), so it isn't a polynomial."
        )
    else:
        sign = "-" if coef < 0 else ""
        special = f"{sign}\\frac{{{abs(coef)}}}{{{var}{'^' + str(power) if power > 1 else ''}}}"
        answer = BASICS_CHOICES[3]
        why = f"${special}$ divides by ${var}$, so the expression isn't a polynomial."

    terms.append(special)
    rng.shuffle(terms)
    return Spec(
        prompt=f"Is ${join_terms(terms)}$ a polynomial?",
        answer=answer,
        kind="choice",
        choices=BASICS_CHOICES,
        explanation=why,
    )


# ---------------------------------------------------------------- 2. classifying


@generator("classifying-polynomials", "Naming polynomials")
def classifying_polynomials(rng: random.Random) -> Spec:
    var = rng.choice(VARS)
    deg = rng.choice([0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7])
    count = rng.randint(1, min(4, deg + 1))
    exps = [deg, *rng.sample(range(0, deg), count - 1)]
    shown = [nonzero(rng) * var**e for e in exps]

    trap = rng.random()
    if trap < 0.35 and deg > 0:
        # Split one term into two like terms.
        i = rng.randrange(len(shown))
        total = shown[i].as_coeff_Mul()[0]
        part = nonzero(rng)
        while part == total:
            part = nonzero(rng)
        rest = shown[i] / total
        shown[i : i + 1] = [part * rest, (total - part) * rest]
    elif trap < 0.6:
        # A higher-degree pair that cancels out.
        hi = deg + rng.randint(1, 2)
        c = nonzero(rng)
        shown += [c * var**hi, -c * var**hi]
    rng.shuffle(shown)

    answer = f"{degree_name(deg)} {terms_name(count)}"
    shown_deg = max(sp.degree(term, var) for term in shown)
    distractors = [
        f"{degree_name(shown_deg)} {terms_name(len(shown))}",
        f"{degree_name(deg + 1)} {terms_name(count)}",
        f"{degree_name(deg)} {terms_name(count % 4 + 1)}",
        f"{degree_name(deg + 1)} {terms_name(count % 4 + 1)}",
    ]
    if deg > 0:
        distractors.append(f"{degree_name(deg - 1)} {terms_name(count)}")

    simplified = sp.Add(*shown)
    simplify_note = (
        f"First combine like terms: ${join_terms(shown)} = {sp.latex(simplified)}$. "
        if len(shown) != count
        else ""
    )
    return Spec(
        prompt=f"Classify the polynomial ${join_terms(shown)}$.",
        answer=answer,
        kind="choice",
        distractors=distractors,
        explanation=(
            f"{simplify_note}The highest exponent is {deg} ({degree_name(deg)}) and there "
            f"{'is' if count == 1 else 'are'} {count} term{'s' if count > 1 else ''} ({terms_name(count)})."
        ),
    )


# ---------------------------------------------------------------- 3. like terms


@generator("combining-like-terms", "Combining like terms")
def combining_like_terms(rng: random.Random) -> Spec:
    var = rng.choice(VARS)
    exps = rng.sample(range(0, 6), 3)
    counts = rng.choice([[2, 2, 1], [3, 2, 1], [2, 2, 2], [3, 1, 2]])
    groups: dict[int, list[int]] = {}
    for e, cnt in zip(exps, counts):
        coefs = [nonzero(rng) for _ in range(cnt)]
        while sum(coefs) == 0:
            coefs[-1] = nonzero(rng)
        groups[e] = coefs

    shown = [c * var**e for e, coefs in groups.items() for c in coefs]
    rng.shuffle(shown)
    correct = sp.Add(*shown)

    distractors = []
    multi = [e for e, coefs in groups.items() if len(coefs) > 1]
    for e in multi:
        total = sum(groups[e])
        distractors.append(correct - total * var**e + sum(abs(c) for c in groups[e]) * var**e)
        if e >= 1:
            distractors.append(correct - total * var**e + total * var ** (e * len(groups[e])))
    for e in groups:
        distractors.append(correct - sum(groups[e]) * var**e)
    negatives = [term for term in shown if term.as_coeff_Mul()[0] < 0]
    if negatives:
        distractors.append(correct - 2 * rng.choice(negatives))

    steps = ", ".join(
        f"${join_terms([c * var**e for c in coefs])} = {sp.latex(sum(coefs) * var**e)}$"
        for e, coefs in sorted(groups.items(), reverse=True)
        if len(coefs) > 1
    )
    return Spec(
        prompt=f"Simplify by combining like terms: ${join_terms(shown)}$",
        answer=tex(correct),
        kind="expr",
        expected=correct,
        distractors=distractors,
        form="expanded",
        input_hint=EXPONENT_HINT,
        explanation=f"Group terms with the same power and add their coefficients: {steps}.",
    )


# ---------------------------------------------------------------- 4. laws of exponents


@generator("laws-of-exponents", "Laws of exponents")
def laws_of_exponents(rng: random.Random) -> Spec:
    variant = rng.choice(["product", "power", "quotient", "negative"])
    v1, v2 = rng.choice([(x, y), (SYMS["a"], SYMS["b"]), (SYMS["m"], SYMS["n"])])

    if variant == "product":
        c1, c2 = nonzero(rng, -6, 9), rng.randint(2, 8)
        a1, a2, b1, b2 = (rng.randint(1, 6) for _ in range(4))
        left, right = c1 * v1**a1 * v2**b1, c2 * v1**a2 * v2**b2
        correct = left * right
        prompt = f"Simplify $({sp.latex(left)})({sp.latex(right)})$"
        distractors = [
            c1 * c2 * v1 ** (a1 * a2) * v2 ** (b1 * b2),
            (c1 + c2 if c1 + c2 != 0 else c1 - c2) * v1 ** (a1 + a2) * v2 ** (b1 + b2),
            c1 * c2 * v1 ** (a1 + a2) * v2 ** (b1 * b2),
            c1 * c2 * v1 ** (a1 * a2) * v2 ** (b1 + b2),
        ]
        why = f"Multiply the coefficients ({c1} · {c2} = {c1 * c2}) and add exponents on matching bases: $x^m x^n = x^{{m+n}}$."
    elif variant == "power":
        c, e = rng.choice([2, 3, -2, 4, 5]), rng.randint(2, 4)
        a1, b1 = rng.randint(1, 5), rng.randint(1, 5)
        inner = c * v1**a1 * v2**b1
        correct = inner**e
        prompt = f"Simplify $\\left({sp.latex(inner)}\\right)^{{{e}}}$"
        distractors = [
            c * v1 ** (a1 * e) * v2 ** (b1 * e),
            c**e * v1 ** (a1 + e) * v2 ** (b1 + e),
            c * e * v1 ** (a1 * e) * v2 ** (b1 * e),
            abs(c) ** e * v1 ** (a1 * e) * v2 ** (b1 * e),
        ]
        why = (
            f"The exponent {e} applies to every factor, including the coefficient: "
            f"$({c})^{{{e}}} = {c**e}$. Then multiply exponents: $(x^m)^n = x^{{mn}}$."
        )
    elif variant == "quotient":
        c2 = rng.randint(2, 6)
        c1 = c2 * rng.randint(2, 6)
        a1, b1 = rng.randint(4, 9), rng.randint(4, 9)
        a2, b2 = rng.randint(1, a1 - 1), rng.randint(1, b1 - 1)
        top, bottom = c1 * v1**a1 * v2**b1, c2 * v1**a2 * v2**b2
        correct = top / bottom
        prompt = f"Simplify $\\dfrac{{{sp.latex(top)}}}{{{sp.latex(bottom)}}}$"
        distractors = [
            sp.Rational(c1, c2) * v1 ** (a1 + a2) * v2 ** (b1 + b2),
            (c1 - c2) * v1 ** (a1 - a2) * v2 ** (b1 - b2),
            sp.Rational(c1, c2) * v1 ** (a1 - a2) * v2 ** (b1 + b2),
            c1 * v1 ** (a1 - a2) * v2 ** (b1 - b2),
        ]
        why = f"Divide the coefficients ({c1} ÷ {c2} = {c1 // c2}) and subtract exponents, top minus bottom: $\\frac{{x^m}}{{x^n}} = x^{{m-n}}$."
    else:
        base, e = rng.randint(2, 6), rng.randint(1, 3)
        if base**e > 250:
            e = 2
        correct = sp.Rational(1, base**e)
        prompt = f"Simplify ${base}^{{-{e}}}$"
        distractors = [-(base**e), sp.Integer(base**e), sp.Rational(1, base * e), -base * e, -sp.Rational(1, base**e), sp.Rational(e, base)]
        why = f"A negative exponent means reciprocal: ${base}^{{-{e}}} = \\frac{{1}}{{{base}^{{{e}}}}} = {sp.latex(correct)}$. It never makes the answer negative."
        return Spec(
            prompt=prompt,
            answer=tex(correct),
            kind="expr",
            expected=correct,
            distractors=distractors,
            form="positive_exponents",
            input_hint="Type a fraction like 1/8",
            explanation=why,
        )

    return Spec(
        prompt=prompt,
        answer=tex(correct),
        kind="expr",
        expected=correct,
        distractors=distractors,
        form="monomial",
        input_hint=EXPONENT_HINT,
        explanation=why,
    )


# ---------------------------------------------------------------- 5. negative exponents


@generator("negative-exponents", "Eliminating negative exponents")
def negative_exponents(rng: random.Random) -> Spec:
    v1, v2 = rng.choice([("x", "y"), ("a", "b"), ("m", "n")])
    s1, s2 = SYMS[v1], SYMS[v2]
    variant = rng.choice(["quotient", "quotient", "power"])

    def exps():
        while True:
            vals = [rng.choice([-4, -3, -2, -1, 1, 2, 3, 4, 5]) for _ in range(4)]
            if any(val < 0 for val in vals) and vals[0] != vals[2] and vals[1] != vals[3]:
                return vals

    if variant == "quotient":
        a1, b1, a2, b2 = exps()
        c2 = rng.randint(1, 6)
        c1 = rng.choice([c2 * rng.randint(1, 4), rng.randint(1, 9)])
        top = sp.Rational(c1) * s1**a1 * s2**b1
        bottom = sp.Rational(c2) * s1**a2 * s2**b2
        correct = top / bottom
        prompt = (
            f"Rewrite without negative exponents: "
            f"$\\dfrac{{{mono(c1, (v1, a1), (v2, b1))}}}{{{mono(c2, (v1, a2), (v2, b2))}}}$"
        )
        distractors = [
            1 / correct,
            sp.Rational(c1, c2) * s1 ** (a1 + a2) * s2 ** (b1 - b2),
            sp.Rational(c1, c2) * s1 ** (a1 - a2) * s2 ** (b1 + b2),
            sp.Rational(c2, c1) * s1 ** (a1 - a2) * s2 ** (b1 - b2),
            sp.Rational(c1, c2) * s1 ** (a2 - a1) * s2 ** (b1 - b2),
        ]
        why = (
            f"Subtract exponents top minus bottom: ${v1}^{{{a1} - ({a2})}} = {v1}^{{{a1 - a2}}}$ and "
            f"${v2}^{{{b1} - ({b2})}} = {v2}^{{{b1 - b2}}}$. Then move any factor with a negative "
            f"exponent to the other side of the fraction: ${sp.latex(correct)}$."
        )
    else:
        a1, b1, a2, b2 = exps()
        c = rng.randint(2, 4)
        power = rng.choice([-1, -2])
        inner_top = c * s1**a1 * s2**b1
        inner_bottom = s1**a2 * s2**b2
        correct = (inner_top / inner_bottom) ** power
        prompt = (
            f"Rewrite without negative exponents: "
            f"$\\left(\\dfrac{{{mono(c, (v1, a1), (v2, b1))}}}{{{mono(1, (v1, a2), (v2, b2))}}}\\right)^{{{power}}}$"
        )
        distractors = [
            1 / correct,
            (inner_top / inner_bottom) ** (-power),
            c * (s1 ** (a1 - a2) * s2 ** (b1 - b2)) ** power,
            (c * s1 ** (a1 + a2) * s2 ** (b1 + b2)) ** power,
        ]
        inside = sp.latex(inner_top / inner_bottom)
        why = (
            f"Simplify inside first: ${inside}$. A power of ${power}$ flips the fraction"
            f"{' and squares everything' if power == -2 else ''}, giving ${sp.latex(correct)}$."
        )

    return Spec(
        prompt=prompt,
        answer=tex(correct),
        kind="expr",
        expected=correct,
        distractors=distractors,
        form="positive_exponents",
        input_hint=FRACTION_HINT,
        explanation=why,
    )


# ---------------------------------------------------------------- 6-7. adding and subtracting


def _show_poly(terms, rng: random.Random, shuffle: bool) -> str:
    terms = list(terms)
    if shuffle:
        rng.shuffle(terms)
    return join_terms(terms)


@generator("adding-polynomials", "Adding polynomials")
def adding_polynomials(rng: random.Random) -> Spec:
    while True:
        p = random_poly(rng, x, 3, rng.randint(3, 4))
        q = random_poly(rng, x, 3, rng.randint(2, 4))
        correct = sp.expand(sp.Add(*p) + sp.Add(*q))
        if len(sp.Add.make_args(correct)) >= 2:
            break
    q_shown = _show_poly(q, rng, rng.random() < 0.5)
    return Spec(
        prompt=f"Add: $({join_terms(p)}) + ({q_shown})$",
        answer=tex(correct),
        kind="expr",
        expected=correct,
        distractors=[
            sp.expand(sp.Add(*p) - sp.Add(*q)),
            flip_one(rng, correct),
            flip_one(rng, correct),
            sp.expand(correct - 2 * q[0]),
        ],
        form="expanded",
        input_hint=EXPONENT_HINT,
        explanation="Drop the parentheses (adding doesn't change any signs), then combine like terms from highest power to lowest.",
    )


@generator("subtracting-polynomials", "Subtracting polynomials")
def subtracting_polynomials(rng: random.Random) -> Spec:
    if rng.random() < 0.3:
        r1, r2 = rng.randrange(40, 400, 10), rng.randint(1, 4)
        c0, c1, c2 = rng.randrange(200, 5000, 100), rng.randrange(5, r1 - 10, 5), rng.randint(1, 4)
        revenue = r1 * x - r2 * x**2
        cost = c0 + c1 * x + c2 * x**2
        correct = sp.expand(revenue - cost)
        return Spec(
            prompt=(
                f"A business's revenue is ${join_terms([r1 * x, -r2 * x**2])}$ and its cost is "
                f"${join_terms([sp.Integer(c0), c1 * x, c2 * x**2])}$, where $x$ is the number of items sold. "
                "Write the profit polynomial (profit = revenue - cost)."
            ),
            answer=tex(correct),
            kind="expr",
            expected=correct,
            distractors=[
                sp.expand(revenue + cost),
                sp.expand(cost - revenue),
                sp.expand(revenue - c0 + c1 * x + c2 * x**2),
                flip_one(rng, correct),
            ],
            form="expanded",
            input_hint=EXPONENT_HINT,
            explanation="Subtract the *whole* cost: every term of the cost polynomial changes sign, then combine like terms.",
        )

    while True:
        p = random_poly(rng, x, 3, rng.randint(3, 4))
        q = random_poly(rng, x, 3, rng.randint(2, 4))
        if rng.random() < 0.5:
            rng.shuffle(q)
        correct = sp.expand(sp.Add(*p) - sp.Add(*q))
        if len(sp.Add.make_args(correct)) >= 2:
            break
    return Spec(
        prompt=f"Subtract: $({join_terms(p)}) - ({join_terms(q)})$",
        answer=tex(correct),
        kind="expr",
        expected=correct,
        distractors=[
            sp.expand(sp.Add(*p) + sp.Add(*q)),
            sp.expand(sp.Add(*p) + sp.Add(*q) - 2 * q[0]),
            sp.expand(sp.Add(*q) - sp.Add(*p)),
            flip_one(rng, correct),
        ],
        form="expanded",
        input_hint=EXPONENT_HINT,
        explanation="Distribute the minus sign to **every** term in the second polynomial, then combine like terms.",
    )


# ---------------------------------------------------------------- 8. multiplying


@generator("multiplying-polynomials", "Multiplying polynomials")
def multiplying_polynomials(rng: random.Random) -> Spec:
    variant = rng.choice(["mono", "binomials", "square", "conjugates", "bin-tri"])

    if variant == "mono":
        c, e = nonzero(rng, -6, 6), rng.randint(1, 4)
        outside = c * x**e
        inner = random_poly(rng, x, 4, 3)
        correct = sp.expand(outside * sp.Add(*inner))
        prompt = f"Multiply: ${sp.latex(outside)}({join_terms(inner)})$"
        distractors = [
            sp.expand(outside * inner[0] + sp.Add(*inner[1:])),
            sp.Add(*[c * term.as_coeff_Mul()[0] * x ** (e * sp.degree(term, x)) for term in inner]),
            sp.Add(*[(c + term.as_coeff_Mul()[0]) * x ** (e + sp.degree(term, x)) for term in inner]),
            flip_one(rng, correct),
        ]
        why = "Distribute the monomial to each term: multiply coefficients and add exponents."
    elif variant == "square":
        a, b = rng.randint(1, 4), nonzero(rng, -8, 8)
        base = a * x + b
        correct = sp.expand(base**2)
        prompt = f"Multiply: $({sp.latex(base)})^2$"
        distractors = [
            a**2 * x**2 + b**2,
            a**2 * x**2 + a * b * x + b**2,
            a**2 * x**2 - 2 * a * b * x + b**2,
            a * x**2 + 2 * a * b * x + b**2,
        ]
        why = (
            f"Squaring means $({sp.latex(base)})({sp.latex(base)})$ - four products, including the two middle ones. "
            f"Pattern: $(A + B)^2 = A^2 + 2AB + B^2$."
        )
    elif variant == "conjugates":
        a, b = rng.randint(1, 4), rng.randint(1, 9)
        correct = sp.expand((a * x + b) * (a * x - b))
        prompt = f"Multiply: $({sp.latex(a * x + b)})({sp.latex(a * x - b)})$"
        distractors = [a**2 * x**2 + b**2, a**2 * x**2 - 2 * a * b * x - b**2, a**2 * x**2 + 2 * a * b * x - b**2, a * x**2 - b**2]
        why = "The middle terms cancel: $(A + B)(A - B) = A^2 - B^2$."
    elif variant == "binomials":
        a1, a2 = rng.randint(1, 5), rng.randint(1, 5)
        b1, b2 = nonzero(rng, -8, 8), nonzero(rng, -8, 8)
        f1, f2 = a1 * x + b1, a2 * x + b2
        correct = sp.expand(f1 * f2)
        prompt = f"Multiply: $({sp.latex(f1)})({sp.latex(f2)})$"
        middle = (a1 * b2 + a2 * b1) * x
        distractors = [
            a1 * a2 * x**2 + b1 * b2,
            sp.expand(correct - 2 * middle),
            sp.expand(correct - 2 * b1 * b2),
            (a1 + a2) * x + b1 + b2,
        ]
        why = "Every term in the first binomial multiplies every term in the second (4 products), then combine the middle terms."
    else:
        b = nonzero(rng, -6, 6)
        tri = random_poly(rng, x, 2, 3)
        correct = sp.expand((x + b) * sp.Add(*tri))
        prompt = f"Multiply: $({sp.latex(x + b)})({join_terms(tri)})$"
        distractors = [
            sp.expand(x * tri[0] + b * tri[-1]),
            sp.expand(x * sp.Add(*tri) + b),
            flip_one(rng, correct),
            flip_one(rng, correct),
        ]
        why = "Distribute each term of the binomial over all three terms of the trinomial (6 products), then combine like terms."

    return Spec(
        prompt=prompt,
        answer=tex(correct),
        kind="expr",
        expected=correct,
        distractors=distractors,
        form="expanded",
        input_hint=EXPONENT_HINT,
        explanation=why,
    )


# ---------------------------------------------------------------- 9. square roots


@generator("square-roots", "Square roots")
def square_roots(rng: random.Random) -> Spec:
    root = rng.randint(2, 15)
    sq = root * root
    variant = rng.choice(["principal", "negative", "plusminus", "squared-negative", "area", "all"])
    plus_minus = [root, -root]

    if variant == "principal":
        prompt, expected = f"Find $\\sqrt{{{sq}}}$.", [root]
        why = f"$\\sqrt{{\\ }}$ on its own means the principal (positive) root: ${root}^2 = {sq}$."
    elif variant == "negative":
        prompt, expected = f"Find $-\\sqrt{{{sq}}}$.", [-root]
        why = f"The minus sign in front asks for the negative root: $-\\sqrt{{{sq}}} = -{root}$."
    elif variant == "plusminus":
        prompt, expected = f"Find $\\pm\\sqrt{{{sq}}}$.", plus_minus
        why = f"$\\pm$ asks for both roots: ${root}$ and $-{root}$."
    elif variant == "squared-negative":
        prompt, expected = f"Find $\\sqrt{{(-{root})^2}}$.", [root]
        why = f"Do the inside first: $(-{root})^2 = {sq}$, and $\\sqrt{{{sq}}} = {root}$. The answer is positive."
    elif variant == "area":
        unit, thing = rng.choice([("ft", "room"), ("in", "tile"), ("m", "garden"), ("cm", "sticker")])
        prompt = f"A square {thing} has an area of ${sq}\\text{{ {unit}}}^2$. How long is each side, in {unit}?"
        expected = [root]
        why = f"Side $= \\sqrt{{{sq}}} = {root}$ {unit}. A length can't be negative, so only the principal root makes sense."
    else:
        prompt, expected = f"Find all values of $x$ where $x^2 = {sq}$.", plus_minus
        why = f"Both ${root}^2$ and $(-{root})^2$ equal ${sq}$, so $x = \\pm {root}$."

    return Spec(
        prompt=prompt,
        answer=show_numbers(expected),
        kind="numbers",
        expected=expected,
        distractors=[[root], [-root], plus_minus, [sq // 2] if sq % 2 == 0 else [root + 1], [2 * root]],
        input_hint="For two answers, separate with a comma or type +- (e.g. +-8)",
        explanation=why,
    )


# ---------------------------------------------------------------- 10. rational exponents


def _radical(base: str, power: int, index: int) -> str:
    inside = base if power == 1 else f"{base}^{{{power}}}"
    return f"\\sqrt{{{inside}}}" if index == 2 else f"\\sqrt[{index}]{{{inside}}}"


def _evaluate_steps(a: int, b: int, p: int, q: int) -> str:
    root = f"\\sqrt{{{a}}}" if q == 2 else f"\\sqrt[{q}]{{{a}}}"
    if p == 1:
        return f"An exponent of $\\frac{{1}}{{{q}}}$ is a root: ${root} = {b}$."
    return f"Take the root first, then the power: ${root} = {b}$, and ${b}^{{{p}}} = {b**p}$."


@generator("rational-exponents", "Rational exponents")
def rational_exponents(rng: random.Random) -> Spec:
    variant = rng.choice(["to-exponent", "to-radical", "evaluate", "evaluate", "identify"])

    def coprime_pair():
        while True:
            index, power = rng.randint(2, 7), rng.randint(1, 8)
            if math.gcd(index, power) == 1 and power != index:
                return index, power

    if variant == "to-exponent":
        index, power = coprime_pair()
        var = rng.choice(["x", "y", "a", "m"])
        sym = SYMS[var]
        correct = sym ** sp.Rational(power, index)
        return Spec(
            prompt=f"Write ${_radical(var, power, index)}$ using a rational exponent.",
            answer=tex(correct, root_notation=False),
            kind="expr",
            expected=correct,
            distractors=[
                sym ** sp.Rational(index, power),
                sym ** (power * index),
                sym ** sp.Rational(1, index * power),
                sym ** sp.Rational(power, index + 1),
                sym ** sp.Rational(-power, index),
                sym / index,
            ],
            form="rational_exponent",
            tex_options={"root_notation": False},
            input_hint="Use parentheses around the fraction, e.g. x^(3/4)",
            explanation=f"Power over root: the exponent inside ({power}) goes on top and the index ({index}) goes on the bottom, so ${sp.latex(correct)}$.",
        )

    if variant == "to-radical":
        index, power = coprime_pair()
        base = rng.choice(["x", "y", "(x - 1)", "(x + 3)", "a"])
        exp_tex = f"{base}^{{\\frac{{{power}}}{{{index}}}}}"
        correct = f"${_radical(base, power, index)}$"
        return Spec(
            prompt=f"Write ${exp_tex}$ as a radical.",
            answer=correct,
            kind="choice",
            distractors=[
                f"${_radical(base, index, power) if power > 1 else base + '^{' + str(index) + '}'}$",
                f"$\\frac{{{base if power == 1 else base + '^{' + str(power) + '}'}}}{{{index}}}$",
                f"${_radical(base, power + 1, index)}$",
                f"${_radical(base, 1, index * power)}$",
            ],
            explanation=f"The denominator ({index}) becomes the index of the radical and the numerator ({power}) becomes the power inside.",
        )

    if variant == "evaluate":
        while True:
            b, q = rng.randint(2, 5), rng.randint(2, 4)
            p = rng.randint(1, 4)
            if math.gcd(p, q) == 1 and p != q and b**q <= 625 and b**p <= 1024:
                break
        a = b**q
        correct = b**p
        return Spec(
            prompt=f"Evaluate ${a}^{{\\frac{{{p}}}{{{q}}}}}$.",
            answer=f"${correct}$",
            kind="numbers",
            expected=[correct],
            distractors=[[b * p], [b ** (p + 1)], [a * p], [b**q], [b], [a // q] if a % q == 0 else [a + p], [b + p], [b ** (p + 2)]],
            explanation=_evaluate_steps(a, b, p, q),
        )

    index, power = coprime_pair()
    base = rng.choice(["x", "(x + 4)", "(x - 2)", "y"])
    whole = rng.randint(2, 6)
    return Spec(
        prompt="Which expression has a rational exponent?",
        answer=f"${base}^{{\\frac{{{power}}}{{{index}}}}}$",
        kind="choice",
        distractors=[
            f"${base}^{{{whole}}}$",
            f"${base}^{{-{whole}}}$",
            f"$\\frac{{{power}}}{{{index}}}$",
            f"${base}^{{\\frac{{{whole}}}{{1}}}}$",
        ],
        explanation="A rational exponent is a fraction that isn't a whole number. Integer exponents (even written over 1) don't count.",
    )
