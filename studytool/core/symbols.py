"""Shared symbols and helpers for building and displaying math.

Every generator and the answer checker use the same symbol objects, so an
expression a generator builds and an expression a student types can be
compared directly. Symbols are declared positive, which matches how this
course treats variables under roots (e.g. sqrt(x^2) = x).
"""

from __future__ import annotations

import random

import sympy as sp

LETTERS = "abcdhkmnpqrstuvwxyz"
SYMS: dict[str, sp.Symbol] = {ch: sp.Symbol(ch, positive=True) for ch in LETTERS}

a, b, c, d, h, k, m, n, p, q, r, s, t, u, v, w, x, y, z = (SYMS[ch] for ch in LETTERS)


def tex(expr, **options) -> str:
    """Inline LaTeX for a SymPy expression, wrapped in $...$."""
    return f"${sp.latex(expr, **options)}$"


def coef_tex(coef) -> str:
    """Coefficient prefix: '' for 1, '-' for -1, otherwise the number."""
    if coef == 1:
        return ""
    if coef == -1:
        return "-"
    return sp.latex(sp.nsimplify(coef))


def mono(coef, *powers) -> str:
    """LaTeX for a monomial exactly as written, e.g. mono(3, ('x', -1), ('y', 2))
    gives '3x^{-1}y^{2}'. SymPy would turn negative exponents into fractions,
    which defeats the point of a negative-exponent question."""
    parts = []
    for var, exp in powers:
        if exp == 0:
            continue
        parts.append(var if exp == 1 else f"{var}^{{{exp}}}")
    body = "".join(parts)
    if not body:
        return sp.latex(coef)
    return coef_tex(coef) + body


def join_terms(terms) -> str:
    """LaTeX for a sum written in the given order, without SymPy reordering or
    combining anything. Used to display unsimplified expressions. Terms may be
    SymPy expressions or ready-made LaTeX strings."""
    out = ""
    for i, term in enumerate(terms):
        body = term if isinstance(term, str) else sp.latex(term)
        if body.startswith("-"):
            out += ("-" if i == 0 else " - ") + body[1:].lstrip()
        else:
            out += body if i == 0 else f" + {body}"
    return out


def nonzero(rng: random.Random, lo: int = -9, hi: int = 9) -> int:
    """Random nonzero integer in [lo, hi]."""
    while True:
        val = rng.randint(lo, hi)
        if val != 0:
            return val


def fmt_num(val) -> str:
    """Format a number for display: integers plainly, decimals trimmed, with
    thousands separators (LaTeX-safe)."""
    val = sp.nsimplify(val)
    if val.is_Integer:
        return f"{int(val):,}".replace(",", "{,}")
    f = float(val)
    text = f"{f:,.4f}".rstrip("0").rstrip(".")
    return text.replace(",", "{,}")


def fmt_linear(coef, const, var: str = "x") -> str:
    """LaTeX for coef*var + const using decimals (used in money/word problems)."""
    out = f"{fmt_num(coef)}{var}" if coef != 1 else var
    if const > 0:
        out += f" + {fmt_num(const)}"
    elif const < 0:
        out += f" - {fmt_num(-const)}"
    return out


def show_numbers(values) -> str:
    """Display a list of numeric answers: ``$8$``, ``$\\pm 8$`` or ``$-1$ and $3$``."""
    vals = [sp.nsimplify(val) for val in values]
    unique = []
    for val in vals:
        if val not in unique:
            unique.append(val)
    if len(unique) == 2 and unique[0] == -unique[1] and unique[0] != 0:
        return f"$\\pm {sp.latex(abs(unique[0]))}$"
    return " and ".join(f"${sp.latex(val)}$" for val in sorted(unique, key=float))


def nice_number(val) -> str:
    """LaTeX for a number: terminating fractions as decimals (0.25), others as fractions."""
    val = sp.nsimplify(val)
    if val.is_Rational and not val.is_Integer:
        q = int(val.q)
        while q % 2 == 0:
            q //= 2
        while q % 5 == 0:
            q //= 5
        if q == 1:
            return fmt_num(val)
    return sp.latex(val)


def show_pair(values) -> str:
    """Display an ordered pair (or tuple) of numbers, e.g. ``$(0.25, 4)$``."""
    return "$(" + ", ".join(nice_number(v) for v in values) + ")$"


def ordinal(nth: int) -> str:
    suffix = "th" if 10 <= nth % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(nth % 10, "th")
    return f"{nth}{suffix}"
