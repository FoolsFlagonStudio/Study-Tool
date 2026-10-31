---
title: Functions and Composition
section: 1 - Foundations of Algebra and Functions
module: 3
status: draft
topics: [relations-domain-range, identifying-functions, function-notation, types-of-functions, asymptotes, evaluating-functions, function-composition, decomposing-functions, composition-models]
---

# Module 3: Functions and Composition

**By the end of this module you can:** tell whether a relation is a function, read and use function notation, recognize linear, quadratic, rational, and radical functions, evaluate functions at numbers and expressions, and chain functions together to model real situations.

> [!info] Why this matters
> Functions are the main character of precalculus - and of calculus after it. Everything from here on is about understanding how one quantity depends on another. This module is the foundation for all of it.

---

## 1. Relations, Domain, and Range

A **relation** is any pairing between two sets. The simplest way to write one is a list of **ordered pairs** $(x, y)$.

- **Domain** - all the first values ($x$'s), the inputs
- **Range** - all the second values ($y$'s), the outputs

List each value **once**, even if it appears in several pairs.

> [!example] $\{(0,4), (1,5), (2,6), (3,7)\}$
> - Domain: $\{0, 1, 2, 3\}$
> - Range: $\{4, 5, 6, 7\}$

> [!example] $\{(2,1), (4,1), (6,1), (4,8)\}$
> - Domain: $\{2, 4, 6\}$ (the $4$ appears twice but is listed once)
> - Range: $\{1, 8\}$

> [!tip] Set notation
> Braces $\{\ \}$ hold the members of a set. "..." means "keep the pattern going":
> $\{1, 2, 3, \ldots, 100\}$ is every whole number from 1 to 100; $\{5, 10, 15, \ldots\}$ is every multiple of 5.

---

## 2. What Makes a Relation a Function?

> [!abstract] Definition
> A **function** is a relation where **every input has exactly one output**.

The input is called the **independent variable** (you choose it). The output is the **dependent variable** (it depends on what you chose).

> [!tip] The vending machine test
> Picture a vending machine. Each button is an input; the snack that drops is the output.
> - Every button gives one specific snack → **function** ✓
> - Two different buttons give the same snack → still a **function** ✓ (that's allowed)
> - One button sometimes gives chips and sometimes gives candy → **not a function** ✗
>
> The rule is about the *inputs*: no input can be ambiguous. Outputs are allowed to repeat.

> [!example] Function or not?
> | Relation | Function? | Why |
> |---|---|---|
> | $\{(1,2), (2,4), (3,6)\}$ | Yes | each $x$ appears once |
> | $\{(2,1), (4,1), (6,1)\}$ | Yes | outputs repeat, but each input has one output |
> | $\{(1,2), (1,7), (3,4)\}$ | **No** | input $1$ has two outputs |

**Quick check for ordered pairs:** scan the $x$-values. If any $x$ repeats with a **different** $y$, it's not a function.

### Function notation

Instead of $y = 2x + 3$, we write $f(x) = 2x + 3$, read "**$f$ of $x$**."

- $f$ is the function's name. $g$, $h$, and anything else work too.
- $x$ is the input. $f(x)$ is the output.
- $f(x)$ **does not** mean $f$ times $x$. The parentheses hold the input, like a slot.

> [!tip] The function machine
> Think of $f(x) = 2x + 3$ as a machine. Drop in $x = 4$: it doubles it (8), adds 3, and $f(4) = 11$ comes out the other side.

### Practice

**1.** Give the domain and range of $\{(-1,3), (0,3), (2,5), (4,-1)\}$. Is it a function?

> [!check]- Answer
> Domain $\{-1, 0, 2, 4\}$, range $\{-1, 3, 5\}$. Yes - every input appears once.

**2.** Is $\{(3,1), (4,1), (5,2), (3,2)\}$ a function?

> [!check]- Answer
> No. Input $3$ goes to both $1$ and $2$.

**3.** Is $\{(-1,4), (0,4), (1,4)\}$ a function?

> [!check]- Answer
> Yes. Every input gives $4$ - repeated outputs are fine.

**4.** A mapping diagram shows $a \to 1$, $b \to 2$, $c \to 2$, $c \to 3$. Function?

> [!check]- Answer
> No. Input $c$ points to two outputs.

---

## 3. Is an Equation a Function?

For an equation, ask: **"If I pick an $x$, can I get more than one $y$?"** The cleanest way to find out is to solve for $y$.

> [!example] $4x - 2y = 8$
> $-2y = -4x + 8$
> $y = 2x - 4$
> One $y$ for every $x$ → **function**.

> [!example] $x^2 + y^2 = 25$
> $y^2 = 25 - x^2$
> $y = \pm\sqrt{25 - x^2}$
> At $x = 3$, $y$ could be $4$ **or** $-4$ → **not a function**. (This equation is a circle.)

> [!example] $y^3 = x + 1$
> $y = \sqrt[3]{x + 1}$
> A cube root has only **one** value, so → **function**.

> [!tip] Red flags
> - **$y$ to an even power** ($y^2$, $y^4$) → usually not a function, because solving introduces $\pm$
> - **$y$ to an odd power** ($y$, $y^3$, $y^5$) → fine
> - **Vertical lines** like $x = -2$ → never a function (one $x$, infinitely many $y$'s)
> - Even powers of $x$ are totally fine: $y = x^2$ is a function.

> [!tip] The Vertical Line Test
> On a graph: if **any** vertical line crosses the graph more than once, it's not a function. A vertical line is "one $x$-value," so crossing twice means that $x$ has two outputs.

### Practice

**1.** $y - x^2 = 3x$

> [!check]- Answer
> Function. $y = x^2 + 3x$.

**2.** $2y^2 = x + 8$

> [!check]- Answer
> Not a function. $y = \pm\sqrt{\frac{x + 8}{2}}$.

**3.** $x + y^5 = 1$

> [!check]- Answer
> Function. $y = \sqrt[5]{1 - x}$ - odd root, one value.

**4.** $3x + 4 = 2y - x$

> [!check]- Answer
> Function. $y = 2x + 2$.

**5.** $x = 7$

> [!check]- Answer
> Not a function - it's a vertical line.

---

## 4. Reading Function Notation in Context

In word problems, the letters usually stand for real things. The trick is always the same: **the value inside the parentheses is the input, and the value on the other side of the $=$ is the output.**

> [!example] $C(m)$ is the cost in dollars of a phone plan using $m$ GB of data. What does $C(10) = 55$ mean?
> Input $m = 10$ GB, output $C = 55$ dollars.
> **Using 10 GB of data costs \$55.**

> [!example] $T(h)$ is the temperature in °F $h$ hours after noon. What does $T(3) = 72$ mean?
> **At 3 PM, the temperature is 72°F.**

> [!warning] Don't flip the input and output
> $C(10) = 55$ does **not** mean "55 GB costs \$10." The number inside the parentheses is always the input.

> [!note] Expressions as inputs
> $f(a + 2)$ means "add first, then use the result as the input." The whole expression goes into the function together.

### Practice

**1.** $P(t)$ is a town's population $t$ years after 2020. What does $P(5) = 12{,}400$ mean?

> [!check]- Answer
> In 2025, the town's population was 12,400.

**2.** $W(d)$ is how much water, in gallons, a garden needs on day $d$ of summer. Write "the garden needs 30 gallons on day 12" in function notation.

> [!check]- Answer
> $W(12) = 30$

**3.** $s = f(n)$ is the score on a game after $n$ levels. In $f(4) = 900$, which number is the input?

> [!check]- Answer
> $4$ (levels) is the input; $900$ (score) is the output.

---

## 5. Four Function Families

A function can be shown as **ordered pairs**, an **equation**, a **table**, a **graph**, or a **word description**. Same function, different views - and each view makes different things obvious.

### Linear functions

**Shape:** a straight line. **Equation:** $x$ to the first power, like $f(x) = mx + b$.

> [!example] A taxi charges \$3 to start plus \$2.50 per mile: $f(m) = 2.5m + 3$
>
> | Miles $m$ | 0 | 2 | 4 | 10 |
> |---|---|---|---|---|
> | Cost $f(m)$ | 3 | 8 | 13 | 28 |
>
> **Graph:** a line starting at $(0, 3)$ - the \$3 base fare - rising \$2.50 for every mile.
> **In words:** "\$2.50 times the miles, plus 3."

### Quadratic functions

**Shape:** a U-shaped **parabola**. **Equation:** highest power of $x$ is 2.

> [!example] $f(x) = x^2 - 4$
>
> | $x$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
> |---|---|---|---|---|---|---|---|
> | $f(x)$ | 5 | 0 | $-3$ | $-4$ | $-3$ | 0 | 5 |
>
> **Graph:** a U opening upward with its bottom at $(0, -4)$. Notice the table is **symmetric**: $x$ and $-x$ give the same output.
> **In words:** "the input squared, minus 4."

### Rational functions

**Equation:** a fraction with polynomials on top and bottom, **with $x$ in the denominator**:
$$f(x) = \frac{p(x)}{q(x)}$$

> [!warning] $x$ must be in the denominator
> $\frac{x^2}{4}$ is just $\frac{1}{4}x^2$ - a **quadratic**, not a rational function. $\frac{4}{x^2}$ is rational.

**Shape:** curves that bend toward invisible guide lines called **asymptotes**.

| Asymptote | Where it is | How to find it |
|---|---|---|
| **Vertical** | where the function is undefined | set the **denominator = 0** and solve. The graph never touches it. |
| **Horizontal** | the height the graph levels off at as $x$ gets huge (positive or negative) | compare the highest powers on top and bottom (below). The graph can cross it, but always comes back toward it. |
| **Oblique (slant)** | a diagonal guide line | covered later in the course |

> [!abstract] Horizontal asymptote shortcut
> Compare the **highest power** of $x$ on top vs. bottom:
> - **Bottom is bigger** → $y = 0$
> - **Same power** → $y = \dfrac{\text{leading coefficient on top}}{\text{leading coefficient on bottom}}$
> - **Top is bigger** → no horizontal asymptote
>
> Memory hook: **B**ottom **B**igger → **B**ottom out at 0.

> [!example] $f(x) = \dfrac{2x}{x + 3}$
> - **Vertical:** $x + 3 = 0 \Rightarrow x = -3$
> - **Horizontal:** both powers are 1 → $y = \frac{2}{1} = 2$
>
> | $x$ | $-5$ | $-4$ | $-3$ | $-2$ | $0$ | $3$ |
> |---|---|---|---|---|---|---|
> | $f(x)$ | 5 | 8 | undefined | $-4$ | 0 | 1 |
>
> Near $x = -3$ the outputs blow up ($8$ on one side, $-4$ on the other) - that's the vertical asymptote. Far out, the outputs settle near 2.

> [!example] $g(x) = \dfrac{5}{x^2 - 9}$
> - **Vertical:** $x^2 - 9 = 0 \Rightarrow x = 3$ and $x = -3$
> - **Horizontal:** top is $5 = 5x^0$ (power 0), bottom is power 2 → bottom bigger → $y = 0$
> As $x$ grows, the denominator gets huge and the fraction shrinks toward 0.

### Radical functions

**Equation:** a variable under a root, like $f(x) = \sqrt{x + 2}$.

> [!example] $f(x) = \sqrt{x + 2}$
>
> | $x$ | $-2$ | $-1$ | $2$ | $7$ |
> |---|---|---|---|---|
> | $f(x)$ | 0 | 1 | 2 | 3 |
>
> **Graph:** starts at $(-2, 0)$ and curves up and to the right, getting flatter. It looks like half of a sideways parabola - because square roots undo squaring.
> **Where does it start?** Set the inside equal to 0: $x + 2 = 0 \Rightarrow x = -2$. Anything less would mean the square root of a negative, which isn't a real number.

> [!tip] Pick good table inputs
> For radical functions, choose $x$-values that make the inside a perfect square ($0, 1, 4, 9, \ldots$) so the outputs come out as whole numbers.

All four families pass the Vertical Line Test - they're all functions.

### Practice

**1.** Name each function's family: $f(x) = 7 - 3x$, $g(x) = \dfrac{x+1}{x-5}$, $h(x) = \sqrt{4x}$, $k(x) = 2x^2 - x$, $m(x) = \dfrac{x^2}{4}$

> [!check]- Answer
> $f$ linear, $g$ rational, $h$ radical, $k$ quadratic, $m$ **quadratic** (no $x$ in the denominator).

**2.** Find the asymptotes of $f(x) = \dfrac{3x}{x - 2}$.

> [!check]- Answer
> Vertical $x = 2$. Horizontal $y = 3$ (same power, $\frac{3}{1}$).

**3.** Find the asymptotes of $f(x) = \dfrac{1}{x^2 - 16}$.

> [!check]- Answer
> Vertical $x = 4$ and $x = -4$. Horizontal $y = 0$ (bottom bigger).

**4.** Find the horizontal asymptote of $f(x) = \dfrac{4x^2}{2x^2 + 1}$. Does it have a vertical asymptote?

> [!check]- Answer
> Horizontal $y = \frac{4}{2} = 2$. **No** vertical asymptote: $2x^2 + 1$ is never 0.

**5.** Where does the graph of $f(x) = \sqrt{x - 5}$ start?

> [!check]- Answer
> At $(5, 0)$.

**6.** Name five ways to represent a function.

> [!check]- Answer
> Ordered pairs, an equation, a table, a graph, a word description.

---

## 6. Evaluating Functions

**Evaluating** means plugging an input in and simplifying. Whatever is inside the parentheses replaces **every** $x$.

> [!tip] Always substitute with parentheses
> Replace $x$ with $(\ \ )$ first, then fill in the value. This one habit prevents most sign errors.

### At a number

> [!example] $f(x) = 3x^2 - 2x + 1$. Find $f(-2)$.
> $$f(-2) = 3(-2)^2 - 2(-2) + 1 = 3(4) + 4 + 1 = 17$$

> [!warning] The negative-squared trap
> If $f(x) = -x^2$, then $f(-3) = -(-3)^2 = -9$, **not** $9$. The exponent happens before the negative out front.

### At an expression

Same process - the result is just an expression instead of a number. Expect to use the distributive property and the square-of-a-binomial pattern from Module 1.

> [!example] $f(x) = 4x + 1$. Find $f(a - 3)$.
> $$f(a - 3) = 4(a - 3) + 1 = 4a - 12 + 1 = 4a - 11$$

> [!example] $g(x) = x^2 + 2x$. Find $g(x - 1)$.
> $$g(x - 1) = (x - 1)^2 + 2(x - 1) = x^2 - 2x + 1 + 2x - 2 = x^2 - 1$$
> Don't let it bother you that the input contains $x$ too - replace every $x$ in the rule with $(x - 1)$.

> [!example] $h(x) = \sqrt{x + 3}$. Find $h(x^2 + 1)$.
> $$h(x^2 + 1) = \sqrt{x^2 + 1 + 3} = \sqrt{x^2 + 4}$$
> This does **not** simplify to $x + 2$. A root doesn't split over addition: $\sqrt{x^2 + 4} \neq \sqrt{x^2} + \sqrt{4}$.

### Practice

**1.** $f(x) = 6 - x^2$. Find $f(4)$ and $f(-1)$.

> [!check]- Answer
> $f(4) = 6 - 16 = -10$; $f(-1) = 6 - 1 = 5$

**2.** $g(x) = 2x^3 - x$. Find $g(-2)$.

> [!check]- Answer
> $2(-8) - (-2) = -16 + 2 = -14$

**3.** $f(x) = 7x - 2$. Find $f(k + 1)$.

> [!check]- Answer
> $7k + 7 - 2 = 7k + 5$

**4.** $f(x) = x^2 + 4$. Find $f(x - 2)$.

> [!check]- Answer
> $x^2 - 4x + 4 + 4 = x^2 - 4x + 8$

**5.** $g(t) = 3t^2$. Find $g(2t)$.

> [!check]- Answer
> $3(2t)^2 = 3 \cdot 4t^2 = 12t^2$ (the 2 gets squared too)

**6.** $p(x) = x^2 - x$. Find $p(x + 1)$.

> [!check]- Answer
> $x^2 + 2x + 1 - x - 1 = x^2 + x$

**7.** $f(x) = -x^2 + 3$. Find $f(x + 1)$.

> [!check]- Answer
> $-(x^2 + 2x + 1) + 3 = -x^2 - 2x + 2$

---

## 7. Function Composition

Sometimes one function's output feeds straight into another function. That chain is called **composition**.

> [!example] A road trip
> - $d(h)$ = miles driven after $h$ hours
> - $g(d)$ = gallons of gas used after $d$ miles
>
> Gallons used after $h$ hours: first find the miles, then the gas for those miles: $g(d(h))$.

$$(f \circ g)(x) = f(g(x))$$

Read it as "**$f$ of $g$ of $x$**." The $\circ$ is the composition symbol.

> [!abstract] Work from the inside out
> 1. Evaluate the **inner** function $g(x)$ first.
> 2. Feed that answer into the **outer** function $f$.

> [!warning] Composition is not multiplication
> $f(g(x))$ is **not** $f(x) \cdot g(x)$. And order matters: $f(g(x))$ and $g(f(x))$ are usually different.

### Composition from tables

| $x$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $f(x)$ | 4 | 1 | 5 | 2 | 3 |
| $g(x)$ | 2 | 5 | 1 | 3 | 4 |

> [!example] Find $f(g(1))$ and $g(f(1))$
> $f(g(1))$: $g(1) = 2$, then $f(2) = 1$. → **1**
> $g(f(1))$: $f(1) = 4$, then $g(4) = 3$. → **3**
> Same input, opposite order, different answers.

### Mixing representations

The two functions don't have to be in the same form. Use whichever form each one is given in.

> [!example] Concert ticket revenue
> $f(d)$ is the number of tickets sold $d$ days before a concert:
>
> | $d$ | 1 | 2 | 3 | 4 |
> |---|---|---|---|---|
> | $f(d)$ | 120 | 200 | 260 | 300 |
>
> Each ticket costs \$15, so revenue is $g(t) = 15t$ for $t$ tickets. Find the revenue from tickets sold 2 days before.
> - **Inner (table):** $f(2) = 200$ tickets
> - **Outer (equation):** $g(200) = 15(200) = 3{,}000$
>
> Revenue: \$3,000.

### Practice

Use the $f$ and $g$ table above for 1-5.

**1.** $f(g(2))$

> [!check]- Answer
> $g(2) = 5$, $f(5) = 3$ → **3**

**2.** $g(f(3))$

> [!check]- Answer
> $f(3) = 5$, $g(5) = 4$ → **4**

**3.** $f(f(2))$

> [!check]- Answer
> $f(2) = 1$, $f(1) = 4$ → **4**

**4.** $g(g(3))$

> [!check]- Answer
> $g(3) = 1$, $g(1) = 2$ → **2**

**5.** $f(g(4))$

> [!check]- Answer
> $g(4) = 3$, $f(3) = 5$ → **5**

**6.** $f(x) = 3x - 1$, and $g$ is given by the table below. Find $g(f(2))$ and $f(g(3))$.

| $x$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $g(x)$ | 4 | 7 | 2 | 9 | 5 |

> [!check]- Answer
> $g(f(2))$: $f(2) = 5$, $g(5) = 5$ → **5**
> $f(g(3))$: $g(3) = 2$, $f(2) = 5$ → **5**

**7.** $f(x) = x^2 - 1$, and $g$ is given below. Find $g(f(1))$ and $f(g(-2))$.

| $x$ | $-2$ | $-1$ | 0 | 1 | 2 |
|---|---|---|---|---|---|
| $g(x)$ | 3 | 0 | $-2$ | 4 | 1 |

> [!check]- Answer
> $g(f(1))$: $f(1) = 0$, $g(0) = -2$ → **$-2$**
> $f(g(-2))$: $g(-2) = 3$, $f(3) = 8$ → **8**

---

## 8. Decomposing Functions

Decomposing goes the other way: start with one complicated function and split it into an **outer** and an **inner** function.

> [!tip] Ask "what would I calculate first?"
> If you were plugging a number into $h(x) = (2x + 1)^3$ by hand, you'd compute $2x + 1$ first, then cube it.
> - What you do first → **inner** $g(x) = 2x + 1$
> - What you do last → **outer** $f(x) = x^3$
>
> Check: $f(g(x)) = (2x + 1)^3$ ✓

> [!example] $h(x) = \sqrt{x^2 + 9}$
> First $x^2 + 9$, then the square root: $g(x) = x^2 + 9$, $f(x) = \sqrt{x}$

> [!example] $h(x) = \dfrac{5}{(x - 4)^2}$
> One option: $g(x) = x - 4$, $f(x) = \dfrac{5}{x^2}$
> Another: $g(x) = (x - 4)^2$, $f(x) = \dfrac{5}{x}$
> Both work - decompositions aren't unique.

> [!note] The "boring" decomposition
> $f(x) = x$ with $g(x) = h(x)$ technically always works, because $f$ just passes the input through unchanged. It's correct, but it doesn't split anything up. Look for the more useful one.

> [!note] Hidden decompositions
> $x^2 + 4x + 7$ doesn't look like a composition, but it equals $(x + 2)^2 + 3$, so $f(x) = x^2 + 3$ with $g(x) = x + 2$ works. Always check a candidate by composing it back.

### Practice

**1.** Decompose $h(x) = (x - 7)^5$.

> [!check]- Answer
> $g(x) = x - 7$, $f(x) = x^5$

**2.** Decompose $h(x) = \dfrac{1}{x^2 + 1}$.

> [!check]- Answer
> $g(x) = x^2 + 1$, $f(x) = \dfrac{1}{x}$

**3.** $g(x) = x + 2$. Find $f$ so that $f(g(x)) = (x + 2)^2 + 1$.

> [!check]- Answer
> $f(x) = x^2 + 1$

**4.** $f(x) = \sqrt{x}$. Find $g$ so that $f(g(x)) = \sqrt{5x - 1}$.

> [!check]- Answer
> $g(x) = 5x - 1$

---

## 9. Building Models with Composition

Composition shows up any time there's a **chain of dependence**: A depends on B, and B depends on C.

> [!abstract] The method
> 1. **Is there a chain?** Does one quantity depend on another quantity that itself changes? If so, you need composition.
> 2. **Find the order.** The quantity you want at the end is the **outer** function. The thing it depends on is the **inner** function.
> 3. **Substitute** the inner function's rule into the outer function and simplify.

> [!example] Spreading pancake batter
> Batter poured on a griddle spreads in a circle. Area depends on the radius, and the radius depends on time.
> - Area $A(r) = \pi r^2$ (outer)
> - Radius $r(t)$ (inner)
> $$A(r(t)) = \pi(r(t))^2$$
> The area is now a function of **time**.

> [!example] Online store profit
> $f(x) = 0.05x + 2$ is the number of orders per day from $x$ website visitors. $g(x) = 25x - 20$ is the daily profit in dollars from $x$ orders. Write profit as a function of visitors.
> - Profit depends on orders, orders depend on visitors → profit is **outer**: $g(f(x))$
> $$g(f(x)) = 25(0.05x + 2) - 20 = 1.25x + 50 - 20 = 1.25x + 30$$

> [!warning] Wrong order = wrong model
> $f(g(x)) = 0.05(25x - 20) + 2 = 1.25x + 1$ is a valid calculation but answers nothing - it plugs profit into the "orders from visitors" function. Always ask which quantity depends on which.

### Practice

**1.** A cube's side length $s$ grows over time $t$. Write the volume as a function of time. ($V = s^3$)

> [!check]- Answer
> $V(s(t)) = (s(t))^3$

**2.** A car uses $f(x) = 0.04x$ gallons for $x$ miles. Gas costs $g(x) = 3.5x$ dollars for $x$ gallons. Write cost as a function of miles.

> [!check]- Answer
> $g(f(x)) = 3.5(0.04x) = 0.14x$ dollars

**3.** A tutor gets $f(x) = 0.5x + 1$ hours booked per week from $x$ inquiries and earns $g(x) = 40x$ dollars for $x$ hours. Write weekly earnings as a function of inquiries.

> [!check]- Answer
> $g(f(x)) = 40(0.5x + 1) = 20x + 40$

**4.** A circle's circumference is $C = 2\pi r$, and its radius changes over time. Write the composite function.

> [!check]- Answer
> $C(r(t)) = 2\pi r(t)$

---

## 10. Using Composition Models

Once you have the model, you answer questions by plugging in a specific input - usually a time or a count.

> [!example] Pancake batter, continued
> The radius grows 0.5 inches per second, so $r(t) = 0.5t$. What's the area after 8 seconds?
> $$A(t) = \pi(0.5t)^2$$
> $$A(8) = \pi(0.5 \cdot 8)^2 = \pi(4)^2 = 16\pi \approx 50.3 \text{ in}^2$$

> [!tip] Exact vs. approximate
> "Exact" means leave $\pi$ (and roots) in the answer: $16\pi$. "Approximate" or "to the nearest..." means use a calculator: $\approx 50.27$.

> [!tip] Two ways to evaluate
> You can find the inner value first ($r(8) = 4$) and then plug it in ($A(4) = 16\pi$), or build the full formula first and plug in once. Same answer either way.

### Practice

**1.** A square garden's side grows 3 ft per day. What is its area after 4 days?

> [!check]- Answer
> $s(t) = 3t$, $A = (3t)^2$. $A(4) = 12^2 = 144 \text{ ft}^2$

**2.** A cube's side grows 2 cm per minute. What is its volume after 5 minutes?

> [!check]- Answer
> $s(5) = 10$, $V = 10^3 = 1{,}000 \text{ cm}^3$

**3.** Using the tutor model $g(f(x)) = 20x + 40$, how much does the tutor earn with 12 inquiries?

> [!check]- Answer
> $20(12) + 40 = \$280$

**4.** A ripple's radius grows 4 cm per second. What's the exact circumference at 2.5 seconds?

> [!check]- Answer
> $r(2.5) = 10$, $C = 2\pi(10) = 20\pi$ cm

**5.** A sphere's radius grows 3 inches per second. What's its exact volume at 2 seconds? ($V = \frac{4}{3}\pi r^3$)

> [!check]- Answer
> $r(2) = 6$, $V = \frac{4}{3}\pi(216) = 288\pi \text{ in}^3$

**6.** Using the online store model $g(f(x)) = 1.25x + 30$, what's the profit with 600 visitors?

> [!check]- Answer
> $1.25(600) + 30 = \$780$

---

## Module Review Quiz

**1.** Is $\{(5,0), (6,1), (5,2)\}$ a function? Give its domain.

> [!check]- Answer
> No - input 5 has two outputs. Domain $\{5, 6\}$.

**2.** Is $y^2 = 4x$ a function?

> [!check]- Answer
> No. $y = \pm 2\sqrt{x}$ gives two outputs for each positive $x$.

**3.** $R(n)$ is the revenue in dollars from selling $n$ shirts. What does $R(40) = 600$ mean?

> [!check]- Answer
> Selling 40 shirts brings in \$600.

**4.** Find the vertical and horizontal asymptotes of $f(x) = \dfrac{6x}{2x + 8}$.

> [!check]- Answer
> Vertical $x = -4$. Horizontal $y = \frac{6}{2} = 3$.

**5.** $f(x) = x^2 - 2x$. Find $f(-3)$ and $f(a + 1)$.

> [!check]- Answer
> $f(-3) = 9 + 6 = 15$
> $f(a+1) = a^2 + 2a + 1 - 2a - 2 = a^2 - 1$

**6.** $f(x) = 2x + 1$ and $g(x) = x^2$. Find $f(g(3))$ and $g(f(3))$.

> [!check]- Answer
> $f(g(3)) = f(9) = 19$
> $g(f(3)) = g(7) = 49$

**7.** Decompose $h(x) = \sqrt{4x - 3}$.

> [!check]- Answer
> $g(x) = 4x - 3$, $f(x) = \sqrt{x}$

**8.** A circle's radius grows 5 m per minute. Write $A(t)$ and find the exact area at 3 minutes.

> [!check]- Answer
> $A(t) = \pi(5t)^2$. $A(3) = \pi(15)^2 = 225\pi \text{ m}^2$
