---
title: Quadratic Functions
section: 2 - Linear and Quadratic Functions
module: 6
status: draft
topics: [parabola-features, quadratic-domain-range, gcf-factoring, difference-of-squares, factoring-by-grouping, graphing-quadratics, vertex-and-axis, vertex-form, completing-the-square, quadratic-formula, height-functions]
---

# Module 6: Quadratic Functions

**By the end of this module you can:** read a parabola's direction, vertex, and intercepts from its equation, give its domain and range, factor with a GCF, a difference of squares, or grouping, rewrite a quadratic in vertex form, solve any quadratic equation with the quadratic formula, and find the highest point of a thrown object.

> [!info] Why this matters
> Lines describe things that change at a steady rate. Lots of things don't: a ball goes up, slows, and comes back down; revenue rises with price until customers stop buying. The simplest curve that turns around is the parabola, and the equations behind it - quadratics - are the next step up from linear equations.

---

## 1. Parabolas: Shape and Direction

A **quadratic function** has a squared term as its highest power:

$$f(x) = ax^2 + bx + c, \qquad a \ne 0$$

This is called **general form**. Its graph is a U-shaped curve called a **parabola**.

**The sign of $a$ decides the direction:**
- $a > 0$: opens **up**, like a cup. The lowest point is a **minimum**.
- $a < 0$: opens **down**, like a hill. The highest point is a **maximum**.

> [!tip] Remember it
> Positive $a$ is a smile, negative $a$ is a frown.

The landmarks of every parabola:

| Feature | What it is | How many |
|---|---|---|
| **Vertex** $(h, k)$ | The turning point - the minimum or maximum | Exactly one |
| **Axis of symmetry** | The vertical line $x = h$ through the vertex; the two halves mirror each other across it | Exactly one |
| **$y$-intercept** | Where it crosses the $y$-axis: plug in $x = 0$ | Exactly one |
| **$x$-intercepts** (zeros) | Where it crosses the $x$-axis: set $y = 0$ | Zero, one, or two |

In general form the $y$-intercept is free: $f(0) = c$.

> [!example] Describe $g(x) = -2x^2 + 5x + 3$
> $a = -2 < 0$, so it opens **down** and the vertex is a maximum. The $y$-intercept is $g(0) = 3$.

### Matching an equation to a graph

To pick the right equation for a picture, check two things: does it open up or down (sign of $a$), and where does it cross the $y$-axis (the constant term)?

### Practice

**1.** Which way does $y = 4x^2 - 7$ open, and where does it cross the $y$-axis?

> [!check]- Answer
> Up ($a = 4$); $y$-intercept $-7$.

**2.** Which way does $y = 3 - x^2$ open?

> [!check]- Answer
> Down. Rearranged, it's $y = -x^2 + 3$, so $a = -1$. The order the terms are written in doesn't matter - find the $x^2$ term.

**3.** A parabola opens down and crosses the $y$-axis at 6. Which equation: $y = x^2 + 6$, $y = -x^2 + 6$, $y = -x^2 - 6$, $y = x^2 - 6$?

> [!check]- Answer
> $y = -x^2 + 6$

**4.** Does $f(x) = 0.5x^2 - 3x$ have a maximum or a minimum?

> [!check]- Answer
> A minimum, since $a = 0.5 > 0$.

---

## 2. Domain and Range of a Quadratic

The **domain** is every $x$ you're allowed to put in. The **range** is every $y$ that can come out.

**Domain:** you can square any number, so the domain of every quadratic is **all real numbers**.

**Range:** this is where parabolas are limited. One that opens up never goes below its vertex; one that opens down never goes above it. So the range is decided entirely by the vertex's $y$-value $k$:

| Opens | Vertex is a | Range (inequality) | Range (interval) |
|---|---|---|---|
| Up ($a > 0$) | minimum | $y \ge k$ | $[k, \infty)$ |
| Down ($a < 0$) | maximum | $y \le k$ | $(-\infty, k]$ |

### Interval notation, quickly

- A **bracket** $[$ or $]$ means the endpoint is included.
- A **parenthesis** $($ or $)$ means it isn't.
- $\infty$ always gets a parenthesis - it's not a number you can reach.

So $[k, \infty)$ is "$k$ and everything above it." The range always gets a bracket at $k$, because the vertex itself is on the graph.

The same set can be written three ways:

| Words | Inequality | Interval |
|---|---|---|
| All real numbers from $-2$ to $5$, including both | $-2 \le x \le 5$ | $[-2, 5]$ |
| All real numbers | $-\infty < x < \infty$, or $\mathbb{R}$ | $(-\infty, \infty)$ |

> [!example] Domain and range of $f(x) = x^2 + 4x + 1$
> Domain: $(-\infty, \infty)$.
> It opens up. The vertex is at $(-2, -3)$ (Section 7 shows how to find it), so the minimum $y$ is $-3$.
> Range: $y \ge -3$, or $[-3, \infty)$.

> [!warning] Common mistakes
> - Using the vertex's **$x$**-value for the range. The range is about $y$, so use $k$.
> - Flipping the direction: opens down means $y \le k$, not $y \ge k$.
> - Writing $[k, \infty]$ - infinity never gets a bracket.

### Practice

**1.** Range of $f(x) = -x^2 + 10$?

> [!check]- Answer
> Opens down, vertex $(0, 10)$: $(-\infty, 10]$, or $y \le 10$.

**2.** The vertex of $f(x) = 2x^2 - 12x + 11$ is $(3, -7)$. Give the domain and range.

> [!check]- Answer
> Domain $(-\infty, \infty)$. Opens up, so range $[-7, \infty)$.

**3.** The vertex of $f(x) = -4x^2 - 8x + 1$ is $(-1, 5)$. Give the range as an inequality.

> [!check]- Answer
> $y \le 5$

**4.** Describe the range of $f(x) = 3x^2$ in words.

> [!check]- Answer
> All non-negative real numbers (0 and every positive number). Squares are never negative, and multiplying by 3 doesn't change that.

---

## 3. Factoring Out the GCF

**Factoring** rewrites a sum as a product. It's distributing in reverse - and it's the first tool for solving quadratics, because a product is easy to set to zero.

This module covers three methods: pulling out a **GCF**, factoring a **difference of squares**, and **grouping**. Always try the GCF first - it makes every other method easier.

The **greatest common factor** is the largest expression that divides evenly into every term.

> [!abstract] Factoring out the GCF
> 1. Find the largest number that divides every coefficient.
> 2. Find each variable that appears in **every** term, using its **smallest** exponent.
> 3. Their product is the GCF. Write it outside the parentheses.
> 4. Divide each term by the GCF to fill in the parentheses.
> 5. Check by distributing back.

> [!example] Factor $18x^3 - 12x^2$
> Numbers: the GCF of 18 and 12 is 6.
> Variables: both terms have $x$; the smallest power is $x^2$.
> GCF: $6x^2$. Divide: $18x^3 \div 6x^2 = 3x$ and $-12x^2 \div 6x^2 = -2$.
> $$18x^3 - 12x^2 = 6x^2(3x - 2)$$

> [!example] Factor $9x^2 - 15x + 21$
> GCF of 9, 15, 21 is 3. The last term has no $x$, so no variable is common.
> $$3(3x^2 - 5x + 7)$$

> [!tip] Leading negative?
> If the first term is negative, it's often cleaner to pull out a negative GCF: $-10x^2 - 25x = -5x(2x + 5)$. Every sign inside flips.

> [!warning] Common mistakes
> - Using the largest exponent instead of the smallest.
> - Dropping a term: when a term *is* the GCF, it leaves a **1**, not nothing. $4x^2 + 4x = 4x(x + 1)$.
> - Taking out a factor that isn't the greatest - $2(6x^2 + 9x)$ still has $3x$ in common.

### Practice

**1.** $24x^2 + 36x$

> [!check]- Answer
> $12x(2x + 3)$

**2.** $14x^3 + 21x^2 - 7x$

> [!check]- Answer
> $7x(2x^2 + 3x - 1)$ - the last term leaves $-1$.

**3.** $-10x^2 - 25x$ (take out a negative GCF)

> [!check]- Answer
> $-5x(2x + 5)$

**4.** What is the GCF of $16x^4$, $40x^3$, and $8x^2$?

> [!check]- Answer
> $8x^2$

---

## 4. Difference of Squares

When one perfect square is **subtracted** from another, there's a shortcut:

$$a^2 - b^2 = (a - b)(a + b)$$

Why it works: multiplying $(a - b)(a + b)$ gives $a^2 + ab - ab - b^2$. The middle terms cancel, leaving $a^2 - b^2$.

> [!abstract] The method
> 1. Check that both terms are perfect squares and that they're **subtracted**.
> 2. Find $a$ and $b$ - the things being squared.
> 3. Write $(a - b)(a + b)$.

Perfect squares to recognize: $1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144$, and any even power of a variable ($x^2$, $x^4 = (x^2)^2$, $y^6 = (y^3)^2$).

> [!example] Factor $49x^2 - 4$
> $49x^2 = (7x)^2$ and $4 = 2^2$. So $a = 7x$, $b = 2$:
> $$(7x - 2)(7x + 2)$$

> [!example] Factor $3x^2 - 75$
> 3 isn't a perfect square - but 3 is a GCF. Pull it out first:
> $$3(x^2 - 25) = 3(x - 5)(x + 5)$$

> [!example] Factor $x^4 - 81$ completely
> $x^4 = (x^2)^2$, so: $(x^2 - 9)(x^2 + 9)$.
> $x^2 - 9$ is another difference of squares: $(x - 3)(x + 3)$.
> $x^2 + 9$ is a **sum**, so it stops there.
> $$x^4 - 81 = (x - 3)(x + 3)(x^2 + 9)$$

> [!warning] Common mistakes
> - Trying it on a **sum**: $x^2 + 25$ does not factor into $(x + 5)(x + 5)$ or anything else with real numbers.
> - Forgetting the GCF first, which leaves a "factored" answer that isn't finished, like $(4x - 6)(4x + 6)$ instead of $4(2x - 3)(2x + 3)$.
> - Stopping too early on fourth powers.

### Practice

**1.** $x^2 - 100$

> [!check]- Answer
> $(x - 10)(x + 10)$

**2.** $36y^2 - 25$

> [!check]- Answer
> $(6y - 5)(6y + 5)$

**3.** $2x^2 - 50$

> [!check]- Answer
> $2(x - 5)(x + 5)$

**4.** $81x^4 - 16$, completely

> [!check]- Answer
> $(9x^2 - 4)(9x^2 + 4) = (3x - 2)(3x + 2)(9x^2 + 4)$

**5.** Why doesn't $20x^2 - 9$ factor this way?

> [!check]- Answer
> 20 isn't a perfect square, and there's no GCF to pull out to fix that.

---

## 5. Factoring by Grouping

Grouping is for polynomials with **four terms** that have no GCF across all four. Split them into two pairs, factor each pair, and look for a shared binomial.

> [!abstract] The method
> 1. Pull out any GCF of all four terms first.
> 2. Group the first two terms and the last two.
> 3. Factor the GCF out of each pair. The two leftover binomials should match.
> 4. Factor that binomial out: $(\text{binomial})(\text{what's left})$.

> [!example] Factor $x^3 + 2x^2 + 5x + 10$
> First pair: $x^2(x + 2)$. Second pair: $5(x + 2)$.
> Both contain $(x + 2)$:
> $$x^2(x + 2) + 5(x + 2) = (x + 2)(x^2 + 5)$$

> [!example] Factor $2x^3 - 6x^2 - 7x + 21$
> First pair: $2x^2(x - 3)$.
> Second pair: $-7x + 21$. Pull out $-7$ (not $7$) so the binomial matches: $-7(x - 3)$.
> $$2x^2(x - 3) - 7(x - 3) = (x - 3)(2x^2 - 7)$$

> [!tip] When the binomials don't match
> If you get $(x - 3)$ and $(-x + 3)$, factor out the negative from the second pair instead. If they still don't match, the four terms may need a different grouping or a different method.

### Practice

**1.** $x^3 - 4x^2 + 3x - 12$

> [!check]- Answer
> $x^2(x - 4) + 3(x - 4) = (x - 4)(x^2 + 3)$

**2.** $5x^3 + 15x^2 - x - 3$

> [!check]- Answer
> $5x^2(x + 3) - 1(x + 3) = (x + 3)(5x^2 - 1)$. Don't drop the $-1$.

**3.** $3x^3 + 2x^2 + 12x + 8$

> [!check]- Answer
> $x^2(3x + 2) + 4(3x + 2) = (3x + 2)(x^2 + 4)$

---

## 6. Graphing with a Table

Graphing a quadratic works like graphing a line: pick $x$-values, compute $y$, plot, connect. The difference is that you need more points, and the curve should be smooth, not a set of straight segments.

> [!example] Graph $y = x^2 - 4x + 1$
> | $x$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ |
> |---|---|---|---|---|---|---|
> | $y$ | $6$ | $1$ | $-2$ | $-3$ | $-2$ | $1$ |
>
> Notice the **symmetry**: $y$ is the same at $x = 1$ and $x = 3$, and at $x = 0$ and $x = 4$. The lowest value, $-3$ at $x = 2$, sits right in the middle - that's the vertex.

> [!tip] Pick $x$-values around the vertex
> If you know the axis of symmetry (Section 7), center your table on it so you capture the turn.

> [!warning] Negative inputs
> $x^2$ when $x = -3$ is $(-3)^2 = 9$. And $-x^2$ when $x = -3$ is $-(9) = -9$. Square first, then apply the sign in front.

### Practice

**1.** Complete the table for $y = -x^2 + 2x + 3$ at $x = -2, -1, 0, 1, 2, 3$.

> [!check]- Answer
> $-5, 0, 3, 4, 3, 0$. The vertex is $(1, 4)$ and it opens down.

**2.** Complete the table for $y = 2x^2 - 3$ at $x = -2, -1, 0, 1, 2$.

> [!check]- Answer
> $5, -1, -3, -1, 5$

**3.** For $y = x^2 + 3x - 4$, find $y$ when $x = -5$.

> [!check]- Answer
> $25 - 15 - 4 = 6$

---

## 7. Vertex and Axis of Symmetry

For $f(x) = ax^2 + bx + c$:

$$\text{axis of symmetry: } x = -\frac{b}{2a} \qquad \text{vertex: } \left(-\frac{b}{2a},\; f\!\left(-\frac{b}{2a}\right)\right)$$

**Why $-\frac{b}{2a}$?** A parabola is symmetric, so its vertex sits exactly halfway between its two $x$-intercepts. The quadratic formula (Section 10) gives those intercepts as $\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$. Their average drops the $\pm$ part, leaving $-\frac{b}{2a}$.

> [!abstract] Finding the vertex
> 1. Read $a$ and $b$ (with their signs).
> 2. $x = -\frac{b}{2a}$.
> 3. Plug that $x$ into the function to get $y$.
> 4. Max or min? $a > 0$ minimum, $a < 0$ maximum. The max or min **value** is the $y$.

> [!example] $f(x) = x^2 - 10x + 21$
> $x = -\frac{-10}{2(1)} = 5$. $f(5) = 25 - 50 + 21 = -4$.
> Vertex $(5, -4)$, axis $x = 5$, minimum value $-4$.

> [!example] $f(x) = -2x^2 - 8x + 3$
> $x = -\frac{-8}{2(-2)} = -\frac{-8}{-4} = -2$. $f(-2) = -8 + 16 + 3 = 11$.
> Vertex $(-2, 11)$. Since $a < 0$, it's a **maximum** of 11.

> [!warning] Common mistakes
> - Dropping the negative in front: $\frac{b}{2a}$ instead of $-\frac{b}{2a}$.
> - Forgetting the 2 in $2a$.
> - Answering "the maximum is at $x = -2$" when asked for the maximum **value** - that's 11.

### Practice

**1.** Vertex of $f(x) = x^2 + 6x - 2$

> [!check]- Answer
> $x = -3$, $f(-3) = 9 - 18 - 2 = -11$. $(-3, -11)$

**2.** Vertex of $f(x) = 3x^2 - 9x + 4$ (decimals)

> [!check]- Answer
> $x = \frac{9}{6} = 1.5$; $f(1.5) = 6.75 - 13.5 + 4 = -2.75$. $(1.5, -2.75)$

**3.** Max or min of $f(x) = -x^2 + 5x$, and its value?

> [!check]- Answer
> $x = 2.5$, $f(2.5) = 6.25$. Maximum value $6.25$.

**4.** Axis of symmetry of $f(x) = 4x^2 + 2x - 1$?

> [!check]- Answer
> $x = -\frac{2}{8} = -\frac{1}{4}$

---

## 8. Vertex Form

$$f(x) = a(x - h)^2 + k$$

In **vertex form** (the course also calls it standard form), the vertex $(h, k)$ is right there in the equation, and $a$ still controls the direction.

> [!warning] The sign trap
> The form has a **minus** inside: $x - h$. So:
> - $(x - 3)^2$ means $h = 3$
> - $(x + 3)^2 = (x - (-3))^2$ means $h = -3$
>
> $k$ is read exactly as written: $+5$ means $k = 5$.

> [!example] $f(x) = -2(x - 3)^2 + 8$
> Vertex $(3, 8)$; opens down, so the max value is 8.
> $y$-intercept: $f(0) = -2(9) + 8 = -10$.
> $x$-intercepts: $-2(x - 3)^2 + 8 = 0 \Rightarrow (x - 3)^2 = 4 \Rightarrow x - 3 = \pm 2 \Rightarrow x = 1$ or $5$.

**Solving for $x$-intercepts in vertex form:** isolate the squared part, then take the square root of both sides - with $\pm$. If the squared part ends up equal to a **negative** number, there are no $x$-intercepts (a square can't be negative).

> [!tip] Quick check for no $x$-intercepts
> If the vertex is above the $x$-axis and it opens up (or below and opens down), it never crosses.

### Practice

**1.** Vertex of $f(x) = (x + 4)^2 - 9$?

> [!check]- Answer
> $(-4, -9)$

**2.** Intercepts of $f(x) = (x + 4)^2 - 9$?

> [!check]- Answer
> $y$-intercept $16 - 9 = 7$. $x$: $(x + 4)^2 = 9$, $x + 4 = \pm 3$, so $x = -1$ or $-7$.

**3.** Does $f(x) = 3(x - 1)^2 + 6$ have $x$-intercepts?

> [!check]- Answer
> No. $(x - 1)^2 = -2$ is impossible. (Vertex $(1, 6)$ is above the axis and it opens up.)

**4.** $x$-intercepts of $f(x) = -(x + 2)^2 + 16$?

> [!check]- Answer
> $(x + 2)^2 = 16$, $x + 2 = \pm 4$, so $x = 2$ or $-6$.

---

## 9. Completing the Square

To get from general form to vertex form, build a **perfect square trinomial** - something like $x^2 + 10x + 25 = (x + 5)^2$.

The pattern: in $x^2 + bx + \left(\frac{b}{2}\right)^2 = \left(x + \frac{b}{2}\right)^2$, the number you need is **half of $b$, squared**.

> [!abstract] Completing the square (when $a = 1$)
> 1. Take half the coefficient of $x$ and square it.
> 2. Add **and** subtract that number right after the $x$ term (adding zero keeps it equal).
> 3. Factor the first three terms as $\left(x + \frac{b}{2}\right)^2$ and combine the leftover constants.

> [!example] $f(x) = x^2 + 10x + 18$
> Half of 10 is 5; $5^2 = 25$.
> $f(x) = (x^2 + 10x + 25) - 25 + 18 = (x + 5)^2 - 7$
> Vertex $(-5, -7)$.

> [!abstract] When $a \ne 1$
> 1. Factor $a$ out of **just** the $x^2$ and $x$ terms.
> 2. Complete the square inside the parentheses.
> 3. Distribute $a$ to the number you subtracted, then combine constants.

> [!example] $f(x) = 2x^2 - 12x + 7$
> $$\begin{aligned}
> f(x) &= 2(x^2 - 6x) + 7 \\
> &= 2[(x^2 - 6x + 9) - 9] + 7 \\
> &= 2(x - 3)^2 - 18 + 7 \\
> &= 2(x - 3)^2 - 11
> \end{aligned}$$
> The $-9$ became $-18$ because it was inside the 2's parentheses. Vertex $(3, -11)$.

> [!tip] Check your answer
> Expand it back out. $2(x - 3)^2 - 11 = 2x^2 - 12x + 18 - 11 = 2x^2 - 12x + 7$ ✓. Or check the vertex with $-\frac{b}{2a} = \frac{12}{4} = 3$.

### Practice

**1.** $x^2 - 4x + 9$

> [!check]- Answer
> $(x - 2)^2 + 5$

**2.** $x^2 + 3x + 1$

> [!check]- Answer
> Half of 3 is $\frac{3}{2}$, squared is $\frac{9}{4}$. $\left(x + \frac{3}{2}\right)^2 - \frac{9}{4} + 1 = \left(x + \frac{3}{2}\right)^2 - \frac{5}{4}$

**3.** $4x^2 + 16x + 5$

> [!check]- Answer
> $4(x^2 + 4x) + 5 = 4[(x + 2)^2 - 4] + 5 = 4(x + 2)^2 - 11$

**4.** $-x^2 + 6x - 4$

> [!check]- Answer
> $-(x^2 - 6x) - 4 = -[(x - 3)^2 - 9] - 4 = -(x - 3)^2 + 5$

---

## 10. The Quadratic Formula

Factoring only works when the numbers cooperate. The **quadratic formula** always works:

$$ax^2 + bx + c = 0 \quad\Longrightarrow\quad x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

The $\pm$ means there are usually two answers: one with $+$, one with $-$.

> [!abstract] The method
> 1. Rearrange so one side is **0**: $ax^2 + bx + c = 0$.
> 2. Read off $a$, $b$, $c$ with their signs.
> 3. Compute $b^2 - 4ac$ first (the part under the root).
> 4. Substitute and simplify the radical. Reduce the fraction if every term shares a factor.

> [!example] Solve $2x^2 + 5x - 3 = 0$
> $a = 2$, $b = 5$, $c = -3$. $b^2 - 4ac = 25 + 24 = 49$.
> $$x = \frac{-5 \pm 7}{4} \quad\Rightarrow\quad x = \frac{2}{4} = \frac{1}{2} \text{ or } x = \frac{-12}{4} = -3$$

> [!example] Solve $x^2 - 4x - 1 = 0$
> $b^2 - 4ac = 16 + 4 = 20$, and $\sqrt{20} = 2\sqrt{5}$.
> $$x = \frac{4 \pm 2\sqrt{5}}{2} = 2 \pm \sqrt{5}$$
> Every term (4, $2\sqrt{5}$, and 2) shared a factor of 2, so it reduced.

> [!warning] Common mistakes
> - Not setting the equation to 0 first.
> - $-b$ when $b$ is negative: if $b = -4$, then $-b = 4$.
> - $b^2$ is always positive (or 0). Write $(-4)^2 = 16$, not $-16$.
> - Dividing only part of the numerator by $2a$. The fraction bar covers everything.

### Practice

**1.** $x^2 + 6x + 5 = 0$

> [!check]- Answer
> $\frac{-6 \pm \sqrt{16}}{2} = \frac{-6 \pm 4}{2}$: $x = -1$ or $x = -5$

**2.** $3x^2 - x - 5 = 0$

> [!check]- Answer
> $\frac{1 \pm \sqrt{1 + 60}}{6} = \frac{1 \pm \sqrt{61}}{6}$

**3.** $x(x + 3) = 10$

> [!check]- Answer
> $x^2 + 3x - 10 = 0$. $\frac{-3 \pm \sqrt{49}}{2}$: $x = 2$ or $x = -5$

**4.** $2x^2 = 4x + 3$

> [!check]- Answer
> $2x^2 - 4x - 3 = 0$. $\frac{4 \pm \sqrt{16 + 24}}{4} = \frac{4 \pm 2\sqrt{10}}{4} = \frac{2 \pm \sqrt{10}}{2}$

---

## 11. Height Problems

When something is thrown or launched straight up and gravity is the only force on it, its height over time is a downward-opening parabola:

| Units | Height function |
|---|---|
| Feet | $h(t) = -16t^2 + v_0t + h_0$ |
| Meters | $h(t) = -5t^2 + v_0t + h_0$ |

- $t$ = seconds since launch
- $v_0$ = starting upward speed (ft/s or m/s)
- $h_0$ = starting height (ft or m). Starting below ground, like in a pit, makes it negative.

The $-16$ or $-5$ comes from gravity. Because it's negative, the vertex is the **maximum height**.

> [!abstract] Max height
> 1. Pick the formula that matches the units.
> 2. Fill in $v_0$ and $h_0$.
> 3. Time at the top: $t = -\frac{b}{2a} = -\frac{v_0}{2(-16)}$ or $-\frac{v_0}{2(-5)}$.
> 4. Max height: plug that $t$ into $h(t)$.

> [!example] A diver jumps up from a 10-meter platform at 5 m/s
> $h(t) = -5t^2 + 5t + 10$
> $t = -\frac{5}{2(-5)} = 0.5$ seconds.
> $h(0.5) = -5(0.25) + 2.5 + 10 = 11.25$ meters.

> [!example] A ball is kicked straight up from the ground at 64 ft/s
> $h(t) = -16t^2 + 64t$ (starting height 0)
> $t = -\frac{64}{-32} = 2$ s; $h(2) = -64 + 128 = 64$ feet.

> [!warning] Time vs. height
> $t = -\frac{b}{2a}$ is **when** it peaks, in seconds - not the height. You still have to plug it in.

### Practice

**1.** A model rocket launches from a 6-foot stand at 96 ft/s. Max height?

> [!check]- Answer
> $h(t) = -16t^2 + 96t + 6$. $t = 3$, $h(3) = -144 + 288 + 6 = 150$ feet.

**2.** A ball is tossed up from 1.5 meters at 20 m/s. When does it peak, and how high?

> [!check]- Answer
> $h(t) = -5t^2 + 20t + 1.5$. $t = 2$ s; $h(2) = -20 + 40 + 1.5 = 21.5$ meters.

**3.** Someone throws a ball upward at 48 ft/s from an 80-foot roof. Max height?

> [!check]- Answer
> $t = 1.5$ s; $h(1.5) = -36 + 72 + 80 = 116$ feet.

---

## Module Review Quiz

**1.** Does $f(x) = -x^2 + 7x - 2$ open up or down? What's its $y$-intercept?

> [!check]- Answer
> Down ($a = -1$); $y$-intercept $-2$.

**2.** The vertex of $f(x) = 2x^2 + 8x + 3$ is $(-2, -5)$. Give the range in interval notation.

> [!check]- Answer
> Opens up: $[-5, \infty)$

**3.** Factor $15x^3 - 25x^2$.

> [!check]- Answer
> $5x^2(3x - 5)$

**4.** Factor completely: $5x^2 - 80$.

> [!check]- Answer
> $5(x^2 - 16) = 5(x - 4)(x + 4)$

**5.** Factor by grouping: $x^3 + 6x^2 - 2x - 12$.

> [!check]- Answer
> $x^2(x + 6) - 2(x + 6) = (x + 6)(x^2 - 2)$

**6.** For $y = x^2 - 2x - 3$, find $y$ at $x = -2$ and $x = 4$.

> [!check]- Answer
> Both are $5$. That's symmetry - both points are 3 units from the axis $x = 1$.

**7.** Find the vertex of $f(x) = -3x^2 + 12x - 5$. Max or min?

> [!check]- Answer
> $x = 2$, $f(2) = -12 + 24 - 5 = 7$. $(2, 7)$, a maximum.

**8.** Vertex and $x$-intercepts of $f(x) = 2(x + 1)^2 - 18$?

> [!check]- Answer
> Vertex $(-1, -18)$. $(x + 1)^2 = 9$, so $x = 2$ or $x = -4$.

**9.** Write $f(x) = x^2 - 8x + 10$ in vertex form.

> [!check]- Answer
> $(x - 4)^2 - 6$

**10.** Solve $x^2 + 2x - 5 = 0$.

> [!check]- Answer
> $\frac{-2 \pm \sqrt{24}}{2} = \frac{-2 \pm 2\sqrt{6}}{2} = -1 \pm \sqrt{6}$

**11.** A ball is thrown up at 40 ft/s from a 25-foot balcony. Max height?

> [!check]- Answer
> $t = \frac{40}{32} = 1.25$ s. $h(1.25) = -25 + 50 + 25 = 50$ feet.

