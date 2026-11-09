---
title: Linear Functions and Systems
section: 2 - Linear and Quadratic Functions
module: 5
status: draft
topics: [solving-linear-equations, linear-models, intercepts, slope-and-line-forms, checking-system-solutions, substitution-method, elimination-method, types-of-systems, system-word-problems]
---

# Module 5: Linear Functions and Systems

**By the end of this module you can:** solve linear equations, turn a pricing or rate situation into a linear model, graph a line from its intercepts or slope, and solve a system of two linear equations three different ways - graphing, substitution, and elimination.

> [!info] Why this matters
> Lines are the simplest relationships in math, and they show up everywhere: a fare that's a base fee plus a per-mile charge, a salary plus commission, a savings balance growing by the same amount each week. Systems answer the next question: when do two of those lines meet? When does revenue catch up to cost? When does one phone plan become cheaper than another?

---

## 1. Solving Linear Equations

A **linear equation** has its variable only to the first power - no $x^2$, no $\sqrt{x}$, no $x$ in a denominator. Solving it means finding the value that makes both sides equal.

> [!tip] Think of a balance scale
> An equation is a scale in balance. You can do almost anything to it - add, subtract, multiply, divide - **as long as you do the same thing to both sides.** Do it to only one side and the scale tips.

The two tools:
- **Addition property:** you can add (or subtract) the same amount on both sides.
- **Multiplication property:** you can multiply (or divide) both sides by the same non-zero amount.

> [!abstract] The method
> 1. Simplify each side (distribute, combine like terms).
> 2. Get all the variable terms on one side and the constants on the other (addition property).
> 3. Get the variable's coefficient to 1 (multiplication property - multiply by the reciprocal).
> 4. Check by plugging your answer back in.

Same idea as inverses in Module 4: **undo the operations in reverse order.** In $4x - 9$, the $x$ gets multiplied by 4, then 9 is subtracted. So undo the $-9$ first, then the $\times 4$.

> [!example] Solve $4x - 9 = 23$
> Add 9 to both sides: $4x = 32$
> Divide both sides by 4: $x = 8$
> Check: $4(8) - 9 = 32 - 9 = 23$ ✓

> [!example] Solve $\frac{x}{3} - 5 = 2$
> Add 5: $\frac{x}{3} = 7$
> Multiply by 3 (the reciprocal of $\frac{1}{3}$): $x = 21$

> [!example] Solve $\frac{2}{3}x + 1 = 7$
> Subtract 1: $\frac{2}{3}x = 6$
> Multiply by the reciprocal $\frac{3}{2}$: $x = 6 \cdot \frac{3}{2} = 9$

> [!example] Bonus: variables on both sides - $5x + 3 = 2x + 15$
> Subtract $2x$ from both sides: $3x + 3 = 15$
> Subtract 3: $3x = 12$, so $x = 4$.

> [!note] Bonus: when there's no single answer
> - $2(x + 3) = 2x + 6$ simplifies to $6 = 6$ - always true. **Every** number is a solution.
> - $2x + 1 = 2x + 5$ simplifies to $1 = 5$ - never true. **No** solution.
> These come back in section 8 as dependent and inconsistent systems.

> [!warning] Common mistakes
> - Doing an operation to only one side.
> - Dividing before subtracting: in $4x - 9 = 23$, dividing first gives $x - 9 = \frac{23}{4}$, which is wrong - the 9 needs dividing too.
> - Sign slips when moving a term: $x - 3 = 7$ means **add** 3, not subtract.

### Practice

**1.** $6x + 11 = -7$

> [!check]- Answer
> $6x = -18$, so $x = -3$

**2.** $\frac{x}{4} - 2 = 3$

> [!check]- Answer
> $\frac{x}{4} = 5$, so $x = 20$

**3.** $0.5x + 3 = 11$

> [!check]- Answer
> $0.5x = 8$, so $x = 16$

**4.** $3(x - 2) = 15$

> [!check]- Answer
> $3x - 6 = 15 \Rightarrow 3x = 21 \Rightarrow x = 7$ (or divide both sides by 3 first: $x - 2 = 5$)

**5.** $7x - 4 = 3x + 12$

> [!check]- Answer
> $4x - 4 = 12 \Rightarrow 4x = 16 \Rightarrow x = 4$

**6.** $3(2x - 1) = 4x + 9$

> [!check]- Answer
> $6x - 3 = 4x + 9 \Rightarrow 2x = 12 \Rightarrow x = 6$

---

## 2. Writing Linear Models

Most real linear situations have two parts:

| Part | What it is | Example | In the equation |
|---|---|---|---|
| **Fixed amount** | Doesn't change - charged once | a \$2.50 pickup fee | the constant $b$ |
| **Rate** | Charged per unit | \$1.75 per mile | the coefficient $m$ on $x$ |

$$\text{total} = (\text{rate}) \cdot x + \text{fixed amount} \qquad\Longrightarrow\qquad y = mx + b$$

> [!tip] Spot the rate
> Words like **per**, **each**, **every**, **an hour**, **a mile** mark the rate - it multiplies $x$. Everything else that's a one-time amount gets added (or subtracted).

> [!abstract] Steps
> 1. Find the known quantities: what's fixed, what's the rate?
> 2. Choose a variable for the unknown quantity (and say what it means and its units).
> 3. Write the equation.
> 4. Answer the question - in words, with units.

> [!example] Rideshare
> A ride costs \$2.50 plus \$1.75 per mile. Model the cost, then find the cost of a 12-mile ride.
> Let $x$ = miles. $y = 1.75x + 2.50$.
> $y = 1.75(12) + 2.50 = 21 + 2.50 = 23.50$. A 12-mile ride costs **\$23.50**.

> [!example] Plumber
> A plumber charges an \$85 call-out fee plus \$60 an hour. What do 3 hours cost?
> $y = 60x + 85$, so $y = 60(3) + 85 = \$265$.

> [!example] Running backward from the total
> Same plumber. The bill was \$325. How long was the job?
> $325 = 60x + 85 \Rightarrow 240 = 60x \Rightarrow x = 4$ hours. (That's the inverse idea from Module 4.)

> [!note] Percents are rates too
> A salary of \$400 a week plus 8% commission on sales $x$: $y = 0.08x + 400$.

### Practice

**1.** A gym charges a \$50 signup fee plus \$25 a month. Write the model for $x$ months.

> [!check]- Answer
> $y = 25x + 50$

**2.** A phone plan costs \$40 a month plus \$0.05 per text. Write the monthly cost for $x$ texts.

> [!check]- Answer
> $y = 0.05x + 40$

**3.** A snow shoveling service charges \$15 per visit, plus a one-time \$20 setup fee for the season. How much do 8 visits cost?

> [!check]- Answer
> $y = 15x + 20$, so $15(8) + 20 = \$140$

**4.** A bicycle shop pays \$300 a week in rent and earns \$45 per repair. Write the profit $y$ for $x$ repairs.

> [!check]- Answer
> $y = 45x - 300$ (rent is a fixed cost, so it's subtracted)

**5.** A car travels at 55 mph. Write the distance after $x$ hours.

> [!check]- Answer
> $y = 55x$ (no fixed part)

---

## 3. Intercepts and Graphing

The two easiest points to find on a line are where it crosses the axes.

| Intercept | Where the line crosses | How to find it |
|---|---|---|
| **$y$-intercept** | the $y$-axis | set $x = 0$, solve for $y$ |
| **$x$-intercept** | the $x$-axis | set $y = 0$, solve for $x$ |

> [!tip] Why it works
> Every point on the $y$-axis has $x = 0$, and every point on the $x$-axis has $y = 0$. That's all there is to it.

Plot both intercepts, draw a line through them, and you've graphed the equation.

> [!example] $y = 3x - 12$
> $y$-intercept: $y = 3(0) - 12 = -12$, so $(0, -12)$.
> $x$-intercept: $0 = 3x - 12 \Rightarrow x = 4$, so $(4, 0)$.

> [!example] $2x + 5y = 20$ (standard form)
> $y$-intercept: $5y = 20 \Rightarrow (0, 4)$
> $x$-intercept: $2x = 20 \Rightarrow (10, 0)$
> In standard form the intercepts take one step each.

> [!note] Shortcut for $y = mx + b$
> In slope-intercept form the $y$-intercept is just $b$. The $x$-intercept is $-\frac{b}{m}$.

### Practice

**1.** Find both intercepts of $y = -4x + 8$.

> [!check]- Answer
> $y$-intercept $8$, i.e. $(0, 8)$. $x$-intercept $2$, i.e. $(2, 0)$.

**2.** Find both intercepts of $y = 0.5x - 3$.

> [!check]- Answer
> $(0, -3)$ and $(6, 0)$

**3.** Find both intercepts of $3x - 4y = 24$.

> [!check]- Answer
> $(0, -6)$ and $(8, 0)$

**4.** Find the $x$-intercept of $y = 9x + 27$.

> [!check]- Answer
> $0 = 9x + 27 \Rightarrow x = -3$

---

## 4. Slope and the Forms of a Line

**Slope** measures steepness: how much $y$ changes for each step in $x$.

$$m = \frac{\text{rise}}{\text{run}} = \frac{y_2 - y_1}{x_2 - x_1}$$

| Slope | The line... |
|---|---|
| positive | rises left to right |
| negative | falls left to right |
| 0 | is horizontal ($y = $ constant) |
| undefined | is vertical ($x = $ constant) |

> [!example] Slope through $(2, 1)$ and $(6, 9)$
> $$m = \frac{9 - 1}{6 - 2} = \frac{8}{4} = 2$$
> Every step right, the line goes up 2.

> [!warning] Keep the order matched
> Subtract in the same order on top and bottom. $\frac{9 - 1}{2 - 6}$ mixes the orders and gives $-2$ - wrong sign.

### Two forms worth knowing

| Form | Equation | Use it when you know... |
|---|---|---|
| **Slope-intercept** | $y = mx + b$ | the slope and the $y$-intercept |
| **Point-slope** | $y - y_1 = m(x - x_1)$ | the slope and any point |

> [!example] Slope 3, through $(2, 7)$
> Point-slope: $y - 7 = 3(x - 2)$
> Convert to slope-intercept by solving for $y$: $y - 7 = 3x - 6 \Rightarrow y = 3x + 1$

> [!example] Through $(0, -4)$ and $(2, 2)$
> Slope: $\frac{2 - (-4)}{2 - 0} = 3$. The $y$-intercept is $-4$ (it's the point with $x = 0$).
> $y = 3x - 4$

> [!tip] Solve for $y$ to read the slope
> Any linear equation can be put in slope-intercept form. $4x + 2y = 10 \Rightarrow 2y = -4x + 10 \Rightarrow y = -2x + 5$: slope $-2$, $y$-intercept 5. This is the fastest way to compare two lines - see section 8.

### Practice

**1.** Slope through $(1, 2)$ and $(4, 11)$.

> [!check]- Answer
> $\frac{11 - 2}{4 - 1} = \frac{9}{3} = 3$

**2.** Slope through $(-2, 5)$ and $(2, -3)$.

> [!check]- Answer
> $\frac{-3 - 5}{2 - (-2)} = \frac{-8}{4} = -2$

**3.** Slope through $(0, 5)$ and $(4, 5)$.

> [!check]- Answer
> $0$ - a horizontal line

**4.** Write the line with slope $-2$ through $(3, 1)$ in slope-intercept form.

> [!check]- Answer
> $y - 1 = -2(x - 3) \Rightarrow y = -2x + 7$

**5.** Find the slope and $y$-intercept of $6x - 3y = 9$.

> [!check]- Answer
> $-3y = -6x + 9 \Rightarrow y = 2x - 3$. Slope 2, $y$-intercept $-3$.

---

## 5. Systems of Equations

A **system** is two (or more) equations that have to be true **at the same time**. A **solution** is a pair $(x, y)$ that works in every equation.

Graphically, each linear equation is a line, so the solution is **where the lines cross**.

### Is it a linear system?

Every equation has to be linear: each term is a number, or a number times **one** variable to the **first** power.

| Equation | Linear? | Why |
|---|---|---|
| $3x - 2y = 7$ | Yes | |
| $\frac{x}{2} + \frac{y}{5} = 1$ | Yes | fractions as *coefficients* are fine |
| $y = 2(x - 4)$ | Yes | distributes to $2x - 8$ |
| $xy = 6$ | No | variables multiplied together |
| $y = x^2 + 1$ | No | squared variable |
| $y = \frac{4}{x}$ | No | variable in a denominator |
| $y = 2^x$ | No | variable in an exponent |

> [!warning] Simplify before you judge
> $y^2 + 3x = (y + 1)^2$ looks nonlinear, but expanding gives $y^2 + 3x = y^2 + 2y + 1$, and the $y^2$ cancels: $3x = 2y + 1$. Linear! Likewise $\ln(e^{2x}) = 2x$ is linear.

### Checking a solution

Plug the pair into **both** equations. It has to work in both.

> [!example] Is $(2, 3)$ a solution of $x + y = 5$ and $3x - y = 3$?
> $2 + 3 = 5$ ✓ and $3(2) - 3 = 3$ ✓. **Yes.**

> [!example] Is $(4, 1)$ a solution of $x + y = 5$ and $3x - y = 3$?
> $4 + 1 = 5$ ✓ but $3(4) - 1 = 11 \neq 3$ ✗. **No** - one out of two isn't enough.

### Practice

**1.** Is $\{2x + y = 9,\; x - 4y = 1\}$ a linear system?

> [!check]- Answer
> Yes

**2.** Is $\{x + y = 10,\; xy = 21\}$ a linear system?

> [!check]- Answer
> No - $xy$ is a product of variables

**3.** Is $(3, -1)$ a solution of $2x + y = 5$ and $x - y = 4$?

> [!check]- Answer
> $6 - 1 = 5$ ✓ and $3 + 1 = 4$ ✓. Yes.

**4.** Which pair solves $x + 2y = 8$ and $3x - y = 3$? $(2, 3)$, $(3, 2)$, $(4, 2)$, $(0, 4)$

> [!check]- Answer
> $(2, 3)$: $2 + 6 = 8$ ✓ and $6 - 3 = 3$ ✓. ($(0, 4)$ only works in the first.)

---

## 6. Solving by Substitution

> [!abstract] Substitution
> 1. Solve one equation for one variable (pick whichever is easiest - a variable with coefficient 1 or $-1$ avoids fractions).
> 2. **Substitute** that expression into the *other* equation. Now there's only one variable - solve it.
> 3. Plug that value back in to get the other variable.
> 4. Write the answer as $(x, y)$ and check it in both equations.

> [!example] $y = 2x + 1$ and $3x + y = 16$
> $y$ is already solved. Substitute $2x + 1$ for $y$ in the second equation:
> $$3x + (2x + 1) = 16 \;\Rightarrow\; 5x + 1 = 16 \;\Rightarrow\; x = 3$$
> Then $y = 2(3) + 1 = 7$. Solution: $(3, 7)$.

> [!example] $x - 2y = 1$ and $3x + 4y = 23$
> The $x$ in the first equation has coefficient 1, so solve for it: $x = 2y + 1$.
> Substitute: $3(2y + 1) + 4y = 23 \Rightarrow 6y + 3 + 4y = 23 \Rightarrow 10y = 20 \Rightarrow y = 2$.
> Then $x = 2(2) + 1 = 5$. Solution: $(5, 2)$.

> [!warning] Use parentheses when you substitute
> $3x - 2(3 - x)$, not $3x - 2 \cdot 3 - x$. The whole expression replaces the variable, and the coefficient multiplies all of it.

> [!tip] If fractions can't be avoided
> Substitute the fraction, then multiply the whole equation by the denominator to clear it before solving.

### Practice

**1.** $y = x + 3$ and $2x + y = 18$

> [!check]- Answer
> $2x + x + 3 = 18 \Rightarrow x = 5$, $y = 8$. **$(5, 8)$**

**2.** $x + y = 7$ and $2x - 3y = -1$

> [!check]- Answer
> $x = 7 - y$. Then $2(7 - y) - 3y = -1 \Rightarrow 14 - 5y = -1 \Rightarrow y = 3$, $x = 4$. **$(4, 3)$**

**3.** $4x - y = 5$ and $x + 2y = 8$

> [!check]- Answer
> $y = 4x - 5$. Then $x + 2(4x - 5) = 8 \Rightarrow 9x = 18 \Rightarrow x = 2$, $y = 3$. **$(2, 3)$**

**4.** $x - 4y = -9$ and $2x + 3y = 4$

> [!check]- Answer
> $x = 4y - 9$. Then $2(4y - 9) + 3y = 4 \Rightarrow 11y = 22 \Rightarrow y = 2$, $x = -1$. **$(-1, 2)$**

---

## 7. Solving by Elimination (Addition)

Elimination adds the two equations together so that one variable cancels out.

> [!abstract] Elimination
> 1. Line the equations up: $x$ terms, $y$ terms, $=$ constants.
> 2. Make the coefficients of one variable **opposites** (like $+2y$ and $-2y$) by multiplying one or both equations.
> 3. **Add** the equations. That variable disappears - solve for the other.
> 4. Substitute back to find the eliminated variable.

> [!example] Already opposites: $3x + 2y = 16$ and $5x - 2y = 0$
> Add: $8x = 16$, so $x = 2$.
> Substitute: $3(2) + 2y = 16 \Rightarrow 2y = 10 \Rightarrow y = 5$. Solution: $(2, 5)$.

> [!example] Multiply one: $5x + 2y = 1$ and $3x + 4y = 9$
> Multiply the first by $-2$: $-10x - 4y = -2$
> Add to the second: $-7x = 7$, so $x = -1$.
> Substitute: $5(-1) + 2y = 1 \Rightarrow y = 3$. Solution: $(-1, 3)$.

> [!example] Multiply both: $2x + 3y = 7$ and $3x - 4y = -15$
> To cancel $y$, aim for $12y$ and $-12y$ (12 is the least common multiple of 3 and 4).
> First $\times 4$: $8x + 12y = 28$
> Second $\times 3$: $9x - 12y = -45$
> Add: $17x = -17$, so $x = -1$.
> Substitute: $2(-1) + 3y = 7 \Rightarrow y = 3$. Solution: $(-1, 3)$.

> [!tip] Substitution or elimination?
> - Some variable already alone, or with coefficient 1? **Substitution** is quick.
> - Everything in $ax + by = c$ form with bigger coefficients? **Elimination** avoids fractions.

> [!warning] Multiply every term
> When you multiply an equation, multiply **every** term, including the constant on the right. Forgetting the right side is the most common elimination mistake.

### Practice

**1.** $x + y = 10$ and $x - y = 4$

> [!check]- Answer
> Add: $2x = 14$, $x = 7$, $y = 3$. **$(7, 3)$**

**2.** $3x + 4y = 10$ and $2x - 3y = 1$

> [!check]- Answer
> First $\times 3$, second $\times 4$: $9x + 12y = 30$ and $8x - 12y = 4$. Add: $17x = 34$, $x = 2$, $y = 1$. **$(2, 1)$**

**3.** $2x + 5y = 4$ and $3x - 2y = 25$

> [!check]- Answer
> First $\times 2$, second $\times 5$: $4x + 10y = 8$ and $15x - 10y = 125$. Add: $19x = 133$, $x = 7$, $y = -2$. **$(7, -2)$**

**4.** $6x + 5y = 7$ and $4x - 3y = 11$

> [!check]- Answer
> First $\times 3$, second $\times 5$: $18x + 15y = 21$ and $20x - 15y = 55$. Add: $38x = 76$, $x = 2$, $y = -1$. **$(2, -1)$**

---

## 8. Types of Systems

Two lines can relate in only three ways:

| Lines | Solutions | Name |
|---|---|---|
| cross once | exactly one | **independent** |
| parallel | none | **inconsistent** |
| the same line | infinitely many | **dependent** |

> [!tip] Compare slopes and intercepts - no graph needed
> Put both equations in $y = mx + b$ form:
> - **Different slopes** → they cross once → independent
> - **Same slope, different $b$** → parallel → inconsistent
> - **Same slope, same $b$** → same line → dependent

> [!example] $y = 2x + 1$ and $4x - 2y = 6$
> Second: $-2y = -4x + 6 \Rightarrow y = 2x - 3$.
> Same slope (2), different intercepts (1 vs. $-3$): **parallel, no solution, inconsistent.**

> [!example] $3x - y = 2$ and $6x - 2y = 4$
> Both become $y = 3x - 2$. **Same line, infinitely many solutions, dependent.** (The second equation is just the first times 2.)

> [!note] What it looks like when you solve algebraically
> - Inconsistent: the variables cancel and you get something false, like $0 = 7$.
> - Dependent: the variables cancel and you get something always true, like $0 = 0$.
> Same as the bonus equations in section 1.

### Solving by graphing

Graph both lines (intercepts or slope-intercept form) and read off where they cross. Always **check** the point in both equations - graphs are only as precise as your drawing.

> [!example] $y = -x + 6$ and $y = 2x$
> The first line runs from $(0, 6)$ down to $(6, 0)$. The second goes through the origin and $(1, 2)$. They cross at $(2, 4)$.
> Check: $4 = -2 + 6$ ✓ and $4 = 2(2)$ ✓

### Practice

**1.** Classify $y = -3x + 2$ and $y = -3x - 5$.

> [!check]- Answer
> Same slope, different intercepts: inconsistent (no solution).

**2.** Classify $x + 2y = 6$ and $3x + 6y = 18$.

> [!check]- Answer
> Both become $y = -\frac{1}{2}x + 3$: dependent (infinitely many solutions).

**3.** Classify $2x - y = 1$ and $x + y = 5$.

> [!check]- Answer
> Slopes 2 and $-1$: independent. (The solution is $(2, 3)$.)

**4.** Solve $x - 3y = 4$ and $2x - 6y = 1$.

> [!check]- Answer
> Slopes are both $\frac{1}{3}$, intercepts $-\frac{4}{3}$ and $-\frac{1}{6}$. Parallel: **no solution.**

---

## 9. Word Problems with Systems

Two unknowns usually means two equations. Name both variables, write one equation for each fact, and solve.

### Rate problems: with and against

A current, wind, or moving walkway either helps or hurts.
- **With** it, speeds add: $b + c$
- **Against** it, speeds subtract: $b - c$

Then use **rate × time = distance** for each trip.

> [!example] Airplane and wind
> A plane flies 1,200 miles with a tailwind in 3 hours, and the same 1,200 miles back into the wind in 4 hours. Find the plane's speed in still air and the wind speed.
> Let $p$ = plane speed, $w$ = wind speed.
>
> | | Rate | Time | Distance |
> |---|---|---|---|
> | With wind | $p + w$ | 3 | 1200 |
> | Against wind | $p - w$ | 4 | 1200 |
>
> $3(p + w) = 1200 \Rightarrow p + w = 400$
> $4(p - w) = 1200 \Rightarrow p - w = 300$
> Add: $2p = 700$, so $p = 350$ mph and $w = 50$ mph.

> [!tip] Divide first
> Dividing each equation by its time before solving gives a clean $p + w = \ldots$, $p - w = \ldots$ pair that adds straight to the answer.

### Mixture and ticket problems

One equation counts **how many**; the other counts **how much they're worth**.

> [!example] Tickets
> A school play sold 50 tickets: adult tickets at \$12 and child tickets at \$7. They took in \$470. How many of each?
> Let $a$ = adult, $k$ = child.
> Count: $a + k = 50$
> Money: $12a + 7k = 470$
> From the first, $k = 50 - a$. Substitute: $12a + 350 - 7a = 470 \Rightarrow 5a = 120 \Rightarrow a = 24$, so $k = 26$.

### Break-even

> [!example] When does a business break even?
> A candle maker spends \$1,200 on equipment plus \$4 per candle, and sells candles for \$10.
> Cost: $y = 4x + 1200$. Revenue: $y = 10x$.
> Break-even is where the lines meet: $10x = 4x + 1200 \Rightarrow 6x = 1200 \Rightarrow x = 200$ candles. After that, every candle is profit.

### Practice

**1.** A kayak goes 24 miles downstream in 3 hours and 24 miles back upstream in 4 hours. Find the kayak's speed in still water and the current's speed.

> [!check]- Answer
> $k + c = 8$ and $k - c = 6$. Kayak **7 mph**, current **1 mph**.

**2.** A boat goes 36 miles with the current in 2 hours and 36 miles against it in 3 hours. Which system fits? (Let $x$ = boat, $y$ = current.)

> [!check]- Answer
> $(x + y)(2) = 36$ and $(x - y)(3) = 36$. (It solves to boat 15 mph, current 3 mph.)

**3.** A concert sold 300 tickets: floor seats at \$45 and balcony at \$30, for \$10,500 total. How many floor tickets?

> [!check]- Answer
> $f + b = 300$, $45f + 30b = 10{,}500$. Substituting $b = 300 - f$: $15f = 1{,}500$, so **100 floor**, 200 balcony.

**4.** A coffee shop mixes a \$8/lb blend with a \$12/lb blend to make 20 lb selling at \$10/lb. How many pounds of each?

> [!check]- Answer
> $x + y = 20$, $8x + 12y = 200$. Substituting gives **10 lb of each**.

**5.** A food truck spends \$900 to start a weekend plus \$3 per meal and sells meals for \$12. How many meals to break even?

> [!check]- Answer
> $12x = 3x + 900 \Rightarrow 9x = 900 \Rightarrow$ **100 meals**

---

## Module Review Quiz

**1.** Solve $5x - 7 = 2x + 8$.

> [!check]- Answer
> $3x = 15$, $x = 5$

**2.** A moving truck rents for \$40 plus \$0.80 per mile. Write the model and find the cost of 150 miles.

> [!check]- Answer
> $y = 0.80x + 40$; $0.80(150) + 40 = \$160$

**3.** Find both intercepts of $4x + 3y = 24$.

> [!check]- Answer
> $(0, 8)$ and $(6, 0)$

**4.** Find the line through $(1, 4)$ and $(3, 10)$ in slope-intercept form.

> [!check]- Answer
> Slope $\frac{6}{2} = 3$; $y - 4 = 3(x - 1) \Rightarrow y = 3x + 1$

**5.** Is $(1, -2)$ a solution of $3x + y = 1$ and $x - y = 3$?

> [!check]- Answer
> $3 - 2 = 1$ ✓ and $1 + 2 = 3$ ✓. Yes.

**6.** Solve by substitution: $y = 3x - 2$ and $2x + y = 13$.

> [!check]- Answer
> $5x - 2 = 13$, $x = 3$, $y = 7$. **$(3, 7)$**

**7.** Solve by elimination: $4x + 3y = 5$ and $2x - 3y = 7$.

> [!check]- Answer
> Add: $6x = 12$, $x = 2$, $y = -1$. **$(2, -1)$**

**8.** Classify $2x + 4y = 8$ and $x + 2y = 3$.

> [!check]- Answer
> Both have slope $-\frac{1}{2}$, intercepts 2 and $\frac{3}{2}$: inconsistent.

**9.** A plane flies 900 miles with the wind in 2 hours and back against it in 3 hours. Find the plane and wind speeds.

> [!check]- Answer
> $p + w = 450$, $p - w = 300$. Plane **375 mph**, wind **75 mph**.
