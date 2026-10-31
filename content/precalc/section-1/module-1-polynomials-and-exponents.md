---
title: Polynomials and Exponents
section: 1 - Foundations of Algebra and Functions
module: 1
status: draft
topics: [polynomial-basics, classifying-polynomials, combining-like-terms, laws-of-exponents, negative-exponents, adding-polynomials, subtracting-polynomials, multiplying-polynomials, square-roots, rational-exponents]
---

# Module 1: Polynomials and Exponents

**By the end of this module you can:** simplify, add, subtract, and multiply polynomials, use the exponent rules confidently, and switch between roots and fractional exponents.

> [!info] Why this matters
> Almost everything later in precalc - factoring, solving equations, graphing functions - is built on being fast and accurate with these moves. If this module feels automatic, the rest of the course gets a lot easier.

---

## 1. What Is a Polynomial?

Imagine you run a food truck. If you sell $x$ meals a day, your revenue might be $40x - x^2$ (you have to discount when you sell a lot), and your costs might be $100 + 10x$. Your profit is revenue minus cost - and every one of those expressions is a **polynomial**. By section 7 you'll be able to find that profit in one line.

### The parts of an expression

Take the expression $6a^2 - b + 9ab - 2$.

| Piece | What it is | In this expression |
|---|---|---|
| **Term** | A chunk separated by $+$ or $-$ (the sign travels with it) | $6a^2$, $-b$, $9ab$, $-2$ |
| **Variable** | A letter standing for a value that can change | $a$, $b$ |
| **Constant** | A plain number that never changes | $-2$ |
| **Coefficient** | The number multiplied onto the variables | $6$, $-1$, $9$ |
| **Exponent** | How many times the base is multiplied by itself | the $2$ in $a^2$ means $a \cdot a$ |

> [!tip] Invisible ones
> $-b$ has a coefficient of $-1$, and $b$ by itself has an exponent of $1$. Nothing written usually means $1$.

### Monomial vs. polynomial

- A **monomial** is a single term: a number, a variable, or numbers and variables multiplied together. ($7$, $x$, $-3a^2b$)
- A **polynomial** is one or more monomials added or subtracted.

A term is **not** allowed in a polynomial if it has:

1. a variable in a denominator ($\frac{3}{x}$)
2. a negative exponent on a variable ($5x^{-2}$)
3. a fractional exponent on a variable ($x^{1/2}$)

(and a polynomial can't go on forever with infinitely many terms).

Coefficients, on the other hand, can be anything - fractions, decimals, even roots.

> [!example] Polynomial or not?
> | Expression | Polynomial? | Reason |
> |---|---|---|
> | $4x^3 - x + 7$ | Yes | whole-number exponents only |
> | $\sqrt{3}\,x^2 - x$ | Yes | a root as a *coefficient* is fine |
> | $0.5ab^2$ | Yes | decimals and multiple variables are fine |
> | $\frac{3}{x} + 2$ | No | dividing by a variable |
> | $5x^{-2}$ | No | negative exponent on a variable |
> | $x^{1/2} + 1$ | No | fractional exponent on a variable |

---

## 2. Naming Polynomials

Every polynomial gets a two-word name: **[how high] + [how many]**.

**How high** - the degree (the biggest exponent):

| Degree | Name |
|---|---|
| 0 | constant |
| 1 | linear |
| 2 | quadratic |
| 3 | cubic |
| 4 | quartic |
| 5+ | "$n$th degree" (5th degree, 6th degree...) |

**How many** - the number of terms:

| Terms | Name |
|---|---|
| 1 | monomial |
| 2 | binomial |
| 3 | trinomial |
| 4+ | polynomial with $n$ terms |

> [!example] Name each polynomial
> - $-3x^5 + x$ → highest power 5, two terms → **5th degree binomial**
> - $7 - 2y^2 + y$ → highest power 2, three terms → **quadratic trinomial** (order doesn't matter - find the biggest exponent wherever it is)
> - $x^3 + 2x^3 - 4$ → *simplify first!* $3x^3 - 4$ → **cubic binomial**, not a trinomial

> [!warning] Always simplify before you name
> $x^2 + 5x - x^2$ looks like a quadratic trinomial, but the $x^2$ terms cancel, leaving $5x$ - a **linear monomial**.

---

## 3. Combining Like Terms

**Like terms** have the *exact same variable part* - same letters, same exponents. Only the coefficients can differ.

| Pair | Like? | Why |
|---|---|---|
| $3a^2$ and $-a^2$ | Yes | both $a^2$ |
| $6xy$ and $xy$ | Yes | both $xy$ |
| $5x^2$ and $5x$ | No | different exponents |
| $2x^2y$ and $2xy^2$ | No | the exponents are on different letters |
| $8$ and $-3$ | Yes | all constants are like terms |

**To combine them, add the coefficients and keep the variable part exactly as it is.** Think of it like counting objects: 3 apples plus 2 apples is 5 apples - the "apple" doesn't change.

> [!example] Simplify $3a^2 + 5a - a^2 + 2a - 8$
> Group the like terms: $(3a^2 - a^2) + (5a + 2a) - 8$
> Add coefficients: $2a^2 + 7a - 8$

> [!example] Simplify $6xy - 2x + xy + 9x$
> $(6xy + xy) + (-2x + 9x) = 7xy + 7x$
> ($xy$ and $x$ are **not** like terms, so this is as far as it goes.)

> [!warning] Common mistake
> Combining like terms never changes an exponent. $3x^2 + 4x^2 = 7x^2$, **not** $7x^4$.

### Practice

**1.** Simplify $7m^3 - 2m + 4 - 3m^3 + m - 10$

> [!check]- Answer
> $4m^3 - m - 6$

**2.** Simplify $2p^2q + 5pq^2 - p^2q + 3pq^2$

> [!check]- Answer
> $p^2q + 8pq^2$ - the two variable parts are different, so there are two separate groups.

**3.** Simplify $9 - 4n^2 + 2n^2 + n - 9$, then name the result.

> [!check]- Answer
> $-2n^2 + n$ → **quadratic binomial** (the constants cancel).

---

## 4. The Laws of Exponents

Every rule below comes from one idea: **an exponent counts how many copies of the base are being multiplied.** If you forget a rule, write out the copies and you can rebuild it.

| Rule | In words | Example |
|---|---|---|
| $x^1 = x$ | One copy is just the base | $9^1 = 9$ |
| $x^0 = 1$ | Zero copies is $1$ (for $x \neq 0$) | $(5xy)^0 = 1$ |
| $x^m \cdot x^n = x^{m+n}$ | Same base, multiplying → **add** exponents | $y^4 \cdot y^3 = y^7$ |
| $\dfrac{x^m}{x^n} = x^{m-n}$ | Same base, dividing → **subtract** (top minus bottom) | $\dfrac{y^9}{y^4} = y^5$ |
| $(x^m)^n = x^{mn}$ | Power of a power → **multiply** exponents | $(a^4)^3 = a^{12}$ |
| $(xy)^n = x^ny^n$ | Exponent hits **every** factor inside | $(3a^2b)^3 = 27a^6b^3$ |
| $\left(\dfrac{x}{y}\right)^n = \dfrac{x^n}{y^n}$ | Exponent hits top and bottom | $\left(\dfrac{2}{k}\right)^4 = \dfrac{16}{k^4}$ |
| $x^{-n} = \dfrac{1}{x^n}$ | Negative exponent → flip to the other side of the fraction | $3^{-2} = \dfrac{1}{9}$ |

> [!example] Why we add when multiplying
> $y^4 \cdot y^3 = (y \cdot y \cdot y \cdot y)(y \cdot y \cdot y)$ - that's 7 copies of $y$, so $y^7$.

> [!example] Why we subtract when dividing
> $\dfrac{y^5}{y^2} = \dfrac{y \cdot y \cdot y \cdot \cancel{y} \cdot \cancel{y}}{\cancel{y} \cdot \cancel{y}} = y^3$ - two copies cancel out of five.

> [!example] Simplify $(3a^2b)^3$
> The exponent applies to the $3$, the $a^2$, **and** the $b$:
> $$3^3 \cdot (a^2)^3 \cdot b^3 = 27a^6b^3$$

> [!warning] Common mistakes
> - $x^2 \cdot x^3 = x^5$, **not** $x^6$ (multiplying bases → add, don't multiply)
> - $(2x)^3 = 8x^3$, **not** $2x^3$ (the coefficient gets the exponent too)
> - $-3^2 = -9$ but $(-3)^2 = 9$ (without parentheses, only the $3$ is squared)
> - $(x + y)^2 \neq x^2 + y^2$ (the product rule only works for multiplication, not addition - see section 8)

### Practice

**1.** $2^{-3}$

> [!check]- Answer
> $\dfrac{1}{2^3} = \dfrac{1}{8}$

**2.** $a^5 \cdot a^{-2} \cdot a$

> [!check]- Answer
> $a^{5 + (-2) + 1} = a^4$

**3.** $(-2m^3n)^2$

> [!check]- Answer
> $(-2)^2(m^3)^2n^2 = 4m^6n^2$

**4.** $\dfrac{10x^7}{2x^3}$

> [!check]- Answer
> Divide the coefficients, subtract the exponents: $5x^4$

**5.** $\left(\dfrac{2a}{b^2}\right)^3$

> [!check]- Answer
> $\dfrac{2^3a^3}{(b^2)^3} = \dfrac{8a^3}{b^6}$

---

## 5. Getting Rid of Negative Exponents

An answer isn't considered fully simplified while it still has negative exponents.

> [!tip] The "wrong floor" trick
> Think of a fraction as a two-story building. A negative exponent means that factor is on the **wrong floor**. Move it to the other floor and the exponent becomes positive.
> $$\frac{a^{-3}}{1} = \frac{1}{a^3} \qquad\qquad \frac{1}{b^{-2}} = b^2$$

> [!warning] Only the factor with the exponent moves
> $2x^{-3} = \dfrac{2}{x^3}$, **not** $\dfrac{1}{2x^3}$. The $2$ has no negative exponent, so it stays put.

**Strategy for bigger problems:**
1. Simplify inside parentheses first (combine same bases).
2. Apply any outside exponent.
3. Move whatever is still negative to the other floor.

> [!example] Simplify $\dfrac{8a^{-2}b^5}{2a^3b^{-1}}$
> Coefficients: $8 \div 2 = 4$
> $a$: $a^{-2-3} = a^{-5}$
> $b$: $b^{5-(-1)} = b^6$
> So we have $4a^{-5}b^6$. The $a$ is on the wrong floor:
> $$= \frac{4b^6}{a^5}$$

> [!example] Simplify $\left(\dfrac{x^2}{3y^{-1}}\right)^{-2}$
> Inside first - move $y^{-1}$ up: $\dfrac{x^2y}{3}$
> A $-2$ outside flips the fraction and squares it:
> $$\left(\frac{x^2y}{3}\right)^{-2} = \left(\frac{3}{x^2y}\right)^{2} = \frac{9}{x^4y^2}$$

> [!tip] Shortcut
> A negative exponent on a whole fraction just means "flip the fraction, then make the exponent positive."

### Practice

**1.** $\dfrac{6m^{-4}n^2}{3m^2n^{-3}}$

> [!check]- Answer
> $2m^{-6}n^{5} = \dfrac{2n^5}{m^6}$

**2.** $(2x^{-3})^{-2}$

> [!check]- Answer
> $2^{-2}x^{6} = \dfrac{x^6}{4}$

**3.** $\left(\dfrac{a^{-2}}{a^3}\right)^{-1}$

> [!check]- Answer
> Inside: $a^{-2-3} = a^{-5}$. Then $(a^{-5})^{-1} = a^5$

**4.** $\left(\dfrac{4x^3y^{-2}}{2xy^3}\right)^{-2}$

> [!check]- Answer
> Inside: $2x^{2}y^{-5}$. Then $2^{-2}x^{-4}y^{10} = \dfrac{y^{10}}{4x^4}$

---

## 6. Adding Polynomials

Adding polynomials is just combining like terms with extra steps of bookkeeping. The parentheses can simply drop away, because adding doesn't change any signs.

> [!example] $(5x^3 - 2x + 9) + (x^3 + 4x^2 + 2x - 11)$
> Drop the parentheses and line up by power:
> $$5x^3 + x^3 + 4x^2 - 2x + 2x + 9 - 11$$
> Combine:
> $$6x^3 + 4x^2 + 0x - 2 = 6x^3 + 4x^2 - 2$$
> The $x$ terms cancelled completely - that's fine, just leave them out.

> [!tip] Stack it vertically
> If it's easy to lose track, write the polynomials on top of each other with matching powers in columns, like adding big numbers:
> ```
>   5x³ + 0x² - 2x +  9
> +  x³ + 4x² + 2x - 11
> ---------------------
>   6x³ + 4x² + 0x -  2
> ```

### Practice

**1.** $(3y^2 - 7y + 1) + (-5y^2 + 2y + 6)$

> [!check]- Answer
> $-2y^2 - 5y + 7$

**2.** $(4a^3 + a - 8) + (2a^2 - 6a^3 + 3)$

> [!check]- Answer
> $-2a^3 + 2a^2 + a - 5$

---

## 7. Subtracting Polynomials

Subtraction has one trap: the minus sign in front of the parentheses applies to **every** term inside, not just the first one.

> [!abstract] The method
> 1. Change the subtraction to "add the opposite."
> 2. Flip the sign of **every** term in the second polynomial.
> 3. Combine like terms, like section 6.

> [!example] $(6x^2 + 3x - 4) - (2x^2 - 5x + 7)$
> Flip every sign in the second group:
> $$6x^2 + 3x - 4 - 2x^2 + 5x - 7$$
> Combine:
> $$4x^2 + 8x - 11$$

> [!warning] Common mistake
> Only flipping the first term: $6x^2 + 3x - 4 - 2x^2 \mathbf{- 5x + 7}$. That gives $4x^2 - 2x + 3$ - wrong. Every term flips.

> [!example] Back to the food truck
> Revenue $40x - x^2$, cost $100 + 10x$:
> $$(40x - x^2) - (100 + 10x) = 40x - x^2 - 100 - 10x = -x^2 + 30x - 100$$

### Practice

**1.** $(9m^3 - 4m + 2) - (3m^3 + m^2 - 4m - 5)$

> [!check]- Answer
> $6m^3 - m^2 + 7$ (the $m$ terms cancel)

**2.** $(x^2 - 1) - (-x^2 + 3x - 1)$

> [!check]- Answer
> $x^2 - 1 + x^2 - 3x + 1 = 2x^2 - 3x$

**3.** A bakery's revenue is $60x - 0.5x^2$ and its cost is $200 + 20x + 0.5x^2$. Write the profit polynomial.

> [!check]- Answer
> $(60x - 0.5x^2) - (200 + 20x + 0.5x^2) = -x^2 + 40x - 200$

---

## 8. Multiplying Polynomials

**One rule covers everything: every term in the first polynomial multiplies every term in the second.** Then combine like terms.

This is the **distributive property**: $a(b + c) = ab + ac$.

### Monomial × monomial

Multiply the coefficients, then add the exponents of matching variables.

> [!example] $-4a^3(5a^2)$
> $(-4)(5) = -20$ and $a^{3+2} = a^5$, so $-20a^5$

### Monomial × polynomial

Distribute the single term to each term inside.

> [!example] $2x^2(3x^2 - x + 6)$
> $$2x^2 \cdot 3x^2 + 2x^2 \cdot (-x) + 2x^2 \cdot 6 = 6x^4 - 2x^3 + 12x^2$$

### Binomial × binomial

Each of the 2 terms hits each of the other 2 → **4 products**.

> [!example] $(2x + 5)(x - 3)$
> $2x \cdot x = 2x^2$
> $2x \cdot (-3) = -6x$
> $5 \cdot x = 5x$
> $5 \cdot (-3) = -15$
> Add and combine: $2x^2 - x - 15$

> [!tip] FOIL
> For two binomials, some people remember the 4 products as **F**irst, **O**uter, **I**nner, **L**ast. It's the same thing - just a checklist so you don't miss one. It only works for binomial × binomial, though, so the general rule is the one to really learn.

### Bigger polynomials

$(\text{2 terms}) \times (\text{3 terms}) = 6$ products. $(\text{3 terms}) \times (\text{4 terms}) = 12$ products. Count first so you know when you're done.

> [!example] $(x - 2)(x^2 + 3x - 1)$
> $x$ times each: $x^3 + 3x^2 - x$
> $-2$ times each: $-2x^2 - 6x + 2$
> Combine: $x^3 + x^2 - 7x + 2$

### The box (table) method

For bigger problems, a grid keeps everything organized. One polynomial goes down the side, the other across the top, and each cell is a product.

> [!example] $(2x^2 + x - 3)(x^2 - 4)$
>
> | $\times$ | $x^2$ | $-4$ |
> |---|---|---|
> | $2x^2$ | $2x^4$ | $-8x^2$ |
> | $x$ | $x^3$ | $-4x$ |
> | $-3$ | $-3x^2$ | $12$ |
>
> Add every cell: $2x^4 + x^3 - 8x^2 - 3x^2 - 4x + 12 = 2x^4 + x^3 - 11x^2 - 4x + 12$

### Bonus: patterns worth recognizing

These show up constantly later in the course:

$$(a + b)^2 = a^2 + 2ab + b^2 \qquad (a - b)^2 = a^2 - 2ab + b^2 \qquad (a + b)(a - b) = a^2 - b^2$$

> [!warning] The most common mistake in algebra
> $(x + 6)^2 \neq x^2 + 36$. Squaring means $(x+6)(x+6)$ - four products, including the two middle ones: $x^2 + 12x + 36$.

### Practice

**1.** $-3m^2n(4mn^3)$

> [!check]- Answer
> $-12m^3n^4$

**2.** $(3x - 1)(2x + 4)$

> [!check]- Answer
> $6x^2 + 12x - 2x - 4 = 6x^2 + 10x - 4$

**3.** $(x + 6)^2$

> [!check]- Answer
> $x^2 + 12x + 36$

**4.** $(2y - 3)(y^2 - y + 5)$

> [!check]- Answer
> $2y^3 - 2y^2 + 10y - 3y^2 + 3y - 15 = 2y^3 - 5y^2 + 13y - 15$

**5.** $(x^2 + 1)(x^2 - 1)$

> [!check]- Answer
> $x^4 - 1$ (the middle terms cancel - it's the $(a+b)(a-b)$ pattern)

**6.** Use a table: $(x^2 - 3x + 2)(2x + 5)$

> [!check]- Answer
>
> | $\times$ | $2x$ | $5$ |
> |---|---|---|
> | $x^2$ | $2x^3$ | $5x^2$ |
> | $-3x$ | $-6x^2$ | $-15x$ |
> | $2$ | $4x$ | $10$ |
>
> $2x^3 - x^2 - 11x + 10$

---

## 9. Square Roots

You're planting a square garden that covers $144$ square feet. How long is each side? You need a number that, multiplied by itself, gives $144$. That's $12$, so each side is 12 feet.

$$12 \cdot 12 = 144 \quad\Longleftrightarrow\quad \sqrt{144} = 12$$

- **Square root** - undoing a square: $\sqrt{a}$ is the number that squares to $a$
- **Radicand** - whatever is under the root symbol
- **Principal square root** - the positive answer; this is what $\sqrt{\ }$ means by default

### Two roots, one symbol

Both $12^2$ and $(-12)^2$ equal $144$, so every positive number actually has two square roots. The symbol $\sqrt{\ }$ by itself means only the positive one. Read the problem to know which you need:

| You see | You give | Example |
|---|---|---|
| $\sqrt{a}$ | positive root only | $\sqrt{49} = 7$ |
| $-\sqrt{a}$ | negative root only | $-\sqrt{100} = -10$ |
| $\pm\sqrt{a}$ | both | $\pm\sqrt{49} = \pm 7$ |
| "find all $x$ where $x^2 = a$" | both | $x^2 = 81 \Rightarrow x = \pm 9$ |
| a length, area, or distance | positive only | a side can't be $-12$ ft |

> [!example] $\sqrt{(-9)^2}$
> Do the inside first: $(-9)^2 = 81$. Then $\sqrt{81} = 9$. The answer is **positive** even though we started with $-9$.

> [!note] Bonus: $\sqrt{-9}$
> There's no real number that squares to a negative, so $\sqrt{-9}$ is **not a real number**. (Later in math this leads to imaginary numbers.)

> [!tip] Memorize the perfect squares
> $1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225$
> Knowing these by sight makes root problems instant. For anything else, you can estimate: $\sqrt{50}$ is between $\sqrt{49} = 7$ and $\sqrt{64} = 8$, just a bit above 7.

### Practice

**1.** A square tile has an area of $225 \text{ in}^2$. How long is each edge?

> [!check]- Answer
> $15$ inches

**2.** $\pm\sqrt{64}$

> [!check]- Answer
> $\pm 8$

**3.** $-\sqrt{144}$

> [!check]- Answer
> $-12$

**4.** $\sqrt{(-15)^2}$

> [!check]- Answer
> $15$

**5.** Find all $x$ such that $x^2 = 81$.

> [!check]- Answer
> $x = 9$ or $x = -9$

---

## 10. Rational Exponents

Roots have a second way to be written: as **fractional exponents**. This is powerful because it means the exponent rules from section 4 suddenly work on roots too.

### Where $x^{1/n}$ comes from

What number, cubed, gives $a$? Using the power-of-a-power rule:
$$\left(a^{1/3}\right)^3 = a^{\frac{1}{3} \cdot 3} = a^1 = a$$
So $a^{1/3}$ does exactly what a cube root does:
$$a^{1/2} = \sqrt{a} \qquad a^{1/3} = \sqrt[3]{a} \qquad a^{1/4} = \sqrt[4]{a}$$

A **rational exponent** is an exponent written as a fraction $\frac{p}{q}$ (where $q \neq 0$). Whole-number exponents like $x^4$ technically equal $x^{4/1}$, but they aren't counted as rational exponents - the point is the fractional part.

### The conversion rule

$$\sqrt[r]{m^n} = m^{n/r}$$

> [!tip] "Power over root"
> - The **power** (exponent inside) goes on **top**.
> - The **root** (index of the radical) goes on the **bottom**.
> - The base stays the base.
>
> A plain $\sqrt{\ }$ has a hidden index of $2$, and a base with no exponent has a hidden power of $1$.

> [!example] Write $\sqrt[5]{y^3}$ with a rational exponent
> Power 3 on top, root 5 on bottom: $y^{3/5}$

> [!example] Write $z^{2/7}$ as a radical
> Bottom 7 is the root, top 2 is the power: $\sqrt[7]{z^2}$

> [!example] Bonus: evaluate $8^{2/3}$
> Take the root first (smaller numbers), then the power:
> $$8^{2/3} = \left(\sqrt[3]{8}\right)^2 = 2^2 = 4$$

### Practice

**1.** Write $\sqrt[6]{x^5}$ with a rational exponent.

> [!check]- Answer
> $x^{5/6}$

**2.** Write $\sqrt{a^3}$ with a rational exponent.

> [!check]- Answer
> $a^{3/2}$ (hidden index of 2)

**3.** Write $b^{4/9}$ as a radical.

> [!check]- Answer
> $\sqrt[9]{b^4}$

**4.** Write $(2x + 1)^{1/3}$ as a radical.

> [!check]- Answer
> $\sqrt[3]{2x + 1}$

**5.** Which has a rational exponent: $x^3$, $x^{-2}$, $x^{2/5}$, $x^{4/1}$?

> [!check]- Answer
> $x^{2/5}$. ($x^{4/1}$ is just $x^4$, a whole-number exponent.)

**6.** Evaluate $27^{1/3}$.

> [!check]- Answer
> $\sqrt[3]{27} = 3$

**7.** Evaluate $25^{3/2}$.

> [!check]- Answer
> $\left(\sqrt{25}\right)^3 = 5^3 = 125$

---

## Module Review Quiz

Mixed questions from the whole module.

**1.** Name the polynomial: $4x - x^3 + 2x^3 + 1$

> [!check]- Answer
> Simplify: $x^3 + 4x + 1$ → **cubic trinomial**

**2.** Simplify $\dfrac{(2a^3)^2}{4a^{-1}}$

> [!check]- Answer
> $\dfrac{4a^6}{4a^{-1}} = a^7$

**3.** $(5x^2 - x + 3) - (2x^2 + 4x - 3)$

> [!check]- Answer
> $3x^2 - 5x + 6$

**4.** $(x - 4)(x + 4)$

> [!check]- Answer
> $x^2 - 16$

**5.** Is $3x^{-1} + 2$ a polynomial? Why or why not?

> [!check]- Answer
> No - a variable has a negative exponent.

**6.** Write $\sqrt[4]{m^3}$ with a rational exponent, then evaluate $16^{3/4}$.

> [!check]- Answer
> $m^{3/4}$, and $16^{3/4} = \left(\sqrt[4]{16}\right)^3 = 2^3 = 8$
