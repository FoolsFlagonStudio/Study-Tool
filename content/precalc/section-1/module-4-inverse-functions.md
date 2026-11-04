---
title: Inverse Functions
section: 1 - Foundations of Algebra and Functions
module: 4
status: draft
topics: [one-to-one-functions, inverse-from-table, inverse-domain-range, verifying-inverses, finding-inverses, inverse-applications, composing-inverses]
---

# Module 4: Inverse Functions

**By the end of this module you can:** tell whether a function is one-to-one, find an inverse from a table, a graph, or a formula, check whether two functions are inverses, and use inverses to answer "what input gave this output?" questions.

> [!info] Why this matters
> A function answers "if I put this in, what comes out?" An inverse answers the opposite question: "this came out - what went in?" That's the question behind converting °F back to °C, working out how many months a bill covers, or decoding a message. Inverses come back constantly, especially with exponential and logarithmic functions later in the course.

---

## 1. One-to-One Functions

Think about student ID numbers. Every student gets one ID, and no two students share an ID. Given a student you can find their ID, and given an ID you can find the student - the pairing works in both directions.

Compare that with birthdays. Every person has one birthday, but plenty of people share the same one. Given a person you can find their birthday, but given a birthday ("March 3") you can't tell which person you mean.

Both are functions. Only the first is **one-to-one**.

> [!abstract] Definition
> A function is **one-to-one** (1-1) if every output comes from exactly one input. No two different inputs share an output.

| | Each input has one output | Each output has one input |
|---|---|---|
| Function | ✓ | not required |
| One-to-one function | ✓ | ✓ |

### Testing a formula

The algebra version of the definition: a function is one-to-one if
$$f(a) = f(b) \text{ always forces } a = b$$
In words: if two inputs give the same output, they must have been the same input.

> [!example] Is $f(x) = 2x + 9$ one-to-one?
> Suppose $f(a) = f(b)$:
> $$2a + 9 = 2b + 9 \;\Rightarrow\; 2a = 2b \;\Rightarrow\; a = b$$
> It's forced, so **yes**, one-to-one.

> [!example] Is $h(x) = x^2 + 1$ one-to-one?
> Suppose $h(a) = h(b)$:
> $$a^2 + 1 = b^2 + 1 \;\Rightarrow\; a^2 = b^2 \;\Rightarrow\; a = \pm b$$
> That allows $a = -b$, so **no**. Proof with numbers: $h(3) = 10$ and $h(-3) = 10$.

> [!tip] The fastest way to say "no"
> To prove a function is **not** one-to-one, you only need one pair of different inputs with the same output. $|5| = |-5|$ is enough to show $|x|$ isn't one-to-one.

> [!warning] Even powers and absolute values hide the sign
> $x^2$, $x^4$, $|x|$ - anything that makes a negative input look like a positive one - breaks one-to-one. Odd powers ($x^3$, $x^5$), roots, and $\frac{1}{x}$ keep inputs separate.
> **Restricting the domain fixes it:** $f(x) = x^2$ for $x \geq 0$ only is one-to-one, because the negative inputs are gone.

### The Horizontal Line Test

On a graph, a horizontal line is "one output." If a horizontal line hits the graph twice, two inputs share that output.

> [!abstract] Horizontal Line Test
> If **no** horizontal line crosses the graph more than once, the function is one-to-one.

| Graph | Vertical line test | Horizontal line test | Verdict |
|---|---|---|---|
| Straight, slanted line | passes | passes | one-to-one function |
| Parabola $y = x^2$ | passes | **fails** ($y = 4$ hits at $x = \pm 2$) | function, not 1-1 |
| V-shape $y = \lvert x\rvert$ | passes | **fails** | function, not 1-1 |
| S-curve $y = x^3$ | passes | passes | one-to-one function |
| Half-parabola $y = \sqrt{x}$ | passes | passes | one-to-one function |
| Sideways parabola $x = y^2$ | **fails** | passes | not a function |

To be a one-to-one function, a graph has to pass **both** tests.

### Practice

**1.** Is $f(x) = 4 - 7x$ one-to-one?

> [!check]- Answer
> Yes. $4 - 7a = 4 - 7b$ forces $a = b$. (Every non-horizontal line is one-to-one.)

**2.** Is $f(x) = x^4$ one-to-one?

> [!check]- Answer
> No. $f(2) = f(-2) = 16$.

**3.** Is $f(x) = x^3 + 2$ one-to-one?

> [!check]- Answer
> Yes. $a^3 + 2 = b^3 + 2$ gives $a^3 = b^3$, and cube roots have one value, so $a = b$.

**4.** Is $f(x) = x^2 - 6x$ one-to-one?

> [!check]- Answer
> No. $f(0) = 0$ and $f(6) = 0$.

**5.** Is $\{(1, 4), (2, 9), (3, 4), (5, 0)\}$ a one-to-one function?

> [!check]- Answer
> No - it's a function, but the output 4 comes from both 1 and 3.

**6.** Is $f(x) = x^2$ with domain $x \geq 0$ one-to-one?

> [!check]- Answer
> Yes. With only non-negative inputs, no two inputs share an output.

---

## 2. What an Inverse Is

If a function is one-to-one, you can run it backward. The backward function is the **inverse**, written $f^{-1}(x)$ (read "f inverse of x").

$$f(a) = b \quad\Longleftrightarrow\quad f^{-1}(b) = a$$

The inverse swaps every input with its output.

> [!example] A secret code
> A code shifts every number up by 3: $f(x) = x + 3$. The message 7 becomes 10.
> To decode, shift back down: $f^{-1}(x) = x - 3$, and $f^{-1}(10) = 7$.
> The inverse undoes exactly what the function did.

> [!warning] $f^{-1}$ is not $\frac{1}{f}$
> The $-1$ is just a label meaning "inverse," not an exponent.
> If $f(x) = x + 3$, then $f^{-1}(x) = x - 3$, but $\frac{1}{f(x)} = \frac{1}{x + 3}$. Completely different.

> [!note] Why it has to be one-to-one
> If two inputs share an output - like $h(3) = h(-3) = 10$ for $h(x) = x^2 + 1$ - then "$h^{-1}(10)$" would have two answers, and a function can't do that. So **only one-to-one functions have inverses.**

### Inverses from a table

Flip each pair: the input row becomes the output row.

> [!example] Make the inverse table
>
> | $x$ | $-2$ | 0 | 3 | 7 |
> |---|---|---|---|---|
> | $f(x)$ | 5 | 1 | $-4$ | 10 |
>
> Every input appears once and every output appears once, so $f$ is one-to-one. Swap the rows:
>
> | $x$ | 5 | 1 | $-4$ | 10 |
> |---|---|---|---|---|
> | $f^{-1}(x)$ | $-2$ | 0 | 3 | 7 |
>
> So $f^{-1}(-4) = 3$: find $-4$ in the **output** row of $f$, and read the input above it.

### Domain and range swap too

Since inputs and outputs trade places:
- the **domain** of $f^{-1}$ is the **range** of $f$
- the **range** of $f^{-1}$ is the **domain** of $f$

> [!example] Domain and range
> $f$ is graphed from $(-1, 0)$ to $(8, 3)$, always rising. Its domain is $[-1, 8]$ and its range is $[0, 3]$.
> So $f^{-1}$ has domain $[0, 3]$ and range $[-1, 8]$.

### Graphs of inverses

Every point $(a, b)$ on $f$ becomes $(b, a)$ on $f^{-1}$. Swapping coordinates is the same as reflecting over the diagonal line $y = x$.

> [!abstract] Graph rule
> The graph of $f^{-1}$ is the graph of $f$ **flipped over the line $y = x$**.

> [!example] $f(x) = 2x + 1$
> Points on $f$: $(0, 1)$, $(1, 3)$, $(2, 5)$.
> Points on $f^{-1}$: $(1, 0)$, $(3, 1)$, $(5, 2)$.
> $f$ is a steep line; its inverse is a shallower line. Plot both and they mirror each other across $y = x$.

> [!tip] Spotting the right inverse graph
> A steep graph has a shallow inverse, and the other way around. If a choice isn't a mirror image across $y = x$, it's wrong - for example, a reflection over the $x$-axis or $y$-axis is a different transformation.

### Practice

Use this table for 1-3:

| $x$ | 1 | 4 | 6 | 10 | 12 |
|---|---|---|---|---|---|
| $g(x)$ | 8 | $-3$ | 0 | 5 | 2 |

**1.** Find $g^{-1}(5)$.

> [!check]- Answer
> $10$ - find 5 in the output row; its input is 10.

**2.** Find $g^{-1}(-3)$.

> [!check]- Answer
> $4$

**3.** What is $g^{-1}(1)$?

> [!check]- Answer
> Trick question - 1 isn't an output of $g$, so it isn't in the domain of $g^{-1}$. $g^{-1}(1)$ is undefined. (Careful: $g(1) = 8$, but that's the wrong direction.)

**4.** $(4, -9)$ is on the graph of a one-to-one function $f$. What point is on the graph of $f^{-1}$?

> [!check]- Answer
> $(-9, 4)$

**5.** $f$ has domain $[-3, 2]$ and range $[-27, 8]$. What are the domain and range of $f^{-1}$?

> [!check]- Answer
> Domain $[-27, 8]$, range $[-3, 2]$.

---

## 3. Checking Whether Two Functions Are Inverses

Inverses undo each other, **in reverse order**. Think about wrapping a gift: first you put it in the box, then you wrap the box. To get the gift out, you unwrap first, then open the box. The last thing done is the first thing undone.

So if you run $f$ and then $f^{-1}$ (or the other way around), you end up back where you started:

> [!abstract] The inverse test
> $f$ and $g$ are inverses if **both**
> $$f(g(x)) = x \quad\text{and}\quad g(f(x)) = x$$

> [!example] Are $f(x) = 5x - 4$ and $g(x) = \dfrac{x + 4}{5}$ inverses?
> $$f(g(x)) = 5\left(\frac{x+4}{5}\right) - 4 = x + 4 - 4 = x \;✓$$
> $$g(f(x)) = \frac{(5x - 4) + 4}{5} = \frac{5x}{5} = x \;✓$$
> Both simplify to $x$, so **yes**.

> [!example] Are $f(x) = 5x - 4$ and $g(x) = \dfrac{x - 4}{5}$ inverses?
> $$f(g(x)) = 5\left(\frac{x-4}{5}\right) - 4 = x - 8$$
> Not $x$, so **no**. You can stop as soon as one composition fails.

> [!tip] Quick check with one number
> Pick an easy input and run it through both. $f(2) = 6$, and the real inverse must send 6 back to 2. $\frac{6 + 4}{5} = 2$ ✓ but $\frac{6 - 4}{5} = 0.4$ ✗. A number check can prove two functions are **not** inverses. To prove they **are**, do the full composition.

> [!tip] Shortcut
> If you know $f$ and $g$ are inverses, then $f(g(\text{anything}))$ is just that anything. $f(g(37)) = 37$ - no arithmetic needed.

### Practice

**1.** Are $f(x) = 2x + 6$ and $g(x) = \frac{x}{2} - 3$ inverses?

> [!check]- Answer
> Yes. $f(g(x)) = 2\left(\frac{x}{2} - 3\right) + 6 = x$, and $g(f(x)) = \frac{2x + 6}{2} - 3 = x$.

**2.** Are $f(x) = 9x - 1$ and $g(x) = \frac{x - 1}{9}$ inverses?

> [!check]- Answer
> No. $f(g(x)) = x - 1 - 1 = x - 2$.

**3.** Are $f(x) = (x + 3)^3$ and $g(x) = \sqrt[3]{x} - 3$ inverses?

> [!check]- Answer
> Yes. $f(g(x)) = (\sqrt[3]{x})^3 = x$, and $g(f(x)) = (x + 3) - 3 = x$.

**4.** Are $f(x) = x^3 + 1$ and $g(x) = \sqrt[3]{x + 1}$ inverses?

> [!check]- Answer
> No. $f(g(x)) = (x + 1) + 1 = x + 2$. The real inverse is $\sqrt[3]{x - 1}$.

**5.** $f$ and $g$ are inverses. What is $g(f(-12))$?

> [!check]- Answer
> $-12$

---

## 4. Finding an Inverse from a Formula

A table only gives a few points of the inverse. To get the whole inverse, find its formula.

> [!abstract] The swap-and-solve method
> 1. Write $y$ instead of $f(x)$.
> 2. **Swap** $x$ and $y$ everywhere.
> 3. **Solve** for $y$.
> 4. Write $f^{-1}(x)$ instead of $y$.
> 5. *(Optional)* Check: $f(f^{-1}(x))$ should simplify to $x$.

> [!tip] Undo in reverse order
> The swap-and-solve method follows the gift-wrapping idea. In $f(x) = 3x + 8$, the function multiplies by 3, **then** adds 8. The inverse subtracts 8, **then** divides by 3: $f^{-1}(x) = \frac{x - 8}{3}$.

### Linear functions

> [!example] $f(x) = 3x + 8$
> $y = 3x + 8$
> Swap: $x = 3y + 8$
> Solve: $x - 8 = 3y \;\Rightarrow\; y = \dfrac{x - 8}{3}$
> $$f^{-1}(x) = \frac{x - 8}{3}$$

> [!example] $f(x) = 10 - 2x$
> Swap: $x = 10 - 2y$
> Solve: $2y = 10 - x \;\Rightarrow\; y = \dfrac{10 - x}{2}$
> $$f^{-1}(x) = \frac{10 - x}{2}$$

> [!example] $f(x) = \dfrac{x}{4} + 1$
> Swap: $x = \dfrac{y}{4} + 1$
> Solve: $x - 1 = \dfrac{y}{4} \;\Rightarrow\; y = 4(x - 1)$
> $$f^{-1}(x) = 4(x - 1) = 4x - 4$$

### Cubic functions

The only new step is undoing a cube with a cube root.

> [!example] $f(x) = (x - 4)^3 + 6$
> Swap: $x = (y - 4)^3 + 6$
> Solve:
> $$x - 6 = (y - 4)^3 \;\Rightarrow\; \sqrt[3]{x - 6} = y - 4 \;\Rightarrow\; y = \sqrt[3]{x - 6} + 4$$
> $$f^{-1}(x) = \sqrt[3]{x - 6} + 4$$
> Notice every sign flipped and the operations reversed: $f$ subtracts 4, cubes, adds 6. $f^{-1}$ subtracts 6, takes the cube root, adds 4.

> [!example] $f(x) = 2x^3 + 5$
> Swap: $x = 2y^3 + 5$
> Solve: $x - 5 = 2y^3 \;\Rightarrow\; \dfrac{x - 5}{2} = y^3 \;\Rightarrow\; y = \sqrt[3]{\dfrac{x - 5}{2}}$
> $$f^{-1}(x) = \sqrt[3]{\frac{x - 5}{2}}$$

### Rational functions

For $f(x) = \dfrac{a}{x - b}$, clear the fraction by multiplying, then gather the $y$ terms.

> [!example] $f(x) = \dfrac{6}{x + 1}$
> Swap: $x = \dfrac{6}{y + 1}$
> Multiply both sides by $(y + 1)$: $x(y + 1) = 6$
> Distribute: $xy + x = 6$
> Isolate the $y$ term: $xy = 6 - x$
> Divide by $x$:
> $$f^{-1}(x) = \frac{6 - x}{x}$$

> [!tip] Rational pattern
> For $f(x) = \dfrac{a}{x - b}$, the inverse is always $f^{-1}(x) = \dfrac{a + bx}{x}$. Check it against the example: $a = 6$, $b = -1$ gives $\frac{6 - x}{x}$ ✓.

> [!note] Bonus: a function that is its own inverse
> $f(x) = \dfrac{x}{x - 1}$. Swap: $x = \dfrac{y}{y - 1}$, so $xy - x = y$, so $y(x - 1) = x$, so $y = \dfrac{x}{x - 1}$. The inverse is the same function! Its graph is perfectly symmetric about $y = x$.

> [!warning] Common mistakes
> - **Forgetting to swap**, then solving $y = 3x + 8$ for $x$ and stopping. You get the right expression but in the wrong letter - always finish with the answer in terms of $x$.
> - **Undoing in the wrong order**, e.g. $f(x) = 3x + 8 \Rightarrow \frac{x}{3} - 8$. Divide first and you only subtract $\frac{8}{3}$, not 8. Compare: $\frac{x - 8}{3} = \frac{x}{3} - \frac{8}{3}$.
> - **Writing the reciprocal**: $\frac{1}{3x + 8}$ is $\frac{1}{f(x)}$, not $f^{-1}(x)$.
> - **Sign slips with cube roots**: the inverse of $(x - 4)^3 + 6$ has $x - 6$ inside the root and $+4$ outside.

### Practice

**1.** $f(x) = 7x - 2$

> [!check]- Answer
> $f^{-1}(x) = \dfrac{x + 2}{7}$

**2.** $f(x) = 12 - 3x$

> [!check]- Answer
> $f^{-1}(x) = \dfrac{12 - x}{3}$

**3.** $f(x) = \frac{2}{5}x + 4$

> [!check]- Answer
> $x - 4 = \frac{2}{5}y \Rightarrow f^{-1}(x) = \frac{5}{2}(x - 4) = \frac{5x - 20}{2}$

**4.** $f(x) = (x + 3)^3$

> [!check]- Answer
> $f^{-1}(x) = \sqrt[3]{x} - 3$

**5.** $f(x) = 1 - x^3$

> [!check]- Answer
> $x = 1 - y^3 \Rightarrow y^3 = 1 - x \Rightarrow f^{-1}(x) = \sqrt[3]{1 - x}$

**6.** $f(x) = \dfrac{4}{x - 2}$

> [!check]- Answer
> $f^{-1}(x) = \dfrac{4 + 2x}{x}$

**7.** $f(x) = \dfrac{7}{x + 3}$

> [!check]- Answer
> $f^{-1}(x) = \dfrac{7 - 3x}{x}$

**8.** $f(x) = \dfrac{-2}{x - 4}$

> [!check]- Answer
> $f^{-1}(x) = \dfrac{-2 + 4x}{x} = \dfrac{4x - 2}{x}$

---

## 5. Using Inverses to Answer Real Questions

A linear model usually goes "input → output": months → total cost, miles → fare. Word problems often give you the **output** and ask for the input. That's exactly what the inverse does.

> [!abstract] Method
> 1. Write the model $f(x)$.
> 2. Find $f^{-1}(x)$.
> 3. Plug the known output into $f^{-1}$.

(For a single question you could also just set $f(x)$ equal to the number and solve - same arithmetic. The inverse is worth it when you need to answer the question repeatedly.)

> [!example] Fahrenheit to Celsius
> Celsius to Fahrenheit is $f(x) = \frac{9}{5}x + 32$. What is 212°F in Celsius?
> Swap and solve: $x = \frac{9}{5}y + 32 \Rightarrow x - 32 = \frac{9}{5}y \Rightarrow y = \frac{5}{9}(x - 32)$
> $$f^{-1}(212) = \frac{5}{9}(212 - 32) = \frac{5}{9}(180) = 100°\text{C}$$
> (Water boils at 100°C - a good check.)

> [!example] Taxi fare
> A taxi charges \$3 plus \$2.50 per mile: $f(m) = 3 + 2.5m$. A ride cost \$28. How far was it?
> $f^{-1}(x) = \dfrac{x - 3}{2.5}$, and $f^{-1}(28) = \dfrac{25}{2.5} = 10$ miles.

> [!example] Draining a tank
> A 500-gallon tank drains 12 gallons per minute: $V(t) = 500 - 12t$. How long until 140 gallons are left?
> $V^{-1}(x) = \dfrac{500 - x}{12}$, and $V^{-1}(140) = \dfrac{360}{12} = 30$ minutes.

### Practice

**1.** You have \$250 saved and add \$40 per week: $S(w) = 250 + 40w$. After how many weeks will you have \$650?

> [!check]- Answer
> $S^{-1}(x) = \dfrac{x - 250}{40}$, and $S^{-1}(650) = 10$ weeks.

**2.** A streaming service charges a \$15 signup fee plus \$12 per month. Someone has paid \$111 total. How many months?

> [!check]- Answer
> $f(x) = 15 + 12x$, $f^{-1}(x) = \dfrac{x - 15}{12}$, $f^{-1}(111) = 8$ months.

**3.** A laptop bought for \$1,800 loses \$300 of value per year. How old is it when it's worth \$600?

> [!check]- Answer
> $f(x) = 1800 - 300x$, $f^{-1}(x) = \dfrac{1800 - x}{300}$, $f^{-1}(600) = 4$ years.

**4.** Convert 77°F to Celsius.

> [!check]- Answer
> $\frac{5}{9}(77 - 32) = \frac{5}{9}(45) = 25°$C

---

## 6. Composing Inverses

Composing inverses works like any composition: inside first. To evaluate an inverse from a table or a set of points, look up the value among the **outputs** and read off the input.

$g$ passes through $(-4, 1)$, $(0, 3)$, $(2, 6)$, $(5, -2)$.

| $x$ | 1 | 3 | 4 | 6 | 8 |
|---|---|---|---|---|---|
| $f(x)$ | 6 | $-4$ | 2 | 0 | 5 |

> [!example] Find $(f^{-1} \circ g^{-1})(6)$, which means $f^{-1}(g^{-1}(6))$
> Inner: $g^{-1}(6)$. The point $(2, 6)$ is on $g$, so $g^{-1}(6) = 2$.
> Outer: $f^{-1}(2)$. The table has $f(4) = 2$, so $f^{-1}(2) = 4$.
> Answer: $4$.

> [!warning] Common mistake
> Using $f$ instead of $f^{-1}$. $f(2) = $ nothing in this table, but $f^{-1}(2) = 4$. Always search the **output** row when the function has a $-1$.

### Practice

**1.** $(f^{-1} \circ g^{-1})(1)$

> [!check]- Answer
> $g^{-1}(1) = -4$. Is $-4$ an output of $f$? Yes: $f(3) = -4$, so $f^{-1}(-4) = 3$. Answer: $3$.

**2.** $(g^{-1} \circ f^{-1})(0)$

> [!check]- Answer
> $f^{-1}(0) = 6$, then $g^{-1}(6) = 2$. Answer: $2$.

**3.** $(g^{-1} \circ f^{-1})(6)$

> [!check]- Answer
> $f^{-1}(6) = 1$, then $g^{-1}(1) = -4$. Answer: $-4$.

**4.** $(f^{-1} \circ g^{-1})(3)$

> [!check]- Answer
> $g^{-1}(3) = 0$. Is 0 an output of $f$? Yes: $f(6) = 0$. Answer: $6$.

---

## Module Review Quiz

**1.** Is $f(x) = x^2 + 4x$ one-to-one?

> [!check]- Answer
> No. $f(0) = 0$ and $f(-4) = 0$.

**2.** $(-6, 11)$ is on the graph of a one-to-one $f$. Name a point on $f^{-1}$.

> [!check]- Answer
> $(11, -6)$

**3.** $f$ has domain $[0, 9]$ and range $[2, 5]$. What is the domain of $f^{-1}$?

> [!check]- Answer
> $[2, 5]$

**4.** Are $f(x) = 4x + 3$ and $g(x) = \frac{x - 3}{4}$ inverses?

> [!check]- Answer
> Yes. $f(g(x)) = x - 3 + 3 = x$ and $g(f(x)) = \frac{4x}{4} = x$.

**5.** Find the inverse of $f(x) = 8 - 5x$.

> [!check]- Answer
> $f^{-1}(x) = \dfrac{8 - x}{5}$

**6.** Find the inverse of $f(x) = (x - 2)^3 - 9$.

> [!check]- Answer
> $f^{-1}(x) = \sqrt[3]{x + 9} + 2$

**7.** Find the inverse of $f(x) = \dfrac{5}{x - 3}$.

> [!check]- Answer
> $f^{-1}(x) = \dfrac{5 + 3x}{x}$

**8.** A gym charges \$60 to join plus \$35 per month. Someone has paid \$410. How many months?

> [!check]- Answer
> $\dfrac{410 - 60}{35} = 10$ months
