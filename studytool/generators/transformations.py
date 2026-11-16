"""Section 2, Module 7 - Function Transformations and Symmetry."""

from __future__ import annotations

import random

import sympy as sp

from ..core.problem import Spec, generator
from ..core.symbols import coef_tex, join_terms, nice_number, nonzero, show_pair, x
from .quadratics import num, num_options

PAIR_HINT = "Type the ordered pair, e.g. (2, -3)"
EVEN_ODD = ["Even", "Odd", "Neither"]
AXES = ["Across the x-axis", "Across the y-axis"]

# name: (key point word, nice points (x, f(x)) for following a point)
PARENTS = {
    "square": ("vertex", [(1, 1), (2, 4), (3, 9), (-2, 4), (-1, 1)]),
    "cube": ("center", [(1, 1), (2, 8), (-1, -1), (-2, -8)]),
    "abs": ("vertex", [(1, 1), (2, 2), (-3, 3), (-4, 4)]),
    "sqrt": ("starting point", [(1, 1), (4, 2), (9, 3), (16, 4)]),
    "cbrt": ("center", [(1, 1), (8, 2), (-1, -1), (-8, -2)]),
}


def body(parent: str, inner: str = "x") -> str:
    """LaTeX for a parent function applied to an inner expression."""
    if parent == "square":
        return "x^2" if inner == "x" else f"({inner})^2"
    if parent == "cube":
        return "x^3" if inner == "x" else f"({inner})^3"
    if parent == "abs":
        return f"|{inner}|"
    if parent == "sqrt":
        return f"\\sqrt{{{inner}}}"
    return f"\\sqrt[3]{{{inner}}}"


def parent_value(parent: str, val):
    val = sp.nsimplify(val)
    return {"square": val**2, "cube": val**3, "abs": abs(val), "sqrt": sp.sqrt(val), "cbrt": sp.sign(val) * sp.root(abs(val), 3)}[parent]


def inner(h) -> str:
    """x - h, written as the course writes it."""
    h = sp.nsimplify(h)
    return "x" if h == 0 else f"x - {sp.latex(h)}" if h > 0 else f"x + {sp.latex(-h)}"


def outer(a, b: str, k=0) -> str:
    """a * b + k, written plainly."""
    k = sp.nsimplify(k)
    out = f"{coef_tex(a)}{b}"
    return out + ("" if k == 0 else f" + {sp.latex(k)}" if k > 0 else f" - {sp.latex(-k)}")


def shift_words(h, k) -> list[str]:
    words = []
    if h:
        words.append(f"{'right' if h > 0 else 'left'} {abs(h)}")
    if k:
        words.append(f"{'up' if k > 0 else 'down'} {abs(k)}")
    return words


def units(n) -> str:
    return f"{n} unit{'' if n == 1 else 's'}"


def pick_parent(rng: random.Random, *names: str) -> str:
    return rng.choice(names or tuple(PARENTS))


# ---------------------------------------------------------------- 1. single shifts


@generator("function-shifts", "Vertical and horizontal shifts")
def function_shifts(rng: random.Random) -> Spec:
    parent = pick_parent(rng)
    n = rng.randint(1, 9)
    direction = rng.choice(["up", "down", "left", "right"])
    forms = {
        "up": outer(1, body(parent), n),
        "down": outer(1, body(parent), -n),
        "left": body(parent, inner(-n)),
        "right": body(parent, inner(n)),
    }
    point = {"up": (0, n), "down": (0, -n), "left": (-n, 0), "right": (n, 0)}
    where = "outside, changing the output" if direction in ("up", "down") else "inside, changing the input"
    rule = {
        "up": f"Adding {n} to the output moves every point up {n}.",
        "down": f"Subtracting {n} from the output moves every point down {n}.",
        "left": f"Adding {n} to $x$ shifts the graph **left** {n} - the inside works backwards.",
        "right": f"Subtracting {n} from $x$ shifts the graph **right** {n} - the inside works backwards.",
    }[direction]
    key = PARENTS[parent][0]
    variant = rng.choice(["describe", "equation", "point"])

    if variant == "describe":
        return Spec(
            prompt=f"Compared with $f(x) = {body(parent)}$, how is $g(x) = {forms[direction]}$ shifted?",
            answer=f"{direction.capitalize()} {units(n)}",
            kind="choice",
            distractors=[f"{d.capitalize()} {units(n)}" for d in forms if d != direction],
            explanation=f"The change is {where}. {rule}",
        )
    if variant == "equation":
        return Spec(
            prompt=f"The graph of $f(x) = {body(parent)}$ is shifted {units(n)} {direction}. Which function is it?",
            answer=f"$g(x) = {forms[direction]}$",
            kind="choice",
            distractors=[f"$g(x) = {forms[d]}$" for d in forms if d != direction],
            explanation=rule,
        )
    return Spec(
        prompt=f"The {key} of $f(x) = {body(parent)}$ is $(0, 0)$. Where is the {key} of $g(x) = {forms[direction]}$?",
        answer=show_pair(point[direction]),
        kind="numbers",
        expected=tuple(sp.Integer(v) for v in point[direction]),
        ordered=True,
        distractors=[tuple(p) for d, p in point.items() if d != direction],
        input_hint=PAIR_HINT,
        explanation=f"{rule} So $(0, 0)$ moves to {show_pair(point[direction])}.",
    )


# ---------------------------------------------------------------- 2. combined shifts


@generator("combined-shifts", "Combining shifts")
def combined_shifts(rng: random.Random) -> Spec:
    parent = pick_parent(rng)
    h, k = nonzero(rng, -7, 7), nonzero(rng, -9, 9)
    g = outer(1, body(parent, inner(h)), k)
    key = PARENTS[parent][0]
    words = shift_words(h, k)
    why = (
        f"Inside, $({inner(h)})$ shifts the graph {words[0]} (backwards from the sign). "
        f"Outside, ${'+' if k > 0 else '-'} {abs(k)}$ shifts it {words[1]}."
    )
    variant = rng.choice(["point", "point", "describe", "equation"])

    if variant == "describe":
        def say(hh, kk):
            w = shift_words(hh, kk)
            return f"{w[0].split()[0].capitalize()} {w[0].split()[1]}, {w[1]}"

        return Spec(
            prompt=f"Starting from $f(x) = {body(parent)}$, describe the graph of $g(x) = {g}$.",
            answer=say(h, k),
            kind="choice",
            distractors=[say(-h, k), say(h, -k), say(-h, -k), say(k, h) if abs(k) <= 9 and k != h else say(-h, k)],
            explanation=why,
        )
    if variant == "equation":
        wrong = [outer(1, body(parent, inner(-h)), k), outer(1, body(parent, inner(h)), -k), outer(1, body(parent, inner(-h)), -k), outer(1, body(parent, inner(k)), h)]
        return Spec(
            prompt=f"The graph of $f(x) = {body(parent)}$ is moved so its {key} is at $({h}, {k})$. Which function is it?",
            answer=f"$g(x) = {g}$",
            kind="choice",
            distractors=[f"$g(x) = {w}$" for w in wrong if w != g],
            explanation=f"To move the {key} to $x = {h}$, the inside must be 0 there: $({inner(h)})$. Then add ${k}$ outside. " + why,
        )
    return Spec(
        prompt=f"The {key} of $f(x) = {body(parent)}$ is $(0, 0)$. Where is the {key} of $g(x) = {g}$?",
        answer=show_pair((h, k)),
        kind="numbers",
        expected=(sp.Integer(h), sp.Integer(k)),
        ordered=True,
        distractors=[(-h, k), (h, -k), (-h, -k), (k, h)],
        input_hint=PAIR_HINT,
        explanation=why + f" The {key} moves to $({h}, {k})$.",
    )


# ---------------------------------------------------------------- 3. reflections


def _random_poly(rng: random.Random):
    degree = rng.choice([2, 2, 3])
    terms = [nonzero(rng, -4, 4) * x**degree]
    for power in range(degree - 1, 0, -1):
        if rng.random() < 0.7:
            terms.append(nonzero(rng, -9, 9) * x**power)
    terms.append(sp.Integer(nonzero(rng, -12, 12)))
    return sum(terms)


@generator("reflections", "Reflections")
def reflections(rng: random.Random) -> Spec:
    variant = rng.choice(["poly", "poly", "radical", "name"])
    axis = rng.choice(["x", "y"])

    if variant == "poly":
        f = _random_poly(rng)
        terms = sp.Add.make_args(f)
        const = [t for t in terms if t.is_Number][0]
        lead = sp.LT(f, x)
        if axis == "x":
            g = sp.expand(-f)
            wrong = [sp.expand(f - 2 * lead), sp.expand(f.subs(x, -x)), sp.expand(-f + 2 * const), sp.expand(-f.subs(x, -x))]
            why = f"Reflecting over the $x$-axis is $-f(x)$: multiply **every** term by $-1$. $-({sp.latex(f)}) = {sp.latex(g)}$."
        else:
            g = sp.expand(f.subs(x, -x))
            wrong = [sp.expand(-f), sp.expand(g - 2 * const), sp.expand(-g), sp.expand(f - 2 * lead)]
            shown = join_terms([t.subs(x, sp.Symbol("(-x)")) if not t.is_Number else t for t in sorted(terms, key=lambda t: -sp.degree(t, x))])
            why = f"Reflecting over the $y$-axis is $f(-x)$: replace each $x$ with $-x$. ${shown} = {sp.latex(g)}$. The constant doesn't change."
        return Spec(
            prompt=f"Reflect $f(x) = {sp.latex(f)}$ over the ${axis}$-axis. What is $g(x)$?",
            answer=f"${sp.latex(g)}$",
            kind="expr",
            expected=g,
            distractors=wrong,
            input_hint="e.g. -x^2 + 10x - 25",
            form="expanded",
            explanation=why,
        )

    parent = pick_parent(rng, "sqrt", "abs", "cbrt", "sqrt")
    h, k = rng.choice([0, nonzero(rng, -6, 6)]), rng.choice([0, nonzero(rng, -8, 8)])
    if h == 0 and k == 0:
        h = rng.choice([2, 3, -4])
    f = outer(1, body(parent, inner(h)), k)
    neg_inner = "-x" if h == 0 else f"-x - {h}" if h > 0 else f"-x + {-h}"
    over_x = outer(-1, body(parent, inner(h)), -k)
    over_y = outer(1, body(parent, neg_inner), k)

    if variant == "name":
        g, right = (over_x, AXES[0]) if axis == "x" else (over_y, AXES[1])
        return Spec(
            prompt=f"$f(x) = {f}$ and $g(x) = {g}$. How is $g$ reflected compared with $f$?",
            answer=right,
            kind="choice",
            choices=AXES,
            explanation=(
                "Every output got multiplied by $-1$: $g(x) = -f(x)$, a vertical reflection over the $x$-axis."
                if axis == "x"
                else "Every $x$ was replaced with $-x$: $g(x) = f(-x)$, a horizontal reflection over the $y$-axis."
            ),
        )
    answer = over_x if axis == "x" else over_y
    wrong = [
        over_y if axis == "x" else over_x,
        outer(-1, body(parent, inner(h)), k),
        outer(1, body(parent, inner(-h)), k),
        outer(1, body(parent, "-x" if h == 0 else f"-x + {h}" if h > 0 else f"-x - {-h}"), k),
        outer(1, body(parent, neg_inner), -k),
    ]
    return Spec(
        prompt=f"Reflect $f(x) = {f}$ over the ${axis}$-axis. Which function is it?",
        answer=f"$g(x) = {answer}$",
        kind="choice",
        distractors=[f"$g(x) = {w}$" for w in dict.fromkeys(wrong) if w != answer],
        explanation=(
            f"Over the $x$-axis means $-f(x)$: negate **every** term, giving ${over_x}$."
            if axis == "x"
            else f"Over the $y$-axis means $f(-x)$: replace $x$ with $-x$ and leave everything else, giving ${over_y}$."
        ),
    )


# ---------------------------------------------------------------- 4. even, odd, neither


def _parity_function(rng: random.Random):
    kind = rng.choice(EVEN_ODD)
    if rng.random() < 0.25:
        n = rng.choice([1, 2, 3])
        a = nonzero(rng, -6, 6)
        c = 0
        if kind == "Even":
            n = 2
            c = rng.choice([0, nonzero(rng, -5, 5)])
        elif kind == "Odd":
            n = rng.choice([1, 3])
        else:
            n, c = rng.choice([1, 3]), nonzero(rng, -5, 5)
        return kind, a / x**n + c
    if kind == "Even":
        powers = rng.sample([0, 2, 4, 6], rng.randint(2, 3))
        if powers == [0]:
            powers = [2, 0]
    elif kind == "Odd":
        powers = rng.sample([1, 3, 5, 7], rng.randint(1, 3))
    else:
        powers = [rng.choice([1, 3, 5]), rng.choice([0, 2, 4])]
        if rng.random() < 0.4:
            powers.append(rng.choice([1, 3, 5, 2, 4]))
    f = sum(nonzero(rng, -7, 7) * x**p for p in set(powers))
    if f.is_Number or f == 0:
        return _parity_function(rng)
    return kind, f


@generator("even-odd-functions", "Even, odd, or neither")
def even_odd_functions(rng: random.Random) -> Spec:
    kind, f = _parity_function(rng)
    actual = "Even" if sp.simplify(f.subs(x, -x) - f) == 0 else "Odd" if sp.simplify(f.subs(x, -x) + f) == 0 else "Neither"
    fneg = sp.expand(f.subs(x, -x))
    test = {
        "Even": f"$f(-x) = {sp.latex(fneg)} = f(x)$, so it's **even** (symmetric about the $y$-axis).",
        "Odd": f"$f(-x) = {sp.latex(fneg)} = -({sp.latex(f)}) = -f(x)$, so it's **odd** (symmetric about the origin).",
        "Neither": f"$f(-x) = {sp.latex(fneg)}$. That isn't $f(x)$, and it isn't $-f(x) = {sp.latex(sp.expand(-f))}$ either, so it's **neither**.",
    }[actual]

    if rng.random() < 0.3:
        return Spec(
            prompt=f"For $f(x) = {sp.latex(f)}$, simplify $f(-x)$.",
            answer=f"${sp.latex(fneg)}$",
            kind="expr",
            expected=fneg,
            distractors=[sp.expand(-f), f, sp.expand(-fneg), sp.expand(f + 1)],
            input_hint="e.g. 2x^4 + x^2",
            explanation=f"Replace every $x$ with $(-x)$. Even powers lose the negative; odd powers keep it. {test}",
        )
    return Spec(
        prompt=f"Is $f(x) = {sp.latex(f)}$ even, odd, or neither?",
        answer=actual,
        kind="choice",
        choices=EVEN_ODD,
        explanation=test,
    )


# ---------------------------------------------------------------- 5. vertical stretches


FACTORS = [2, 3, 4, 5, sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 4)]


def _stretch_words(direction: str, a) -> str:
    a = sp.nsimplify(a)
    if direction == "vertical":
        verb = "stretch" if a > 1 else "compression"
    else:
        verb = "compression" if a > 1 else "stretch"
    return f"{direction.capitalize()} {verb} by a factor of ${nice_number(a)}$"


def _other_words(direction: str, a) -> list[str]:
    other = "horizontal" if direction == "vertical" else "vertical"
    a = sp.nsimplify(a)
    flip = {"stretch": "compression", "compression": "stretch"}
    right = _stretch_words(direction, a)
    verb = right.split()[1]
    return [
        right.replace(verb, flip[verb]),
        _stretch_words(other, a),
        _stretch_words(other, a).replace(_stretch_words(other, a).split()[1], flip[_stretch_words(other, a).split()[1]]),
    ]


@generator("vertical-stretches", "Vertical stretches and compressions")
def vertical_stretches(rng: random.Random) -> Spec:
    parent = pick_parent(rng, "square", "cube", "abs", "sqrt")
    a = rng.choice(FACTORS)
    if rng.random() < 0.45:
        g = outer(a, body(parent))
        return Spec(
            prompt=f"Compared with $f(x) = {body(parent)}$, what does $g(x) = {g}$ do to the graph?",
            answer=_stretch_words("vertical", a),
            kind="choice",
            distractors=_other_words("vertical", a),
            explanation=(
                f"The ${nice_number(a)}$ multiplies the **output**, so every $y$-value is multiplied by ${nice_number(a)}$. "
                + ("Greater than 1 pulls the graph away from the $x$-axis: a vertical stretch." if a > 1 else "Between 0 and 1 squashes it toward the $x$-axis: a vertical compression.")
            ),
        )
    px, py = rng.choice([p for p in PARENTS[parent][1] if p[1] != 0 and abs(p[1]) != 1 or parent == "sqrt"])
    gy = a * py
    word = "stretched" if a > 1 else "compressed"
    return Spec(
        prompt=f"The graph of $f(x) = {body(parent)}$ is vertically {word}. The new graph $g(x) = a \\cdot {body(parent)}$ passes through $({px}, {nice_number(gy)})$. What is $a$?",
        answer=num(a),
        kind="numbers",
        expected=[a],
        distractors=num_options(a, [1 / a, gy, gy - py, py / gy if gy else 2]),
        input_hint="A number, e.g. 3 or 1/4",
        explanation=f"Substitute the point: ${nice_number(gy)} = a \\cdot {body(parent, str(px))} = {py}a$, so $a = {nice_number(a)}$.",
    )


# ---------------------------------------------------------------- 6. horizontal stretches


@generator("horizontal-stretches", "Horizontal stretches and compressions")
def horizontal_stretches(rng: random.Random) -> Spec:
    b = rng.choice([2, 3, 4, sp.Rational(3, 2), sp.Rational(4, 3), sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(3, 4), sp.Rational(1, 4)])
    b = sp.nsimplify(b)
    variant = rng.choice(["describe", "find-b", "find-b", "new-point"])
    btex = nice_number(b) if b.is_Integer or b.q == 2 else sp.latex(b)

    if variant == "describe":
        parent = pick_parent(rng, "square", "cube", "abs", "sqrt")
        if b.q not in (1, 2, 3, 4):
            b = sp.Integer(2)
        inside = f"{btex}x"
        return Spec(
            prompt=f"Compared with $f(x) = {body(parent)}$, what does $g(x) = {body(parent, inside)}$ do to the graph?",
            answer=_stretch_words("horizontal", b),
            kind="choice",
            distractors=_other_words("horizontal", b),
            explanation=(
                f"The ${nice_number(b)}$ multiplies the **input**, and inside changes work backwards: every $x$-coordinate is divided by ${nice_number(b)}$. "
                + ("Greater than 1 squeezes the graph toward the $y$-axis: a horizontal compression." if b > 1 else "Between 0 and 1 spreads it away from the $y$-axis: a horizontal stretch.")
            ),
        )

    new_x = sp.Rational(rng.choice([1, 2, 3, 4, 6, -2, -3, -4]), 1)
    old_x = b * new_x
    if not (old_x * 2).is_Integer:
        new_x = sp.Integer(4)
        old_x = b * new_x
    yv = rng.choice([0, 0, 2, 4, 5, -3])
    name = rng.choice(["s", "c"])
    if variant == "find-b":
        return Spec(
            prompt=f"The point $({nice_number(old_x)}, {yv})$ on the graph of ${name}(x)$ corresponds to the point $({nice_number(new_x)}, {yv})$ on $f(x) = {name}(bx)$. What is $b$?",
            answer=num(b),
            kind="numbers",
            expected=[b],
            distractors=num_options(b, [1 / b, old_x - new_x, old_x * new_x, b + 1]),
            input_hint="A number, e.g. 2 or 3/4",
            explanation=(
                f"To give the same output, the input of ${name}$ must be $b$ times the input of $f$: "
                f"${nice_number(old_x)} = b \\cdot {nice_number(new_x) if new_x >= 0 else '(' + nice_number(new_x) + ')'}$, so $b = {nice_number(b)}$. "
                + ("That's a horizontal compression." if b > 1 else "That's a horizontal stretch.")
            ),
        )
    return Spec(
        prompt=f"The point $({nice_number(old_x)}, {yv})$ is on the graph of $y = {name}(x)$. Where is the corresponding point on $y = {name}({btex}x)$?",
        answer=show_pair((new_x, yv)),
        kind="numbers",
        expected=(new_x, sp.Integer(yv)),
        ordered=True,
        distractors=[(old_x * b, yv), (old_x, yv * b if yv else b), (old_x, yv)],
        input_hint=PAIR_HINT,
        explanation=f"Inside changes divide the $x$-coordinate: ${nice_number(old_x)} \\div {nice_number(b)} = {nice_number(new_x)}$. The $y$-value stays ${yv}$.",
    )


# ---------------------------------------------------------------- 7. sequences of transformations


def _sequence_words(a, h, k) -> str:
    a = sp.nsimplify(a)
    parts = []
    if h:
        parts.append(f"shift {'right' if h > 0 else 'left'} {abs(h)}")
    if a < 0:
        parts.append("reflect over the x-axis")
    if abs(a) != 1:
        parts.append(f"{'stretch' if abs(a) > 1 else 'compress'} vertically by a factor of ${nice_number(abs(a))}$")
    if k:
        parts.append(f"shift {'up' if k > 0 else 'down'} {abs(k)}")
    text = ", ".join(parts[:-1]) + ", then " + parts[-1] if len(parts) > 1 else parts[0]
    return text[0].upper() + text[1:]


@generator("transformation-sequences", "Sequences of transformations")
def transformation_sequences(rng: random.Random) -> Spec:
    parent = pick_parent(rng, "square", "cube", "abs", "sqrt")
    variant = rng.choice(["describe", "find-a", "find-a", "reflect", "key-point"])
    key = PARENTS[parent][0]

    if variant == "reflect":
        parent = pick_parent(rng, "sqrt", "abs", "cube")
        c, k = rng.randint(1, 6), nonzero(rng, -6, 6)
        g = outer(-1, body(parent, f"{c} - x"), k)
        answer = f"Reflect over the y-axis, shift right {c}; reflect over the x-axis, shift {'up' if k > 0 else 'down'} {abs(k)}"
        wrong = [
            answer.replace(f"right {c}", f"left {c}"),
            answer.replace("up" if k > 0 else "down", "down" if k > 0 else "up"),
            f"Shift right {c}; reflect over the x-axis, shift {'up' if k > 0 else 'down'} {abs(k)}",
            answer.replace("Reflect over the y-axis", "Reflect over the x-axis").replace("; reflect over the x-axis", "; reflect over the y-axis"),
        ]
        return Spec(
            prompt=f"Starting from $f(x) = {body(parent)}$, which describes $g(x) = {g}$?",
            answer=answer,
            kind="choice",
            distractors=wrong,
            explanation=(
                f"Rewrite the inside: ${c} - x = -(x - {c})$. The $-x$ reflects over the $y$-axis, then the graph shifts right {c}. "
                f"The minus sign outside reflects over the $x$-axis, then ${'+' if k > 0 else '-'} {abs(k)}$ shifts it {'up' if k > 0 else 'down'} {abs(k)}. "
                f"Reflections come before shifts in the same direction."
            ),
        )

    a = rng.choice([2, 3, 4, sp.Rational(1, 2), sp.Rational(1, 3), -1, -2, sp.Rational(-1, 2)])
    h, k = nonzero(rng, -5, 5), nonzero(rng, -6, 6)
    g = outer(a, body(parent, inner(h)), k)

    if variant == "describe":
        a = abs(a) if a != -1 else 2
        g = outer(a, body(parent, inner(h)), k)
        right = _sequence_words(a, h, k)
        wrong = [_sequence_words(a, -h, k), _sequence_words(a, h, -k), _sequence_words(1 / sp.nsimplify(a), h, k)]
        stretch = f"{'stretch' if a > 1 else 'compress'} vertically by a factor of ${nice_number(a)}$"
        wrong.append(f"Shift {'right' if h > 0 else 'left'} {abs(h)}, shift {'up' if k > 0 else 'down'} {abs(k)}, then {stretch}")
        return Spec(
            prompt=f"Starting from $f(x) = {body(parent)}$, which sequence of transformations gives $g(x) = {g}$?",
            answer=right,
            kind="choice",
            distractors=[w for w in wrong if w != right],
            explanation=(
                f"Inside: $({inner(h)})$ shifts {'right' if h > 0 else 'left'} {abs(h)}. Outside, in order of operations: "
                f"multiply by ${nice_number(a)}$ first (the {'stretch' if a > 1 else 'compression'}), then add ${k}$ (the shift). "
                f"Shifting before stretching would stretch the shift too."
            ),
        )
    if variant == "key-point":
        return Spec(
            prompt=f"The {key} of $f(x) = {body(parent)}$ is $(0, 0)$. Where is the {key} of $g(x) = {g}$?",
            answer=show_pair((h, k)),
            kind="numbers",
            expected=(sp.Integer(h), sp.Integer(k)),
            ordered=True,
            distractors=[(-h, k), (h, a * k), (h, -k), (k, h)],
            input_hint=PAIR_HINT,
            explanation=f"The stretch doesn't move $(0, 0)$ (since ${nice_number(a)} \\cdot 0 = 0$). The shifts move it {', '.join(shift_words(h, k))}: $({h}, {k})$.",
        )

    parent = pick_parent(rng, "square", "cube", "abs")
    key = PARENTS[parent][0]
    d = rng.choice([1, 2, 3, -1, -2])
    px = h + d
    py = k + a * parent_value(parent, d)
    shape = {"square": "parabola", "cube": "cubic", "abs": "V-shaped graph"}[parent]
    general = outer(1, "a" + body(parent, inner(h)), k)
    return Spec(
        prompt=(
            f"The graph of $f(x) = {body(parent)}$ is transformed into a {shape} with {key} $({h}, {k})$ that passes through "
            f"$({px}, {nice_number(py)})$. In $g(x) = {general}$, what is $a$?"
        ),
        answer=num(a),
        kind="numbers",
        expected=[sp.nsimplify(a)],
        distractors=num_options(a, [1 / sp.nsimplify(a), py - k, -a, py]),
        input_hint="A number, e.g. 2 or -1/2",
        explanation=(
            f"Substitute the point: ${nice_number(py)} = a \\cdot {body(parent, f'{px} - ({h})' if h < 0 else f'{px} - {h}')} {'+' if k > 0 else '-'} {abs(k)}$, "
            f"so ${nice_number(py - k)} = {parent_value(parent, d)}a$ and $a = {nice_number(a)}$."
        ),
    )


# ---------------------------------------------------------------- 8. corresponding points


@generator("corresponding-points", "Corresponding points")
def corresponding_points(rng: random.Random) -> Spec:
    parent = pick_parent(rng)
    p, q = rng.choice(PARENTS[parent][1])
    a = rng.choice([1, 2, 3, -1, -2, sp.Rational(1, 2)])
    if a == sp.Rational(1, 2) and q % 2:
        a = 2
    flip = rng.random() < 0.25
    h = 0 if flip else nonzero(rng, -6, 6)
    k = rng.choice([0, nonzero(rng, -8, 8), nonzero(rng, -8, 8)])
    inside = "-x" if flip else inner(h)
    g = outer(a, body(parent, inside), k)
    nx = -p if flip else p + h
    ny = a * q + k
    steps = []
    if flip:
        steps.append(f"reflect across the $y$-axis: $({-p}, {q})$")
    else:
        steps.append(f"shift {'right' if h > 0 else 'left'} {abs(h)}: $({p + h}, {q})$")
    if a != 1:
        word = "reflect across the $x$-axis" if a == -1 else f"multiply $y$ by ${nice_number(a)}$"
        steps.append(f"{word}: $({nx}, {nice_number(a * q)})$")
    if k:
        steps.append(f"shift {'up' if k > 0 else 'down'} {abs(k)}: $({nx}, {nice_number(ny)})$")
    wrong = [(p - h if not flip else p, ny), (nx, a * (q + k)), (nx, q + k), (nx, -ny) if ny else (nx, a * q - k)]
    return Spec(
        prompt=f"$({p}, {q})$ is a point on $y = {body(parent)}$. Find the corresponding point on $y = {g}$.",
        answer=show_pair((nx, ny)),
        kind="numbers",
        expected=(sp.Integer(nx), sp.nsimplify(ny)),
        ordered=True,
        distractors=[w for w in wrong if tuple(w) != (nx, ny)],
        input_hint=PAIR_HINT,
        explanation="Follow the point in order - horizontal changes affect only $x$, vertical changes only $y$, and stretches come before shifts: " + "; then ".join(steps) + ".",
    )


# ---------------------------------------------------------------- 9. domain and range


def _pad(wrong: list[str], answer: str, kind: str, e) -> list[str]:
    """Distinct wrong intervals, topped up with near misses if mistakes collapsed together."""
    out = [w for w in dict.fromkeys(wrong) if w != answer]
    for delta in (1, -1, 2, -2, 3):
        if len(out) >= 3:
            break
        extra = interval_tex(kind, e + delta)
        if extra not in out and extra != answer:
            out.append(extra)
    return out


def interval_tex(kind: str, e) -> str:
    e = nice_number(e)
    return {"up": f"$[{e}, \\infty)$", "down": f"$(-\\infty, {e}]$", "hole": f"$(-\\infty, {e}) \\cup ({e}, \\infty)$"}[kind]


@generator("transformed-domain-range", "Domain and range of transformed functions")
def transformed_domain_range(rng: random.Random) -> Spec:
    if rng.random() < 0.5:
        kind = rng.choice(["up", "down", "hole"])
        d = rng.randint(-6, 6)
        flip = kind != "hole" and rng.random() < 0.3
        h = 0 if flip else nonzero(rng, -8, 8)
        a, k = rng.choice([1, 1, 2, 3, -1, 5]), rng.choice([0, nonzero(rng, -9, 9)])
        inside = "-x" if flip else inner(h)
        g = outer(a, f"f({inside})", k)
        if flip:
            new_kind, new_d = ("down" if kind == "up" else "up"), -d
            why = f"$f(-x)$ reflects the graph about the $y$-axis, so the domain flips: every $x$ becomes $-x$."
        else:
            new_kind, new_d = kind, d + h
            why = f"$f({inside})$ shifts the graph {'right' if h > 0 else 'left'} {abs(h)}, so the domain shifts too: ${d} {'+' if h > 0 else '-'} {abs(h)} = {d + h}$."
        wrong = [interval_tex(new_kind, d - h if not flip else d), interval_tex(kind, d), interval_tex(new_kind, new_d + k) if k else interval_tex(new_kind, -new_d),
                 interval_tex("down" if new_kind == "up" else "up" if new_kind == "down" else "hole", new_d), interval_tex(new_kind, new_d + 1)]
        answer = interval_tex(new_kind, new_d)
        return Spec(
            prompt=f"The domain of $y = f(x)$ is {interval_tex(kind, d)}. What is the domain of $y = {g}$?",
            answer=answer,
            kind="choice",
            distractors=_pad(wrong, answer, new_kind, new_d),
            explanation=why + " The outside numbers change $y$, not $x$, so they don't affect the domain.",
        )

    kind = rng.choice(["up", "down"])
    r = rng.randint(-5, 6)
    a = rng.choice([1, 2, 3, 4, -1, -1, -2])
    k = nonzero(rng, -9, 9) if rng.random() < 0.85 else 0
    h = rng.choice([0, 0, nonzero(rng, -5, 5)])
    g = outer(a, f"f({inner(h)})", k)
    new_r = a * r + k
    new_kind = kind if a > 0 else ("down" if kind == "up" else "up")
    steps = []
    if a != 1:
        steps.append(f"multiply the endpoint by ${a}$: ${a}({r}) = {a * r}$" + (" and flip the direction (a negative factor reflects over the $x$-axis)" if a < 0 else ""))
    if k:
        steps.append(f"then add ${k}$: ${a * r} {'+' if k > 0 else '-'} {abs(k)} = {new_r}$")
    wrong = [interval_tex(new_kind, r + k), interval_tex(new_kind, a * (r + k)), interval_tex(kind if a < 0 else ("down" if kind == "up" else "up"), new_r), interval_tex(new_kind, new_r + h) if h else interval_tex(new_kind, a * r - k)]
    answer = interval_tex(new_kind, new_r)
    return Spec(
        prompt=f"The range of $y = f(x)$ is {interval_tex(kind, r)}. What is the range of $y = {g}$?",
        answer=answer,
        kind="choice",
        distractors=_pad(wrong, answer, new_kind, new_r),
        explanation=(
            "The range depends only on the outside (vertical) changes"
            + (f" - the $({inner(h)})$ inside doesn't matter" if h else "")
            + ". Apply them to the endpoint in order: "
            + ("; ".join(steps) if steps else "nothing changes")
            + f". The range is {answer}."
        ),
    )
