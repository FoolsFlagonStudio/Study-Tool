"""Section 4, Module 11 - Preparing for Trigonometry."""

from __future__ import annotations

import math
import random

import sympy as sp

from ..core.problem import Spec, generator
from .exponentials import dec, dec_options, rounded
from .quadratics import num, num_options

QUADRANTS = ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV", "Quadrantal (on an axis)"]
ANGLE_TYPES = ["Acute", "Right", "Obtuse", "Straight", "None of these"]
NICE_DEGREES = [d for d in range(15, 361, 15)] + [36, 72, 108, 144, 20, 40, 80, 100, 140, 160, 10, 50, 70, 110, 130, 170]


def rad(deg) -> sp.Expr:
    return sp.Rational(deg, 180) * sp.pi


def rad_tex(deg) -> str:
    """Exact radian measure as LaTeX: 5pi/6 -> \\frac{5\\pi}{6}."""
    q = sp.Rational(deg, 180)
    if q == 0:
        return "0"
    sign = "-" if q < 0 else ""
    p, d = abs(q.p), q.q
    top = "\\pi" if p == 1 else f"{p}\\pi"
    return f"{sign}{top}" if d == 1 else f"{sign}\\frac{{{top}}}{{{d}}}"


def deg_tex(deg) -> str:
    return f"{sp.nsimplify(deg)}°" if sp.nsimplify(deg).is_Integer else f"{float(deg):.2f}°"


def show(deg, radians: bool) -> str:
    return rad_tex(deg) if radians else deg_tex(deg)


def reduce(deg) -> int:
    return deg % 360


def quadrant_of(deg) -> str:
    d = reduce(deg)
    if d % 90 == 0:
        return QUADRANTS[4]
    return QUADRANTS[int(d // 90)]


# ---------------------------------------------------------------- 1. quadrants


@generator("angle-quadrants", "Angles in standard position")
def angle_quadrants(rng: random.Random) -> Spec:
    radians = rng.random() < 0.4
    base = rng.choice([d for d in NICE_DEGREES if d < 360] + [90, 180, 270])
    turns = rng.choice([0, 0, 0, 1, -1, 2])
    deg = base + 360 * turns
    if rng.random() < 0.35:
        deg = -deg if deg else -90
    answer = quadrant_of(deg)
    d = reduce(deg)
    why = ("Negative angles rotate **clockwise** from the positive $x$-axis. " if deg < 0 else "") + (
        f"${show(deg, radians)}$ is coterminal with ${show(d, radians)}$" + (", which" if answer != QUADRANTS[4] else "") if d != deg else f"${show(deg, radians)}$"
    )
    why += (
        f". Its terminal side lies on an axis, so it's quadrantal - not in any quadrant."
        if answer == QUADRANTS[4]
        else f" is between ${show(90 * (int(d // 90)), radians)}$ and ${show(90 * (int(d // 90) + 1), radians)}$, so it's in {answer}."
    )
    return Spec(
        prompt=f"An angle of ${show(deg, radians)}$ is in standard position. Where is its terminal side?",
        answer=answer,
        kind="choice",
        choices=QUADRANTS,
        explanation=why,
    )


# ---------------------------------------------------------------- 2. conversion


@generator("degree-radian-conversion", "Converting degrees and radians")
def degree_radian_conversion(rng: random.Random) -> Spec:
    deg = rng.choice(NICE_DEGREES + [-30, -45, -60, -120, -135, -210, -35, 400, 420, 540, 14])
    to_radians = rng.random() < 0.5
    q = sp.Rational(deg, 180)

    if rng.random() < 0.15:
        r = rng.choice([0.5, 1, 1.2, 2, 2.5, 3, 4, 5])
        val = r * 180 / math.pi
        return Spec(
            prompt=f"Convert ${r:g}$ radians to degrees. Round to two decimal places.",
            answer=f"${dec(val)}°$",
            kind="numbers",
            expected=[rounded(val, 2)],
            distractors=[o[:-1] + "°$" for o in dec_options(val, [r * math.pi / 180, r * 180, r * 360 / math.pi, val / 2])],
            tolerance=0.006,
            input_hint="Degrees, e.g. 143.24",
            explanation=f"Multiply by $\\frac{{180°}}{{\\pi}}$: ${r:g} \\cdot \\frac{{180°}}{{\\pi}} \\approx {dec(val)}°$. There's no $\\pi$ to cancel, so use a calculator.",
        )
    if to_radians:
        g = math.gcd(abs(deg), 180)
        return Spec(
            prompt=f"Convert ${deg}°$ to radians. Give the exact answer.",
            answer=f"${rad_tex(deg)}$",
            kind="numbers",
            expected=[rad(deg)],
            distractors=[f"${w}$" for w in dict.fromkeys([rad_tex(-deg), rad_tex(deg * 2), rad_tex(180 - deg) if deg != 90 else rad_tex(45), f"\\frac{{180}}{{{deg}\\pi}}" if deg > 0 else rad_tex(deg + 180), rad_tex(deg + 180)]) if w != rad_tex(deg)],
            input_hint="e.g. 5pi/6",
            explanation=f"Multiply by $\\frac{{\\pi}}{{180°}}$: $\\frac{{{deg}\\pi}}{{180}}$. Simplify by dividing top and bottom by ${g}$: ${rad_tex(deg)}$.",
        )
    return Spec(
        prompt=f"Convert ${rad_tex(deg)}$ radians to degrees.",
        answer=f"${deg}°$",
        kind="numbers",
        expected=[sp.Integer(deg)],
        distractors=[f"${w}°$" for w in dict.fromkeys([-deg, deg * 2, 180 - deg, deg + 180, int(q * 360) if q * 360 != deg else deg + 90]) if w != deg],
        input_hint="Degrees, e.g. 120",
        explanation=f"Multiply by $\\frac{{180°}}{{\\pi}}$: the $\\pi$ cancels, leaving ${sp.latex(q)} \\cdot 180° = {deg}°$.",
    )


# ---------------------------------------------------------------- 3. angle types


@generator("angle-types", "Types of angles")
def angle_types(rng: random.Random) -> Spec:
    radians = rng.random() < 0.45
    deg = rng.choice([90, 180, 270, 360, -45, -120, 200, 300] + [d for d in NICE_DEGREES if d < 180] * 2)
    if deg < 0 or deg > 180 or deg == 0:
        answer = "None of these"
    elif deg < 90:
        answer = "Acute"
    elif deg == 90:
        answer = "Right"
    elif deg < 180:
        answer = "Obtuse"
    else:
        answer = "Straight"
    if answer == "None of these" and deg in (270, 360):
        why_extra = " (It's quadrantal - its terminal side is on an axis - but it isn't acute, right, obtuse, or straight.)"
    else:
        why_extra = ""
    conv = f"${rad_tex(deg)} \\cdot \\frac{{180°}}{{\\pi}} = {deg}°$. " if radians else ""
    rule = {
        "Acute": "Between $0°$ and $90°$: acute.",
        "Right": "Exactly $90°$: a right angle.",
        "Obtuse": "Between $90°$ and $180°$: obtuse.",
        "Straight": "Exactly $180°$: a straight angle.",
        "None of these": "Acute and obtuse only cover positive angles less than $180°$, and right and straight are exactly $90°$ and $180°$.",
    }[answer]
    return Spec(
        prompt=f"Classify an angle measuring ${show(deg, radians)}$.",
        answer=answer,
        kind="choice",
        choices=ANGLE_TYPES,
        explanation=conv + rule + why_extra,
    )


# ---------------------------------------------------------------- 4. coterminal


@generator("coterminal-angles", "Coterminal angles")
def coterminal_angles(rng: random.Random) -> Spec:
    radians = rng.random() < 0.4
    variant = rng.choice(["reduce", "reduce", "positive-negative", "check"])
    if variant == "check":
        base = rng.choice([d for d in NICE_DEGREES if d < 360])
        k = rng.choice([1, 2, -1, -2])
        same = rng.random() < 0.5
        other = base + 360 * k if same else base + 360 * k + rng.choice([180, 90, -90, 10, 20])
        diff = other - base
        return Spec(
            prompt=f"Are ${show(base, radians)}$ and ${show(other, radians)}$ coterminal?",
            answer="Yes" if same else "No",
            kind="choice",
            choices=["Yes", "No"],
            explanation=f"Subtract: ${show(other, radians)} - {'(' + show(base, radians) + ')' if base < 0 else show(base, radians)} = {show(diff, radians)}$. "
            + (f"That's {abs(k)} full turn{'s' if abs(k) > 1 else ''}, so yes." if same else f"That isn't a whole number of turns ({show(360, radians)} each), so no."),
        )
    if variant == "positive-negative":
        base = rng.choice([d for d in NICE_DEGREES if d < 360] + [-30, -150, -230, -100])
        want_negative = base > 0 if rng.random() < 0.7 else rng.random() < 0.5
        answer_deg = base - 360 if want_negative else base + 360
        if not want_negative and base > 0 and rng.random() < 0.3:
            answer_deg = base + 360
        wrong = [base + 180, base - 180, -base, base + (360 if want_negative else -360) if (base + (360 if want_negative else -360)) * (1 if not want_negative else -1) < 0 else base * 2]
        return Spec(
            prompt=f"Find a {'negative' if want_negative else 'positive'} angle coterminal with ${show(base, radians)}$ by {'subtracting' if want_negative else 'adding'} one full rotation.",
            answer=f"${show(answer_deg, radians)}$",
            kind="numbers",
            expected=[rad(answer_deg) if radians else sp.Integer(answer_deg)],
            distractors=[f"${show(w, radians)}$" for w in dict.fromkeys(wrong) if w != answer_deg],
            input_hint="e.g. -330 or -11pi/6",
            explanation=f"${show(base, radians)} {'-' if want_negative else '+'} {show(360, radians)} = {show(answer_deg, radians)}$.",
        )
    base = rng.choice([d for d in NICE_DEGREES if d < 360])
    k = rng.choice([-3, -2, -1, 1, 2, 3])
    deg = base + 360 * k
    turns = -k
    return Spec(
        prompt=f"Find the angle between ${show(0, radians)}$ and ${show(360, radians)}$ that is coterminal with ${show(deg, radians)}$.",
        answer=f"${show(base, radians)}$",
        kind="numbers",
        expected=[rad(base) if radians else sp.Integer(base)],
        distractors=[f"${show(w, radians)}$" for w in dict.fromkeys([(base + 180) % 360, (360 - base) % 360, abs(deg) % 360 if deg < 0 else (deg - 180) % 360, (base + 90) % 360]) if w != base],
        input_hint="e.g. 280 or 5pi/6",
        explanation=f"{'Add' if turns > 0 else 'Subtract'} {abs(turns)} full rotation{'s' if abs(turns) > 1 else ''} (${show(360 * abs(turns), radians)}$): ${show(deg, radians)} {'+' if turns > 0 else '-'} {show(360 * abs(turns), radians)} = {show(base, radians)}$.",
    )


# ---------------------------------------------------------------- 5. complements and supplements


@generator("complements-supplements", "Complementary and supplementary angles")
def complements_supplements(rng: random.Random) -> Spec:
    radians = rng.random() < 0.3
    kind = rng.choice(["complement", "supplement"])
    total = 90 if kind == "complement" else 180
    pool = [d for d in NICE_DEGREES if d < total] if radians else list(range(1, total))
    if rng.random() < 0.15:
        x = rng.randint(total, total + 60) if not radians else rng.choice([d for d in NICE_DEGREES if total <= d < 270])
        return Spec(
            prompt=f"Does an angle of ${show(x, radians)}$ have a {kind}?",
            answer="No",
            kind="choice",
            choices=["Yes", "No"],
            explanation=f"${show(total, radians)} - {show(x, radians)}$ is {'zero' if x == total else 'negative'}. A {kind} must be a positive angle, so there isn't one.",
        )
    x = rng.choice(pool)
    ans = total - x
    other = (180 if total == 90 else 90) - x
    return Spec(
        prompt=f"Find the {kind} of an angle measuring ${show(x, radians)}$.",
        answer=f"${show(ans, radians)}$",
        kind="numbers",
        expected=[rad(ans) if radians else sp.Integer(ans)],
        distractors=[f"${show(w, radians)}$" for w in dict.fromkeys([other, 360 - x, ans + 10 if not radians else ans + 15, x]) if w != ans and w > 0],
        input_hint="e.g. 67 or pi/3",
        explanation=f"{'Complementary angles add to' if total == 90 else 'Supplementary angles add to'} ${show(total, radians)}$: ${show(total, radians)} - {show(x, radians)} = {show(ans, radians)}$.",
    )


# ---------------------------------------------------------------- 6. arc length


def _angle_given(rng: random.Random):
    """A central angle, either in radians (exact or decimal) or degrees. Returns (text, radians value, conversion note)."""
    style = rng.choice(["exact", "exact", "degrees", "decimal"])
    if style == "decimal":
        t = rng.choice([0.5, 0.8, 1.2, 1.5, 2, 2.4, 3])
        return f"\\theta = {t:g}", t, ""
    deg = rng.choice([30, 45, 60, 72, 90, 120, 135, 150, 210, 240, 270, 300])
    val = float(rad(deg))
    if style == "degrees":
        return f"\\theta = {deg}°", val, f"Convert first: ${deg}° = {rad_tex(deg)}$. "
    return f"\\theta = {rad_tex(deg)}", val, ""


@generator("arc-length", "Arc length")
def arc_length(rng: random.Random) -> Spec:
    variant = rng.choice(["s", "s", "theta", "r"])
    r = rng.choice([2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 20, 25])
    unit = rng.choice(["cm", "in", "ft", "m"])
    if variant == "theta":
        s = round(rng.uniform(0.3, 6.0) * r, 1)
        theta = s / r
        return Spec(
            prompt=f"An arc of length {s:g} {unit} is cut off by a central angle in a circle of radius {r} {unit}. Find the angle in radians, to two decimal places.",
            answer=f"${dec(theta)}$",
            kind="numbers",
            expected=[rounded(theta, 2)],
            distractors=dec_options(theta, [r / s, s * r, theta * 180 / math.pi, s / (2 * r)]),
            tolerance=0.006,
            input_hint="Radians, e.g. 2.25",
            explanation=f"$s = r\\theta$, so $\\theta = \\frac{{s}}{{r}} = \\frac{{{s:g}}}{{{r}}} \\approx {dec(theta)}$.",
        )
    text, theta, note = _angle_given(rng)
    if variant == "r":
        s = round(r * theta, 2)
        return Spec(
            prompt=f"A central angle ${text}$ cuts off an arc of length {s:g} {unit}. Find the radius to two decimal places.",
            answer=f"${dec(s / theta)}$ {unit}",
            kind="numbers",
            expected=[rounded(s / theta, 2)],
            distractors=[o + f" {unit}" for o in dec_options(s / theta, [s * theta, theta / s, s / (theta * 180 / math.pi), s / (2 * theta)])],
            tolerance=0.006,
            input_hint="e.g. 2.7",
            explanation=note + f"$s = r\\theta$, so $r = \\frac{{s}}{{\\theta}} = \\frac{{{s:g}}}{{{theta:.4g}}} \\approx {dec(s / theta)}$ {unit}.",
        )
    s = r * theta
    deg_value = theta * 180 / math.pi
    return Spec(
        prompt=f"Find the arc length cut off by a central angle ${text}$ in a circle of radius {r} {unit}. Round to two decimal places.",
        answer=f"${dec(s)}$ {unit}",
        kind="numbers",
        expected=[rounded(s, 2)],
        distractors=[o + f" {unit}" for o in dec_options(s, [r * deg_value, r * r * theta / 2, theta / r, 2 * r * theta])],
        tolerance=0.006,
        input_hint="e.g. 8.38",
        explanation=note + f"$s = r\\theta = {r} \\cdot {text.split('= ')[1]} \\approx {dec(s)}$ {unit}." + (" Using the degree number directly would be way off - $s = r\\theta$ needs radians." if note else ""),
    )


# ---------------------------------------------------------------- 7. sector area


@generator("sector-area", "Area of a sector")
def sector_area(rng: random.Random) -> Spec:
    r = rng.choice([2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 5.5, 2.5])
    unit = rng.choice(["cm", "in", "ft", "m"])
    text, theta, note = _angle_given(rng)
    area = 0.5 * r * r * theta
    if rng.random() < 0.3:
        area_r = round(area, 2)
        r_back = math.sqrt(2 * area_r / theta)
        return Spec(
            prompt=f"A sector with central angle ${text}$ has area {area_r:g} {unit}². Find the radius to two decimal places.",
            answer=f"${dec(r_back)}$ {unit}",
            kind="numbers",
            expected=[rounded(r_back, 2)],
            distractors=[o + f" {unit}" for o in dec_options(r_back, [2 * area_r / theta, math.sqrt(area_r / theta), area_r / theta, math.sqrt(2 * area_r * theta)])],
            tolerance=0.006,
            input_hint="e.g. 1.6",
            explanation=note + f"$A = \\frac{{1}}{{2}}r^2\\theta$, so $r^2 = \\frac{{2A}}{{\\theta}} = \\frac{{2({area_r:g})}}{{{theta:.4g}}} \\approx {dec(r_back ** 2)}$ and $r \\approx {dec(r_back)}$ {unit}.",
        )
    return Spec(
        prompt=f"Find the area of a sector with radius {r:g} {unit} and central angle ${text}$. Round to two decimal places.",
        answer=f"${dec(area)}$ {unit}²",
        kind="numbers",
        expected=[rounded(area, 2)],
        distractors=[o + f" {unit}²" for o in dec_options(area, [r * r * theta, 0.5 * r * theta, r * theta, 0.5 * r * r * theta * 180 / math.pi])],
        tolerance=0.006,
        input_hint="e.g. 10.94",
        explanation=note + f"$A = \\frac{{1}}{{2}}r^2\\theta = \\frac{{1}}{{2}}({r:g})^2 \\cdot {text.split('= ')[1]} \\approx {dec(area)}$ {unit}². Square only the radius.",
    )


# ---------------------------------------------------------------- 8. applications


@generator("sector-applications", "Arc and sector applications")
def sector_applications(rng: random.Random) -> Spec:
    story = rng.choice(["clock", "sprinkler", "orbit", "perimeter", "wheel", "detector"])
    if story == "clock":
        r = rng.choice([4, 5, 6, 8, 10, 12, 13.8, 14])
        minutes = rng.choice([5, 10, 15, 20, 25, 30, 40, 45, 50])
        theta = minutes / 60 * 2 * math.pi
        ask_area = rng.random() < 0.4
        val = 0.5 * r * r * theta if ask_area else r * theta
        prompt = f"A clock's minute hand is {r:g} {'ft' if r > 10 else 'in'} long. " + (f"What area does it sweep in {minutes} minutes?" if ask_area else f"How far does its tip travel in {minutes} minutes?")
        why = f"{minutes} minutes is $\\frac{{{minutes}}}{{60}}$ of a full turn: $\\theta = \\frac{{{minutes}}}{{60}} \\cdot 2\\pi \\approx {theta:.4f}$. " + (f"$A = \\frac{{1}}{{2}}r^2\\theta \\approx {dec(val)}$." if ask_area else f"$s = r\\theta \\approx {dec(val)}$.")
        wrong = [r * minutes, val * 2, r * theta / 2 if not ask_area else r * r * theta, val * 60 / minutes]
    elif story in ("sprinkler", "detector"):
        r, deg = rng.choice([15, 20, 25, 30, 40, 50]), rng.choice([30, 45, 60, 75, 90, 120, 135, 150])
        theta = float(rad(deg))
        val = 0.5 * r * r * theta
        thing = "sprinkler sprays" if story == "sprinkler" else "motion detector reaches"
        unit = "ft" if story == "sprinkler" else "m"
        prompt = f"A {thing} {r} {unit} and covers an angle of ${deg}°$. What area does it cover?"
        why = f"Convert: ${deg}° = {rad_tex(deg)}$. $A = \\frac{{1}}{{2}}({r})^2 \\cdot {rad_tex(deg)} \\approx {dec(val)}$ {unit}²."
        wrong = [0.5 * r * r * deg, r * r * theta, r * theta, 0.5 * r * theta]
    elif story == "orbit":
        height, deg = rng.choice([300, 400, 500, 600, 800]), rng.choice([30, 45, 60, 90])
        r = 6_400 + height
        theta = float(rad(deg))
        val = r * theta
        prompt = f"A satellite orbits {height} km above Earth's surface. Earth's radius is 6,400 km. A ground station tracks it through a ${deg}°$ central angle. How far does it travel while tracked?"
        why = f"The orbit's radius is $6{{,}}400 + {height} = {r:,}$ km".replace(",", "{,}") + f". $s = r\\theta = {r:,}".replace(",", "{,}") + f" \\cdot {rad_tex(deg)} \\approx {dec(val)}$ km."
        wrong = [6_400 * theta, height * theta, r * deg, 0.5 * r * r * theta]
    elif story == "perimeter":
        r, deg = rng.choice([5, 6, 7, 8, 9, 10, 12]), rng.choice([45, 60, 90, 120, 150])
        theta = float(rad(deg))
        val = r * theta + 2 * r
        prompt = f"A garden is shaped like a sector with a ${deg}°$ central angle and straight sides {r} ft long. How much edging goes all the way around it?"
        why = f"Perimeter = arc + both radii. Arc: ${r} \\cdot {rad_tex(deg)} \\approx {r * theta:.2f}$. Total: ${r * theta:.2f} + {2 * r} \\approx {dec(val)}$ ft."
        wrong = [r * theta, r * theta + r, 0.5 * r * r * theta, r * deg + 2 * r]
    else:
        diameter = rng.choice([20, 24, 26, 30, 400])
        stops, k = rng.choice([(8, 3), (12, 5), (32, 6), (16, 4), (10, 3)])
        r = diameter / 2
        theta = k * 2 * math.pi / stops
        val = r * theta
        prompt = f"A wheel {diameter} {'ft' if diameter > 100 else 'in'} across has {stops} evenly spaced stops. How far does a point on the rim travel moving {k} stops?"
        why = f"Radius $= {diameter} \\div 2 = {r:g}$. Each stop is $\\frac{{2\\pi}}{{{stops}}}$, so {k} stops is $\\theta = \\frac{{{2 * k}\\pi}}{{{stops}}}$. $s = r\\theta \\approx {dec(val)}$."
        wrong = [diameter * theta, r * k, r * theta / 2, 0.5 * r * r * theta]
    return Spec(
        prompt=prompt + " Round to two decimal places.",
        answer=f"${dec(val)}$",
        kind="numbers",
        expected=[rounded(val, 2)],
        distractors=dec_options(val, wrong),
        tolerance=0.006,
        input_hint="A number, e.g. 245.44",
        explanation=why,
    )
