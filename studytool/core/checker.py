"""Reading typed answers and deciding whether they're right.

Typed answers are parsed with SymPy, so ``2(x+3)``, ``2x+6`` and ``6 + 2*x``
are all recognised as the same answer. Some topics also care about the
*form* of the answer (an unsimplified expression is equivalent but not what
the question asked for), which is what ``FORMS`` handles.
"""

from __future__ import annotations

import random
import re
from dataclasses import dataclass

import sympy as sp
from sympy.parsing.sympy_parser import (
    convert_xor,
    implicit_multiplication_application,
    parse_expr,
    standard_transformations,
)

from .problem import Problem, Spec
from .symbols import SYMS

TRANSFORMS = standard_transformations + (implicit_multiplication_application, convert_xor)
FUNCTION_WORDS = {"sqrt", "cbrt", "root", "pi"}
MAX_INPUT = 200


class InputError(ValueError):
    """The response couldn't be read as math."""


@dataclass
class Result:
    correct: bool
    valid: bool = True  # False means "couldn't read it", so it shouldn't count as an attempt
    feedback: str = ""


# ---------------------------------------------------------------- parsing


def _local_dict(evaluate: bool) -> dict:
    def pow_fn(expo):
        return lambda arg, *_, **__: sp.Pow(arg, expo, evaluate=evaluate)

    def root_fn(arg, index, *_, **__):
        return sp.Pow(arg, sp.Integer(1) / sp.sympify(index), evaluate=evaluate)

    return {
        **SYMS,
        "pi": sp.pi,
        "sqrt": pow_fn(sp.S.Half),
        "cbrt": pow_fn(sp.Rational(1, 3)),
        "root": root_fn,
    }


def normalize(text: str) -> str:
    text = text.strip()
    replacements = {
        "−": "-", "–": "-", "×": "*", "·": "*", "÷": "/", "π": "pi",
        "√": "sqrt", "∛": "cbrt", "²": "^2", "³": "^3", "**": "^",
    }
    text = re.sub(r"√\s*(\d+(\.\d+)?|[a-z])", r"sqrt(\1)", text)  # √57 means sqrt(57), not sqrt·57
    for old, new in replacements.items():
        text = text.replace(old, new)
    # Drop a leading "y =" / "f(x) =" if the student wrote one.
    if text.count("=") == 1:
        left, right = text.split("=")
        if re.fullmatch(r"\s*[a-zA-Z](\([a-z]\))?\s*", left):
            text = right
    return text.strip()


def _validate(text: str) -> None:
    if not text:
        raise InputError("Type an answer first.")
    if len(text) > MAX_INPUT:
        raise InputError("That answer is too long.")
    if not re.fullmatch(r"[A-Za-z0-9\s+\-*/^().,]*", text):
        raise InputError("Use numbers, letters, + - * / ^ and parentheses.")
    for word in re.findall(r"[A-Za-z]+", text):
        if word in FUNCTION_WORDS:
            continue
        stripped = word
        for fn in sorted(FUNCTION_WORDS, key=len, reverse=True):
            stripped = stripped.replace(fn, "")
        if not all(ch in SYMS for ch in stripped):
            raise InputError(f"I don't recognise “{word}”.")
    if re.search(r"[A-Za-z)]\s*\.|\.\s*[A-Za-z(]", text):
        raise InputError("Decimal points can only go between digits.")
    if re.search(r"\d{10,}", text):
        raise InputError("That number is too large.")
    if re.search(r"\^\s*(\d+|\([^()]*\))\s*\^", text):
        raise InputError("Use parentheses for stacked exponents, like (x^2)^3.")


def parse_expression(text: str, evaluate: bool = True) -> sp.Expr:
    text = normalize(text)
    _validate(text)
    if _has_top_level_comma(text):
        raise InputError("Enter a single expression.")
    try:
        expr = parse_expr(text, local_dict=_local_dict(evaluate), transformations=TRANSFORMS, evaluate=evaluate)
    except Exception as exc:  # SymPy raises many exception types for bad input
        raise InputError("I couldn't read that. Check your parentheses and operators.") from exc
    if not isinstance(expr, sp.Expr):
        raise InputError("Enter a math expression.")
    if evaluate:
        expr = sp.nsimplify(expr, rational=True) if expr.has(sp.Float) else expr
    return expr


def _has_top_level_comma(text: str) -> bool:
    depth = 0
    for ch in text:
        depth += {"(": 1, ")": -1}.get(ch, 0)
        if ch == "," and depth == 0:
            return True
    return False


def _split_top_level(text: str) -> list[str]:
    parts, depth, current = [], 0, ""
    for ch in text:
        depth += {"(": 1, ")": -1}.get(ch, 0)
        if ch == "," and depth == 0:
            parts.append(current)
            current = ""
        else:
            current += ch
    return [*parts, current]


def parse_numbers(text: str) -> list[sp.Expr]:
    """Parse one or more numbers: ``27``, ``-27, 27``, ``±27``, ``{1, 2, 3}``, ``x = 8 or x = -8``."""
    text = normalize(text.replace("+/-", "±").replace("+-", "±")) if "=" not in text else text
    text = re.sub(r"\b[a-z]\s*=", "", text)
    text = text.replace("{", "").replace("}", "").strip()
    if text.startswith("(") and text.endswith(")") and _has_top_level_comma(text[1:-1]):
        text = text[1:-1]  # an ordered pair like (2, -3)
    text = re.sub(r"\b(or|and)\b", ",", text)
    values: list[sp.Expr] = []
    for chunk in (c.strip() for c in _split_top_level(text)):
        if not chunk:
            continue
        chunk = chunk.replace("+-", "±")
        # "±27" or "(3 ± sqrt(57))/8": one value with +, one with -
        options = [chunk.replace("±", sign, 1) for sign in "+-"] if "±" in chunk else [chunk]
        for option in options:
            expr = parse_expression(option.lstrip("+"))
            if expr.free_symbols:
                raise InputError("Enter numbers only.")
            values.append(expr)
    if not values:
        raise InputError("Type an answer first.")
    return values


# ---------------------------------------------------------------- comparing


def equivalent(left: sp.Expr, right: sp.Expr) -> bool:
    diff = sp.simplify(left - right)
    if diff == 0:
        return True
    symbols = sorted(diff.free_symbols, key=str)
    rng = random.Random(0)
    for _ in range(6):
        point = {sym: sp.Rational(rng.randint(5, 40), 10) for sym in symbols}
        try:
            val = complex(sp.N(diff.subs(point)))
            scale = abs(complex(sp.N(left.subs(point)))) + 1
        except (TypeError, ValueError):
            return False
        if abs(val) > 1e-9 * scale:
            return False
    return True


def same_sequence(given, expected, tolerance: float = 0.0) -> bool:
    """Ordered comparison, for answers like (x, y)."""
    return len(given) == len(expected) and all(
        abs(float(g) - float(e)) <= max(tolerance, 1e-9) for g, e in zip(given, expected)
    )


def same_numbers(given, expected, tolerance: float = 0.0) -> bool:
    def close(u, v):
        return abs(float(u) - float(v)) <= max(tolerance, 1e-9)

    given_set = _dedupe(given, close)
    expected_set = _dedupe(expected, close)
    if len(given_set) != len(expected_set):
        return False
    return all(any(close(g, e) for g in given_set) for e in expected_set)


def _dedupe(values, close):
    out = []
    for val in values:
        if not any(close(val, seen) for seen in out):
            out.append(val)
    return out


def same_answer(spec: Spec, option) -> bool:
    """Is a candidate distractor actually the right answer in disguise?"""
    if spec.kind == "expr" and isinstance(option, sp.Basic):
        return equivalent(option, spec.expected)
    if spec.kind == "numbers" and isinstance(option, (list, tuple)):
        if spec.ordered:
            return same_sequence(option, spec.expected, spec.tolerance)
        return same_numbers(option, spec.expected, spec.tolerance)
    return False


# ---------------------------------------------------------------- forms


def _factor_list(expr, sign=1):
    if expr.is_Mul:
        for arg in expr.args:
            yield from _factor_list(arg, sign)
    elif expr.is_Pow and expr.exp == -1:
        yield from _factor_list(expr.base, -sign)
    else:
        yield expr, sign


def _is_simplified_monomial(text: str) -> bool:
    expr = parse_expression(text, evaluate=False)
    seen: set = set()
    numbers = {1: 0, -1: 0}
    for factor, sign in _factor_list(expr):
        if factor.is_Number:
            if factor != -1:
                numbers[sign] += 1
        elif factor.is_Symbol:
            if factor in seen:
                return False
            seen.add(factor)
        elif factor.is_Pow and factor.base.is_Symbol and factor.exp.is_Number:
            if factor.base in seen:
                return False
            seen.add(factor.base)
        else:
            return False  # e.g. (x^2)^3, (2x)^3, 2^5, or a sum
    return numbers[1] <= 1 and numbers[-1] <= 1


def _form_expanded(text: str, expr: sp.Expr) -> str | None:
    if sp.expand(expr) != expr:
        return "Multiply everything out - your answer still has parentheses to expand."
    raw = parse_expression(text, evaluate=False)
    if len(sp.Add.make_args(raw)) > len(sp.Add.make_args(sp.expand(expr))):
        return "Combine all of the like terms."
    return None


def _form_monomial(text: str, expr: sp.Expr) -> str | None:
    if not _is_simplified_monomial(text):
        return "Simplify fully - each variable should appear once, with a single exponent."
    return None


def _form_positive_exponents(text: str, expr: sp.Expr) -> str | None:
    if re.search(r"\^\s*\(?\s*-", normalize(text)):
        return "Rewrite it without negative exponents."
    return _form_monomial(text, expr)


def _form_radical(text: str, expr: sp.Expr) -> str | None:
    raw = parse_expression(text, evaluate=False)
    for node in sp.preorder_traversal(raw):
        if node.is_Pow and node.exp.is_Rational and not node.exp.is_Integer and node.base.is_Integer:
            index = node.exp.q
            radicand = abs(int(node.base))
            for base in range(int(radicand ** (1 / index)) + 1, 1, -1):
                if radicand % (base**index) == 0:
                    return f"The radicand {radicand} still has a perfect power factor ({base**index}) to pull out."
    return None


def _form_rational_exponent(text: str, expr: sp.Expr) -> str | None:
    if re.search(r"sqrt|cbrt|root|√", text):
        return "Write it with a fractional exponent, like x^(2/3), instead of a radical."
    return None


def _product_factors(text: str) -> list[sp.Expr]:
    """The top-level factors of an answer exactly as typed, e.g. 2x(x - 3)^2 gives
    [2, x, x - 3, x - 3]. Raises if the answer isn't written as a product."""
    raw = parse_expression(text, evaluate=False)
    factors = []
    for factor, _ in _factor_list(raw):
        if factor.is_Pow and factor.exp.is_Integer and factor.exp > 0:
            factors.extend([factor.base] * int(factor.exp))
        else:
            factors.append(factor)
    return factors


def _polynomial_factors(text: str) -> list[sp.Expr] | None:
    factors = [sp.expand(f) for f in _product_factors(text)]
    polys = [f for f in factors if f.free_symbols]
    if len(factors) < 2 and all(f.is_Add for f in polys):
        return None  # still a sum, nothing has been factored out
    return polys


def _form_gcf(text: str, expr: sp.Expr) -> str | None:
    polys = _polynomial_factors(text)
    if polys is None:
        return "Write it as a product: the GCF times what's left in parentheses."
    for poly in polys:
        if not poly.is_Add:
            continue
        shared_powers, rest = sp.Poly(poly, *sorted(poly.free_symbols, key=str)).terms_gcd()
        if any(shared_powers) or abs(rest.primitive()[0]) != 1:
            return "There's still a common factor inside the parentheses - take out the greatest common factor."
    return None


def _form_factored(text: str, expr: sp.Expr) -> str | None:
    polys = _polynomial_factors(text)
    if polys is None:
        return "Write it as a product of factors."
    for poly in polys:
        content, pieces = sp.factor_list(poly)
        if abs(content) != 1:
            return f"Factor completely - ${sp.latex(poly)}$ still has a common factor of {abs(content)}."
        if sum(mult for _, mult in pieces) > 1:
            return f"Factor completely - ${sp.latex(poly)}$ can be factored further."
    return None


def _form_vertex(text: str, expr: sp.Expr) -> str | None:
    var = SYMS["x"]
    raw = parse_expression(text, evaluate=False)
    squares = []

    def is_square(node) -> bool:
        if not (node.is_Pow and node.exp == 2 and node.base.is_Add):
            return False
        base = sp.expand(node.base)
        return sp.Poly(base, var).degree() == 1 and sp.Poly(base, var).LC() == 1 if base.has(var) else False

    replaced = raw.replace(is_square, lambda node: squares.append(node) or sp.Dummy())
    if not squares or replaced.has(var):
        return "Write it in vertex form, $a(x - h)^2 + k$."
    if len(sp.Add.make_args(raw)) > 2:
        return "Combine the constants at the end."
    return None


FORMS = {
    "expanded": _form_expanded,
    "monomial": _form_monomial,
    "positive_exponents": _form_positive_exponents,
    "radical": _form_radical,
    "rational_exponent": _form_rational_exponent,
    "gcf": _form_gcf,
    "factored": _form_factored,
    "vertex": _form_vertex,
}


# ---------------------------------------------------------------- checking


def check(problem: Problem, fmt: str, response: str) -> Result:
    spec = problem.spec
    if fmt == "mc":
        if response not in problem.choices:
            return Result(False, valid=False, feedback="Pick one of the choices.")
        return Result(response == spec.answer)

    if not problem.supports_input:
        return Result(False, valid=False, feedback="This question is multiple choice only.")

    try:
        if spec.kind == "numbers":
            return _check_numbers(spec, parse_numbers(response))
        return _check_expr(spec, response, parse_expression(response))
    except InputError as err:
        return Result(False, valid=False, feedback=str(err))


def _check_expr(spec: Spec, text: str, expr: sp.Expr) -> Result:
    if not equivalent(expr, spec.expected):
        return Result(False)
    if spec.form:
        try:
            problem = FORMS[spec.form](text, expr)
        except InputError:
            problem = None
        if problem:
            return Result(False, feedback=f"Equivalent, but not finished. {problem}")
    return Result(True)


def _check_numbers(spec: Spec, values: list) -> Result:
    if spec.ordered:
        if same_sequence(values, spec.expected, spec.tolerance):
            return Result(True)
        if len(values) != len(spec.expected):
            return Result(False, valid=False, feedback=f"Enter {len(spec.expected)} values, like (2, -3).")
        if same_sequence(values[::-1], spec.expected, spec.tolerance):
            return Result(False, feedback="Close - you have the coordinates swapped. Write it as (x, y).")
        return Result(False)
    if same_numbers(values, spec.expected, spec.tolerance):
        return Result(True)
    expected = spec.expected
    if len(values) < len(expected) and all(
        any(abs(float(v) - float(e)) <= max(spec.tolerance, 1e-9) for e in expected) for v in values
    ):
        return Result(False, feedback="Close - but there's more than one answer.")
    if len(values) > len(expected) and all(
        any(abs(float(v) - float(e)) <= max(spec.tolerance, 1e-9) for v in values) for e in expected
    ):
        return Result(False, feedback="Close - but not all of those values work. Check which ones belong.")
    return Result(False)


def preview(text: str) -> str:
    """LaTeX for what the student has typed so far, keeping their structure."""
    if not text.strip():
        return ""
    stripped = text.strip()
    if stripped.startswith("(") and stripped.endswith(")") and _has_top_level_comma(stripped[1:-1]):
        parts = [_preview_number(part) for part in _split_top_level(stripped[1:-1])]
        return "\\left(" + ",\\ ".join(parts) + "\\right)"
    if _has_top_level_comma(text) or "±" in text or "+-" in text or " or " in text:
        chunks = [piece for part in _split_top_level(text) for piece in part.split(" or ")]
        return ",\\ ".join(_preview_number(chunk) for chunk in chunks if chunk.strip())
    return sp.latex(parse_expression(text, evaluate=False))


def _preview_number(chunk: str) -> str:
    chunk = chunk.strip().replace("+-", "±")
    sign = "\\pm " if chunk.startswith("±") else ""
    body = chunk.lstrip("±")
    if "±" in body:
        # Show (3 ± sqrt(57))/8 by rendering it with + and swapping that plus back to ±.
        nth = sum(1 for ch in body[: body.index("±")] if ch == "+")
        pieces = sp.latex(parse_expression(body.replace("±", "+", 1), evaluate=False)).split("+")
        if len(pieces) > nth + 1:
            return sign + "+".join(pieces[: nth + 1]) + "\\pm" + "+".join(pieces[nth + 1 :])
    if re.fullmatch(r"\s*-?\s*\d+(\.\d+)?\s*(/\s*\d+)?\s*", body):
        # A plain number or fraction: show it as typed ("0.5", "-3/4") rather than as SymPy's 1·(1/4).
        number = body.replace(" ", "")
        if "/" in number:
            top, bottom = number.split("/")
            neg = top.startswith("-")
            return sign + ("-" if neg else "") + f"\\frac{{{top.lstrip('-')}}}{{{bottom}}}"
        return sign + number
    return sign + sp.latex(parse_expression(body, evaluate=False))
