"""Section 1, Module 3 - Functions and Composition."""

from __future__ import annotations

import random

import sympy as sp

from ..core.problem import Spec, generator
from ..core.symbols import SYMS, coef_tex, fmt_linear, fmt_num, nonzero, tex, x

YES_NO = ["Yes", "No"]


def _set_tex(values) -> str:
    return "$\\{" + ", ".join(str(v) for v in sorted(set(values))) + "\\}$"


def _pairs_tex(pairs) -> str:
    return "$\\{" + ", ".join(f"({a}, {b})" for a, b in pairs) + "\\}$"


def _table(rows: dict[str, list], header: str = "x", domain=None) -> str:
    domain = domain if domain is not None else list(range(1, len(next(iter(rows.values()))) + 1))
    lines = [
        f"| ${header}$ | " + " | ".join(str(v) for v in domain) + " |",
        "|" + "---|" * (len(domain) + 1),
    ]
    for name, values in rows.items():
        lines.append(f"| ${name}$ | " + " | ".join(str(v) for v in values) + " |")
    return "\n".join(lines)


# ---------------------------------------------------------------- 1. domain and range


@generator("relations-domain-range", "Domain and range")
def relations_domain_range(rng: random.Random) -> Spec:
    count = rng.randint(4, 6)
    xs = [rng.randint(-5, 9) for _ in range(count)]
    if rng.random() < 0.5:
        xs[-1] = xs[0]  # a repeated input
    pairs = [(xv, rng.randint(-5, 12)) for xv in xs]
    rng.shuffle(pairs)
    domain = sorted({p[0] for p in pairs})
    range_ = sorted({p[1] for p in pairs})
    ask_domain = rng.random() < 0.5
    want, other = (domain, range_) if ask_domain else (range_, domain)
    label = "domain" if ask_domain else "range"

    distractors = [_set_tex(other), _set_tex(want[:-1]) if len(want) > 1 else _set_tex(other + [0])]
    distractors.append(_set_tex(sorted(set(want) | {other[0]})) if other[0] not in want else _set_tex(want + [max(want) + 1]))
    distractors.append(_set_tex(sorted(set(domain) | set(range_))))
    return Spec(
        prompt=f"What is the **{label}** of the relation {_pairs_tex(pairs)}?",
        answer=_set_tex(want),
        kind="numbers",
        expected=want,
        distractors=distractors,
        input_hint="List the values separated by commas, e.g. 1, 2, 5",
        explanation=(
            f"The {label} is the set of all {'first ($x$)' if ask_domain else 'second ($y$)'} values, "
            "each listed once."
        ),
    )


# ---------------------------------------------------------------- 2. is it a function?


def _lin(coef: int, var: str) -> str:
    return f"{coef_tex(coef)}{var}"


@generator("identifying-functions", "Is it a function?")
def identifying_functions(rng: random.Random) -> Spec:
    if rng.random() < 0.45:
        count = rng.randint(4, 6)
        xs = rng.sample(range(-5, 8), count)
        pairs = [(xv, rng.randint(-5, 10)) for xv in xs]
        is_fn = rng.random() < 0.5
        if not is_fn:
            dup = pairs[rng.randrange(count)][0]
            new_y = rng.choice([v for v in range(-5, 11) if v != dict(pairs)[dup]])
            pairs.append((dup, new_y))
        elif rng.random() < 0.5:
            # repeated outputs are fine - a good trap
            pairs[-1] = (pairs[-1][0], pairs[0][1])
        rng.shuffle(pairs)
        if is_fn:
            why = "Every input ($x$-value) appears only once, so each input has exactly one output. Repeated outputs are allowed."
        else:
            outs = sorted(b for a, b in pairs if a == dup)
            why = f"The input ${dup}$ is paired with more than one output ({', '.join(map(str, outs))}), so this is not a function."
        return Spec(
            prompt=f"Does {_pairs_tex(pairs)} represent a function?",
            answer="Yes" if is_fn else "No",
            kind="choice",
            choices=YES_NO,
            explanation=why,
        )

    a, b, c = rng.randint(2, 9), rng.randint(2, 9), rng.randint(1, 20)
    d = rng.randint(2, 9)
    while d == b:
        d = rng.randint(2, 9)
    equations = [
        (f"{a}x + {b}y = {c}", True, f"Solving for $y$ gives $y = {sp.latex(sp.Rational(c, b) - sp.Rational(a, b) * x)}$ - one output per input."),
        (f"y^2 + {a}x = {c}", False, f"Solving gives $y = \\pm\\sqrt{{{c} - {a}x}}$ - two outputs for most inputs."),
        (f"{a}y^3 - {b}x = x^2 + {c}", True, "Solving for $y$ needs a cube root, which has only one value."),
        (f"x^2 + y^2 = {c * c}", False, "This is a circle. Solving gives $y = \\pm\\sqrt{" + str(c * c) + " - x^2}$ - two outputs."),
        (f"x = {c}", False, f"This is a vertical line: the input ${c}$ has infinitely many outputs."),
        (f"y = {a}x^2 - {c}", True, "Squaring $x$ is fine - each $x$ still gives one $y$."),
        (f"x^2 + {_lin(a, 'y')} - {c} = {b}x", True, "$y$ appears only to the first power, so solving gives exactly one $y$."),
        (f"{a}y^4 = x + {c}", False, "Solving needs an even (4th) root, which gives $\\pm$ - two outputs."),
        (f"{a}x + {b}y = {d}y - {c}x", True, "$y$ appears only to the first power, so solving gives exactly one $y$."),
        (f"y^2 - {a}x = x^2 + {c}", False, "Solving for $y$ needs a square root, which gives $\\pm$ - two outputs."),
    ]
    equation, is_fn, why = rng.choice(equations)
    return Spec(
        prompt=f"Does the equation ${equation}$ represent $y$ as a function of $x$?",
        answer="Yes" if is_fn else "No",
        kind="choice",
        choices=YES_NO,
        explanation=why,
    )


# ---------------------------------------------------------------- 3. function notation


CONTEXTS = [
    {
        "setup": "$C(g)$ is the monthly cost, in dollars, of a phone plan that uses $g$ GB of data.",
        "fn": "C", "ins": (2, 50), "outs": (20, 150),
        "right": "Using {a} GB of data in a month costs \\${b}.",
        "wrong": ["Using {b} GB of data in a month costs \\${a}.", "Each extra {a} GB of data costs \\${b} more.",
                  "Using {a} GB of data saves \\${b} a month."],
        "sentence": "Using {a} GB of data costs \\${b}.",
    },
    {
        "setup": "$P(t)$ is the population of a town $t$ years after 2020.",
        "fn": "P", "ins": (1, 15), "outs": (1000, 50000),
        "right": "In {year}, the town's population was {b:,}.",
        "wrong": ["In {b:,}, the town's population was {a}.", "In {year}, the population grew by {b:,}.",
                  "{a} years ago, the population was {b:,}."],
        "sentence": "{a} years after 2020, the population is {b:,}.",
    },
    {
        "setup": "$W(d)$ is the number of gallons of water a garden needs on day $d$ of summer.",
        "fn": "W", "ins": (2, 90), "outs": (5, 60),
        "right": "On day {a}, the garden needs {b} gallons of water.",
        "wrong": ["On day {b}, the garden needs {a} gallons of water.", "Over {a} days, the garden needs {b} gallons in total.",
                  "The garden needs {b} more gallons on day {a} than the day before."],
        "sentence": "On day {a}, the garden needs {b} gallons.",
    },
    {
        "setup": "$S(n)$ is the number of students enrolled in grade $n$ at a school.",
        "fn": "S", "ins": (1, 12), "outs": (80, 400),
        "right": "There are {b} students in grade {a}.",
        "wrong": ["There are {a} students in grade {b}.", "Grade {a} has {b} more students than the grade before.",
                  "There are {b} grades with {a} students each."],
        "sentence": "Grade {a} has {b} students.",
    },
    {
        "setup": "$H(a)$ is a child's height, in centimeters, at age $a$ years.",
        "fn": "H", "ins": (2, 14), "outs": (80, 165),
        "right": "At age {a}, the child is {b} cm tall.",
        "wrong": ["At age {b}, the child is {a} cm tall.", "The child grew {b} cm by age {a}.",
                  "The child grows {b} cm every {a} years."],
        "sentence": "At age {a}, the child is {b} cm tall.",
    },
]


@generator("function-notation", "Function notation in context")
def function_notation(rng: random.Random) -> Spec:
    ctx = rng.choice(CONTEXTS)
    a = rng.randint(*ctx["ins"])
    b = rng.randint(*ctx["outs"])
    if ctx["fn"] == "P":
        b = round(b, -2)
    fill = {"a": a, "b": b, "year": 2020 + a}
    fn = ctx["fn"]
    if rng.random() < 0.65:
        return Spec(
            prompt=f"{ctx['setup']} What does ${fn}({a}) = {fmt_num(b)}$ mean?",
            answer=ctx["right"].format(**fill),
            kind="choice",
            distractors=[w.format(**fill) for w in ctx["wrong"]],
            explanation=f"The number inside the parentheses, ${a}$, is the input. The number on the other side, ${fmt_num(b)}$, is the output.",
        )
    return Spec(
        prompt=f"{ctx['setup']} Write this statement in function notation: “{ctx['sentence'].format(**fill)}”",
        answer=f"${fn}({a}) = {fmt_num(b)}$",
        kind="choice",
        distractors=[f"${fn}({fmt_num(b)}) = {a}$", f"${a}{fn} = {fmt_num(b)}$", f"${fn} = {a}({fmt_num(b)})$", f"${fn}({a} + {fmt_num(b)})$"],
        explanation=f"The input (${a}$) goes inside the parentheses and the output (${fmt_num(b)}$) goes on the other side of the equals sign.",
    )


# ---------------------------------------------------------------- 4. types of functions


FAMILIES = ["Linear", "Quadratic", "Rational", "Radical"]


@generator("types-of-functions", "Function families")
def types_of_functions(rng: random.Random) -> Spec:
    a, b, c = nonzero(rng, -6, 6), nonzero(rng, -9, 9), nonzero(rng, -9, 9)
    k = rng.randint(2, 9)
    options = {
        "Linear": [
            (a * x + b, "The highest power of $x$ is 1, so the graph is a straight line."),
            (sp.Integer(b) - k * x, "The highest power of $x$ is 1, so the graph is a straight line."),
        ],
        "Quadratic": [
            (a * x**2 + b * x + c, "The highest power of $x$ is 2 - a parabola."),
            (x**2 / k, "$x$ is only in the numerator, so this is just $\\frac{1}{" + str(k) + "}x^2$ - a quadratic, not a rational function."),
        ],
        "Rational": [
            (sp.Integer(k) / (x + b), "$x$ is in the denominator of a fraction of polynomials."),
            ((x - k) / (x + b), "$x$ is in the denominator of a fraction of polynomials."),
            (a * x / (x**2 - k * k), "$x$ is in the denominator of a fraction of polynomials."),
        ],
        "Radical": [
            (sp.sqrt(k * x + abs(b)), "$x$ is under a square root."),
            (sp.sqrt(x) + b, "$x$ is under a square root."),
            (sp.cbrt(x - k), "$x$ is under a cube root."),
        ],
    }
    family = rng.choice(FAMILIES)
    expr, why = rng.choice(options[family])
    return Spec(
        prompt=f"What type of function is $f(x) = {sp.latex(expr)}$?",
        answer=family,
        kind="choice",
        choices=FAMILIES,
        explanation=why,
    )


# ---------------------------------------------------------------- 5. asymptotes


def _lines(var: str, values) -> str:
    values = sorted(set(values))
    if not values:
        return "None"
    return " and ".join(f"${var} = {sp.latex(v)}$" for v in values)


@generator("asymptotes", "Asymptotes of rational functions")
def asymptotes(rng: random.Random) -> Spec:
    while True:
        den_kind = rng.choice(["linear", "linear", "difference", "no-real"])
        lead_d = rng.randint(1, 4)
        if den_kind == "linear":
            root = nonzero(rng, -6, 6)
            den = sp.expand(lead_d * (x - root))
            roots = [root]
        elif den_kind == "difference":
            root = rng.randint(1, 5)
            den = sp.expand(lead_d * (x**2 - root**2))
            roots = [root, -root]
        else:
            den = sp.expand(lead_d * x**2 + rng.randint(1, 9))
            roots = []
        num_deg = rng.choice([0, 1, 2]) if sp.degree(den, x) == 2 else rng.choice([0, 1, 1, 2])
        lead_n = nonzero(rng, -6, 6)
        num = lead_n * x**num_deg + (rng.randint(-9, 9) if num_deg else 0)
        num = sp.expand(num)
        if all(num.subs(x, r) != 0 for r in roots):
            break

    den_deg = sp.degree(den, x)
    shown = f"f(x) = \\dfrac{{{sp.latex(num)}}}{{{sp.latex(den)}}}"
    lead_d_full = sp.Poly(den, x).LC()

    if rng.random() < 0.5:
        plain = sp.Symbol("X")
        num_roots = [r for r in sp.solve(num.subs(x, plain), plain) if r.is_real and r.is_Rational] if num_deg else []
        candidates = [_lines("x", [-r for r in roots]) if roots else "$x = 0$", "None", "$x = 0$"]
        candidates += [_lines("x", num_roots)] if num_roots else []
        candidates += [_lines("x", [roots[0]]) if len(roots) == 2 else _lines("x", [-1, 1]), f"$x = {lead_d}$"]
        return Spec(
            prompt=f"Find the **vertical** asymptote(s) of ${shown}$.",
            answer=_lines("x", roots),
            kind="choice",
            distractors=candidates,
            explanation=(
                f"Set the denominator equal to 0: ${sp.latex(den)} = 0$ gives " + _lines("x", roots) + "."
                if roots
                else f"The denominator ${sp.latex(den)}$ is never 0 (it's always positive), so there's no vertical asymptote."
            ),
        )

    if num_deg < den_deg:
        answer = "$y = 0$"
        why = "The denominator has the higher power, so the fraction shrinks toward 0 as $x$ grows: $y = 0$."
    elif num_deg == den_deg:
        ratio = sp.Rational(lead_n, lead_d_full)
        answer = f"$y = {sp.latex(ratio)}$"
        why = f"The highest powers match, so divide the leading coefficients: $y = \\frac{{{lead_n}}}{{{lead_d_full}}} = {sp.latex(ratio)}$."
    else:
        answer = "No horizontal asymptote"
        why = "The numerator has the higher power, so the function keeps growing - no horizontal asymptote."
    candidates = [
        "$y = 0$",
        f"$y = {sp.latex(sp.Rational(lead_d_full, lead_n))}$",
        f"$y = {lead_n}$",
        "No horizontal asymptote",
        f"$y = {sp.latex(sp.Rational(lead_n, lead_d_full))}$",
        "$y = 1$",
        f"$y = {-lead_n}$",
        "$y = -1$",
        f"$y = {lead_n + lead_d}$",
    ]
    return Spec(
        prompt=f"Find the **horizontal** asymptote of ${shown}$.",
        answer=answer,
        kind="choice",
        distractors=candidates,
        explanation=why,
    )


# ---------------------------------------------------------------- 6. evaluating


def _negative_square_slip(f, val):
    """Evaluate f(val) the wrong way, treating (-3)^2 as -9."""
    total = 0
    for term in sp.Add.make_args(f):
        coeff, deg = term.as_coeff_exponent(x)
        if deg > 0 and deg % 2 == 0:
            total += coeff * -(abs(val) ** deg)
        else:
            total += term.subs(x, val)
    return total


@generator("evaluating-functions", "Evaluating functions")
def evaluating_functions(rng: random.Random) -> Spec:
    if rng.random() < 0.5:
        A, B, C = nonzero(rng, -4, 4), nonzero(rng, -9, 9), rng.randint(-9, 9)
        cubic = rng.random() < 0.3
        if cubic:
            f = -(x**3) + A * x**2 + B * x + C if rng.random() < 0.5 else x**3 + A * x + C
        else:
            f = A * x**2 + B * x + C
        val = nonzero(rng, -4, 4)
        correct = f.subs(x, val)
        distractors = [
            [f.subs(x, -val)],
            [correct + 1],
            [correct - 2 * (B * val)] if not cubic else [correct + 2],
            [_negative_square_slip(f, val)] if val < 0 else [correct - 1],
            [f.subs(x, val) - C] if C else [correct - 3],
        ]
        return Spec(
            prompt=f"Let $f(x) = {sp.latex(f)}$. Find $f({val})$.",
            answer=f"${correct}$",
            kind="numbers",
            expected=[correct],
            distractors=distractors,
            explanation=(
                f"Replace every $x$ with $({val})$ - parentheses included: "
                f"$f({val}) = {sp.latex(f.subs(x, sp.Symbol('(' + str(val) + ')')))} = {correct}$."
            ),
        )

    var = rng.choice(["a", "c", "k", "t"])
    sym = SYMS[var]
    variant = rng.choice(["linear", "quadratic", "scaled"])
    if variant == "linear":
        A, B = nonzero(rng, -7, 7), nonzero(rng, -9, 9)
        h = nonzero(rng, -6, 6)
        f = A * x + B
        inp = sym + h
        correct = sp.expand(A * inp + B)
        distractors = [A * sym + h + B, A * sym + B, sp.expand(A * inp - B), sp.expand(inp + B)]
        why = f"Replace $x$ with $({sp.latex(inp)})$ and distribute: ${A}({sp.latex(inp)}) {'+' if B > 0 else '-'} {abs(B)} = {sp.latex(correct)}$."
    elif variant == "quadratic":
        B, C = rng.randint(-6, 6), rng.randint(-9, 9)
        h = nonzero(rng, -5, 5)
        lead = rng.choice([1, 1, -1, 2])
        f = lead * x**2 + B * x + C
        inp = x + h
        correct = sp.expand(lead * inp**2 + B * inp + C)
        distractors = [
            sp.expand(lead * (x**2 + h**2) + B * inp + C),
            sp.expand(lead * inp**2 + B * x + C),
            sp.expand(lead * (x**2 + h * x + h**2) + B * inp + C),
            sp.expand(-lead * inp**2 + B * inp + C) if lead < 0 else sp.expand(lead * inp**2 + B * inp - C) if C else sp.expand(correct + 1),
        ]
        why = (
            f"Replace every $x$ with $({sp.latex(inp)})$: ${sp.latex(f.subs(x, sp.Symbol('(' + sp.latex(inp) + ')')))}$. "
            f"Remember $({sp.latex(inp)})^2 = {sp.latex(sp.expand(inp**2))}$ - don't drop the middle term. "
            f"Result: ${sp.latex(correct)}$."
        )
    else:
        A, C = rng.choice([1, 2, 3, -1]), rng.randint(1, 30)
        kk = rng.randint(2, 5)
        f = C - A * x**2 if rng.random() < 0.5 else A * x**2 + C
        inp = kk * sym
        correct = sp.expand(f.subs(x, inp))
        distractors = [sp.expand(f.subs(x, sym) * kk), sp.expand(f.subs(x**2, kk * sym**2)), sp.expand(correct + 2 * C) if C else correct + 1, sp.expand(f.subs(x, sym) + kk)]
        why = f"Replace $x$ with $({sp.latex(inp)})$. The {kk} gets squared too: $({sp.latex(inp)})^2 = {sp.latex(inp**2)}$. Result: ${sp.latex(correct)}$."
    return Spec(
        prompt=f"Let $f(x) = {sp.latex(f)}$. Find $f({sp.latex(inp)})$ and simplify.",
        answer=tex(correct),
        kind="expr",
        expected=correct,
        distractors=distractors,
        form="expanded",
        input_hint=f"Your answer will be in terms of {'x' if variant == 'quadratic' else var}",
        explanation=why,
    )


# ---------------------------------------------------------------- 7. composition


@generator("function-composition", "Composing functions")
def function_composition(rng: random.Random) -> Spec:
    if rng.random() < 0.55:
        domain = list(range(1, 6))
        f = [rng.randint(1, 5) for _ in domain]
        g = [rng.randint(1, 5) for _ in domain]
        fns = {"f": dict(zip(domain, f)), "g": dict(zip(domain, g))}
        outer, inner = rng.choice([("f", "g"), ("g", "f"), ("f", "f"), ("g", "g")])
        start = rng.choice(domain)
        mid = fns[inner][start]
        correct = fns[outer][mid]
        swapped = fns[inner][fns[outer][start]]
        return Spec(
            prompt=f"Use the table to find ${outer}({inner}({start}))$.\n\n" + _table({"f(x)": f, "g(x)": g}),
            answer=f"${correct}$",
            kind="numbers",
            expected=[correct],
            distractors=[[swapped], [mid], [fns[outer][start]], [start], [fns[inner][mid]]],
            explanation=f"Work inside out: ${inner}({start}) = {mid}$, then ${outer}({mid}) = {correct}$.",
        )

    # one function as an equation, one as a table
    domain = sorted(rng.sample(range(-3, 7), 5))
    g_vals = [rng.randint(-5, 9) for _ in domain]
    g = dict(zip(domain, g_vals))
    table = _table({"g(x)": g_vals}, domain=domain)
    if rng.random() < 0.5:
        # f(g(a)) where f is an equation
        A, B = nonzero(rng, -4, 6), rng.randint(-9, 9)
        f_expr = rng.choice([A * x + B, x**2 + B])
        start = rng.choice(domain)
        mid = g[start]
        correct = f_expr.subs(x, mid)
        wrong_order = f_expr.subs(x, start)
        return Spec(
            prompt=f"Let $f(x) = {sp.latex(f_expr)}$ and use the table for $g$. Find $f(g({start}))$.\n\n{table}",
            answer=f"${correct}$",
            kind="numbers",
            expected=[correct],
            distractors=[[wrong_order], [mid], [g.get(int(wrong_order), correct + 3)], [correct + 1], [correct - 2]],
            explanation=f"Inner first, from the table: $g({start}) = {mid}$. Then the equation: $f({mid}) = {sp.latex(f_expr.subs(x, sp.Symbol('(' + str(mid) + ')')))} = {correct}$.",
        )
    # g(f(a)) where f is an equation - make sure f(a) lands in the table
    A = rng.choice([1, 2, -1, 3])
    start = rng.randint(-3, 5)
    target = rng.choice(domain)
    B = target - A * start
    if A == 1 and B == 0:  # f(x) = x would make the question trivial
        A, B = 2, target - 2 * start
    f_expr = A * x + B
    correct = g[target]
    return Spec(
        prompt=f"Let $f(x) = {sp.latex(f_expr)}$ and use the table for $g$. Find $g(f({start}))$.\n\n{table}",
        answer=f"${correct}$",
        kind="numbers",
        expected=[correct],
        distractors=[[target], [f_expr.subs(x, g.get(start, start))], [g.get(start, correct + 2)], [correct + 1], [correct - 1]],
        explanation=f"Inner first, from the equation: $f({start}) = {target}$. Then the table: $g({target}) = {correct}$.",
    )


# ---------------------------------------------------------------- 8. decomposing


def _decompositions(rng: random.Random):
    a, b = rng.randint(2, 5), nonzero(rng, -9, 9)
    n = rng.randint(2, 5)
    k = rng.randint(1, 9)
    return rng.choice(
        [
            (a * x + b, x**n),
            (a * x + b, sp.sqrt(x)),
            (x**2 + k, 1 / x),
            (x - k, x**2 + b),
            (x - k, sp.Integer(a) / x**2),
            (x**2 + k, sp.sqrt(x)),
            (x + k, 1 / x),
        ]
    )


@generator("decomposing-functions", "Decomposing functions")
def decomposing_functions(rng: random.Random) -> Spec:
    inner, outer = _decompositions(rng)
    h = outer.subs(x, inner)
    variant = rng.choice(["find-f", "find-g", "pair"])

    def composes(f_expr, g_expr):
        return sp.simplify(f_expr.subs(x, g_expr) - h) == 0

    if variant == "find-f":
        candidates = [h, outer.subs(x, x + 1), outer.subs(x, inner).subs(x, x**2), outer + inner, outer * 2]
        distractors = [f"$f(x) = {sp.latex(c)}$" for c in candidates if not composes(c, inner)]
        return Spec(
            prompt=f"If $g(x) = {sp.latex(inner)}$, which $f(x)$ makes $f(g(x)) = {sp.latex(h)}$?",
            answer=f"$f(x) = {sp.latex(outer)}$",
            kind="choice",
            distractors=distractors,
            explanation=f"$g(x)$ is the part that gets calculated first. Replace it with $x$ in $h$: $f(x) = {sp.latex(outer)}$. Check: $f(g(x)) = {sp.latex(h)}$.",
        )
    if variant == "find-g":
        candidates = [h, outer, -inner, inner + 1, inner**2]
        distractors = [f"$g(x) = {sp.latex(c)}$" for c in candidates if not composes(outer, c)]
        return Spec(
            prompt=f"If $f(x) = {sp.latex(outer)}$, which $g(x)$ makes $f(g(x)) = {sp.latex(h)}$?",
            answer=f"$g(x) = {sp.latex(inner)}$",
            kind="choice",
            distractors=distractors,
            explanation=f"Look at what's been plugged into $f$'s pattern: $g(x) = {sp.latex(inner)}$. Check: $f(g(x)) = {sp.latex(h)}$.",
        )
    candidates = [(inner, outer), (x, inner), (outer, x + 1), (h, inner), (outer + 1, inner)]
    distractors = [f"$f(x) = {sp.latex(f_)}$, $g(x) = {sp.latex(g_)}$" for f_, g_ in candidates if not composes(f_, g_)]
    return Spec(
        prompt=f"Which pair of functions gives $f(g(x)) = {sp.latex(h)}$?",
        answer=f"$f(x) = {sp.latex(outer)}$, $g(x) = {sp.latex(inner)}$",
        kind="choice",
        distractors=distractors,
        explanation=f"Ask what you'd calculate first: ${sp.latex(inner)}$ is the inner function $g$, and what happens to it afterward is the outer function $f(x) = {sp.latex(outer)}$.",
    )


# ---------------------------------------------------------------- 9. composition models


SHAPES = [
    ("A circular puddle spreads out", "radius", "area", lambda r: sp.pi * r**2, "A = \\pi r^2", 2),
    ("Ripples from a stone spread out in circles", "radius", "circumference", lambda r: 2 * sp.pi * r, "C = 2\\pi r", 1),
    ("A square garden bed is being expanded", "side length", "area", lambda s: s**2, "A = s^2", 2),
    ("A cube-shaped balloon sculpture is being inflated", "side length", "volume", lambda s: s**3, "V = s^3", 3),
    ("A spherical balloon is being inflated", "radius", "volume", lambda r: sp.Rational(4, 3) * sp.pi * r**3, "V = \\frac{4}{3}\\pi r^3", 3),
]

BUSINESS = [
    {
        "who": "A realtor", "inputs": "clients she takes out", "middle": "houses she sells",
        "short": "houses sold", "money": "her commission, in dollars", "goal": "her commission", "unit": "clients",
        "ask": "How much commission, in dollars, does she earn if she takes out {n} clients?",
        "A": [500, 1000, 1500, 2000, 2500], "B": [200, 400, 1000, 1500, 2000],
    },
    {
        "who": "An online store", "inputs": "website visitors", "middle": "orders it gets",
        "short": "orders", "money": "its profit, in dollars", "goal": "its profit", "unit": "website visitors",
        "ask": "How much profit, in dollars, does it make from {n} website visitors?",
        "A": [20, 25, 30, 40, 45], "B": [-20, 10, 30, 50],
    },
    {
        "who": "A tutor", "inputs": "inquiries he gets", "middle": "hours he books",
        "short": "hours booked", "money": "his earnings, in dollars", "goal": "his earnings", "unit": "inquiries",
        "ask": "How much does he earn, in dollars, from {n} inquiries?",
        "A": [25, 30, 40, 45, 60], "B": [0, 10, 20],
    },
]


def _plus(val) -> str:
    if val == 0:
        return ""
    return f" + {fmt_num(val)}" if val > 0 else f" - {fmt_num(-val)}"


@generator("composition-models", "Modeling with composition")
def composition_models(rng: random.Random) -> Spec:
    if rng.random() < 0.5:
        story, dim, quantity, formula, formula_tex, power = rng.choice(SHAPES)
        rate = rng.choice([1, 2, 3, 4, 5, sp.Rational(5, 2), sp.Rational(1, 2)])
        time = rng.randint(2, 10)
        unit = rng.choice(["inches", "centimeters", "feet"])
        r_t = rate * SYMS["t"]
        correct = formula(rate * time)
        units = {1: unit, 2: f"square {unit}", 3: f"cubic {unit}"}[power]
        return Spec(
            prompt=(
                f"{story}. Its {dim} grows by {fmt_num(rate)} {unit} every second. "
                f"What is the exact {quantity}, in {units}, after {time} seconds? (Use ${formula_tex}$.)"
            ),
            answer=tex(correct),
            kind="expr",
            expected=correct,
            distractors=[formula(time) * rate, formula(rate) + time, formula(rate + time), correct * 2, formula(time)],
            input_hint="Leave π in your answer, e.g. 100pi",
            explanation=(
                f"The {dim} after $t$ seconds is ${sp.latex(r_t)}$, so the {quantity} is the composition "
                f"${sp.latex(formula(sp.Symbol('(' + sp.latex(r_t) + ')')))}$. At $t = {time}$ the {dim} is "
                f"${fmt_num(rate * time)}$, giving ${sp.latex(correct)}$."
            ),
        )

    biz = rng.choice(BUSINESS)
    inputs, middle, middle_short, money = biz["inputs"], biz["middle"], biz["short"], biz["money"]
    p = sp.Rational(rng.choice([5, 10, 15, 20, 25, 50]), 100)
    q = sp.Rational(rng.choice([1, 2, 3, 5, 10]), 10)
    A, B = rng.choice(biz["A"]), rng.choice(biz["B"])
    setup = (
        f"{biz['who']} models the number of {middle} with $f(x) = {fmt_linear(p, q)}$, where $x$ is the number of {inputs}. "
        f"Then $g(x) = {fmt_linear(A, B)}$ gives {money}, where $x$ is the number of {middle_short}."
    )
    composite_coef, composite_const = A * p, A * q + B
    if rng.random() < 0.5:
        return Spec(
            prompt=f"{setup} Which function gives {biz['goal']} as a function of the number of {biz['unit']}?",
            answer=f"$g(f(x)) = {fmt_linear(composite_coef, composite_const)}$",
            kind="choice",
            distractors=[
                f"$f(g(x)) = {fmt_linear(p * A, p * B + q)}$",
                f"$g(f(x)) = {fmt_linear(A * p, q + B)}$",
                f"$g(f(x)) = {fmt_linear(A + p, B + q)}$",
                f"$f(g(x)) = {fmt_linear(composite_coef, composite_const)}$",
            ],
            explanation=(
                f"The money depends on {middle_short}, and {middle_short} depend on {inputs}, so $g$ is the outer function: "
                f"$g(f(x)) = {fmt_num(A)}({fmt_linear(p, q)}){_plus(B)} = {fmt_linear(composite_coef, composite_const)}$."
            ),
        )
    count = rng.randint(4, 20)
    correct = A * (p * count + q) + B
    return Spec(
        prompt=f"{setup} {biz['ask'].format(n=count)}",
        answer=f"${fmt_num(correct)}$",
        kind="numbers",
        expected=[correct],
        tolerance=0.005,
        distractors=[[p * (A * count + B) + q], [A * p * count + B], [A * count + B], [correct + A], [A * (p * count) + q + B]],
        input_hint="Type the number only, e.g. 5450",
        explanation=(
            f"Inner first: $f({count}) = {fmt_num(p * count + q)}$ {middle_short}. "
            f"Then $g({fmt_num(p * count + q)}) = {fmt_num(A)}({fmt_num(p * count + q)}){_plus(B)} = {fmt_num(correct)}$."
        ),
    )
