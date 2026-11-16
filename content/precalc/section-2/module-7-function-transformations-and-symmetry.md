---
title: Function Transformations and Symmetry
section: 2 - Linear and Quadratic Functions
module: 7
status: draft
topics: [function-shifts, combined-shifts, reflections, even-odd-functions, vertical-stretches, horizontal-stretches, transformation-sequences, corresponding-points, transformed-domain-range]
---

# Module 7: Function Transformations and Symmetry

**By the end of this module you can:** read a transformed function like $g(x) = -2(x + 3)^2 + 5$ and describe exactly what happened to the original graph; write the equation of a moved, flipped, or stretched graph; follow a single point through a transformation; decide whether a function is even, odd, or neither; and find the domain and range of a transformed function.

> [!info] Why this matters
> You already know a handful of basic graphs: $x^2$, $x^3$, $|x|$, $\sqrt{x}$, $\sqrt[3]{x}$. Transformations turn that handful into thousands. Instead of plotting $g(x) = 2\sqrt{x - 1} + 3$ point by point, you start from $\sqrt{x}$ and move it. Once you can read the four kinds of changes - shift, reflect, stretch, compress - every new graph is an old graph in disguise.

### The parent functions

| Parent | Key point | Shape |
|---|---|---|
| $x^2$ | vertex $(0, 0)$ | U-shaped parabola |
| $x^3$ | center $(0, 0)$ | S-shaped, rising |
| $\lvert x \rvert$ | vertex $(0, 0)$ | V-shape |
| $\sqrt{x}$ | starting point $(0, 0)$ | half-curve, going right |
| $\sqrt[3]{x}$ | center $(0, 0)$ | sideways S, rising |

Tracking the key point is the fastest way to place a transformed graph.

---

## 1. Shifting Up, Down, Left, and Right

A **shift** (or **translation**) slides the whole graph without changing its shape.

**Outside changes move it up or down.** Adding to the output, $f(x) + k$, adds $k$ to every $y$-value:
- $f(x) + k$ with $k > 0$: up $k$
- $f(x) - k$ with $k > 0$: down $k$

**Inside changes move it left or right - backwards from what you'd guess.** In $f(x - h)$, the graph moves right $h$:
- $f(x - h)$ with $h > 0$: **right** $h$
- $f(x + h)$ with $h > 0$: **left** $h$

> [!tip] Why inside changes feel backwards
> For $g(x) = (x - 3)^2$ to equal $f$'s value at $0$, you need $x - 3 = 0$, so $x = 3$. Every point arrives 3 units *later* on the $x$-axis - to the right. The question is always "what $x$ makes the inside what it used to be?"

> [!example] $g(x) = |x| - 3$
> Outside change, subtract 3: the V moves **down 3**. Vertex $(0, -3)$.

> [!example] $g(x) = \sqrt{x + 6}$
> Inside change, add 6: the curve moves **left 6**. It starts at $(-6, 0)$, because that's where the inside is 0.

### Practice

**1.** Describe $g(x) = x^3 + 7$.

> [!check]- Answer
> Up 7. The center moves to $(0, 7)$.

**2.** Describe $g(x) = (x - 9)^2$.

> [!check]- Answer
> Right 9. Vertex $(9, 0)$.

**3.** $\sqrt{x}$ is moved so it starts at $(-2, 0)$. Write the function.

> [!check]- Answer
> $g(x) = \sqrt{x + 2}$

**4.** $-|x|$ is shifted 5 units left. Write the function.

> [!check]- Answer
> $g(x) = -|x + 5|$

**5.** Which shift is $g(x) = \sqrt[3]{x} - 4$?

> [!check]- Answer
> Down 4 - the 4 is outside the root.

---

## 2. Combining Shifts

Inside and outside changes are independent, so a graph can move both ways at once:

$$g(x) = f(x - h) + k \quad\text{moves the key point from } (0, 0) \text{ to } (h, k)$$

The order doesn't matter for two shifts.

> [!example] $g(x) = (x - 3)^2 + 4$
> Right 3, up 4. Vertex $(3, 4)$.

> [!example] $g(x) = \sqrt{x + 1} - 6$
> Left 1, down 6. It starts at $(-1, -6)$.

> [!warning] Read $h$ with the sign flipped, $k$ as written
> $(x + 1)$ means $h = -1$ (left). $-6$ means $k = -6$ (down).

### Practice

**1.** Describe $g(x) = |x - 5| + 2$ and give the vertex.

> [!check]- Answer
> Right 5, up 2. Vertex $(5, 2)$.

**2.** $x^3$ is moved so its center is at $(-4, 1)$. Write the function.

> [!check]- Answer
> $g(x) = (x + 4)^3 + 1$

**3.** $\sqrt{x}$ is moved to start at $(2, -3)$. Write the function.

> [!check]- Answer
> $g(x) = \sqrt{x - 2} - 3$

**4.** A parabola $y = x^2$ is moved so its vertex is $(-1, -7)$. Write it.

> [!check]- Answer
> $g(x) = (x + 1)^2 - 7$

---

## 3. Reflections

A reflection flips the graph over an axis.

| Change | Formula | Flips over | What changes |
|---|---|---|---|
| Negate the **output** | $-f(x)$ | the **$x$-axis** (vertical flip) | every $y$ becomes $-y$ |
| Negate the **input** | $f(-x)$ | the **$y$-axis** (horizontal flip) | every $x$ becomes $-x$ |

> [!tip] Remember it
> The minus sign **outside** flips the outputs (up and down). The minus sign **inside** flips the inputs (left and right). It's the same inside/outside pattern as shifts.

**Writing $-f(x)$:** multiply **every term** by $-1$.

**Writing $f(-x)$:** replace every $x$ with $(-x)$ and simplify. Constants don't change.

> [!example] $f(x) = x^2 + 3x - 4$
> Over the $x$-axis: $-f(x) = -x^2 - 3x + 4$
> Over the $y$-axis: $f(-x) = (-x)^2 + 3(-x) - 4 = x^2 - 3x - 4$

> [!example] $f(x) = \sqrt{x + 2}$ (starts at $(-2, 0)$, goes right)
> Over the $x$-axis: $-\sqrt{x + 2}$ - still starts at $(-2, 0)$, but goes down to the right.
> Over the $y$-axis: $\sqrt{-x + 2}$ - starts at $(2, 0)$ and goes left.

> [!warning] Common mistakes
> - Negating only the first term for $-f(x)$: $-(x^2 + 3x - 4)$ is not $-x^2 + 3x - 4$.
> - Changing the constant for $f(-x)$. Only the $x$'s change.
> - Mixing up which axis: the $x$-axis flip changes the $y$-values.

### Practice

**1.** Reflect $f(x) = x^3 - 2x + 5$ over the $x$-axis.

> [!check]- Answer
> $-x^3 + 2x - 5$

**2.** Reflect $f(x) = x^3 - 2x + 5$ over the $y$-axis.

> [!check]- Answer
> $(-x)^3 - 2(-x) + 5 = -x^3 + 2x + 5$

**3.** Reflect $f(x) = |x - 4|$ over the $y$-axis. Where's the vertex?

> [!check]- Answer
> $|-x - 4| = |x + 4|$. Vertex $(-4, 0)$ - the old vertex $(4, 0)$ flipped across the $y$-axis.

**4.** Reflect $f(x) = \sqrt{x} + 1$ over the $x$-axis.

> [!check]- Answer
> $-\sqrt{x} - 1$ - both terms get negated.

---

## 4. Even, Odd, or Neither

Some graphs are their own reflection.

| Type | Test | Symmetry | Matching points |
|---|---|---|---|
| **Even** | $f(-x) = f(x)$ | mirror image across the $y$-axis | $(x, y)$ and $(-x, y)$ |
| **Odd** | $f(-x) = -f(x)$ | unchanged by a half-turn about the origin | $(x, y)$ and $(-x, -y)$ |
| **Neither** | neither test works | neither | - |

> [!abstract] Testing an equation
> 1. Find $f(-x)$: replace every $x$ with $(-x)$ and simplify.
> 2. If it's identical to $f(x)$: **even**.
> 3. If it's identical to $-f(x)$ (every sign flipped): **odd**.
> 4. Otherwise: **neither**.

Remember: $(-x)^{\text{even}} = x^{\text{even}}$ and $(-x)^{\text{odd}} = -x^{\text{odd}}$.

> [!example] $f(x) = 3x^4 - 2x^2 + 7$
> $f(-x) = 3x^4 - 2x^2 + 7 = f(x)$. **Even.**

> [!example] $f(x) = x^5 - 4x^3$
> $f(-x) = -x^5 + 4x^3 = -(x^5 - 4x^3) = -f(x)$. **Odd.**

> [!example] $f(x) = x^2 + x$
> $f(-x) = x^2 - x$. Not $f(x)$. And $-f(x) = -x^2 - x$, which isn't it either. **Neither.**

> [!tip] Shortcut for polynomials
> All even powers (constants count as even, $x^0$) → even. All odd powers with no constant → odd. A mix → neither.
> Careful: "odd" and "even" functions aren't opposites. Most functions are neither.

### Practice

**1.** $f(x) = 5x^3 + x$

> [!check]- Answer
> Odd - only odd powers.

**2.** $f(x) = x^4 + x^3$

> [!check]- Answer
> Neither - a mix.

**3.** $f(x) = -6x^2 + 1$

> [!check]- Answer
> Even

**4.** $f(x) = \frac{3}{x^3}$

> [!check]- Answer
> $f(-x) = \frac{3}{-x^3} = -\frac{3}{x^3} = -f(x)$. Odd.

**5.** $f(x) = |x|$

> [!check]- Answer
> $|-x| = |x|$. Even.

---

## 5. Vertical Stretches and Compressions

Multiplying the **output** by $a > 0$, as in $g(x) = a \cdot f(x)$, multiplies every $y$-value by $a$.
- $a > 1$: **vertical stretch** - taller, steeper, pulled away from the $x$-axis.
- $0 < a < 1$: **vertical compression** - flatter, squashed toward the $x$-axis.
- $a < 0$: a stretch or compression **plus** a reflection over the $x$-axis.

Points on the $x$-axis ($y = 0$) don't move, since $a \cdot 0 = 0$.

> [!example] $g(x) = 3x^2$
> $(1, 1) \to (1, 3)$ and $(2, 4) \to (2, 12)$. Stretched by a factor of 3.

> [!example] $g(x) = \frac{1}{2}|x|$
> $(2, 2) \to (2, 1)$ and $(4, 4) \to (4, 2)$. Compressed by a factor of $\frac{1}{2}$.

### Finding $a$ from a point

Substitute a point from the new graph into $g(x) = a \cdot f(x)$ and solve.

> [!example] $x^3$ is compressed and passes through $(2, 4)$
> $4 = a(2)^3 = 8a$, so $a = \frac{1}{2}$.

### Practice

**1.** Describe $g(x) = 5\sqrt{x}$.

> [!check]- Answer
> Vertical stretch by a factor of 5.

**2.** Describe $g(x) = 0.2x^2$.

> [!check]- Answer
> Vertical compression by a factor of 0.2.

**3.** $x^2$ is stretched and passes through $(3, 18)$. Find $a$.

> [!check]- Answer
> $18 = 9a$, so $a = 2$.

**4.** $|x|$ is compressed and passes through $(6, 2)$. Find $a$.

> [!check]- Answer
> $2 = 6a$, so $a = \frac{1}{3}$.

**5.** Describe $g(x) = -2x^2$.

> [!check]- Answer
> Vertical stretch by a factor of 2 and a reflection over the $x$-axis.

---

## 6. Horizontal Stretches and Compressions

Multiplying the **input** by $b > 0$, as in $g(x) = f(bx)$, squeezes or stretches the graph sideways - and once again it works backwards:
- $b > 1$: **horizontal compression** by a factor of $b$ (narrower, pulled toward the $y$-axis).
- $0 < b < 1$: **horizontal stretch** by a factor of $b$ (wider, pushed away from the $y$-axis).

**Why backwards?** To get the same output, $bx$ has to reach the old input. With $b = 3$, $g$ gets there at one-third of the old $x$. Every point's $x$-coordinate is **divided** by $b$:

$$(p, q) \text{ on } f \quad\longrightarrow\quad \left(\frac{p}{b}, q\right) \text{ on } f(bx)$$

> [!example] $g(x) = (3x)^2$
> $(3, 9)$ on $x^2$ becomes $\left(\frac{3}{3}, 9\right) = (1, 9)$. Compressed horizontally by a factor of 3.

> [!example] $g(x) = \left(\frac{1}{4}x\right)^2$
> $(1, 1)$ becomes $\left(\frac{1}{1/4}, 1\right) = (4, 1)$. Stretched horizontally by a factor of $\frac{1}{4}$.

### Finding $b$ from matching points

$$b = \frac{\text{original } x}{\text{new } x}$$

> [!example] A point $(6, 2)$ on $s(x)$ moves to $(2, 2)$ on $f(x) = s(bx)$
> $b = \frac{6}{2} = 3$.

> [!warning] Don't mix up the two kinds of stretch
> $3f(x)$ is three times as **tall**. $f(3x)$ is one-third as **wide**. For parabolas they can look alike ($(3x)^2 = 9x^2$), but for most functions they're different.

### Practice

**1.** Describe $g(x) = \sqrt{4x}$.

> [!check]- Answer
> Horizontal compression by a factor of 4. $(4, 2)$ moves to $(1, 2)$.

**2.** The point $(2, 5)$ on $s(x)$ moves to $(10, 5)$ on $f(x) = s(bx)$. Find $b$.

> [!check]- Answer
> $b = \frac{2}{10} = \frac{1}{5}$ - a horizontal stretch.

**3.** For $g(x) = f(2x)$, where does the point $(4, 16)$ on $f$ go?

> [!check]- Answer
> $(2, 16)$

---

## 7. Putting Transformations in Order

Most problems combine several transformations. The general form is

$$g(x) = a \cdot f(x - h) + k$$

> [!abstract] The order
> - **Inside (horizontal):** reflect (if $-x$), then shift by $h$.
> - **Outside (vertical):** stretch or compress by $a$, reflect (if $a < 0$), **then** shift by $k$.
> - Horizontal and vertical steps don't affect each other, so do either group first.

Why stretch before shifting vertically? Order of operations. In $2f(x) + 3$, the output is multiplied by 2 **then** has 3 added. Shifting first would mean $2(f(x) + 3) = 2f(x) + 6$ - a different graph.

> [!example] $g(x) = 2(x + 3)^2 - 5$
> Left 3, stretch vertically by 2, down 5. Vertex $(-3, -5)$, and it's narrower than $x^2$.

> [!example] $g(x) = -\sqrt{4 - x} + 3$
> Rewrite the inside: $4 - x = -(x - 4)$. So: reflect over the $y$-axis, shift right 4. Then reflect over the $x$-axis, shift up 3. It starts at $(4, 3)$ and runs to the left, going down.

### Writing the equation from a vertex and a point

1. Use the key point $(h, k)$ to write $g(x) = a \cdot f(x - h) + k$.
2. Substitute another point on the graph and solve for $a$.

> [!example] A parabola has vertex $(1, -2)$ and passes through $(3, 6)$
> $g(x) = a(x - 1)^2 - 2$. Then $6 = a(2)^2 - 2$, so $8 = 4a$ and $a = 2$.
> $$g(x) = 2(x - 1)^2 - 2$$

### Practice

**1.** Describe $g(x) = 4\sqrt{x - 2} - 1$.

> [!check]- Answer
> Right 2, stretch vertically by 4, down 1. Starts at $(2, -1)$.

**2.** A V-shape ($|x|$) has vertex $(3, 1)$ and passes through $(5, 7)$. Write it.

> [!check]- Answer
> $7 = a|5 - 3| + 1 = 2a + 1$, so $a = 3$: $g(x) = 3|x - 3| + 1$

**3.** A cubic ($x^3$) has center $(2, -1)$ and passes through $(3, 1)$. Write it.

> [!check]- Answer
> $1 = a(1)^3 - 1$, so $a = 2$: $g(x) = 2(x - 2)^3 - 1$

**4.** Describe $g(x) = -|5 - x| + 4$.

> [!check]- Answer
> Reflect over the $y$-axis and shift right 5; reflect over the $x$-axis and shift up 4. Vertex $(5, 4)$, opening down.

---

## 8. Following a Point Through a Transformation

To find where a point $(p, q)$ on $f$ lands on $g(x) = a \cdot f(\pm x - h) + k$, apply the steps in order. **Horizontal steps change only $x$. Vertical steps change only $y$.**

> [!example] $(9, 3)$ is on $\sqrt{x}$. Where does it go on $y = 2\sqrt{x - 4} - 1$?
> - Right 4: $(13, 3)$
> - Stretch by 2: $(13, 6)$
> - Down 1: $(13, 5)$

> [!tip] A quick check
> Plug the new $x$ in: $2\sqrt{13 - 4} - 1 = 2(3) - 1 = 5$ ✓

### Practice

**1.** $(3, 9)$ is on $x^2$. Where does it go on $y = -(x + 1)^2 + 2$?

> [!check]- Answer
> Left 1: $(2, 9)$. Reflect over the $x$-axis: $(2, -9)$. Up 2: $(2, -7)$.

**2.** $(8, 2)$ is on $\sqrt[3]{x}$. Where does it go on $y = 3\sqrt[3]{x + 8} - 5$?

> [!check]- Answer
> $(0, 2) \to (0, 6) \to (0, 1)$

**3.** $(4, 2)$ is on $\sqrt{x}$. Where does it go on $y = \sqrt{-x} + 6$?

> [!check]- Answer
> Reflect over the $y$-axis: $(-4, 2)$. Up 6: $(-4, 8)$.

**4.** $(-2, -8)$ is on $x^3$. Where does it go on $y = \frac{1}{2}(x - 3)^3 + 4$?

> [!check]- Answer
> $(1, -8) \to (1, -4) \to (1, 0)$

---

## 9. Domain and Range After a Transformation

The domain is about $x$, so only **horizontal** changes (inside) affect it. The range is about $y$, so only **vertical** changes (outside) affect it.

> [!abstract] The method
> - **Domain:** apply the inside reflection and shift to each endpoint (or excluded value). Ignore $a$ and $k$.
> - **Range:** apply the outside stretch, reflection, and shift to each endpoint, **in order**: multiply by $a$, then add $k$. If $a$ is negative, the interval flips direction.

> [!example] The domain of $f$ is $[2, \infty)$
> - $f(x + 5)$: left 5, so $[-3, \infty)$.
> - $f(-x)$: reflected, so $(-\infty, -2]$.

> [!example] The domain of $f$ is $(-\infty, 0) \cup (0, \infty)$. Find the domain of $f(x + 3) - 7$.
> The excluded value moves left 3: $(-\infty, -3) \cup (-3, \infty)$. The $-7$ doesn't matter.

> [!example] The range of $f$ is $[-1, \infty)$
> - $2f(x) + 5$: $2(-1) + 5 = 3$, so $[3, \infty)$.
> - $-f(x)$: flips to $(-\infty, 1]$.
> - $-f(x) + 4$: flip to $(-\infty, 1]$, then up 4: $(-\infty, 5]$.

> [!warning] Don't skip the stretch
> For the range of $a \cdot f(x) + k$, both $a$ and $k$ matter. With range $[-1, \infty)$, $2f(x) + 5$ starts at $3$, not $4$.

### Practice

**1.** The domain of $f$ is $(-\infty, 4]$. Domain of $f(x - 6)$?

> [!check]- Answer
> $(-\infty, 10]$

**2.** The domain of $f$ is $[1, \infty)$. Domain of $2f(x + 1) - 3$?

> [!check]- Answer
> $[0, \infty)$ - only the $+1$ inside matters.

**3.** The range of $f$ is $[3, \infty)$. Range of $f(x - 8)$?

> [!check]- Answer
> $[3, \infty)$ - a horizontal shift doesn't change the range.

**4.** The range of $f$ is $[2, \infty)$. Range of $4f(x) - 1$?

> [!check]- Answer
> $4(2) - 1 = 7$: $[7, \infty)$

**5.** The range of $f$ is $(-\infty, 5]$. Range of $-2f(x) + 1$?

> [!check]- Answer
> $-2(5) + 1 = -9$, and the negative flips the direction: $[-9, \infty)$

---

## Module Review Quiz

**1.** Describe $g(x) = (x + 4)^3 - 2$.

> [!check]- Answer
> Left 4, down 2. Center $(-4, -2)$.

**2.** $\sqrt{x}$ is moved to start at $(3, 5)$. Write it.

> [!check]- Answer
> $\sqrt{x - 3} + 5$

**3.** Reflect $f(x) = 2x^2 - x + 6$ over the $y$-axis, then over the $x$-axis (separately).

> [!check]- Answer
> $y$-axis: $2x^2 + x + 6$. $x$-axis: $-2x^2 + x - 6$.

**4.** Even, odd, or neither: $f(x) = x^3 - x^2$?

> [!check]- Answer
> Neither - a mix of odd and even powers.

**5.** Even, odd, or neither: $f(x) = 7x - x^5$?

> [!check]- Answer
> Odd

**6.** $|x|$ is compressed vertically and passes through $(8, 2)$. Find the factor.

> [!check]- Answer
> $2 = 8a$, $a = \frac{1}{4}$

**7.** The point $(9, 3)$ on $s(x)$ moves to $(3, 3)$ on $s(bx)$. Find $b$ and describe it.

> [!check]- Answer
> $b = 3$: horizontal compression by a factor of 3.

**8.** A parabola has vertex $(-2, 3)$ and passes through $(0, -5)$. Write it.

> [!check]- Answer
> $-5 = a(2)^2 + 3$, so $a = -2$: $g(x) = -2(x + 2)^2 + 3$

**9.** $(1, 1)$ is on $x^3$. Where does it go on $y = -3(x - 2)^3 + 4$?

> [!check]- Answer
> $(3, 1) \to (3, -3) \to (3, 1)$

**10.** The range of $f$ is $[0, \infty)$. Range of $-3f(x) + 2$?

> [!check]- Answer
> $(-\infty, 2]$

