"""Section 3, Module 10 - Sequences and Series."""

from __future__ import annotations

import random

import sympy as sp

from ..core.problem import Spec, generator
from ..core.symbols import SYMS, nice_number, nonzero
from .exponentials import dec, dec_options, rounded
from .functions import YES_NO
from .linear import money
from .quadratics import num, num_options

n = SYMS["n"]


def seq_list(values, more: bool = True) -> str:
    return ", ".join(f"{nice_number(v)}" for v in values) + (", \\ldots" if more else "")


def ratio_tex(r) -> str:
    """A ratio ready to raise to a power: 3, or (-2), or (1/2) in parentheses."""
    r = sp.nsimplify(r)
    return str(r) if r.is_Integer and r >= 0 else f"\\left({sp.latex(r)}\\right)"


def geo_formula(a1, r) -> str:
    a1 = sp.nsimplify(a1)
    lead = "" if a1 == 1 else "-" if a1 == -1 else (sp.latex(a1) if not a1.is_Integer else str(a1))
    sep = " \\cdot " if a1.is_Integer and a1 not in (1, -1) and sp.nsimplify(r).is_Integer and r > 0 else ""
    return f"{lead}{sep}{ratio_tex(r)}^{{n - 1}}"


# ---------------------------------------------------------------- 1. terms and formulas

FORMULAS = [
    (lambda k: k**3, "n^3"),
    (lambda k: 3 * k**2 + 1, "3n^2 + 1"),
    (lambda k: k**2 - 2 * k, "n^2 - 2n"),
    (lambda k: k * (k + 1), "n(n + 1)"),
    (lambda k: 2**k, "2^n"),
    (lambda k: sp.Rational(k, k + 1), "\\frac{n}{n + 1}"),
    (lambda k: (-1) ** k * k, "(-1)^n n"),
    (lambda k: 5 * k - 7, "5n - 7"),
    (lambda k: k**2 + 4, "n^2 + 4"),
    (lambda k: sp.Rational(1, 2**k), "\\frac{1}{2^n}"),
]

PATTERNS = [  # (formula, tex) families used for "which formula" questions
    (lambda k: 2 * k - 1, "2n - 1"),
    (lambda k: 2 * k + 1, "2n + 1"),
    (lambda k: k * (k + 1), "n(n + 1)"),
    (lambda k: k**2, "n^2"),
    (lambda k: k**2 + 1, "n^2 + 1"),
    (lambda k: k**2 - 1, "n^2 - 1"),
    (lambda k: 2**k, "2^n"),
    (lambda k: 3 * k, "3n"),
    (lambda k: 4 * k - 2, "4n - 2"),
    (lambda k: 2 * 3 ** (k - 1), "2 \\cdot 3^{n - 1}"),
    (lambda k: k * (k - 1), "n(n - 1)"),
    (lambda k: 5 * k - 4, "5n - 4"),
]


@generator("sequence-terms", "Terms and formulas of sequences")
def sequence_terms(rng: random.Random) -> Spec:
    if rng.random() < 0.5:
        f, tex = rng.choice(FORMULAS)
        k = rng.randint(2, 9) if "2^n" not in tex else rng.randint(2, 7)
        val = sp.nsimplify(f(k))
        return Spec(
            prompt=f"If $a_n = {tex}$, what is the {ordinal(k)} term of the sequence?",
            answer=num(val),
            kind="numbers",
            expected=[val],
            distractors=num_options(val, [f(k - 1), f(k + 1), f(k) + 1, k * 2]),
            input_hint="A number",
            explanation=f"Substitute $n = {k}$: $a_{{{k}}} = {tex.replace('n', '(' + str(k) + ')') if len(tex) > 3 else tex.replace('n', str(k))} = {nice_number(val)}$.",
        )
    f, tex = rng.choice(PATTERNS)
    shown = [f(k) for k in range(1, 6)]
    others = [(g, t) for g, t in PATTERNS if [g(k) for k in range(1, 6)] != shown]
    rng.shuffle(others)
    # prefer wrong formulas that match the first term, since those are the tempting ones
    others.sort(key=lambda gt: gt[0](1) != shown[0])
    return Spec(
        prompt=f"Which formula gives the sequence ${seq_list(shown)}$, starting at $n = 1$?",
        answer=f"$a_n = {tex}$",
        kind="choice",
        distractors=[f"$a_n = {t}$" for _, t in others[:4]],
        explanation=f"Test it at each position: " + ", ".join(f"$n = {k}$ gives ${f(k)}$" for k in range(1, 4)) + ". It matches every listed term. Check more than one term - some wrong formulas match the first.",
    )


def ordinal(k: int) -> str:
    return f"{k}{'th' if 10 <= k % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(k % 10, 'th')}"


# ---------------------------------------------------------------- 2. arithmetic sequences

APPLICATIONS_ARITH = [
    ("{name} has \\${a1} in savings and adds \\${d} every week. How much will {name} have after {k} weeks?", "dollars"),
    ("A theater's front row has {a1} seats, and each row behind it has {d} more seats than the row in front. How many seats are in row {n}?", "seats"),
    ("A town had {a1} residents and the population grows by {d} people each year. What is the population after {k} years?", "people"),
]


@generator("arithmetic-sequences", "Arithmetic sequences")
def arithmetic_sequences(rng: random.Random) -> Spec:
    a1 = rng.randint(-10, 20)
    d = nonzero(rng, -7, 9) if rng.random() < 0.85 else sp.Rational(rng.choice([1, 3, 5]), 2)
    term = lambda k: a1 + (k - 1) * d
    variant = rng.choice(["difference", "term", "two-terms", "two-terms", "application", "is-it"])

    if variant == "difference":
        return Spec(
            prompt=f"What is the common difference of the arithmetic sequence ${seq_list([term(k) for k in range(1, 6)])}$?",
            answer=num(d),
            kind="numbers",
            expected=[sp.nsimplify(d)],
            distractors=num_options(d, [-d, term(2) / term(1) if term(1) else 2 * d, a1, d + 1]),
            input_hint="A number, e.g. -3",
            explanation=f"Subtract any term from the next one: ${nice_number(term(2))} - {'(' + nice_number(a1) + ')' if a1 < 0 else nice_number(a1)} = {nice_number(d)}$. It's the same between every pair of terms.",
        )
    if variant == "term":
        k = rng.randint(10, 60)
        val = term(k)
        return Spec(
            prompt=f"Find the {ordinal(k)} term of the arithmetic sequence ${seq_list([term(i) for i in range(1, 5)])}$.",
            answer=num(val),
            kind="numbers",
            expected=[sp.nsimplify(val)],
            distractors=num_options(val, [a1 + k * d, k * d, term(k - 1), a1 + (k - 1) * (-d)]),
            input_hint="A number",
            explanation=f"$a_1 = {nice_number(a1)}$ and $d = {nice_number(d)}$. $a_{{{k}}} = a_1 + ({k} - 1)d = {nice_number(a1)} + {k - 1}({nice_number(d)}) = {nice_number(val)}$. Use $k - 1$: the first term already counts as one.",
        )
    if variant == "two-terms":
        d = sp.Integer(nonzero(rng, -8, 9))
        a1 = sp.Integer(rng.randint(-12, 15))
        j, k = sorted(rng.sample(range(2, 21), 2))
        aj, ak = a1 + (j - 1) * d, a1 + (k - 1) * d
        formula = sp.expand(a1 + (n - 1) * d)
        return Spec(
            prompt=f"The {ordinal(j)} term of an arithmetic sequence is ${aj}$ and the {ordinal(k)} term is ${ak}$. Find a formula for the $n$th term, simplified.",
            answer=f"${sp.latex(formula)}$",
            kind="expr",
            expected=formula,
            distractors=[sp.expand(a1 + n * d), sp.expand(aj + (n - 1) * d), sp.expand(a1 - (n - 1) * d), sp.expand((a1 + d) + (n - 1) * d * 2)],
            input_hint="e.g. 6n + 1",
            explanation=(
                f"$d = \\frac{{{ak} - ({aj})}}{{{k} - {j}}} = {d}$. Then $a_1 = {aj} - ({j} - 1)({d}) = {a1}$. "
                f"$a_n = {a1} + {d}(n - 1) = {sp.latex(formula)}$."
            ),
        )
    if variant == "is-it":
        kind = rng.choice(["arith", "arith", "geo", "square"])
        if kind == "arith":
            shown, ok = [term(i) for i in range(1, 6)], "Yes"
            why = f"The difference between consecutive terms is always ${nice_number(d)}$."
        elif kind == "geo":
            r = rng.choice([2, 3])
            start = rng.randint(1, 5)
            shown, ok = [start * r**i for i in range(5)], "No"
            why = f"The differences are ${shown[1] - shown[0]}$, ${shown[2] - shown[1]}$, ... - not constant. (It's geometric: each term is multiplied by ${r}$.)"
        else:
            shown, ok = [i * i for i in range(1, 6)], "No"
            why = "The differences are $3, 5, 7, 9$ - not constant, so it isn't arithmetic."
        return Spec(
            prompt=f"Is ${seq_list(shown)}$ an arithmetic sequence?",
            answer=ok,
            kind="choice",
            choices=YES_NO,
            explanation=why,
        )
    a1, d = rng.randint(5, 60), rng.randint(2, 25)
    template, unit = rng.choice(APPLICATIONS_ARITH)
    k = rng.randint(5, 30)
    name = rng.choice(["Maya", "Jordan", "Sam", "Priya", "Luis"])
    if unit == "seats":
        answer = a1 + (k - 1) * d
        why = f"Row 1 has {a1}, so row {k} has $a_{{{k}}} = {a1} + ({k} - 1)({d}) = {answer}$."
        prompt = template.format(a1=a1, d=d, n=k)
        wrong = [a1 + k * d, k * d, a1 + (k - 2) * d]
    else:
        answer = a1 + k * d
        why = f"The starting amount is $a_1 = {a1}$. After {k} {'weeks' if unit == 'dollars' else 'years'} of adding {d}, you're at $a_{{{k + 1}}} = {a1} + {k}({d}) = {answer}$ - one step further than the number of changes."
        prompt = template.format(a1=a1, d=d, k=k, name=name)
        wrong = [a1 + (k - 1) * d, k * d, a1 + (k + 1) * d]
    return Spec(
        prompt=prompt,
        answer=num(answer),
        kind="numbers",
        expected=[sp.Integer(answer)],
        distractors=num_options(answer, wrong),
        input_hint="A number",
        explanation=why,
    )


# ---------------------------------------------------------------- 3. geometric sequences


@generator("geometric-sequences", "Geometric sequences")
def geometric_sequences(rng: random.Random) -> Spec:
    r = rng.choice([2, 3, 4, 5, -2, -3, sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(-1, 2)])
    a1 = sp.Integer(rng.choice([1, 2, 3, 4, 5, 6, 8, 10])) if sp.nsimplify(r).is_Integer else sp.Integer(rng.choice([64, 81, 128, 243, 256, 1024, 486]))
    if not sp.nsimplify(r).is_Integer and (a1 % sp.nsimplify(r).q):
        a1 = sp.nsimplify(r).q ** 5
    r = sp.nsimplify(r)
    term = lambda k: a1 * r ** (k - 1)
    variant = rng.choice(["ratio", "term", "two-terms", "two-terms", "growth", "is-it"])

    if variant == "ratio":
        return Spec(
            prompt=f"What is the common ratio of the geometric sequence ${seq_list([term(k) for k in range(1, 6)])}$?",
            answer=num(r),
            kind="numbers",
            expected=[r],
            distractors=num_options(r, [1 / r, -r, term(2) - term(1), r * 2]),
            input_hint="A number or fraction, e.g. 1/2",
            explanation=f"Divide any term by the one before it: $\\frac{{{nice_number(term(2))}}}{{{nice_number(term(1))}}} = {nice_number(r)}$.",
        )
    if variant == "term":
        k = rng.randint(5, 9)
        val = term(k)
        return Spec(
            prompt=f"Find the {ordinal(k)} term of the geometric sequence ${seq_list([term(i) for i in range(1, 5)])}$.",
            answer=num(val),
            kind="numbers",
            expected=[val],
            distractors=num_options(val, [a1 * r**k, term(k - 1), a1 * r * (k - 1), (a1 * r) ** (k - 1)]),
            input_hint="A number or fraction",
            explanation=f"$a_{{{k}}} = a_1 r^{{{k} - 1}} = {nice_number(a1)} \\cdot {ratio_tex(r)}^{{{k - 1}}} = {nice_number(val)}$.",
        )
    if variant == "two-terms":
        j, k = rng.choice([(1, 4), (2, 5), (3, 6), (4, 9), (3, 8), (6, 11), (2, 4), (3, 5)])
        aj, ak = term(j), term(k)
        if abs(ak) > 10**6 or abs(aj) > 10**6:
            j, k = 2, 4
            aj, ak = term(j), term(k)
        even_gap = (k - j) % 2 == 0
        answer = f"$a_n = {geo_formula(a1, r)}$"
        wrong = [f"$a_n = {geo_formula(a1, 1 / r)}$", f"$a_n = {geo_formula(aj, r)}$", f"$a_n = {geo_formula(a1 * r, r)}$", f"$a_n = {geo_formula(-a1, -r)}$" if not even_gap else f"$a_n = {geo_formula(a1, -r)}$"]
        return Spec(
            prompt=f"The {ordinal(j)} term of a geometric sequence is ${nice_number(aj)}$ and the {ordinal(k)} term is ${nice_number(ak)}$"
            + (f", and the ratio is {'positive' if r > 0 else 'negative'}" if even_gap else "")
            + ". Find a formula for the $n$th term.",
            answer=answer,
            kind="choice",
            distractors=[w for w in dict.fromkeys(wrong) if w != answer],
            explanation=(
                f"Divide: $r^{{{k} - {j}}} = \\frac{{{nice_number(ak)}}}{{{nice_number(aj)}}} = {nice_number(ak / aj)}$, so $r = {nice_number(r)}$. "
                f"Then $a_1 = \\frac{{a_{{{j}}}}}{{r^{{{j - 1}}}}} = {nice_number(a1)}$. So {answer}."
            ),
        )
    if variant == "is-it":
        kind = rng.choice(["geo", "geo", "arith"])
        if kind == "geo":
            shown, ok, why = [term(i) for i in range(1, 6)], "Yes", f"Each term is the previous one times ${nice_number(r)}$."
        else:
            start, d = rng.randint(1, 9), rng.randint(2, 6)
            shown, ok = [start + d * i for i in range(5)], "No"
            why = f"The ratios $\\frac{{{shown[1]}}}{{{shown[0]}}}$ and $\\frac{{{shown[2]}}}{{{shown[1]}}}$ aren't equal. (It's arithmetic: add ${d}$ each time.)"
        return Spec(
            prompt=f"Is ${seq_list(shown)}$ a geometric sequence?",
            answer=ok,
            kind="choice",
            choices=YES_NO,
            explanation=why,
        )
    up = rng.random() < 0.55
    pct = rng.choice([2, 2.5, 3, 4, 5, 6, 8]) if up else rng.choice([5, 7, 10, 12, 15, 20])
    start = rng.choice([1_000, 1_200, 5_000, 12_000, 25_000, 30_000, 40_000])
    years = rng.randint(3, 12)
    rate = 1 + pct / 100 if up else 1 - pct / 100
    val = start * rate**years
    what = rng.choice(["A salary that starts at", "An investment of"]) if up else rng.choice(["A car bought for", "A machine that cost"])
    prompt = f"{what} {money(start)} {'increases' if up else 'loses'} {pct:g}% {'each year' if up else 'of its value each year'}. What will it be after {years} years? Round to the nearest cent."
    return Spec(
        prompt=prompt,
        answer=f"$\\${dec(val)}$",
        kind="numbers",
        expected=[rounded(val, 2)],
        distractors=dec_options(val, [w for w in (start * rate ** (years - 1), start * rate ** (years + 1), start * (1 + (rate - 1) * years), start * (2 - rate) ** years) if w > 0], 2, prefix="\\$"),
        tolerance=0.015,
        input_hint="Dollars and cents",
        explanation=f"Each year multiplies the value by $r = {rate:g}$ ({'1 plus' if up else '1 minus'} the rate). After {years} years: ${start:,}".replace(",", "{,}") + f"({rate:g})^{{{years}}} \\approx \\${dec(val)}$.",
    )


# ---------------------------------------------------------------- 4. summation notation

SUM_TERMS = [
    (lambda i: 3 * i, "3i"),
    (lambda i: 2 * i + 1, "(2i + 1)"),
    (lambda i: i**2, "i^2"),
    (lambda i: i**2 + 1, "(i^2 + 1)"),
    (lambda i: 2**i, "2^i"),
    (lambda i: 5 - i, "(5 - i)"),
    (lambda i: 4 * i - 3, "(4i - 3)"),
    (lambda i: i**3, "i^3"),
    (lambda i: 10 - 2 * i, "(10 - 2i)"),
]


@generator("summation-notation", "Summation notation")
def summation_notation(rng: random.Random) -> Spec:
    f, tex = rng.choice(SUM_TERMS)
    lo = rng.choice([1, 1, 1, 2, 3])
    hi = lo + rng.randint(2, 5)
    total = sum(f(i) for i in range(lo, hi + 1))
    wrong = [sum(f(i) for i in range(1, hi + 1)), sum(f(i) for i in range(lo, hi)), f(hi), sum(f(i) for i in range(lo + 1, hi + 1)), total + f(hi + 1)]
    terms = " + ".join(f"({f(i)})" if f(i) < 0 else str(f(i)) for i in range(lo, hi + 1))
    return Spec(
        prompt=f"Evaluate $\\displaystyle\\sum_{{i = {lo}}}^{{{hi}}} {tex}$.",
        answer=num(total),
        kind="numbers",
        expected=[sp.Integer(total)],
        distractors=num_options(total, wrong),
        input_hint="A number",
        explanation=f"Substitute $i = {lo}$ through $i = {hi}$ ({hi - lo + 1} terms) and add: ${terms} = {total}$.",
    )


# ---------------------------------------------------------------- 5. arithmetic series


@generator("arithmetic-series", "Arithmetic series")
def arithmetic_series(rng: random.Random) -> Spec:
    if rng.random() < 0.4:
        story = rng.choice(["seats", "points", "gifts"])
        if story == "seats":
            first, d, rows = rng.randint(14, 40), rng.choice([1, 2, 3, 4]), rng.randint(10, 25)
            sign = rng.choice([1, -1]) if first - (rows - 1) * 4 > 0 else 1
            d *= sign
            prompt = f"A theater has {rows} rows. The front row has {first} seats, and each row behind it has {abs(d)} {'more' if d > 0 else 'fewer'} seats than the row in front. How many seats are there in total?"
            k, a1 = rows, first
        elif story == "points":
            a1, d, k = rng.randint(2, 10), rng.randint(1, 3), rng.randint(10, 25)
            prompt = f"A player scores {a1} points in game 1, and each game after that scores {d} more point{'s' if d > 1 else ''} than the game before. How many total points after {k} games?"
        else:
            a1, d, k = rng.randint(1, 5), rng.randint(1, 4), rng.randint(8, 18)
            prompt = f"Someone saves {money(a1)} in week 1, {money(a1 + d)} in week 2, {money(a1 + 2 * d)} in week 3, and so on. How much have they saved in total after {k} weeks?"
    else:
        a1, d, k = rng.randint(-10, 15), nonzero(rng, -5, 8), rng.randint(8, 40)
        prompt = None
    last = a1 + (k - 1) * d
    total = sp.Rational(k * (a1 + last), 2)
    if prompt is None:
        prompt = f"Find the sum of the first {k} terms of the arithmetic sequence ${seq_list([a1 + i * d for i in range(4)])}$."
    return Spec(
        prompt=prompt,
        answer=num(total),
        kind="numbers",
        expected=[total],
        distractors=num_options(total, [k * (a1 + last), k * (a1 + a1 + k * d) / 2, (k - 1) * (a1 + last) / 2, k * last]),
        input_hint="A number",
        explanation=f"$a_1 = {a1}$, $d = {d}$, $n = {k}$. The last term is $a_{{{k}}} = {a1} + {k - 1}({d}) = {last}$. $S_{{{k}}} = {k}\\left(\\frac{{{a1} + {'(' + str(last) + ')' if last < 0 else last}}}{{2}}\\right) = {nice_number(total)}$.",
    )


# ---------------------------------------------------------------- 6. geometric series


@generator("geometric-series", "Geometric series")
def geometric_series(rng: random.Random) -> Spec:
    if rng.random() < 0.35:
        salary = rng.choice([25_000, 30_000, 40_000, 45_000, 50_000, 60_000])
        pct = rng.choice([2, 2.5, 3, 4, 5])
        years = rng.randint(5, 15)
        r = 1 + pct / 100
        total = salary * (1 - r**years) / (1 - r)
        return Spec(
            prompt=f"A job pays {money(salary)} the first year with a guaranteed {pct:g}% raise every year. How much is earned in total over {years} years? Round to the nearest dollar.",
            answer=f"$\\${dec(total, 0)}$",
            kind="numbers",
            expected=[rounded(total, 0)],
            distractors=dec_options(total, [salary * r ** (years - 1), salary * (1 - r ** (years + 1)) / (1 - r), salary * years * r, salary * r**years], 0, prefix="\\$"),
            tolerance=1.01,
            input_hint="Dollars, e.g. 280085",
            explanation=(
                f"The yearly pay is geometric with $a_1 = {salary:,}$".replace(",", "{,}") + f" and $r = {r:g}$. "
                f"$S_{{{years}}} = \\frac{{{salary:,}".replace(",", "{,}") + f"(1 - {r:g}^{{{years}}})}}{{1 - {r:g}}} \\approx \\${dec(total, 0)}$."
            ),
        )
    r = sp.nsimplify(rng.choice([2, 3, -2, -3, sp.Rational(1, 2), sp.Rational(1, 3), 4]))
    a1 = sp.Integer(rng.choice([1, 2, 3, 4, 5, 6])) if r.is_Integer else sp.Integer(r.q ** rng.randint(4, 7))
    k = rng.randint(5, 10) if abs(r) < 4 else rng.randint(4, 7)
    total = a1 * (1 - r**k) / (1 - r)
    return Spec(
        prompt=f"Find the sum of the first {k} terms of the geometric sequence ${seq_list([a1 * r**i for i in range(4)])}$.",
        answer=num(total),
        kind="numbers",
        expected=[total],
        distractors=num_options(total, [a1 * (1 - r ** (k - 1)) / (1 - r), a1 * (1 - r ** (k + 1)) / (1 - r), a1 * r ** (k - 1), a1 * (1 + r**k) / (1 - r)]),
        input_hint="A number or fraction",
        explanation=(
            f"$a_1 = {nice_number(a1)}$, $r = {nice_number(r)}$, $n = {k}$. "
            f"$S_{{{k}}} = \\frac{{{nice_number(a1)}(1 - {ratio_tex(r)}^{{{k}}})}}{{1 - {ratio_tex(r)}}} = {nice_number(total)}$. The exponent is the number of terms, ${k}$."
        ),
    )
