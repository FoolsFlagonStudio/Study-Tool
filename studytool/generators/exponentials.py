"""Section 3, Module 8 - Exponential Functions and Transformations."""

from __future__ import annotations

import math
import random

import sympy as sp

from ..core.problem import Spec, generator
from ..core.symbols import nice_number, nonzero, show_pair
from .linear import money
from .quadratics import num, num_options

PAIR_HINT = "Type the ordered pair, e.g. (2, -3)"
KINDS = ["Exponential", "Power", "Linear"]
GROWTH = ["Growth", "Decay"]
WHOLE_BASES = [2, 3, 4, 5, 10]
FRACTION_BASES = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 4), sp.Rational(2, 3)]


def base_tex(b) -> str:
    b = sp.nsimplify(b)
    if b.is_Integer:
        return str(b)
    if b.is_Rational and b.q in (2, 4, 5, 10, 20, 25) and b.p > b.q:
        return nice_number(b)  # 1.5, 1.25 read fine without parentheses
    return f"\\left({sp.latex(b)}\\right)" if b.is_Rational and not b.is_Integer else sp.latex(b)


def exponent_tex(h) -> str:
    h = sp.nsimplify(h)
    return "x" if h == 0 else f"x - {h}" if h > 0 else f"x + {-h}"


def exp_tex(a, b, h=0, k=0) -> str:
    """a * b^(x - h) + k, with a multiplication dot so 2·3^x doesn't read as 23^x."""
    a, k = sp.nsimplify(a), sp.nsimplify(k)
    lead = "" if a == 1 else "-" if a == -1 else f"{sp.latex(a)} \\cdot "
    out = f"{lead}{base_tex(b)}^{{{exponent_tex(h)}}}"
    return out + ("" if k == 0 else f" + {sp.latex(k)}" if k > 0 else f" - {sp.latex(-k)}")


def value(a, b, h, k, x):
    return sp.nsimplify(a) * sp.nsimplify(b) ** (x - h) + k


def rounded(val, places: int):
    """Exact rational of a rounded decimal, so typed answers parse cleanly."""
    return sp.Rational(round(float(val) * 10**places), 10**places)


def dec(val, places=2) -> str:
    return f"{float(val):,.{places}f}".replace(",", "{,}")


def dec_options(correct: float, wrongs, places=2, prefix="", suffix="") -> list[str]:
    """Rounded wrong answers that are visibly different from the right one."""
    out, seen = [], {dec(correct, places)}
    for w in wrongs:
        try:
            w = float(w)
        except (TypeError, ValueError):
            continue
        if not math.isfinite(w) or abs(w - correct) < 10 ** -places * 1.5:
            continue
        text = dec(w, places)
        if text not in seen:
            seen.add(text)
            out.append(f"${prefix}{text}{suffix}$")
    return out


# ---------------------------------------------------------------- 1. identifying


@generator("identifying-exponentials", "Identifying exponential functions")
def identifying_exponentials(rng: random.Random) -> Spec:
    variant = rng.choice(["classify", "classify", "growth", "growth", "which"])
    n = rng.choice([2, 3, 4, 5, 6, 7, 8])

    if variant == "classify":
        kind = rng.choice(KINDS)
        coef = rng.choice([1, 1, 2, 3, 4])
        lead = "" if coef == 1 else str(coef)
        shown = {"Exponential": f"{lead}({n})^x" if lead else f"{n}^x", "Power": f"{lead}x^{n}", "Linear": f"{coef * n}x"}[kind]
        why = {
            "Exponential": "The variable is in the **exponent** and the base is a fixed positive number - that's exponential.",
            "Power": "The variable is the **base**, raised to a fixed power - that's a power function.",
            "Linear": "$x$ is only multiplied by a number (exponent 1) - that's linear: it adds the same amount each step.",
        }[kind]
        return Spec(
            prompt=f"What type of function is $f(x) = {shown}$?",
            answer=kind,
            kind="choice",
            choices=KINDS,
            explanation=why,
        )

    if variant == "growth":
        b = rng.choice([2, 3, 5, sp.Rational(3, 2), sp.Rational(5, 4), sp.Rational(7, 4), sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(3, 4), sp.Rational(2, 5), sp.Rational(9, 10)])
        a = rng.choice([1, 1, 2, 3, 5, sp.Rational(1, 2), 10, 100])
        shown = exp_tex(a, b)
        if rng.random() < 0.4 and not sp.nsimplify(b).is_Integer:
            shown = shown.replace(base_tex(b), f"({float(b):g})")
        growth = b > 1
        return Spec(
            prompt=f"Does $f(x) = {shown}$ show exponential growth or decay?",
            answer=GROWTH[0 if growth else 1],
            kind="choice",
            choices=GROWTH,
            explanation=(
                f"Only the base decides: $b = {nice_number(b)}$ is {'greater than 1' if growth else 'between 0 and 1'}, so it's **{'growth' if growth else 'decay'}**. "
                "The positive coefficient in front doesn't change that."
            ),
        )

    answer = f"$f(x) = {n}^x$"
    wrong = [f"$f(x) = x^{n}$", f"$f(x) = {n}x$", f"$f(x) = \\frac{{x}}{{{n}}}$", f"$f(x) = x^{n} + {n}$"]
    return Spec(
        prompt="Which of these is an exponential function?",
        answer=answer,
        kind="choice",
        distractors=wrong,
        explanation=f"In ${n}^x$ the variable is the exponent. $x^{n}$ is a power function (variable in the base), and ${n}x$ and $\\frac{{x}}{{{n}}}$ are linear.",
    )


# ---------------------------------------------------------------- 2. evaluating


@generator("evaluating-exponentials", "Evaluating exponential functions")
def evaluating_exponentials(rng: random.Random) -> Spec:
    b = rng.choice(WHOLE_BASES + FRACTION_BASES)
    if rng.random() < 0.4:
        a, h, k = 1, 0, 0
    else:
        a, h, k = rng.choice([1, 2, 3, 4, -1, -2, sp.Rational(1, 2)]), rng.randint(-3, 3), rng.randint(-6, 6)
    e = rng.choice([-2, -1, -1, 0, 1, 2, 2, 3] if sp.nsimplify(b) <= 5 else [-2, -1, 0, 1, 2])
    xv = e + h
    val = value(a, b, h, k, xv)
    b = sp.nsimplify(b)
    wrong = [
        a * b ** (-e) + k,  # sign of the exponent lost
        (a * b) ** e + k if a != 1 else -(b**e) + k,  # coefficient pushed into the base
        a * b ** (xv + h) + k,  # wrong sign on the shift
        a * b**e,  # forgot k
        a * b * e + k,  # multiplied instead of raising
    ]
    return Spec(
        prompt=f"Evaluate $f(x) = {exp_tex(a, b, h, k)}$ at $x = {xv}$.",
        answer=num(val),
        kind="numbers",
        expected=[val],
        distractors=num_options(val, wrong),
        tolerance=0.005,
        input_hint="A number or fraction, e.g. 1/9",
        explanation=(
            (f"The exponent is ${xv} {'-' if h > 0 else '+'} {abs(h)} = {e}$. " if h else "")
            + f"${base_tex(b)}^{{{e}}} = {nice_number(b**e)}$"
            + (" (a negative exponent flips the base)" if e < 0 else " (anything to the 0 power is 1)" if e == 0 else "")
            + (f", times ${sp.latex(a)}$" if a != 1 else "")
            + (f", {'plus' if k > 0 else 'minus'} ${abs(k)}$" if k else "")
            + f" gives ${nice_number(val)}$. Exponent first, then multiply, then add."
        ),
    )


# ---------------------------------------------------------------- 3. graphs and key points


@generator("exponential-graphs", "Graphs of exponential functions")
def exponential_graphs(rng: random.Random) -> Spec:
    b = rng.choice([2, 3, 4, 5, sp.Rational(1, 2), sp.Rational(1, 3)])
    a = rng.choice([1, 1, 2, 3, -1, -2, sp.Rational(1, 2)])
    h, k = rng.choice([0, 0, *range(-4, 5)]), rng.randint(-6, 6)
    shown = f"f(x) = {exp_tex(a, b, h, k)}"
    b = sp.nsimplify(b)
    variant = rng.choice(["asymptote", "point", "point", "range", "growth"])

    if variant == "asymptote":
        return Spec(
            prompt=f"What is the horizontal asymptote of ${shown}$? Give the value of $y$.",
            answer=f"$y = {k}$",
            kind="numbers",
            expected=[sp.Integer(k)],
            distractors=[f"$y = {w}$" for w in dict.fromkeys([0, -k, h, a + k, -h]) if w != k],
            input_hint="The y-value, e.g. -4",
            explanation=f"Only the vertical shift moves the asymptote. Here $k = {k}$, so the asymptote is $y = {k}$. The {'shift inside the exponent' if h else 'base'} and the coefficient don't change it.",
        )
    if variant == "point":
        e = rng.choice([-1, 0, 1])
        px = h + e
        py = sp.nsimplify(a) * b**e + k
        return Spec(
            prompt=f"Find the key point of ${shown}$ where the exponent equals ${e}$.",
            answer=show_pair((px, py)),
            kind="numbers",
            expected=(sp.Integer(px), py),
            ordered=True,
            distractors=[(e - h, py), (px, sp.nsimplify(a) * b**e), (px, b**e + k), (e, py)],
            tolerance=0.005,
            input_hint=PAIR_HINT,
            explanation=(
                f"Set the exponent equal to ${e}$: $x - ({h}) = {e}$, so $x = {px}$. " if h < 0 else f"Set the exponent equal to ${e}$: $x = {px}$. "
            ) + f"Then $f({px}) = {sp.latex(sp.nsimplify(a))} \\cdot {nice_number(b**e)} {'+' if k >= 0 else '-'} {abs(k)} = {nice_number(py)}$.",
        )
    if variant == "range":
        up = a > 0
        answer = f"$y {'>' if up else '<'} {k}$"
        wrong = [f"$y {'<' if up else '>'} {k}$", f"$y {'>' if up else '<'} 0$", f"$y {'>' if up else '<'} {h}$", "all real numbers", f"$y {'>' if up else '<'} {a + k}$"]
        return Spec(
            prompt=f"What is the range of ${shown}$?",
            answer=answer,
            kind="choice",
            distractors=[w for w in dict.fromkeys(wrong) if w != answer],
            explanation=(
                f"The asymptote is $y = {k}$. Since $a = {sp.latex(sp.nsimplify(a))}$ is {'positive' if up else 'negative'}, the graph stays {'above' if up else 'below'} it: {answer}. "
                "The domain is all real numbers; the range never is."
            ),
        )
    a = abs(sp.nsimplify(a))
    shown = f"f(x) = {exp_tex(a, b, h, k)}"
    growth = b > 1
    return Spec(
        prompt=f"Is ${shown}$ increasing or decreasing?",
        answer="Increasing" if growth else "Decreasing",
        kind="choice",
        choices=["Increasing", "Decreasing"],
        explanation=f"With a positive coefficient, the base decides: $b = {nice_number(b)}$ is {'greater than 1 (growth)' if growth else 'between 0 and 1 (decay)'}. Shifts don't change the direction.",
    )


# ---------------------------------------------------------------- 4. logarithmic form


def _neg(v) -> str:
    return str(-v) if isinstance(v, int) else f"-{v}"


def _log_tex(b, x) -> str:
    return f"\\log {x}" if str(b) == "10" else f"\\ln {x}" if str(b) == "e" else f"\\log_{{{b}}} {x}"


@generator("logarithmic-form", "Exponential and logarithmic form")
def logarithmic_form(rng: random.Random) -> Spec:
    if rng.random() < 0.3:
        b, x, y = rng.sample(["a", "b", "c", "m", "n", "p", "q", "r", "t", "w"], 3)
        if rng.random() < 0.25:
            b = "e"
        xv, yv = x, y
    else:
        b = rng.choice([2, 3, 4, 5, 6, 7, 10])
        yv = rng.choice([-3, -2, -1, 2, 3, 4] if b < 7 else [-2, -1, 2, 3])
        if b == 10 and rng.random() < 0.5:
            yv = rng.randint(-4, 6)
        val = sp.Integer(b) ** yv
        xv = sp.latex(val).replace("\\frac", "\\tfrac") if not val.is_Integer else f"{int(val):,}".replace(",", "{,}")
    if rng.random() < 0.5:
        answer = f"${_log_tex(b, xv)} = {yv}$"
        wrong = [f"${_log_tex(xv, b)} = {yv}$" if str(b) not in ("10", "e") else f"$\\log_{{{xv}}} {b} = {yv}$", f"${_log_tex(b, yv)} = {xv}$", f"$\\log_{{{yv}}} {xv} = {b}$", f"${_log_tex(b, xv)} = {_neg(yv)}$"]
        return Spec(
            prompt=f"Write ${b}^{{{yv}}} = {xv}$ in logarithmic form.",
            answer=answer,
            kind="choice",
            distractors=list(dict.fromkeys(w for w in wrong if w != answer)),
            explanation=f"$b^y = x$ becomes $\\log_b x = y$: the base stays ${b}$, the result ${xv}$ goes inside the log, and the exponent ${yv}$ is the answer."
            + (" A log with base 10 is written $\\log$ with no base." if str(b) == "10" else " A log with base $e$ is written $\\ln$." if str(b) == "e" else ""),
        )
    answer = f"${b}^{{{yv}}} = {xv}$"
    wrong = [f"${yv}^{{{b}}} = {xv}$", f"${xv}^{{{yv}}} = {b}$", f"${b}^{{{xv}}} = {yv}$", f"${b}^{{{_neg(yv)}}} = {xv}$", f"${b} \\cdot {yv} = {xv}$"]
    return Spec(
        prompt=f"Write ${_log_tex(b, xv)} = {yv}$ in exponential form.",
        answer=answer,
        kind="choice",
        distractors=list(dict.fromkeys(w for w in wrong if w != answer)),
        explanation=f"$\\log_b x = y$ means $b^y = x$. The base is ${b}$, the answer ${yv}$ becomes the exponent, and ${xv}$ is the result: {answer}.",
    )


# ---------------------------------------------------------------- 5. evaluating logarithms


@generator("evaluating-logarithms", "Evaluating logarithms")
def evaluating_logarithms(rng: random.Random) -> Spec:
    variant = rng.choice(["power", "power", "shared", "common", "natural", "calculator"])

    if variant == "power":
        b = rng.choice([2, 3, 4, 5, 6, 7, 8, 9])
        y = rng.choice([v for v in range(-3, 6) if abs(sp.Integer(b) ** v) <= 1000 and v not in (0,)])
        x = sp.Integer(b) ** y
        prompt, why = f"\\log_{{{b}}} {sp.latex(x)}", f"${b}^{{{y}}} = {sp.latex(x)}$, so the log is ${y}$."
        answer = sp.Integer(y)
        wrong = [-y, sp.Rational(1, y), y + 1, x / b]
    elif variant == "shared":
        c = rng.choice([2, 3, 5])
        m = rng.choice([2, 3] if c > 2 else [2, 3, 4])
        n = rng.choice([v for v in range(-4, 6) if v % m and abs(c**v) <= 243])
        b, x = sp.Integer(c) ** m, sp.Integer(c) ** n
        prompt = f"\\log_{{{b}}} {sp.latex(x)}"
        answer = sp.Rational(n, m)
        why = f"Write both as powers of ${c}$: ${b} = {c}^{{{m}}}$ and ${sp.latex(x)} = {c}^{{{n}}}$. Then ${c}^{{{m}y}} = {c}^{{{n}}}$, so ${m}y = {n}$ and $y = {sp.latex(answer)}$."
        wrong = [sp.Rational(m, n), n - m, -answer, sp.Rational(n, m + 1)]
    elif variant == "common":
        y = rng.choice([v for v in range(-7, 9) if v != 0])
        shown = f"{10**y:,}".replace(",", "{,}") if y > 0 else "0." + "0" * (-y - 1) + "1"
        prompt = f"\\log {shown}"
        answer = sp.Integer(y)
        why = f"$\\log$ with no base means base 10. ${shown} = 10^{{{y}}}$"
        why += f" - the decimal point moved {abs(y)} place{'s' if abs(y) != 1 else ''} {'right' if y > 0 else 'left'} from 1."
        wrong = [-y, y - 1 if y < 0 else y + 1, -y - 1, 10 * y]
    elif variant == "natural":
        y = rng.choice([v for v in range(-9, 14) if v != 0])
        prompt, answer = f"\\ln e^{{{y}}}", sp.Integer(y)
        why = f"$\\ln$ is log base $e$, so $\\ln e^{{{y}}}$ asks what power of $e$ gives $e^{{{y}}}$: ${y}$."
        wrong = [-y, y + 1, sp.Rational(1, y), 0]
    else:
        fn = rng.choice(["log", "ln"])
        arg = rng.choice([2, 3, 5, 7, 12, 20, 45, 75, 150, 500, sp.Rational(18, 10), sp.Rational(32, 10), sp.Rational(5, 10)])
        val = math.log10(float(arg)) if fn == "log" else math.log(float(arg))
        other = math.log(float(arg)) if fn == "log" else math.log10(float(arg))
        return Spec(
            prompt=f"Use a calculator: $\\{fn} {nice_number(arg)}$. Round to four decimal places.",
            answer=f"${dec(val, 4)}$",
            kind="numbers",
            expected=[rounded(val, 4)],
            distractors=dec_options(val, [other, float(arg) / 10, -val, val * 10], 4),
            tolerance=0.00015,
            input_hint="e.g. 1.6532",
            explanation=f"Use the {'LOG' if fn == 'log' else 'LN'} key: $\\{fn} {nice_number(arg)} \\approx {dec(val, 4)}$, meaning ${'10' if fn == 'log' else 'e'}^{{{dec(val, 4)}}} \\approx {nice_number(arg)}$.",
        )
    return Spec(
        prompt=f"Evaluate ${prompt}$.",
        answer=num(answer),
        kind="numbers",
        expected=[answer],
        distractors=num_options(answer, wrong),
        input_hint="A number, e.g. -2 or 3/4",
        explanation=why,
    )


# ---------------------------------------------------------------- 6. solving exponential equations


@generator("solving-exponential-equations", "Solving exponential equations")
def solving_exponential_equations(rng: random.Random) -> Spec:
    variant = rng.choice(["one-base", "two-bases", "two-bases", "isolate", "shifted"])
    b = rng.choice([2, 3, 4, 5, 6, 7])

    if variant == "isolate":
        a, k = rng.choice([2, 3, 4, 5]), rng.randint(2, 5)
        c = a * b**k
        return Spec(
            prompt=f"Solve ${a} \\cdot {b}^x = {c}$.",
            answer=f"$x = {k}$",
            kind="numbers",
            expected=[sp.Integer(k)],
            distractors=[f"$x = {w}$" for w in dict.fromkeys([k + 1, k - 1, round(math.log(c) / math.log(a * b), 2), c // b]) if w != k],
            input_hint="e.g. 4",
            explanation=f"Isolate the exponential first: divide by ${a}$ to get ${b}^x = {b**k}$. Then ${b}^{{{k}}} = {b**k}$, so $x = {k}$.",
        )
    if variant in ("one-base", "shifted"):
        c = rng.choice([v for v in range(5, 90) if abs(math.log(v, b) - round(math.log(v, b))) > 0.05])
        m = 0 if variant == "one-base" else nonzero(rng, -4, 4)
        x = math.log(c) / math.log(b) - m
        lhs = f"{b}^{{x {'+' if m > 0 else '-'} {abs(m)}}}" if m else f"{b}^x"
        why = f"Take $\\ln$ of both sides and bring the exponent down: ${'(x + ' + str(m) + ')' if m > 0 else '(x - ' + str(-m) + ')' if m else 'x'}\\ln {b} = \\ln {c}$. "
        why += f"So {'$x + ' + str(m) if m > 0 else '$x - ' + str(-m) if m else '$x'} = \\frac{{\\ln {c}}}{{\\ln {b}}} \\approx {dec(x + m)}$" + (f", and $x \\approx {dec(x)}$." if m else ".")
        wrong = [math.log(b) / math.log(c) - m, x + 2 * m if m else c / b, math.log(c - b) / math.log(b) if c > b + 1 else x + 1, math.log(c) - math.log(b)]
    else:
        c = rng.choice([v for v in [2, 3, 4, 5, 6, 7, 10] if v != b])
        m, n = rng.sample(range(-3, 4), 2)
        lb, lc = (math.log10, math.log10) if 10 in (b, c) else (math.log, math.log)
        # (x + m) ln b = (x + n) ln c  ->  x (ln b - ln c) = n ln c - m ln b
        x = (n * lc(c) - m * lb(b)) / (lb(b) - lc(c))
        side = lambda base, s: f"{base}^{{x {'+' if s > 0 else '-'} {abs(s)}}}" if s else f"{base}^{{x}}"
        lhs = side(b, m)
        rhs_tex = side(c, n)
        fn = "\\log" if 10 in (b, c) else "\\ln"
        fac = lambda sh: "x" if not sh else f"(x {'+' if sh > 0 else '-'} {abs(sh)})"
        rhs = " ".join(
            f"{'-' if v < 0 else '+'} {abs(v) if abs(v) != 1 else ''}{fn} {base}" for v, base in ((n, c), (-m, b)) if v
        ).lstrip("+ ").replace("- ", "-", 1) if (n or m) else "0"
        why = (
            f"Take ${fn}$ of both sides{' (a base is 10, so use the common log)' if fn == chr(92) + 'log' else ''} and use the power rule: "
            f"${fac(m)}{fn} {b} = {fac(n)}{fn} {c}$. "
            f"Distribute, gather the $x$-terms on one side, and factor out $x$: $x({fn} {b} - {fn} {c}) = {rhs}$. "
            f"Divide: $x = \\frac{{{rhs}}}{{{fn} {b} - {fn} {c}}} \\approx {dec(x)}$."
        )
        wrong = [(m * lb(b) - n * lc(c)) / (lb(b) - lc(c)), (n * lc(c) - m * lb(b)) / (lb(b) + lc(c)), (n - m) * lc(c) / lb(b), x + 1]
        return Spec(
            prompt=f"Solve ${lhs} = {rhs_tex}$. Round to the nearest hundredth.",
            answer=f"$x \\approx {dec(x)}$",
            kind="numbers",
            expected=[rounded(x, 4)],
            distractors=dec_options(x, wrong, prefix="x \\approx "),
            tolerance=0.006,
            input_hint="A decimal, e.g. -1.76",
            explanation=why,
        )
    return Spec(
        prompt=f"Solve ${lhs} = {c}$. Round to the nearest hundredth.",
        answer=f"$x \\approx {dec(x)}$",
        kind="numbers",
        expected=[rounded(x, 4)],
        distractors=dec_options(x, wrong, prefix="x \\approx "),
        tolerance=0.006,
        input_hint="A decimal, e.g. 2.73",
        explanation=why,
    )


# ---------------------------------------------------------------- 7. compound interest and growth


@generator("compound-interest", "Compound interest and continuous growth")
def compound_interest(rng: random.Random) -> Spec:
    variant = rng.choice(["periodic", "periodic", "continuous", "decay"])
    if variant == "decay":
        p = rng.choice([50_000, 100_000, 150_000, 200_000, 500_000])
        pct = rng.choice([10, 15, 20, 25, 30])
        t, unit_text = rng.choice([(24, "one day"), (24, "one day"), (12, "12 hours"), (6, "6 hours")])
        days = t / 24
        amount = p * math.exp(-pct / 100 * t)
        wrong = [p * math.exp(-pct / 100 * days), p * math.exp(-pct * t / 1000), p * (1 - pct / 100) ** t, p * math.exp(-pct / 100 * t / 2)]
        return Spec(
            prompt=(
                f"A bacteria culture treated with an antibiotic follows $C(t) = C_0 e^{{-kt}}$, with $t$ in hours. "
                f"The bacteria die at a continuous rate of {pct}% per hour, starting from {p:,} per ml. How many are left after {unit_text}? Round to the nearest whole number."
            ),
            answer=f"${dec(amount, 0)}$",
            kind="numbers",
            expected=[rounded(amount, 0)],
            distractors=dec_options(amount, wrong, 0),
            tolerance=1.01,
            input_hint="A whole number, e.g. 373",
            explanation=(
                f"$C_0 = {p:,}$".replace(",", "{,}") + f", $k = {pct / 100:g}$ (the percent as a decimal), and $t = {t}$ hours"
                + (" - the rate is per hour, so convert the day to hours" if t == 24 else "")
                + f". $C({t}) = {p:,}".replace(",", "{,}") + f"e^{{-{pct / 100:g}({t})}} \\approx {dec(amount, 0)}$."
            ),
        )

    p = rng.choice([1_000, 2_000, 2_500, 5_000, 10_000, 25_000, 50_000])
    r = rng.choice([2, 3, 4, 5, 6, 7, 8, 12, sp.Rational(7, 2), sp.Rational(9, 2)])
    rf = float(r) / 100
    t = rng.choice([2, 3, 5, 8, 10, 15, 20])
    if variant == "continuous":
        amount = p * math.exp(rf * t)
        how = f"compounded continuously"
        why = f"Continuous: $A = Pe^{{rt}} = {p:,}".replace(",", "{,}") + f"e^{{{rf:g}({t})}} = {p:,}".replace(",", "{,}") + f"e^{{{rf * t:g}}} \\approx \\${dec(amount)}$."
        wrong = [p * (1 + rf) ** t, p * math.exp(float(r) * t / 10), p * (1 + rf * t), p * math.exp(rf) * t]
    else:
        n, name = rng.choice([(1, "annually"), (2, "semiannually"), (4, "quarterly"), (12, "monthly")])
        amount = p * (1 + rf / n) ** (n * t)
        how = f"compounded {name}"
        why = (
            f"$A = P\\left(1 + \\frac{{r}}{{n}}\\right)^{{nt}}$ with $r = {rf:g}$, $n = {n}$, $t = {t}$: "
            + f"${p:,}".replace(",", "{,}") + f"\\left(1 + \\frac{{{rf:g}}}{{{n}}}\\right)^{{{n * t}}} \\approx \\${dec(amount)}$."
        )
        wrong = [p * (1 + rf / n) ** t, p * math.exp(rf * t), p * (1 + rf) ** (n * t), p * (1 + rf * t)]
        if n == 1:
            wrong[0] = p * (1 + rf) ** (t + 1)
    return Spec(
        prompt=f"{money(p)} is invested at {nice_number(r)}% interest, {how}. How much is in the account after {t} years? Round to the nearest cent.",
        answer=f"$\\${dec(amount)}$",
        kind="numbers",
        expected=[rounded(amount, 2)],
        distractors=dec_options(amount, wrong, 2, prefix="\\$"),
        tolerance=0.015,
        input_hint="Dollars and cents, e.g. 13498.59",
        explanation=why + " Write the rate as a decimal first.",
    )
