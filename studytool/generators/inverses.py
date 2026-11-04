"""Section 1, Module 4 - Inverse Functions."""

from __future__ import annotations

import random

import sympy as sp

from ..core.problem import Spec, generator
from ..core.symbols import fmt_num, nonzero, tex, x
from .functions import YES_NO, _pairs_tex, _table

INVERSE_HINT = "Use x as the variable, e.g. (x - 8)/3 or cbrt(x - 6) + 4"


def over(num, den):
    """num/den kept as a single fraction for display (SymPy would split (x - 8)/3 into x/3 - 8/3)."""
    if den.is_Number and den < 0:
        num, den = -num, -den
    if den == 1:
        return num
    return sp.Mul(num, sp.Pow(den, -1, evaluate=False), evaluate=False)


def cbrt(expr):
    return sp.Pow(expr, sp.Rational(1, 3))


def _signed(val) -> str:
    """' + 3' or ' - 3' for writing a constant after a term."""
    return f" + {fmt_num(val)}" if val >= 0 else f" - {fmt_num(-val)}"


# ---------------------------------------------------------------- 1. one-to-one


@generator("one-to-one-functions", "One-to-one functions")
def one_to_one_functions(rng: random.Random) -> Spec:
    if rng.random() < 0.3:
        count = rng.randint(4, 6)
        xs = rng.sample(range(-5, 9), count)
        ys = rng.sample(range(-6, 12), count)
        one_to_one = rng.random() < 0.5
        if not one_to_one:
            ys[-1] = ys[0]
        pairs = list(zip(xs, ys))
        rng.shuffle(pairs)
        if one_to_one:
            why = "Every input has one output and every output comes from one input, so it's one-to-one."
        else:
            shared = [a for a, b in pairs if b == ys[0]]
            why = f"The output {ys[0]} comes from two inputs ({shared[0]} and {shared[1]}), so it's a function but not one-to-one."
        return Spec(
            prompt=f"Is the function {_pairs_tex(pairs)} one-to-one?",
            answer="Yes" if one_to_one else "No",
            kind="choice",
            choices=YES_NO,
            explanation=why,
        )

    a, b = nonzero(rng, -7, 7), nonzero(rng, -9, 9)
    k = rng.randint(1, 6)
    options = [
        (sp.latex(a * x + b), True, f"$f(a) = f(b)$ gives ${a}a{_signed(b)} = {a}b{_signed(b)}$, which forces $a = b$."),
        (sp.latex(x**3 + b), True, "$a^3 = b^3$ forces $a = b$ - a cube root has only one value."),
        (f"\\sqrt{{x{_signed(k)}}}", True, "Square roots only output one (non-negative) value per input and never repeat, so it passes the horizontal line test."),
        (f"\\frac{{{abs(a)}}}{{x{_signed(-k)}}}", True, f"$\\frac{{{abs(a)}}}{{a - {k}}} = \\frac{{{abs(a)}}}{{b - {k}}}$ forces $a = b$."),
        (f"\\sqrt[3]{{x}}{_signed(b)}", True, "Cube roots never repeat an output, so $f(a) = f(b)$ forces $a = b$."),
        (f"x^2, \\; x \\geq 0", True, "With only non-negative inputs, no two inputs share an output. Restricting the domain makes $x^2$ one-to-one."),
        (sp.latex(abs(a) * x**2 + b), False, f"$f({k}) = f(-{k})$ - squaring hides the sign, so two inputs share an output."),
        (f"|x{_signed(-k)}|", False, f"$f({k} + 1) = f({k} - 1) = 1$ - two inputs share an output."),
        (sp.latex(x**2 + k * x), False, f"$f(0) = f(-{k}) = 0$ - two inputs share an output."),
        (sp.latex(x**4 + b), False, "$f(1) = f(-1)$ - even powers hide the sign."),
        (f"(x{_signed(-k)})^2", False, f"$f({k} + 1) = f({k} - 1) = 1$ - two inputs share an output."),
    ]
    shown, is_one, why = rng.choice(options)
    return Spec(
        prompt=f"Is $f(x) = {shown}$ one-to-one?",
        answer="Yes" if is_one else "No",
        kind="choice",
        choices=YES_NO,
        explanation=why,
    )


# ---------------------------------------------------------------- 2. inverses from tables and points


@generator("inverse-from-table", "Inverses from tables and points")
def inverse_from_table(rng: random.Random) -> Spec:
    if rng.random() < 0.3:
        a, b = nonzero(rng, -12, 12), nonzero(rng, -12, 12)
        while abs(a) == abs(b):
            b = nonzero(rng, -12, 12)
        name = rng.choice(["f", "g", "h"])
        return Spec(
            prompt=f"${name}$ is one-to-one and $({a}, {b})$ is on its graph. Which point must be on the graph of ${name}^{{-1}}$?",
            answer=f"$({b}, {a})$",
            kind="choice",
            distractors=[f"$({a}, {b})$", f"$({-a}, {-b})$", f"$({-b}, {-a})$", f"$({a}, {-b})$", f"$({b}, {-a})$"],
            explanation=f"An inverse swaps inputs and outputs: $({a}, {b})$ on ${name}$ becomes $({b}, {a})$ on ${name}^{{-1}}$.",
        )

    xs = sorted(rng.sample(range(-5, 16), 5))
    ys = rng.sample(range(-8, 16), 5)
    name = rng.choice(["f", "g"])
    pick = rng.randrange(5)
    target = ys[pick]
    correct = xs[pick]
    forward = dict(zip(xs, ys))
    distractors = [[forward[target]]] if target in forward else []
    distractors += [[ys[(pick + 1) % 5]], [xs[(pick + 1) % 5]], [xs[(pick - 1) % 5]], [-correct]]
    return Spec(
        prompt=f"Use the table to find ${name}^{{-1}}({target})$.\n\n" + _table({f"{name}(x)": ys}, domain=xs),
        answer=f"${correct}$",
        kind="numbers",
        expected=[correct],
        distractors=distractors,
        explanation=(
            f"${name}^{{-1}}({target})$ asks which input gives the output {target}. Find {target} in the "
            f"${name}(x)$ row: ${name}({correct}) = {target}$, so ${name}^{{-1}}({target}) = {correct}$."
        ),
    )


# ---------------------------------------------------------------- 3. domain and range of inverses


@generator("inverse-domain-range", "Domain and range of inverses")
def inverse_domain_range(rng: random.Random) -> Spec:
    p = rng.randint(-6, 3)
    q = p + rng.randint(2, 8)
    r = rng.randint(-10, 4)
    s = r + rng.randint(2, 30)
    shape = rng.choice(["cubic", "root", "line"])
    if rng.random() < 0.5:
        setup = f"The graph of a one-to-one function $f$ runs from $({p}, {r})$ to $({q}, {s})$ and is always rising."
    else:
        setup = f"A one-to-one function $f$ has domain $[{p}, {q}]$ and range $[{r}, {s}]$."
    ask_domain = rng.random() < 0.5
    want = (r, s) if ask_domain else (p, q)
    other = (p, q) if ask_domain else (r, s)
    label = "domain" if ask_domain else "range"
    return Spec(
        prompt=f"{setup} What is the **{label}** of $f^{{-1}}$?",
        answer=f"$[{want[0]}, {want[1]}]$",
        kind="choice",
        distractors=[
            f"$[{other[0]}, {other[1]}]$",
            f"$[{want[1]}, {want[0]}]$",
            f"$({want[0]}, {want[1]})$",
            f"$[{other[0]}, {want[1]}]$",
            f"$[{want[0]}, {other[1]}]$",
        ],
        explanation=(
            f"An inverse swaps inputs and outputs, so the {label} of $f^{{-1}}$ is the "
            f"{'range' if ask_domain else 'domain'} of $f$: $[{want[0]}, {want[1]}]$."
            + (" (The shape of the graph doesn't matter, only its endpoints.)" if shape == "cubic" else "")
        ),
    )


# ---------------------------------------------------------------- 4. verifying inverses


def _linear_pair(rng: random.Random):
    """f, its true inverse, and a near-miss with the composition that exposes it."""
    a, b = nonzero(rng, -9, 9), nonzero(rng, -12, 12)
    while abs(a) == 1:
        a = nonzero(rng, -9, 9)
    f = a * x + b
    true_inv = over(x - b, sp.Integer(a))
    near = rng.choice([over(x + b, sp.Integer(a)), x / a - b, over(b - x, sp.Integer(a))])
    return f, true_inv, near, ("f(g(x))", sp.expand(f.subs(x, near)))


def _cubic_pair(rng: random.Random):
    h, k = nonzero(rng, -8, 8), nonzero(rng, -9, 9)
    f = (x + h) ** 3 + k
    true_inv = cbrt(x - k) - h
    if rng.random() < 0.5:
        near = cbrt(x + k) - h  # f(g(x)) = (x + k) + k
        exposed = ("f(g(x))", x + 2 * k)
    else:
        near = cbrt(x - k) + h  # g(f(x)) = (x + h) + h
        exposed = ("g(f(x))", x + 2 * h)
    return f, true_inv, near, exposed


@generator("verifying-inverses", "Checking whether functions are inverses")
def verifying_inverses(rng: random.Random) -> Spec:
    f, true_inv, near, (which, bad) = (_linear_pair if rng.random() < 0.55 else _cubic_pair)(rng)
    are_inverses = rng.random() < 0.5
    g = true_inv if are_inverses else near
    if are_inverses:
        why = (
            f"Composing in both orders gives back $x$: $f(g(x)) = x$ and $g(f(x)) = x$, so they're inverses. "
            "Each one undoes the other's steps in reverse order."
        )
    else:
        why = (
            f"${which} = {sp.latex(bad)}$, which isn't $x$, so they're not inverses. "
            f"The real inverse of $f$ is ${sp.latex(true_inv)}$."
        )
    return Spec(
        prompt=f"Are $f(x) = {sp.latex(f)}$ and $g(x) = {sp.latex(g)}$ inverses of each other?",
        answer="Yes" if are_inverses else "No",
        kind="choice",
        choices=YES_NO,
        explanation=why,
    )


# ---------------------------------------------------------------- 5. finding inverses


@generator("finding-inverses", "Finding an inverse from a formula")
def finding_inverses(rng: random.Random) -> Spec:
    variant = rng.choice(["linear", "linear", "cubic-shift", "cubic-scale", "rational"])

    if variant == "linear":
        a, b = nonzero(rng, -9, 9), nonzero(rng, -15, 15)
        while abs(a) == 1:
            a = nonzero(rng, -9, 9)
        f = a * x + b
        correct = over(x - b, sp.Integer(a))
        distractors = [over(x + b, sp.Integer(a)), x / a - b, 1 / (a * x + b), over(b - x, sp.Integer(a)), a * x - b]
        why = (
            f"Swap: $x = {sp.latex(a * sp.Symbol('y') + b)}$. Undo in reverse order: "
            f"{'subtract' if b > 0 else 'add'} {abs(b)}, then divide by {a}: $y = {sp.latex(correct)}$."
        )
    elif variant == "cubic-shift":
        h, k = nonzero(rng, -8, 8), nonzero(rng, -9, 9)
        f = (x + h) ** 3 + k
        correct = cbrt(x - k) - h
        distractors = [cbrt(x + k) - h, cbrt(x - k) + h, cbrt(x + k) + h, (x - k) ** 3 - h, 1 / f]
        why = (
            f"Swap: $x = (y{_signed(h)})^3{_signed(k)}$. Undo in reverse order: "
            f"$x{_signed(-k)} = (y{_signed(h)})^3$, take the cube root, then {'subtract' if h > 0 else 'add'} {abs(h)}: "
            f"$y = {sp.latex(correct)}$."
        )
    elif variant == "cubic-scale":
        a, k = rng.choice([2, 3, 4, 5, -2]), nonzero(rng, -9, 9)
        f = a * x**3 + k
        correct = cbrt(over(x - k, sp.Integer(a)))
        distractors = [cbrt(over(x + k, sp.Integer(a))), over(cbrt(x - k), sp.Integer(a)), cbrt(x) / a - k, cbrt(a * x - k)]
        why = (
            f"Swap: $x = {a}y^3{_signed(k)}$. {'Subtract' if k > 0 else 'Add'} {abs(k)}, divide by {a}, "
            f"then take the cube root: $y = {sp.latex(correct)}$."
        )
    else:
        a, b = nonzero(rng, -9, 9), nonzero(rng, -7, 7)
        f = over(sp.Integer(a), x - b)
        correct = over(a + b * x, x)
        distractors = [over(a - b * x, x), over(x, a + b * x), over(x - b, sp.Integer(a)), over(sp.Integer(a), x + b), over(b + a * x, x)]
        why = (
            f"Swap: $x = \\frac{{{a}}}{{y{_signed(-b)}}}$. Multiply both sides by $(y{_signed(-b)})$: "
            f"$xy{_signed(-b)}x = {a}$. Move the $x$ term: $xy = {sp.latex(a + b * x)}$. Divide by $x$: "
            f"$y = {sp.latex(correct)}$."
        )

    return Spec(
        prompt=f"Find the inverse of $f(x) = {sp.latex(f)}$.",
        answer=tex(correct),
        kind="expr",
        expected=correct,
        distractors=distractors,
        input_hint=INVERSE_HINT,
        explanation=why,
    )


# ---------------------------------------------------------------- 6. applications


APPLICATIONS = [
    # (story template, base, rate sign, unit name, question)
    ("A gym charges a \\${c} joining fee plus \\${r} per month. Someone has paid \\${total} in total.", "How many months have they been a member?", 1),
    ("A taxi charges \\${c} plus \\${r} per mile. A ride cost \\${total}.", "How many miles long was the ride?", 1),
    ("You have \\${c} saved and add \\${r} every week. You now have \\${total}.", "How many weeks have you been saving?", 1),
    ("A car bought for \\${c} loses \\${r} of value each year. It's now worth \\${total}.", "How many years ago was it bought?", -1),
    ("A loan starts at \\${c} and gets a \\${r} payment every month. The balance is now \\${total}.", "How many payments have been made?", -1),
    ("A tank holds {c} gallons and drains {r} gallons per minute. There are {total} gallons left.", "How many minutes has it been draining?", -1),
]


@generator("inverse-applications", "Using inverses in word problems")
def inverse_applications(rng: random.Random) -> Spec:
    if rng.random() < 0.2:
        celsius = rng.randrange(-20, 105, 5)
        fahrenheit = sp.Rational(9, 5) * celsius + 32
        return Spec(
            prompt=(
                f"$f(x) = \\frac{{9}}{{5}}x + 32$ converts Celsius to Fahrenheit. Use its inverse to convert "
                f"${fmt_num(fahrenheit)}$°F to Celsius."
            ),
            answer=f"${celsius}$",
            kind="numbers",
            expected=[celsius],
            tolerance=0.01,
            distractors=[[sp.Rational(9, 5) * fahrenheit + 32], [sp.Rational(5, 9) * fahrenheit - 32], [fahrenheit - 32], [celsius + 5]],
            input_hint="Number only, in °C",
            explanation=(
                f"$f^{{-1}}(x) = \\frac{{5}}{{9}}(x - 32)$, so $f^{{-1}}({fmt_num(fahrenheit)}) = "
                f"\\frac{{5}}{{9}}({fmt_num(fahrenheit - 32)}) = {celsius}$°C."
            ),
        )

    story, question, sign = rng.choice(APPLICATIONS)
    answer = rng.randint(3, 30)
    if sign > 0:
        c, r = rng.randrange(10, 200, 5), rng.choice([2, 3, 5, 12, 15, 20, 25, 35, 40, 49])
    else:
        r = rng.choice([25, 50, 100, 250, 500, 1500, 2500]) if "\\$" in story else rng.choice([3, 4, 5, 8, 12])
        c = r * (answer + rng.randint(2, 20))
    total = c + sign * r * answer
    model = f"{fmt_num(c)} + {fmt_num(r)}x" if sign > 0 else f"{fmt_num(c)} - {fmt_num(r)}x"
    inverse = f"\\frac{{x - {fmt_num(c)}}}{{{fmt_num(r)}}}" if sign > 0 else f"\\frac{{{fmt_num(c)} - x}}{{{fmt_num(r)}}}"
    wrong_forward = c + sign * r * total
    return Spec(
        prompt=f"{story.format(c=fmt_num(c).replace('{,}', ','), r=fmt_num(r), total=fmt_num(total).replace('{,}', ','))} {question}",
        answer=f"${answer}$",
        kind="numbers",
        expected=[answer],
        distractors=[[sp.Rational(total, r)], [sp.Rational(total + c, r)], [answer + 1], *([[wrong_forward]] if wrong_forward > 0 else []), [answer - 1]],
        input_hint="Number only",
        explanation=(
            f"The model is $f(x) = {model}$. Its inverse is $f^{{-1}}(x) = {inverse}$, so "
            f"$f^{{-1}}({fmt_num(total)}) = {answer}$."
        ),
    )


# ---------------------------------------------------------------- 7. composing inverses


@generator("composing-inverses", "Composing inverses")
def composing_inverses(rng: random.Random) -> Spec:
    g_x = rng.sample(range(-5, 7), 4)
    g_y = rng.sample(range(-4, 8), 4)
    f_x = rng.sample(range(-3, 10), 5)
    f_y = rng.sample(range(-5, 9), 5)
    order = rng.choice(["f-g", "g-f"])  # (f^-1 o g^-1) or (g^-1 o f^-1)

    if order == "f-g":
        # a -> g^-1(a) = m -> f^-1(m): m (an input of g) must be an output of f
        i = rng.randrange(4)
        a, m = g_y[i], g_x[i]
        j = rng.randrange(5)
        f_y[j] = m
        f_y = _unique_except(f_y, j, rng)
        result = f_x[j]
        outer, inner = "f", "g"
    else:
        # a -> f^-1(a) = m -> g^-1(m): m (an input of f) must be an output of g
        j = rng.randrange(5)
        a, m = f_y[j], f_x[j]
        i = rng.randrange(4)
        g_y[i] = m
        g_y = _unique_except(g_y, i, rng)
        result = g_x[i]
        outer, inner = "g", "f"

    points = ", ".join(f"$({px}, {py})$" for px, py in sorted(zip(g_x, g_y)))
    table = _table({"f(x)": f_y}, domain=f_x)
    f_map, g_map = dict(zip(f_x, f_y)), dict(zip(g_x, g_y))
    forward = {"f": f_map, "g": g_map}
    distractors = [[m], [a]]
    if a in forward[inner] and forward[inner][a] in forward[outer]:
        distractors.append([forward[outer][forward[inner][a]]])  # used f and g instead of the inverses
    distractors += [[result + 1], [result - 1], [-result]]
    return Spec(
        prompt=(
            f"The graph of $g$ passes through {points}. The table gives $f$.\n\n{table}\n\n"
            f"Find $({outer}^{{-1}} \\circ {inner}^{{-1}})({a})$."
        ),
        answer=f"${result}$",
        kind="numbers",
        expected=[result],
        distractors=distractors,
        explanation=(
            f"Inside first: ${inner}^{{-1}}({a}) = {m}$ because ${inner}({m}) = {a}$. "
            f"Then ${outer}^{{-1}}({m}) = {result}$ because ${outer}({result}) = {m}$."
        ),
    )


def _unique_except(values: list[int], keep: int, rng: random.Random) -> list[int]:
    """Make the values distinct (so the function stays one-to-one) without touching values[keep]."""
    out = list(values)
    used = {out[keep]}
    for idx, val in enumerate(out):
        if idx == keep:
            continue
        while val in used:
            val = rng.randint(-6, 12)
        out[idx] = val
        used.add(val)
    return out
