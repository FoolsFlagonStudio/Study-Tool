"""Section 1, Module 2 - Algebraic Expressions and Equations."""

from __future__ import annotations

import math
import random

import sympy as sp

from ..core.problem import Spec, generator
from ..core.symbols import SYMS, show_numbers, tex, x, y

WORDS_HINT = "Use x for the number, e.g. 3x - 7 or (x + 2)/5"


# ---------------------------------------------------------------- 1. single operations


def _single_phrases(n: int, pct: int):
    """(phrase, correct, distractors, why) - distractors are the usual misreadings."""
    return [
        (f"{n} more than a number", x + n, [x - n, n * x, n - x], "**more than** means add."),
        (f"a number increased by {n}", x + n, [x - n, n * x, x / n], "**increased by** means add."),
        (f"the sum of a number and {n}", x + n, [n * x, x - n, x / n], "**sum** means add."),
        (f"{n} less than a number", x - n, [n - x, x + n, n * x],
         "**less than** flips the order: start with the number, then take away " + str(n) + "."),
        (f"{n} subtracted from a number", x - n, [n - x, x + n, x / n],
         "**subtracted from** flips the order: you take " + str(n) + " away *from* the number."),
        (f"a number subtracted from {n}", n - x, [x - n, x + n, n * x],
         f"Start with {n} and take the number away from it."),
        (f"a number decreased by {n}", x - n, [n - x, x + n, x / n], "**decreased by** means subtract."),
        (f"the difference of a number and {n}", x - n, [n - x, x + n, n * x],
         "**difference** means subtract, in the order given."),
        (f"the product of {n} and a number", n * x, [x + n, x / n, n - x], "**product** means multiply."),
        (f"the quotient of a number and {n}", x / n, [n / x, n * x, x - n],
         "**quotient** means divide, in the order given."),
        (f"the ratio of {n} and a number", n / x, [x / n, n * x, n - x],
         "**ratio** means divide, in the order given."),
        ("half of a number", x / 2, [2 * x, x - sp.Rational(1, 2), x + sp.Rational(1, 2)], "**half of** means divide by 2."),
        ("triple a number", 3 * x, [x + 3, x / 3, x**3], "**triple** means multiply by 3."),
        ("twice a number", 2 * x, [x + 2, x / 2, x**2], "**twice** means multiply by 2."),
        (f"{pct} percent of a number", sp.Rational(pct, 100) * x, [pct * x, x / pct, x + sp.Rational(pct, 100)],
         f"**percent** means divide by 100, and **of** means multiply: ${sp.latex(sp.Rational(pct, 100))}x$."),
    ]


@generator("translating-words", "Translating words into math")
def translating_words(rng: random.Random) -> Spec:
    n = rng.randint(2, 30)
    pct = rng.choice([5, 10, 15, 20, 25, 30, 40, 60, 75])
    phrase, correct, distractors, why = rng.choice(_single_phrases(n, pct))
    return Spec(
        prompt=f"Translate into an algebraic expression, using $x$ for the number: “{phrase}”",
        answer=tex(correct),
        kind="expr",
        expected=correct,
        distractors=distractors,
        input_hint=WORDS_HINT,
        explanation=why,
    )


# ---------------------------------------------------------------- 2. multiple operations


@generator("multi-operation-expressions", "Phrases with multiple operations")
def multi_operation_expressions(rng: random.Random) -> Spec:
    a, b = rng.randint(2, 9), rng.randint(2, 20)
    while b == a:
        b = rng.randint(2, 20)
    templates = [
        (f"the product of {a} and a number, plus {b}", a * x + b, [a * (x + b), a + x + b, b * x + a],
         f"The comma groups “the product of {a} and a number” first: ${a}x$, then add {b}."),
        (f"{a} times the sum of a number and {b}", a * (x + b), [a * x + b, a + x + b, a * b * x],
         f"“The sum of a number and {b}” is one group, $(x + {b})$, and the whole group is multiplied by {a}."),
        (f"{b} less than {a} times a number", a * x - b, [b - a * x, a * (x - b), a - b * x],
         f"“{a} times a number” is ${a}x$, and “{b} less than” that takes {b} away from it."),
        (f"the ratio of {b} less than a number and {a}", (x - b) / a, [(b - x) / a, x / a - b, a / (x - b)],
         f"“{b} less than a number” is $x - {b}$, and that whole quantity is divided by {a}."),
        (f"the quotient of a number and {a}, increased by {b}", x / a + b, [x / (a + b), (x + b) / a, a / x + b],
         f"The comma means divide first, $\\frac{{x}}{{{a}}}$, then add {b}."),
        (f"twice the difference of a number and {b}", 2 * (x - b), [2 * x - b, 2 * (b - x), 2 * x + b],
         f"“The difference of a number and {b}” is the group $(x - {b})$, and the whole group is doubled."),
        (f"the sum of a number and {b}, divided by the number", (x + b) / x, [x + b / x, x / (x + b), b / x],
         "The comma means the whole sum is divided by the number."),
        (f"the quotient of two numbers decreased by {a} times their sum", x / y - a * (x + y),
         [x / y - a * x + y, a * (x + y) - x / y, x / y - a * x - a],
         f"Using $x$ and $y$: “quotient” is $\\frac{{x}}{{y}}$, and “{a} times their sum” is ${a}(x + y)$, which is subtracted."),
    ]
    words = [
        ("you have \\${s} saved and deposit \\${d} every week", "w", "weeks", lambda s, d, v: s + d * v,
         lambda s, d, v: [s * v + d, s - d * v, (s + d) * v], "Start amount plus the weekly deposit times the number of weeks."),
        ("a gym charges a \\${s} signup fee plus \\${d} per month", "m", "months", lambda s, d, v: s + d * v,
         lambda s, d, v: [s * v + d, (s + d) * v, s - d * v], "One-time fee plus the monthly price times the number of months."),
        ("you have \\${s} saved and spend \\${d} every week", "w", "weeks", lambda s, d, v: s - d * v,
         lambda s, d, v: [s + d * v, d * v - s, (s - d) * v], "Start amount minus the weekly spending times the number of weeks."),
        ("a {s}-foot board is cut into two pieces, and one piece is $x$ feet long", "x", None, lambda s, d, v: s - v,
         lambda s, d, v: [v - s, s + v, s * v], "The two pieces add up to the whole board, so the other piece is what's left."),
    ]
    if rng.random() < 0.35:
        story, var, unit, rule, wrong, why = rng.choice(words)
        s, d = rng.randrange(50, 1000, 10), rng.randrange(5, 60, 5)
        if unit is None:
            s = rng.randint(8, 40)
        sym = SYMS[var]
        story = story.format(s=s, d=d)
        correct = rule(s, d, sym)
        ask = (
            f"Write an expression for the amount after ${var}$ {unit}."
            if unit
            else "Write an expression for the length of the other piece."
        )
        prompt = f"Suppose {story}. {ask}"
        distractors = wrong(s, d, sym)
        hint = f"Use {var} as the variable"
    else:
        phrase, correct, distractors, why = rng.choice(templates)
        uses_y = correct.has(y)
        prompt = (
            f"Translate into an algebraic expression{', using $x$ and $y$ for the two numbers' if uses_y else ', using $x$ for the number'}: “{phrase}”"
        )
        hint = WORDS_HINT
    return Spec(
        prompt=prompt,
        answer=tex(correct),
        kind="expr",
        expected=correct,
        distractors=distractors,
        input_hint=hint,
        explanation=why,
    )


# ---------------------------------------------------------------- 3. simplifying roots


SQUAREFREE = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15]
CUBEFREE = [2, 3, 4, 5, 6, 7, 9, 10]


def _root_tex(index: int, inside: str) -> str:
    return f"\\sqrt{{{inside}}}" if index == 2 else f"\\sqrt[{index}]{{{inside}}}"


def _var_part(pairs) -> str:
    return "".join(var if e == 1 else f"{var}^{{{e}}}" for var, e in pairs if e > 0)


@generator("simplifying-rational-exponents", "Simplifying roots with rational exponents")
def simplifying_rational_exponents(rng: random.Random) -> Spec:
    variant = rng.choice(["square", "square", "cube", "variables", "product"])

    if variant in ("square", "cube"):
        index = 2 if variant == "square" else 3
        outside = rng.randint(2, 10 if index == 2 else 5)
        inside = rng.choice(SQUAREFREE if index == 2 else CUBEFREE)
        number = outside**index * inside
        correct = outside * sp.root(inside, index)
        shown = f"{number}^{{\\frac{{1}}{{{index}}}}}" if rng.random() < 0.6 else _root_tex(index, str(number))
        distractors = [
            f"${inside}{_root_tex(index, str(outside))}$",
            f"${_root_tex(index, str(inside))}$",
            f"${outside}{_root_tex(5 - index, str(inside))}$",
            f"${outside**index}{_root_tex(index, str(inside))}$",
            f"${outside + 1}{_root_tex(index, str(inside))}$",
        ]
        if outside % 2 == 0 and index == 2:
            distractors.append(f"${outside // 2}{_root_tex(2, str(4 * inside))}$")
        perfect = "square" if index == 2 else "cube"
        return Spec(
            prompt=f"Simplify ${shown}$.",
            answer=f"${outside}{_root_tex(index, str(inside))}$",
            kind="expr",
            expected=correct,
            distractors=distractors,
            form="radical",
            input_hint="Type roots as sqrt(2) or cbrt(2), e.g. 6sqrt(2)",
            explanation=(
                f"Find the largest perfect {perfect} factor: ${number} = {outside**index} \\cdot {inside}$. "
                f"Then $({outside**index} \\cdot {inside})^{{\\frac{{1}}{{{index}}}}} = "
                f"{outside**index}^{{\\frac{{1}}{{{index}}}}} \\cdot {inside}^{{\\frac{{1}}{{{index}}}}} = {sp.latex(correct)}$."
            ),
        )

    if variant == "variables":
        index = rng.choice([2, 3])
        names = sorted(rng.sample(["x", "y", "z"], rng.choice([2, 3])))
        while True:
            exps = [rng.randint(1, 9) for _ in names]
            if any(e >= index for e in exps) and any(e % index for e in exps):
                break
        pairs = list(zip(names, exps))
        out = [(var, e // index) for var, e in pairs]
        ins = [(var, e % index) for var, e in pairs]

        def show(outside, inside, idx=index):
            inner = _var_part(inside)
            return f"${_var_part(outside)}{_root_tex(idx, inner) if inner else ''}$"

        answer = show(out, ins)
        partial = list(out)
        j = next(i for i, (_, e) in enumerate(out) if e > 0)
        partial[j] = (out[j][0], out[j][1] - 1)
        partial_in = list(ins)
        partial_in[j] = (ins[j][0], ins[j][1] + index)
        distractors = [
            show([(v, e) for v, e in ins], [(v, e) for v, e in out]),
            show(out, ins, 5 - index),
            show(partial, partial_in),
            show([(v, e // index + 1) for v, e in pairs], ins),
        ]
        rule = "square" if index == 2 else "cube"
        return Spec(
            prompt=f"Simplify $\\left({_var_part(pairs)}\\right)^{{\\frac{{1}}{{{index}}}}}$.",
            answer=answer,
            kind="choice",
            distractors=distractors,
            explanation=(
                f"Divide each exponent by {index}: the whole-number part comes out of the {rule} root and the "
                f"remainder stays inside. "
                + ", ".join(f"${v}^{{{e}}}$: {e} ÷ {index} = {e // index} R {e % index}" for v, e in pairs)
                + "."
            ),
        )

    # product of two radicals with the same base
    while True:
        i1, i2 = rng.sample([2, 3, 4, 5], 2)
        e1, e2 = rng.randint(1, i1 - 1 if i1 > 2 else 1), rng.randint(1, max(1, i2 - 1))
        total = sp.Rational(e1, i1) + sp.Rational(e2, i2)
        if total.q > 1:
            break
    var = rng.choice(["x", "y", "a"])

    def rad(power, index):
        return _root_tex(index, var if power == 1 else f"{var}^{{{power}}}")

    answer = f"${rad(total.p, total.q)}$"
    return Spec(
        prompt=f"Simplify ${rad(e1, i1)} \\cdot {rad(e2, i2)}$ and write the answer as a single radical.",
        answer=answer,
        kind="choice",
        distractors=[
            f"${rad(e1 + e2, i1 + i2)}$",
            f"${rad(e1 * e2, i1 * i2)}$",
            f"${rad(e1 + e2, total.q)}$",
            f"${rad(total.q, total.p)}$" if total.p > 1 else f"${var}^{{{total.q}}}$",
        ],
        explanation=(
            f"Convert to exponents: ${var}^{{\\frac{{{e1}}}{{{i1}}}}} \\cdot {var}^{{\\frac{{{e2}}}{{{i2}}}}}$. "
            f"Same base, so add: $\\frac{{{e1}}}{{{i1}}} + \\frac{{{e2}}}{{{i2}}} = \\frac{{{total.p}}}{{{total.q}}}$. "
            f"Back to a radical (power over root): ${rad(total.p, total.q)}$."
        ),
    )


# ---------------------------------------------------------------- 4. solving equations


@generator("solving-rational-exponent-equations", "Solving equations with rational exponents")
def solving_rational_exponent_equations(rng: random.Random) -> Spec:
    while True:
        q, p = rng.randint(2, 5), rng.randint(1, 4)
        r = rng.randint(2, 9)
        if math.gcd(p, q) == 1 and p != q and r**p <= 1000 and r**q <= 5000:
            break
    root_val = r**q  # the positive solution
    rhs = r**p  # x^(p/q) equals this after isolating
    exp_tex = f"\\frac{{{p}}}{{{q}}}"
    expected = [root_val, -root_val] if p % 2 == 0 else [root_val]

    form = rng.choice(["minus", "plus", "coef", "nested" if p > 1 else "minus"])
    if form == "minus":
        d = rng.randint(1, 12)
        equation = f"x^{{{exp_tex}}} - {d} = {rhs - d}"
        isolate = f"Add {d} to both sides: $x^{{{exp_tex}}} = {rhs}$."
    elif form == "plus":
        d = rng.randint(1, 12)
        equation = f"x^{{{exp_tex}}} + {d} = {rhs + d}"
        isolate = f"Subtract {d} from both sides: $x^{{{exp_tex}}} = {rhs}$."
    elif form == "coef":
        k = rng.randint(2, 5)
        equation = f"{k}x^{{{exp_tex}}} = {k * rhs}"
        isolate = f"Divide both sides by {k}: $x^{{{exp_tex}}} = {rhs}$."
    else:
        equation = f"\\left(x^{{{p}}}\\right)^{{\\frac{{1}}{{{q}}}}} - {rhs} = 0"
        isolate = f"Simplify the power and isolate: $x^{{{exp_tex}}} = {rhs}$."

    wrong_power = sp.nsimplify(sp.Integer(rhs) ** sp.Rational(p, q))
    distractors = [
        [root_val] if p % 2 == 0 else [root_val, -root_val],
        [rhs],
        [r],
        [root_val * r],
    ]
    if wrong_power.is_Rational:
        distractors.append([wrong_power])

    sign_note = (
        f"The numerator {p} is even, so $x$ was effectively squared: both ${root_val}$ and $-{root_val}$ work."
        if p % 2 == 0
        else f"The numerator {p} is odd, so there's only one solution."
    )
    return Spec(
        prompt=f"Solve for $x$: ${equation}$",
        answer=show_numbers(expected),
        kind="numbers",
        expected=expected,
        distractors=distractors,
        input_hint="For two answers, separate with a comma or type +- (e.g. +-27)",
        explanation=(
            f"{isolate} Raise both sides to the reciprocal power $\\frac{{{q}}}{{{p}}}$: "
            f"${rhs}^{{\\frac{{{q}}}{{{p}}}}} = {root_val}$. {sign_note}"
        ),
    )
