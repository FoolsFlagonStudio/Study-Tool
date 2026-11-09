"""Section 2, Module 5 - Linear Functions and Systems."""

from __future__ import annotations

import math
import random

import sympy as sp

from ..core.problem import Spec, generator
from ..core.symbols import coef_tex, fmt_linear, fmt_num, join_terms, nice_number, nonzero, show_pair, x, y
from .functions import YES_NO

PAIR_HINT = "Type the ordered pair, e.g. (2, -3)"


def side(a, b) -> str:
    """LaTeX for ax + by, written as given."""
    terms = [t for t in (a * x, b * y) if t != 0]
    return join_terms(terms) if terms else "0"


def equation(a, b, c) -> str:
    return f"{side(a, b)} = {sp.latex(sp.nsimplify(c))}"


def system(*rows: str) -> str:
    """Display-math system of equations, one per line, aligned at the equals sign."""
    lines = " \\\\ ".join(row.replace(" = ", " &= ", 1) for row in rows)
    return f"$$\\begin{{aligned}} {lines} \\end{{aligned}}$$"


def money(val) -> str:
    """Plain-text dollar amount for prompts: \\$350, \\$1.20, \\$2,500."""
    val = sp.nsimplify(val)
    if val.is_Integer:
        return f"\\${int(val):,}"
    return f"\\${float(val):,.2f}"


def solution_value(rng: random.Random, allow_half: bool = True):
    """Mostly integers, sometimes a half or quarter - like the course's decimal answers."""
    if allow_half and rng.random() < 0.2:
        return sp.Rational(rng.choice([-7, -5, -3, -1, 1, 3, 5, 7]), rng.choice([2, 4]))
    return sp.Integer(rng.randint(-8, 9))


def random_row(rng: random.Random, sol, lo: int = -7, hi: int = 8):
    a, b = nonzero(rng, lo, hi), nonzero(rng, lo, hi)
    return a, b, a * sol[0] + b * sol[1]


def line_tex(m, b) -> str:
    """'$y = -5x + 35$' - slope first, the way the course writes slope-intercept form."""
    m, b = sp.nsimplify(m), sp.nsimplify(b)
    body = "" if m == 0 else f"{coef_tex(m)}x"
    if b != 0 or not body:
        body += (f" + {sp.latex(b)}" if body and b > 0 else f" - {sp.latex(-b)}" if body else sp.latex(b))
    return f"$y = {body}$"


def independent(rows) -> bool:
    (a1, b1, _), (a2, b2, _) = rows
    return a1 * b2 - a2 * b1 != 0


def integer_rhs(rows) -> bool:
    return all(sp.nsimplify(c).is_Integer for _, _, c in rows)


# ---------------------------------------------------------------- 1. solving linear equations


@generator("solving-linear-equations", "Solving linear equations")
def solving_linear_equations(rng: random.Random) -> Spec:
    sol = sp.Integer(rng.randint(-12, 15))
    variant = rng.choice(["ax+b", "ax+b", "x/a+b", "a(x+b)", "both-sides", "fraction"])

    if variant == "ax+b":
        a, b = nonzero(rng, -9, 9), nonzero(rng, -20, 20)
        while abs(a) < 2:
            a = nonzero(rng, -9, 9)
        c = a * sol + b
        shown = f"{sp.latex(a * x + b)} = {c}"
        wrong = [[sp.Rational(c + b, a)], [c - b], [sp.Rational(c, a) - b], [-sol]]
        why = f"{'Subtract' if b > 0 else 'Add'} {abs(b)} on both sides: ${a}x = {c - b}$. Divide both sides by ${a}$: $x = {sol}$."
    elif variant == "x/a+b":
        a, b = rng.randint(2, 6), nonzero(rng, -12, 12)
        sol = sp.Integer(a * rng.randint(-5, 6))
        c = sol / a + b
        shown = f"\\frac{{x}}{{{a}}}{' + ' if b > 0 else ' - '}{abs(b)} = {c}"
        wrong = [[(c + b) * a], [sp.Rational(c - b, a)], [c * a - b], [-sol]]
        why = f"{'Subtract' if b > 0 else 'Add'} {abs(b)}: $\\frac{{x}}{{{a}}} = {c - b}$. Multiply both sides by {a}: $x = {sol}$."
    elif variant == "a(x+b)":
        a, b = rng.choice([2, 3, 4, 5, -2, -3]), nonzero(rng, -9, 9)
        c = a * (sol + b)
        shown = f"{a}({sp.latex(x + b)}) = {c}"
        wrong = [[sp.Rational(c, a) + b], [c - b], [sp.Rational(c - b, a)], [-sol]]
        why = f"Divide both sides by ${a}$: $x{' + ' if b > 0 else ' - '}{abs(b)} = {sp.Rational(c, a)}$. Then $x = {sol}$. (Distributing first works too.)"
    elif variant == "both-sides":
        a, d = rng.sample([-5, -4, -3, -2, 2, 3, 4, 5, 6, 7], 2)
        b = nonzero(rng, -15, 15)
        e = (a - d) * sol + b
        shown = f"{sp.latex(a * x + b)} = {sp.latex(d * x + e)}"
        wrong = [[sp.Rational(e + b, a - d)], [e - b], [-sol], [sp.Rational(e - b, a + d)] if a + d else [sol + 1]]
        why = (
            f"Move the $x$ terms to one side: ${a - d}x{' + ' if b > 0 else ' - '}{abs(b)} = {e}$. "
            f"Then ${a - d}x = {e - b}$, so $x = {sol}$."
        )
    else:
        p, q = rng.choice([(2, 3), (3, 4), (2, 5), (3, 2), (5, 2), (3, 5)])
        b = nonzero(rng, -10, 10)
        sol = sp.Integer(q * rng.randint(-4, 5))
        c = sp.Rational(p, q) * sol + b
        shown = f"\\frac{{{p}}}{{{q}}}x{' + ' if b > 0 else ' - '}{abs(b)} = {c}"
        wrong = [[sp.Rational(p, q) * (c - b)], [sp.Rational(q, p) * (c + b)], [c - b], [-sol]]
        why = (
            f"{'Subtract' if b > 0 else 'Add'} {abs(b)}: $\\frac{{{p}}}{{{q}}}x = {c - b}$. "
            f"Multiply by the reciprocal $\\frac{{{q}}}{{{p}}}$: $x = {sol}$."
        )

    return Spec(
        prompt=f"Solve for $x$: ${shown}$",
        answer=f"${sp.latex(sol)}$",
        kind="numbers",
        expected=[sol],
        distractors=wrong,
        input_hint="Number only, e.g. -4 or 3/2",
        explanation=why + f" Check by plugging ${sol}$ back in.",
    )


# ---------------------------------------------------------------- 2. linear models


MODELS = [
    ("A moving company charges {F} to pack everything plus {R} per mile to move it.", "miles", "money", [250, 300, 350, 400], [0.15, 0.25, 0.5, 1.2]),
    ("A rideshare trip costs {F} plus {R} per mile.", "miles", "money", [2, 2.5, 3, 4], [1.25, 1.5, 1.75, 2]),
    ("A plumber charges a {F} call-out fee plus {R} per hour.", "hours", "money", [60, 75, 85, 100], [45, 55, 60, 80]),
    ("A gym charges a {F} signup fee plus {R} per month.", "months", "money", [25, 40, 50, 99], [15, 20, 25, 35]),
    ("A salesperson earns {F} each week plus {R} commission on all sales.", "dollars of sales", "pct", [300, 350, 400, 500], [5, 8, 10, 12]),
    ("A phone plan costs {F} a month plus {R} per GB of data.", "GB", "money", [20, 30, 40, 45], [2, 3, 5, 10]),
    ("An oil spill starts with a radius of {F} miles and the radius grows {R} miles every hour.", "hours", "plain", [1, 2, 3, 4], [0.5, 1.5, 2, 2.5]),
]


@generator("linear-models", "Writing linear models")
def linear_models(rng: random.Random) -> Spec:
    story, unit, style, fixed_opts, rate_opts = rng.choice(MODELS)
    F = sp.nsimplify(rng.choice(fixed_opts))
    R_raw = sp.nsimplify(rng.choice(rate_opts))
    R = R_raw / 100 if style == "pct" else R_raw
    if style == "money":
        text = story.format(F=money(F), R=money(R))
    elif style == "pct":
        text = story.format(F=money(F), R=f"{fmt_num(R_raw)}%")
    else:
        text = story.format(F=fmt_num(F), R=fmt_num(R))
    model = R * x + F
    variant = rng.choice(["write", "write", "evaluate", "backward"])

    if variant == "write":
        return Spec(
            prompt=f"{text} Write a linear model $y$ for $x$ {unit}.",
            answer=f"$y = {fmt_linear(R, F)}$",
            kind="expr",
            expected=model,
            distractors=[
                f"$y = {fmt_linear(F, R)}$",
                f"$y = {fmt_linear(R + F, 0)}$",
                f"$y = {fmt_linear(R, -F)}$",
                f"$y = {fmt_linear(R_raw, F)}$" if style == "pct" else f"$y = {fmt_num(R)}(x + {fmt_num(F)})$",
            ],
            input_hint="e.g. 0.15x + 350",
            explanation=(
                f"The rate (\"per\" amount) multiplies $x$: ${fmt_num(R)}x$. The one-time amount is added: "
                f"$y = {fmt_linear(R, F)}$."
                + (f" A percent is divided by 100: {fmt_num(R_raw)}% = {fmt_num(R)}." if style == "pct" else "")
            ),
        )

    n = rng.choice([3, 4, 5, 6, 8, 10, 12, 20]) if style != "pct" else rng.choice([1000, 2000, 2500, 4000, 5000])
    total = model.subs(x, n)
    if variant == "evaluate":
        return Spec(
            prompt=f"{text} What is the total for {fmt_num(n).replace('{,}', ',')} {unit}?",
            answer=f"${fmt_num(total)}$",
            kind="numbers",
            expected=[total],
            tolerance=0.005,
            distractors=[[F * n + R], [(R + F) * n], [R * n], [R * n - F]],
            input_hint="Number only",
            explanation=f"$y = {fmt_linear(R, F)}$, so $y = {fmt_num(R)}({fmt_num(n)}) + {fmt_num(F)} = {fmt_num(total)}$.",
        )
    return Spec(
        prompt=f"{text} The total came to {money(total) if style != 'plain' else fmt_num(total)}. How many {unit}?",
        answer=f"${fmt_num(n)}$",
        kind="numbers",
        expected=[n],
        tolerance=0.005,
        distractors=[[sp.nsimplify(total / R)], [sp.nsimplify((total + F) / R)], [n + 1], [n - 1]],
        input_hint="Number only",
        explanation=(
            f"Set the model equal to the total: ${fmt_num(total)} = {fmt_linear(R, F)}$. "
            f"Subtract {fmt_num(F)}: ${fmt_num(total - F)} = {fmt_num(R)}x$. Divide: $x = {fmt_num(n)}$."
        ),
    )


# ---------------------------------------------------------------- 3. intercepts


@generator("intercepts", "Intercepts")
def intercepts(rng: random.Random) -> Spec:
    want_x = rng.random() < 0.55
    if rng.random() < 0.55:
        m = nonzero(rng, -9, 12)
        r = nonzero(rng, -8, 8)
        b = -m * r  # x-intercept is r
        shown = f"y = {sp.latex(m * x + b)}"
        x_int, y_int = sp.Integer(r), sp.Integer(b)
        steps_x = f"Set $y = 0$: $0 = {sp.latex(m * x + b)}$, so $x = {r}$."
        steps_y = f"Set $x = 0$: $y = {m}(0){' + ' if b >= 0 else ' - '}{abs(b)} = {b}$."
        extra = [[sp.Rational(b, m)], [m]]
    else:
        a, bb = nonzero(rng, -6, 8), nonzero(rng, -6, 8)
        c = math.lcm(abs(a), abs(bb)) * rng.choice([1, 2, -1, 3])
        shown = equation(a, bb, c)
        x_int, y_int = sp.Rational(c, a), sp.Rational(c, bb)
        steps_x = f"Set $y = 0$: ${a}x = {c}$, so $x = {sp.latex(x_int)}$."
        steps_y = f"Set $x = 0$: ${bb}y = {c}$, so $y = {sp.latex(y_int)}$."
        extra = [[c], [a]]
    want, other = (x_int, y_int) if want_x else (y_int, x_int)
    label = "$x$-intercept" if want_x else "$y$-intercept"
    return Spec(
        prompt=f"Find the {label} of ${shown}$. (Give the {'$x$' if want_x else '$y$'}-value.)",
        answer=f"${sp.latex(want)}$",
        kind="numbers",
        expected=[want],
        distractors=[[other], [-want], *extra],
        input_hint="Number only",
        explanation=steps_x if want_x else steps_y,
    )


# ---------------------------------------------------------------- 4. slope and line forms


@generator("slope-and-line-forms", "Slope and equations of lines")
def slope_and_line_forms(rng: random.Random) -> Spec:
    variant = rng.choice(["slope", "slope", "point-slope", "two-points", "standard"])

    if variant == "slope":
        x1, x2 = rng.sample(range(-6, 9), 2)
        y1, y2 = rng.randint(-8, 9), rng.randint(-8, 9)
        m = sp.Rational(y2 - y1, x2 - x1)
        wrong = [[-m], [y2 - y1], [sp.Rational(y2 + y1, x2 + x1)] if x2 + x1 else [m + 1]]
        if m != 0:
            wrong.append([1 / m])
        return Spec(
            prompt=f"Find the slope of the line through $({x1}, {y1})$ and $({x2}, {y2})$.",
            answer=f"${sp.latex(m)}$",
            kind="numbers",
            expected=[m],
            distractors=wrong,
            input_hint="Number or fraction, e.g. -3/2",
            explanation=f"$m = \\frac{{y_2 - y_1}}{{x_2 - x_1}} = \\frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\frac{{{y2 - y1}}}{{{x2 - x1}}} = {sp.latex(m)}$.",
        )

    if variant == "standard":
        b = rng.choice([1, 2, 3, 4, 5, -1, -2, -3])
        m = nonzero(rng, -5, 5)
        a, c = -m * b, b * rng.randint(-6, 6)
        return Spec(
            prompt=f"What is the slope of ${equation(a, b, c)}$?",
            answer=f"${m}$",
            kind="numbers",
            expected=[sp.Integer(m)],
            distractors=[[-m], [a], [sp.Rational(c, b)], [b]],
            input_hint="Number only",
            explanation=f"Solve for $y$: ${b}y = {sp.latex(-a * x + c)}$, so $y = {sp.latex(m * x + sp.Rational(c, b))}$. The slope is the coefficient of $x$: ${m}$.",
        )

    m = nonzero(rng, -6, 6)
    x1, y1 = rng.randint(-5, 6), rng.randint(-8, 9)
    b = y1 - m * x1
    line = m * x + b
    if variant == "point-slope":
        prompt = f"Write the equation of the line with slope ${m}$ through $({x1}, {y1})$ in slope-intercept form."
        why = (
            f"Point-slope: $y - ({y1}) = {m}(x - ({x1}))$. Distribute and solve for $y$: $y = {sp.latex(line)}$."
        )
    else:
        x2 = x1 + rng.choice([1, 2, 3, -1, -2])
        y2 = y1 + m * (x2 - x1)
        prompt = f"Write the equation of the line through $({x1}, {y1})$ and $({x2}, {y2})$ in slope-intercept form."
        why = (
            f"Slope: $\\frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = {m}$. Then $y - ({y1}) = {m}(x - ({x1}))$, "
            f"so $y = {sp.latex(line)}$."
        )
    return Spec(
        prompt=prompt,
        answer=line_tex(m, b),
        kind="expr",
        expected=line,
        distractors=[line_tex(m, y1), line_tex(m, y1 + m * x1), line_tex(m, -b), line_tex(-m, b), line_tex(m, x1)],
        input_hint="e.g. 3x - 4",
        explanation=why,
    )


# ---------------------------------------------------------------- 5. checking solutions


def _two_rows(rng: random.Random, sol):
    while True:
        rows = [random_row(rng, sol), random_row(rng, sol)]
        if independent(rows) and integer_rhs(rows):
            return rows


@generator("checking-system-solutions", "Checking a solution to a system")
def checking_system_solutions(rng: random.Random) -> Spec:
    sol = (sp.Integer(rng.randint(-6, 7)), sp.Integer(rng.randint(-6, 7)))
    rows = _two_rows(rng, sol)
    (a1, b1, c1), (a2, b2, c2) = rows
    shown = system(equation(a1, b1, c1), equation(a2, b2, c2))
    # A point on the first line only.
    off = (sol[0] + b1, sol[1] - a1)

    def check_text(pt):
        v1 = a1 * pt[0] + b1 * pt[1]
        v2 = a2 * pt[0] + b2 * pt[1]
        mark = lambda v, c: "✓" if v == c else "✗"
        return (
            f"First: ${a1}({pt[0]}) + {b1}({pt[1]}) = {v1}$ {mark(v1, c1)}. "
            f"Second: ${a2}({pt[0]}) + {b2}({pt[1]}) = {v2}$ {mark(v2, c2)}."
        ).replace("+ -", "- ")

    if rng.random() < 0.5:
        candidate = sol if rng.random() < 0.5 else off
        is_sol = candidate == sol
        return Spec(
            prompt=f"Is $({candidate[0]}, {candidate[1]})$ a solution of this system?\n\n{shown}",
            answer="Yes" if is_sol else "No",
            kind="choice",
            choices=YES_NO,
            explanation=check_text(candidate) + (" Both are true, so it's a solution." if is_sol else " It has to work in **both** equations, so it isn't a solution."),
        )

    options = [off, (sol[1], sol[0]), (-sol[0], sol[1]), (sol[0], -sol[1]), (sol[0] + 1, sol[1])]
    return Spec(
        prompt=f"Which ordered pair is the solution of this system?\n\n{shown}",
        answer=show_pair(sol),
        kind="choice",
        distractors=[show_pair(o) for o in options if o != sol],
        explanation=check_text(sol) + " Both are true.",
    )


# ---------------------------------------------------------------- 6. substitution


@generator("substitution-method", "Solving by substitution")
def substitution_method(rng: random.Random) -> Spec:
    solved_for_x = rng.random() < 0.3
    while True:
        # x stays an integer when the solved equation is x = py + q, so q is an integer too.
        sol = (solution_value(rng, allow_half=not solved_for_x), solution_value(rng, allow_half=False))
        m = nonzero(rng, -6, 6)
        intercept = sol[1] - m * sol[0]
        a, b, c = random_row(rng, sol)
        if a + b * m != 0 and sp.nsimplify(c).is_Integer and sp.nsimplify(intercept).is_Integer:
            break
    if solved_for_x:
        # x = py + q form: rewrite the line through sol with x as the subject.
        p = nonzero(rng, -5, 5)
        q = sol[0] - p * sol[1]
        while a * p + b == 0:
            p = nonzero(rng, -5, 5)
            q = sol[0] - p * sol[1]
        first = f"x = {sp.latex(p * y + q)}"
        sub = sp.expand(a * (p * y + q) + b * y)
        steps = (
            f"Substitute $x = {sp.latex(p * y + q)}$ into the other equation: "
            f"${a}({sp.latex(p * y + q)}) + {b}y = {c}$, so ${sp.latex(sub)} = {c}$ and $y = {nice_number(sol[1])}$. "
            f"Then $x = {nice_number(sol[0])}$."
        )
    else:
        first = f"y = {sp.latex(m * x + intercept)}"
        sub = sp.expand(a * x + b * (m * x + intercept))
        steps = (
            f"Substitute $y = {sp.latex(m * x + intercept)}$ into the other equation: "
            f"${a}x + {b}({sp.latex(m * x + intercept)}) = {c}$, so ${sp.latex(sub)} = {c}$ and $x = {nice_number(sol[0])}$. "
            f"Then $y = {sp.latex(m)}({nice_number(sol[0])}){' + ' if intercept >= 0 else ' - '}{abs(intercept)} = {nice_number(sol[1])}$."
        ).replace("+ -", "- ")
    rows = [equation(a, b, c), first]
    rng.shuffle(rows)
    return Spec(
        prompt=f"Solve the system by substitution.\n\n{system(*rows)}",
        answer=show_pair(sol),
        kind="numbers",
        ordered=True,
        expected=list(sol),
        distractors=[tuple(sol[::-1]), (sol[0], -sol[1]), (-sol[0], sol[1]), (sol[0] + 1, sol[1] - 1)],
        input_hint=PAIR_HINT,
        explanation=steps.replace("+ -", "- "),
    )


# ---------------------------------------------------------------- 7. elimination


@generator("elimination-method", "Solving by elimination (addition)")
def elimination_method(rng: random.Random) -> Spec:
    variant = rng.choice(["opposites", "multiply-one", "multiply-one", "multiply-both"])
    while True:
        sol = (solution_value(rng), solution_value(rng))
        a1, b1 = nonzero(rng, -7, 8), nonzero(rng, -7, 8)
        if variant == "opposites":
            a2, b2 = nonzero(rng, -7, 8), -b1
        elif variant == "multiply-one":
            k = rng.choice([2, 3, 4, -2, -3])
            a2, b2 = nonzero(rng, -7, 8), b1 * k
        else:
            a2, b2 = nonzero(rng, -7, 8), nonzero(rng, -7, 8)
            if abs(b1) == abs(b2) or b2 % b1 == 0 or b1 % b2 == 0:
                continue
        rows = [(a1, b1, a1 * sol[0] + b1 * sol[1]), (a2, b2, a2 * sol[0] + b2 * sol[1])]
        if independent(rows) and integer_rhs(rows):
            break

    (a1, b1, c1), (a2, b2, c2) = rows
    lcm = math.lcm(abs(b1), abs(b2))
    k1, k2 = lcm // abs(b1), lcm // abs(b2)
    if (b1 > 0) == (b2 > 0):
        k2 = -k2
    new_x = k1 * a1 + k2 * a2
    new_c = k1 * c1 + k2 * c2
    if k1 == 1 and k2 == 1:
        plan = "The $y$ terms are already opposites, so add the equations"
    elif k1 == 1:
        plan = f"Multiply the second equation by ${k2}$ so the $y$ terms are opposites, then add"
    elif k2 == 1:
        plan = f"Multiply the first equation by ${k1}$ so the $y$ terms are opposites, then add"
    else:
        plan = f"Multiply the first equation by ${k1}$ and the second by ${k2}$ so the $y$ terms are opposites, then add"
    return Spec(
        prompt=f"Solve the system using the addition (elimination) method.\n\n{system(equation(a1, b1, c1), equation(a2, b2, c2))}",
        answer=show_pair(sol),
        kind="numbers",
        ordered=True,
        expected=list(sol),
        distractors=[tuple(sol[::-1]), (sol[0], -sol[1]), (-sol[0], sol[1]), (-sol[0], -sol[1])],
        input_hint=PAIR_HINT,
        explanation=(
            f"{plan}: ${new_x}x = {new_c}$, so $x = {nice_number(sol[0])}$. "
            f"Substitute into the first equation: ${a1}({nice_number(sol[0])}) + {b1}y = {c1}$, so $y = {nice_number(sol[1])}$."
        ).replace("+ -", "- "),
    )


# ---------------------------------------------------------------- 8. types of systems


SYSTEM_TYPES = [
    "Independent: one solution",
    "Dependent: infinitely many solutions",
    "Inconsistent: no solution",
]


@generator("types-of-systems", "Types of systems")
def types_of_systems(rng: random.Random) -> Spec:
    kind = rng.choice(SYSTEM_TYPES)
    sol = (sp.Integer(rng.randint(-5, 6)), sp.Integer(rng.randint(-5, 6)))
    a1, b1 = nonzero(rng, -6, 7), nonzero(rng, -6, 7)
    c1 = a1 * sol[0] + b1 * sol[1]
    k = rng.choice([2, 3, -1, -2, 4])
    if kind == SYSTEM_TYPES[0]:
        while True:
            a2, b2 = nonzero(rng, -6, 7), nonzero(rng, -6, 7)
            if a1 * b2 - a2 * b1 != 0:
                break
        c2 = a2 * sol[0] + b2 * sol[1]
        why = f"Different slopes (${sp.latex(sp.Rational(-a1, b1))}$ and ${sp.latex(sp.Rational(-a2, b2))}$), so the lines cross exactly once."
    elif kind == SYSTEM_TYPES[1]:
        a2, b2, c2 = k * a1, k * b1, k * c1
        why = f"The second equation is the first multiplied by ${k}$ - they're the same line, so every point on it is a solution."
    else:
        a2, b2 = k * a1, k * b1
        c2 = k * c1 + nonzero(rng, -6, 6)
        why = (
            f"Same slope (${sp.latex(sp.Rational(-a1, b1))}$) but different $y$-intercepts "
            f"(${sp.latex(sp.Rational(c1, b1))}$ and ${sp.latex(sp.Rational(c2, b2))}$): parallel lines that never meet."
        )
    rows = [equation(a1, b1, c1), equation(a2, b2, c2)]
    if rng.random() < 0.35 and sp.Rational(c1, b1).is_Integer and sp.Rational(a1, b1).is_Integer:
        rows[0] = f"y = {sp.latex(sp.Rational(-a1, b1) * x + sp.Rational(c1, b1))}"
    return Spec(
        prompt=f"What type of system is this?\n\n{system(*rows)}",
        answer=kind,
        kind="choice",
        choices=SYSTEM_TYPES,
        explanation=why + " Tip: put both in $y = mx + b$ form and compare slopes, then intercepts.",
    )


# ---------------------------------------------------------------- 9. word problems


@generator("system-word-problems", "Word problems with systems")
def system_word_problems(rng: random.Random) -> Spec:
    variant = rng.choice(["current", "current", "tickets", "break-even"])

    if variant == "current":
        vehicle, helper, unit = rng.choice([("boat", "current", "mph"), ("plane", "wind", "mph"), ("kayak", "current", "mph")])
        if vehicle == "plane":
            speed, extra = rng.randrange(200, 600, 25), rng.randrange(10, 80, 5)
        else:
            speed, extra = rng.randint(6, 30), rng.randint(1, 5)
        t1, t2 = rng.choice([(2, 3), (3, 4), (3, 5), (4, 5), (4, 6), (2, 4), (4, 10), (5, 6)])
        d1, d2 = (speed + extra) * t1, (speed - extra) * t2
        trip = (
            f"A {vehicle} travels {d1:,} miles with the {helper} in {t1} hours. "
            f"The return trip against the {helper}, {d2:,} miles, takes {t2} hours."
        )
        if rng.random() < 0.4:
            return Spec(
                prompt=f"{trip} If $x$ is the {vehicle}'s speed in still {'air' if vehicle == 'plane' else 'water'} and $y$ is the {helper}'s speed, which system represents the situation?",
                answer=system(f"(x + y)({t1}) = {d1}", f"(x - y)({t2}) = {d2}"),
                kind="choice",
                distractors=[
                    system(f"(x + y)({t2}) = {d1}", f"(x - y)({t1}) = {d2}"),
                    system(f"(x - y)({t1}) = {d1}", f"(x + y)({t2}) = {d2}"),
                    system(f"(x + y)({d1}) = {t1}", f"(x - y)({d2}) = {t2}"),
                ],
                explanation=f"Rate · time = distance. With the {helper} the speeds add ($x + y$); against it they subtract ($x - y$).",
            )
        return Spec(
            prompt=f"{trip} Find the {vehicle}'s speed in still {'air' if vehicle == 'plane' else 'water'} and the speed of the {helper}, as ({vehicle} speed, {helper} speed).",
            answer=show_pair((speed, extra)),
            kind="numbers",
            ordered=True,
            expected=[sp.Integer(speed), sp.Integer(extra)],
            distractors=[(extra, speed), (speed + extra, extra), (speed, speed - extra)],
            input_hint=f"({vehicle} speed, {helper} speed), e.g. (12, 3)",
            explanation=(
                f"$(x + y)({t1}) = {d1}$ gives $x + y = {speed + extra}$. $(x - y)({t2}) = {d2}$ gives $x - y = {speed - extra}$. "
                f"Add: $2x = {2 * speed}$, so $x = {speed}$ {unit} and $y = {extra}$ {unit}."
            ),
        )

    if variant == "tickets":
        event, a_name, b_name = rng.choice([("school play", "adult", "child"), ("concert", "floor", "balcony"), ("museum", "adult", "student")])
        pa = rng.choice([12, 15, 20, 25, 45])
        pb = rng.choice([p for p in [5, 7, 8, 10, 12, 30] if p < pa])
        na, nb = rng.randint(10, 200), rng.randint(10, 200)
        total, money_in = na + nb, pa * na + pb * nb
        return Spec(
            prompt=(
                f"A {event} sold {total} tickets: {a_name} tickets at {money(pa)} and {b_name} tickets at {money(pb)}. "
                f"It took in {money(money_in)}. How many {a_name} tickets were sold?"
            ),
            answer=f"${na}$",
            kind="numbers",
            expected=[sp.Integer(na)],
            distractors=[[nb], [na + 10], [sp.nsimplify(sp.Rational(money_in, pa + pb))], [na - 5]],
            input_hint="Number only",
            explanation=(
                f"Count: $a + b = {total}$. Money: ${pa}a + {pb}b = {money_in}$. Substitute $b = {total} - a$: "
                f"${pa}a + {pb}({total} - a) = {money_in}$, so ${pa - pb}a = {money_in - pb * total}$ and $a = {na}$."
            ),
        )

    unit_cost = rng.choice([2, 3, 4, 5, 6, 8])
    price = unit_cost + rng.choice([3, 4, 5, 6, 8, 10])
    count = rng.choice([50, 80, 100, 120, 150, 200, 250])
    fixed = (price - unit_cost) * count
    item = rng.choice(["candle", "T-shirt", "meal", "mug", "poster"])
    return Spec(
        prompt=(
            f"A business spends {money(fixed)} on setup plus {money(unit_cost)} per {item}, and sells each {item} for {money(price)}. "
            f"How many must it sell to break even?"
        ),
        answer=f"${count}$",
        kind="numbers",
        expected=[sp.Integer(count)],
        distractors=[[sp.nsimplify(sp.Rational(fixed, price))], [sp.nsimplify(sp.Rational(fixed, price + unit_cost))], [count + 10], [count - 10]],
        input_hint="Number only",
        explanation=(
            f"Cost: $y = {unit_cost}x + {fixed}$. Revenue: $y = {price}x$. Break-even is where they're equal: "
            f"${price}x = {unit_cost}x + {fixed}$, so ${price - unit_cost}x = {fixed}$ and $x = {count}$."
        ),
    )
