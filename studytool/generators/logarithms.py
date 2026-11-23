"""Section 3, Module 9 - Logarithmic Functions and Equations."""

from __future__ import annotations

import math
import random

import sympy as sp

from ..core.problem import Spec, generator
from ..core.symbols import nice_number, nonzero, show_numbers, show_pair
from .exponentials import dec, dec_options, rounded
from .quadratics import num, num_options

PAIR_HINT = "Type the ordered pair, e.g. (2, -3)"


def base_sub(b) -> str:
    b = sp.nsimplify(b)
    return sp.latex(b) if b.is_Integer else f"\\frac{{{b.p}}}{{{b.q}}}"


def log_tex(b, arg: str) -> str:
    """log_b(arg), with log for base 10 and ln for base e."""
    wrap = arg if (arg.replace(".", "").isdigit() or len(arg) == 1) else f"({arg})"
    if str(b) == "10":
        return f"\\log {wrap}" if wrap == arg else f"\\log{wrap}"
    if str(b) == "e":
        return f"\\ln {wrap}" if wrap == arg else f"\\ln{wrap}"
    return f"\\log_{{{base_sub(b)}}} {wrap}" if wrap == arg else f"\\log_{{{base_sub(b)}}}{wrap}"


def inside(h) -> str:
    return "x" if h == 0 else f"x - {h}" if h > 0 else f"x + {-h}"


def shifted(b, h, k) -> str:
    out = log_tex(b, inside(h))
    return out + ("" if k == 0 else f" + {k}" if k > 0 else f" - {-k}")


def big(n) -> str:
    return f"{n:,}".replace(",", "{,}")


# ---------------------------------------------------------------- 1. graph features


@generator("log-graph-features", "Features of logarithmic graphs")
def log_graph_features(rng: random.Random) -> Spec:
    b = rng.choice([2, 3, 4, 5, 10, sp.Rational(1, 2), sp.Rational(1, 3)])
    h, k = rng.choice([0, *range(-6, 7)]), rng.choice([0, 0, *range(-4, 5)])
    shown = f"f(x) = {shifted(b, h, k)}"
    variant = rng.choice(["asymptote", "domain", "intercept", "direction", "base", "base"])

    if variant == "asymptote":
        return Spec(
            prompt=f"What is the vertical asymptote of ${shown}$? Give the value of $x$.",
            answer=f"$x = {h}$",
            kind="numbers",
            expected=[sp.Integer(h)],
            distractors=[f"$x = {w}$" for w in dict.fromkeys([-h, k, h + 1, 0, h + k]) if w != h],
            input_hint="The x-value, e.g. -2",
            explanation=f"The asymptote is where the inside of the log equals 0: ${inside(h)} = 0$, so $x = {h}$. "
            + ("The outside " + ("+" if k > 0 else "-") + f" {abs(k)} shifts the graph vertically but never moves a vertical asymptote." if k else ""),
        )
    if variant == "domain":
        answer = f"$x > {h}$"
        wrong = [f"$x > {-h}$", f"$x \\ge {h}$", "all real numbers", f"$x > {h + 1}$", f"$x > {k}$"]
        return Spec(
            prompt=f"What is the domain of ${shown}$?",
            answer=answer,
            kind="choice",
            distractors=[w for w in dict.fromkeys(wrong) if w != answer],
            explanation=f"You can only take the log of a positive number: ${inside(h)} > 0$, so $x > {h}$. The asymptote $x = {h}$ itself isn't included.",
        )
    if variant == "direction":
        up = b > 1
        return Spec(
            prompt=f"Is ${shown}$ increasing or decreasing?",
            answer="Increasing" if up else "Decreasing",
            kind="choice",
            choices=["Increasing", "Decreasing"],
            explanation=f"The base decides: $b = {nice_number(b)}$ is {'greater than 1, so it increases' if up else 'between 0 and 1, so it decreases'}. Shifts don't change the direction.",
        )
    if variant == "intercept":
        if not sp.nsimplify(b).is_Integer:
            b = rng.choice([2, 3, 5, 10])
        b = sp.Integer(b)
        k = rng.choice([0, 0, -1, -2, 1, 2]) if b < 10 else rng.choice([0, -1, -2])
        shown = f"f(x) = {shifted(b, h, k)}"
        xi = h + b ** (-k)
        return Spec(
            prompt=f"Find the $x$-intercept of ${shown}$.",
            answer=show_pair((xi, 0)),
            kind="numbers",
            expected=(sp.nsimplify(xi), sp.Integer(0)),
            ordered=True,
            distractors=[(h, 0), (-h + 1, 0), (h + b**k, 0), (h + 1, 0) if k else (h - 1, 0)],
            input_hint=PAIR_HINT,
            explanation=(
                f"Set $f(x) = 0$: ${log_tex(b, inside(h))} = {-k}$. Rewrite in exponential form: ${inside(h)} = {b}^{{{-k}}} = {nice_number(b ** (-k))}$, so $x = {nice_number(xi)}$."
                if k
                else f"Set $f(x) = 0$: ${log_tex(b, inside(h))} = 0$, so the inside equals $1$ (since $\\log_b 1 = 0$): ${inside(h)} = 1$ and $x = {h + 1}$."
            ),
        )
    c = rng.choice([2, 3, 4, 5, 6, 7])
    flip = rng.random() < 0.4
    n = rng.choice([v for v in (-2, -1, 2, 3) if abs(c**v) < 400 and v not in (-1,) or flip and v == -1])
    base = sp.Rational(1, c) if flip else sp.Integer(c)
    xv = base**n
    return Spec(
        prompt=f"The graph of $y = \\log_b x$ is {'decreasing' if flip else 'increasing'} and passes through $({nice_number(xv)}, {n})$. What is $b$?",
        answer=num(base),
        kind="numbers",
        expected=[base],
        distractors=num_options(base, [1 / base, n, xv, c if flip else sp.Rational(1, c), xv / n]),
        input_hint="A number, e.g. 3 or 1/2",
        explanation=f"The point means $b^{{{n}}} = {nice_number(xv)}$. Solving gives $b = {nice_number(base)}$"
        + (", which is between 0 and 1 - matching a decreasing graph." if flip else ", which is greater than 1 - matching an increasing graph."),
    )


# ---------------------------------------------------------------- 2. following points


@generator("log-graph-points", "Shifting points on log graphs")
def log_graph_points(rng: random.Random) -> Spec:
    b = rng.choice([2, 3, 4, 5, 10])
    n = rng.choice([v for v in range(-2, 5) if b**v <= 1000])
    px = sp.Integer(b) ** n
    h, k = rng.choice([0, *range(-9, 10)]), rng.choice([0, *range(-8, 9)])
    if h == 0 and k == 0:
        k = rng.choice([-7, 4, 5])
    nx, ny = px + h, n + k
    words = []
    if h:
        words.append(f"inside, ${'-' if h > 0 else '+'} {abs(h)}$ moves it {'right' if h > 0 else 'left'} {abs(h)} (add ${h}$ to $x$)")
    if k:
        words.append(f"outside, ${'+' if k > 0 else '-'} {abs(k)}$ moves it {'up' if k > 0 else 'down'} {abs(k)} (add ${k}$ to $y$)")
    return Spec(
        prompt=f"$({nice_number(px)}, {n})$ is on the graph of $g(x) = {log_tex(b, 'x')}$. What is the corresponding point on $h(x) = {shifted(b, h, k)}$?",
        answer=show_pair((nx, ny)),
        kind="numbers",
        expected=(sp.nsimplify(nx), sp.Integer(ny)),
        ordered=True,
        distractors=[(px - h, ny), (px + k, n + h), (px, n + k + h), (nx, n - k)],
        input_hint=PAIR_HINT,
        explanation=f"Horizontal changes affect only $x$ and vertical changes only $y$. " + "; ".join(words).capitalize() + f". The point is {show_pair((nx, ny))}.",
    )


# ---------------------------------------------------------------- 3. change of base


@generator("change-of-base", "Change of base")
def change_of_base(rng: random.Random) -> Spec:
    a = rng.choice([2, 3, 5, 6, 7, 8, 9, 12, 15, sp.Rational(1, 2)])
    m = rng.choice([v for v in range(2, 600) if abs(math.log(v, float(a)) - round(math.log(v, float(a)))) > 0.05])
    val = math.log(m) / math.log(float(a))
    use = rng.choice(["\\log", "\\ln"])
    return Spec(
        prompt=f"Use the change-of-base formula to approximate $\\log_{{{base_sub(a)}}} {m}$ to three decimal places.",
        answer=f"${dec(val, 3)}$",
        kind="numbers",
        expected=[rounded(val, 3)],
        distractors=dec_options(val, [math.log(float(a)) / math.log(m), math.log10(m / float(a)), m / float(a), math.log10(m), math.log(m)], 3),
        tolerance=0.0015,
        input_hint="e.g. 1.861",
        explanation=(
            f"$\\log_{{{base_sub(a)}}} {m} = \\frac{{{use} {m}}}{{{use} {nice_number(a)}}} \\approx {dec(val, 3)}$. "
            "The number you're taking the log **of** goes on top; LOG and LN give the same answer."
        ),
    )


# ---------------------------------------------------------------- 4. inverse properties


@generator("inverse-properties", "Inverse properties of logarithms")
def inverse_properties(rng: random.Random) -> Spec:
    variant = rng.choice(["cancel-out", "power", "fraction", "root", "natural"])
    b = rng.choice([2, 3, 4, 5, 6, 7, 10])

    if variant == "cancel-out":
        base = rng.choice([b, b, "e"])
        m = rng.choice([sp.Integer(rng.randint(2, 99)), sp.Rational(rng.randint(11, 99), 10)])
        lg = log_tex(base, nice_number(m)).replace(f"\\log_{{{base}}} ", f"\\log_{{{base}}}")
        return Spec(
            prompt=f"Evaluate ${base}^{{{lg}}}$.",
            answer=num(m),
            kind="numbers",
            expected=[m],
            distractors=num_options(m, [sp.Integer(base) if base != "e" else 3, m * (b if base != "e" else 2), 1, sp.Integer(base) ** 2 if base != "e" else 7]),
            input_hint="A number",
            explanation=f"A power and a log with the same base cancel: $b^{{\\log_b M}} = M$. "
            + ("($\\log$ with no base means base 10.) " if base == 10 else "($\\ln$ means base $e$.) " if base == "e" else "")
            + f"The answer is ${nice_number(m)}$.",
        )
    if variant == "power":
        n = rng.choice([v for v in range(2, 7) if b**v <= 100_000])
        arg, answer = big(b**n), sp.Integer(n)
        why = f"${arg} = {b}^{{{n}}}$, and $\\log_b(b^n) = n$."
        wrong = [b**n // b, n + 1, -n, b]
    elif variant == "fraction":
        n = rng.choice([v for v in range(1, 5) if b**v <= 10_000])
        arg, answer = f"\\frac{{1}}{{{big(b**n)}}}", sp.Integer(-n)
        why = f"$\\frac{{1}}{{{big(b**n)}}} = {b}^{{{-n}}}$ (a reciprocal is a negative exponent), so the log is ${-n}$."
        wrong = [n, sp.Rational(1, n), sp.Rational(-1, n), -n - 1]
    elif variant == "root":
        r = rng.choice([2, 3, 4])
        p = rng.choice([1, 1, 2, 3]) if r != 2 else rng.choice([1, 1, 3])
        if math.gcd(p, r) != 1:
            p = 1
        arg = f"\\sqrt[{r}]{{{b}{'^' + str(p) if p > 1 else ''}}}" if r != 2 else f"\\sqrt{{{b}{'^' + str(p) if p > 1 else ''}}}"
        answer = sp.Rational(p, r)
        why = f"Write the root as a fractional exponent: ${arg} = {b}^{{{p}/{r}}}$, so the log is ${sp.latex(answer)}$."
        wrong = [sp.Integer(r), sp.Rational(r, p), sp.Integer(p * r), -answer]
    else:
        n = rng.choice([v for v in range(-6, 10) if v])
        if rng.random() < 0.3:
            r = rng.choice([2, 3])
            prompt_arg, answer = f"\\sqrt{{e}}" if r == 2 else "\\sqrt[3]{e}", sp.Rational(1, r)
            why = f"${prompt_arg} = e^{{1/{r}}}$, so $\\ln$ of it is ${sp.latex(answer)}$."
            wrong = [sp.Integer(r), sp.Rational(-1, r), 1]
        else:
            prompt_arg, answer = f"e^{{{n}}}", sp.Integer(n)
            why = f"$\\ln$ is log base $e$, and $\\log_e(e^{{{n}}}) = {n}$."
            wrong = [-n, n + 1, sp.Rational(1, n), 0]
        return Spec(
            prompt=f"Evaluate $\\ln\\left({prompt_arg}\\right)$.",
            answer=num(answer),
            kind="numbers",
            expected=[answer],
            distractors=num_options(answer, wrong),
            input_hint="A number or fraction, e.g. 1/2",
            explanation=why,
        )
    return Spec(
        prompt=f"Use the inverse property to evaluate ${log_tex(b, arg) if b != 10 else chr(92) + 'log' + ('(' + arg + ')' if 'frac' in arg or 'sqrt' in arg else ' ' + arg)}$.",
        answer=num(answer),
        kind="numbers",
        expected=[answer],
        distractors=num_options(answer, wrong),
        input_hint="A number or fraction, e.g. -2 or 1/3",
        explanation=why,
    )


# ---------------------------------------------------------------- 5. expanding


def _power_tex(var: str, p) -> str:
    p = sp.nsimplify(p)
    if p == 1:
        return var
    if p == sp.Rational(1, 2):
        return f"\\sqrt{{{var}}}"
    if p.q == 3 and p.p == 1:
        return f"\\sqrt[3]{{{var}}}"
    return f"{var}^{{{p}}}"


def _coef(p) -> str:
    p = sp.nsimplify(p)
    return "" if p == 1 else sp.latex(p)


def _terms_tex(terms) -> str:
    """[(sign, text)] -> '3 + 2\\log x - \\log y'."""
    out = ""
    for i, (sign, text) in enumerate(terms):
        out += (("-" if sign < 0 else "") if i == 0 else (" - " if sign < 0 else " + ")) + text
    return out


@generator("expanding-logs", "Expanding logarithms")
def expanding_logs(rng: random.Random) -> Spec:
    b = rng.choice([2, 3, 5, 10, "e"])
    variables = rng.sample(["x", "y", "z", "a", "w"], 3)
    powers = [rng.choice([1, 2, 3, 4, 5, sp.Rational(1, 2), sp.Rational(1, 3)]) for _ in variables]
    n_top = rng.choice([1, 2, 2])
    top, bottom = list(zip(variables, powers))[:n_top], list(zip(variables, powers))[n_top:]
    const_pow = rng.choice([0, 0, 1, 2, 3]) if b != "e" else 0
    const = (10 if b == 10 else b) ** const_pow if const_pow else 1
    const_on_top = rng.random() < 0.7
    num_parts = ([big(const)] if const != 1 and const_on_top else []) + [_power_tex(v, p) for v, p in top]
    den_parts = ([big(const)] if const != 1 and not const_on_top else []) + [_power_tex(v, p) for v, p in bottom]
    arg = f"\\frac{{{' '.join(num_parts)}}}{{{' '.join(den_parts)}}}" if den_parts else " ".join(num_parts)
    lg = lambda v: log_tex(b, v)

    def build(sign_bottom=-1, bring_down=True, const_value=True, root_as=None):
        terms = []
        if const != 1:
            s = 1 if const_on_top else sign_bottom
            terms.append((s, str(const_pow) if const_value else lg(big(const))))
        for v, p in top:
            pp = root_as(p) if root_as else p
            terms.append((1, f"{_coef(pp)}{lg(v)}" if bring_down else lg(_power_tex(v, p))))
        for v, p in bottom:
            pp = root_as(p) if root_as else p
            terms.append((sign_bottom, f"{_coef(pp)}{lg(v)}" if bring_down else lg(_power_tex(v, p))))
        return f"${_terms_tex(terms)}$"

    answer = build()
    wrong = [
        build(sign_bottom=1),
        build(const_value=False) if const != 1 else build(bring_down=False),
        build(root_as=lambda p: sp.nsimplify(1 / p) if p < 1 else p) if any(p < 1 for p in powers) else build(sign_bottom=1, bring_down=False),
        build(bring_down=False),
        build(root_as=lambda p: p + 1),
    ]
    return Spec(
        prompt=f"Expand ${lg(arg) if not arg.startswith(chr(92) + 'frac') else log_tex(b, arg)}$ using the product, quotient, and power rules.",
        answer=answer,
        kind="choice",
        distractors=[w for w in dict.fromkeys(wrong) if w != answer],
        explanation=(
            ("Rewrite roots as fractional exponents. " if any(p < 1 for p in powers) else "")
            + ("Quotient rule: everything in the denominator gets subtracted. " if den_parts else "")
            + "Product rule: each factor gets its own log. Power rule: exponents come to the front. "
            + (f"Finally ${lg(big(const))} = {const_pow}$. " if const != 1 else "")
            + f"Result: {answer}."
        ),
    )


# ---------------------------------------------------------------- 6. condensing


@generator("condensing-logs", "Condensing logarithms")
def condensing_logs(rng: random.Random) -> Spec:
    if rng.random() < 0.3:
        b = rng.choice([2, 3, 10, "e"])
        v = rng.sample(["x", "y", "z", "a", "c"], 3)
        p = [rng.choice([1, 2, 3, 4, sp.Rational(1, 2)]) for _ in v]
        lg = lambda s: log_tex(b, s)
        shown = f"{_coef(p[0])}{lg(v[0])} + {_coef(p[1])}{lg(v[1])} - {_coef(p[2])}{lg(v[2])}"
        top = f"{_power_tex(v[0], p[0])} {_power_tex(v[1], p[1])}"
        answer = f"${lg(chr(92) + 'frac{' + top + '}{' + _power_tex(v[2], p[2]) + '}')}$"
        wrong = [
            f"${lg(top + ' ' + _power_tex(v[2], p[2]))}$",
            f"${lg(chr(92) + 'frac{' + _power_tex(v[0], p[0]) + '}{' + _power_tex(v[1], p[1]) + ' ' + _power_tex(v[2], p[2]) + '}')}$",
            f"${lg(chr(92) + 'frac{' + v[0] + ' ' + v[1] + '}{' + v[2] + '}')}$",
            f"${lg(_power_tex(v[0], p[0]) + ' + ' + _power_tex(v[1], p[1]) + ' - ' + _power_tex(v[2], p[2]))}$",
        ]
        return Spec(
            prompt=f"Write ${shown}$ as a single logarithm.",
            answer=answer,
            kind="choice",
            distractors=[w for w in dict.fromkeys(wrong) if w != answer],
            explanation="Power rule first: each coefficient becomes an exponent. Then added logs multiply together in the numerator and subtracted logs go in the denominator.",
        )

    b = rng.choice([2, 3, 5, 10])
    n = rng.choice([v for v in (1, 2, 3, 4) if b**v <= 1000])
    target = b**n
    style = rng.choice(["sum", "difference", "coefficient", "three"])
    if style == "sum":
        a = rng.choice([d for d in range(2, target) if target % d == 0] or [1])
        shown, combine = f"{log_tex(b, str(a))} + {log_tex(b, str(target // a))}", f"{a} \\cdot {target // a}"
    elif style == "difference":
        a = rng.choice([2, 3, 4, 5, 6])
        shown, combine = f"{log_tex(b, big(target * a))} - {log_tex(b, str(a))}", f"\\frac{{{big(target * a)}}}{{{a}}}"
    elif style == "coefficient":
        b, r, base_val, divisor, n = rng.choice(COEFFICIENT_CASES)
        target = b**n
        shown = f"{r}{log_tex(b, str(base_val))} - {log_tex(b, str(divisor))}"
        combine = f"\\frac{{{base_val}^{{{r}}}}}{{{divisor}}}"
    else:
        a, c = rng.choice([2, 4, 5, 8]), rng.choice([2, 3, 6])
        d = sp.Rational(a * c, target)
        shown = f"{log_tex(b, str(a))} + {log_tex(b, str(c))} - {log_tex(b, nice_number(d))}"
        combine = f"\\frac{{{a} \\cdot {c}}}{{{nice_number(d)}}}"
    value = sp.Integer(n)
    return Spec(
        prompt=f"Condense ${shown}$ into a single logarithm and evaluate it.",
        answer=num(value),
        kind="numbers",
        expected=[value],
        distractors=num_options(value, [n + 1, n - 1 if n > 1 else 2 * n, target, -n]),
        input_hint="A number, e.g. 2",
        explanation=f"Power rule for any coefficients, then product and quotient rules: ${log_tex(b, combine)} = {log_tex(b, big(target))} = {n}$, since ${b}^{{{n}}} = {big(target)}$.",
    )


# ---------------------------------------------------------------- 7. solving log equations


COEFFICIENT_CASES = [  # (base, r, value, divisor, n): r*log_b(value) - log_b(divisor) = n
    (3, 2, 6, 4, 2), (10, 2, 50, 25, 2), (2, 3, 4, 2, 5), (5, 2, 10, 4, 2), (10, 3, 20, 8, 3), (2, 2, 6, 9, 2), (3, 3, 6, 8, 3), (2, 2, 12, 9, 4),
]

CONDENSE_CASES = [  # (base, d, n, root): log_b(x) + log_b(x + d) = n has the single valid root
    (2, 2, 3, 2), (2, 7, 3, 1), (6, -1, 1, 3), (10, 3, 1, 2), (10, 21, 2, 4), (3, 8, 2, 1), (2, 6, 4, 2), (5, -4, 1, 5), (3, -8, 2, 9), (2, -2, 3, 4),
]


@generator("solving-log-equations", "Solving logarithmic equations")
def solving_log_equations(rng: random.Random) -> Spec:
    variant = rng.choice(["definition", "definition", "extraneous", "both-valid", "condense", "difference"])

    if variant == "definition":
        b = rng.choice([2, 3, 4, 5, 10])
        n = rng.choice([v for v in (1, 2, 3, 4) if b**v <= 1000])
        p = rng.choice([1, 2, 3, 4, 5])
        x = sp.Rational(rng.randint(1, 30), rng.choice([1, 1, 2]))
        q = b**n - p * x
        if not q.is_Integer:
            x, q = sp.Integer(5), b**n - p * 5
        arg = f"{p if p > 1 else ''}x {'+' if q >= 0 else '-'} {abs(q)}" if q else f"{p}x"
        return Spec(
            prompt=f"Solve ${log_tex(b, arg)} = {n}$.",
            answer=f"$x = {nice_number(x)}$",
            kind="numbers",
            expected=[x],
            distractors=[f"$x = {nice_number(w)}$" for w in dict.fromkeys([sp.Rational(n**b - q, p), sp.Rational(b * n - q, p), sp.Rational(b**n + q, p), x + 1]) if w != x],
            input_hint="e.g. 11",
            explanation=f"Rewrite in exponential form: ${arg} = {b}^{{{n}}} = {b**n}$. Solve: $x = {nice_number(x)}$. Check: the argument is ${b**n} > 0$ ✓.",
        )
    if variant in ("extraneous", "both-valid"):
        b = rng.choice([10, "e", 2, 3])
        if variant == "extraneous":
            r1, r2 = rng.randint(2, 9), -rng.randint(1, 8)
            if r1 + r2 <= 0:
                r1 = -r2 + rng.randint(1, 4)
            m, c = r1 + r2, -r1 * r2
            shown = f"{log_tex(b, f'x^2 - {c}')} = {log_tex(b, f'{m}x' if m != 1 else 'x')}"
            quad = f"x^2 - {m if m != 1 else ''}x - {c} = 0"
            answer_vals = [sp.Integer(r1)]
            why_tail = f"Check: $x = {r2}$ makes ${m if m != 1 else ''}x$ negative, so it's extraneous. Only $x = {r1}$ works."
        else:
            r1, r2 = rng.randint(1, 8), -rng.randint(1, 8)
            s, t = r1 + r2, -r1 * r2
            inner = f"x^2 - {s if s != 1 else ''}x" if s > 0 else (f"x^2 + {-s if s != -1 else ''}x" if s < 0 else "x^2")
            shown = f"{log_tex(b, inner)} = {log_tex(b, str(t))}"
            quad = f"{inner} - {t} = 0"
            answer_vals = sorted([sp.Integer(r1), sp.Integer(r2)])
            why_tail = f"Check both: each makes the argument equal ${t}$, which is positive, so **both** work."
        wrong_sets = [[r1, r2], [r2], [-r1, -r2], [r1]] if variant == "extraneous" else [[r1], [r2], [-r1, -r2], [r1, -r2]]
        return Spec(
            prompt=f"Solve ${shown}$. Give every valid solution.",
            answer=show_numbers(answer_vals),
            kind="numbers",
            expected=answer_vals,
            distractors=[w for w in wrong_sets if sorted(w) != [int(v) for v in answer_vals]],
            input_hint="All solutions, separated by commas",
            explanation=f"Same base on both sides, so set the arguments equal (one-to-one property): ${quad}$, giving $x = {r1}$ or $x = {r2}$. {why_tail}",
        )
    if variant == "condense":
        b, d, n, root = rng.choice(CONDENSE_CASES)
        other = -(root + d)
        second = f"x + {d}" if d > 0 else f"x - {-d}"
        return Spec(
            prompt=f"Solve ${log_tex(b, 'x')} + {log_tex(b, second)} = {n}$.",
            answer=f"$x = {root}$",
            kind="numbers",
            expected=[sp.Integer(root)],
            distractors=[show_numbers([root, other]), f"$x = {other}$", f"$x = {b**n - d}$", f"$x = {root + 1}$"],
            input_hint="All valid solutions, separated by commas",
            explanation=(
                f"Condense with the product rule: ${log_tex(b, 'x(' + second + ')')} = {n}$. Exponential form: $x({second}) = {b**n}$, "
                f"so $x^2 {'+' if d > 0 else '-'} {abs(d) if abs(d) != 1 else ''}x - {b**n} = 0$ and $x = {root}$ or $x = {other}$. "
                f"$x = {other}$ makes an argument negative, so it's extraneous."
            ),
        )
    b, n, mult = rng.choice([(2, 2, 3), (3, 1, 2), (10, 1, 9), (2, 1, 1), (5, 1, 4), (3, 2, 8)])
    x = rng.randint(1, 6)
    d = mult * x
    return Spec(
        prompt=f"Solve ${log_tex(b, f'x + {d}')} - {log_tex(b, 'x')} = {n}$.",
        answer=f"$x = {x}$",
        kind="numbers",
        expected=[sp.Integer(x)],
        distractors=[f"$x = {w}$" for w in dict.fromkeys([nice_number(sp.Rational(d, b**n + 1)), d, nice_number(sp.Rational(d, b * n - 1)) if b * n != 1 else d + 1, x + 1]) if str(w) != str(x)],
        input_hint="e.g. 2",
        explanation=(
            f"Condense with the quotient rule: ${log_tex(b, chr(92) + 'frac{x + ' + str(d) + '}{x}')} = {n}$. "
            f"Exponential form: $\\frac{{x + {d}}}{{x}} = {b**n}$, so $x + {d} = {b**n}x$, ${d} = {b**n - 1}x$, and $x = {x}$."
        ),
    )


# ---------------------------------------------------------------- 8. applications


@generator("log-applications", "Applications of logarithms")
def log_applications(rng: random.Random) -> Spec:
    variant = rng.choice(["decibels", "decibels-back", "richter", "ph", "ph-decimal"])

    if variant == "decibels":
        n = rng.randint(1, 13)
        thing = rng.choice(["A sound", "A whisper", "A lawn mower", "A concert", "A vacuum cleaner", "Traffic noise"])
        return Spec(
            prompt=f"{thing} is ${big(10**n) if n < 7 else '10^{' + str(n) + '}'}$ times as intense as the threshold of hearing. Using $\\text{{dB}} = 10\\log\\left(\\frac{{I}}{{I_0}}\\right)$, how many decibels is it?",
            answer=f"${10 * n}$ dB",
            kind="numbers",
            expected=[sp.Integer(10 * n)],
            distractors=[f"${w}$ dB" for w in dict.fromkeys([n, 10**n if n < 4 else 100 * n, 20 * n, 10 * n + 10]) if w != 10 * n],
            input_hint="Decibels, e.g. 60",
            explanation=f"$\\frac{{I}}{{I_0}} = 10^{{{n}}}$, so $\\text{{dB}} = 10\\log 10^{{{n}}} = 10({n}) = {10 * n}$.",
        )
    if variant == "decibels-back":
        db = 10 * rng.randint(2, 8)
        return Spec(
            prompt=f"A sound measures {db} dB. Using $\\text{{dB}} = 10\\log\\left(\\frac{{I}}{{I_0}}\\right)$, how many times as intense as the threshold is it? Give the power of 10 - for example, type 1000 or 10^3.",
            answer=f"$10^{{{db // 10}}}$",
            kind="numbers",
            expected=[sp.Integer(10) ** (db // 10)],
            distractors=[f"$10^{{{w}}}$" for w in (db, db // 10 + 1, db // 10 - 1)] + [f"${db}$"],
            input_hint="e.g. 10^6",
            explanation=f"${db} = 10\\log k$, so $\\log k = {db // 10}$ and $k = 10^{{{db // 10}}}$.",
        )
    if variant == "richter":
        big_m = rng.choice([v / 10 for v in range(55, 95)])
        d = rng.randint(1, 4)
        small = round(big_m - d, 1)
        return Spec(
            prompt=f"One earthquake measures {big_m:g} on the Richter scale and another measures {small:g}. How many times stronger is the first?",
            answer=f"${big(10**d)}$",
            kind="numbers",
            expected=[sp.Integer(10**d)],
            distractors=[f"${w}$" for w in dict.fromkeys([10 * d if d > 1 else 2, d if d > 1 else 1, big(10 ** (d + 1)), f"{big_m / small:.2f}"])],
            input_hint="e.g. 100",
            explanation=f"Each whole step on the Richter scale is 10 times stronger. The difference is {d}, so it's $10^{{{d}}} = {big(10**d)}$ times stronger" + (f" - not ${10 * d}$." if d > 1 else "."),
        )
    if variant == "ph":
        n = rng.randint(1, 13)
        kind = "acidic" if n < 7 else "alkaline" if n > 7 else "neutral"
        return Spec(
            prompt=f"A solution has $[\\text{{H}}^+] = 10^{{{-n}}}$. Using $\\text{{pH}} = -\\log[\\text{{H}}^+]$, what is its pH?",
            answer=f"${n}$",
            kind="numbers",
            expected=[sp.Integer(n)],
            distractors=[f"${w}$" for w in dict.fromkeys([-n, 14 - n if n != 7 else 8, n + 1, 10 * n]) if w != n],
            input_hint="e.g. 3",
            explanation=f"$-\\log(10^{{{-n}}}) = -({-n}) = {n}$. A pH of {n} is {kind} (below 7 is acidic, above 7 is alkaline).",
        )
    mant = rng.choice([1.5, 2, 2.5, 3.2, 4, 5, 6.3, 7.9, 8])
    e = rng.randint(2, 11)
    conc = mant * 10 ** (-e)
    ph = -math.log10(conc)
    return Spec(
        prompt=f"A solution has $[\\text{{H}}^+] = {mant:g} \\times 10^{{{-e}}}$. Using $\\text{{pH}} = -\\log[\\text{{H}}^+]$, find its pH to two decimal places.",
        answer=f"${dec(ph)}$",
        kind="numbers",
        expected=[rounded(ph, 2)],
        distractors=dec_options(ph, [-ph, e, math.log10(conc) + 14, ph + 1], 2),
        tolerance=0.006,
        input_hint="e.g. 3.49",
        explanation=f"$-\\log({mant:g} \\times 10^{{{-e}}}) \\approx {dec(ph)}$ (use the LOG key). It's {'acidic' if ph < 7 else 'alkaline'}.",
    )
