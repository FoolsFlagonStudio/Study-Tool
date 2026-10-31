---
title: Algebraic Expressions and Equations
section: 1 - Foundations of Algebra and Functions
module: 2
status: draft
topics: [translating-words, commutative-property, multi-operation-expressions, simplifying-rational-exponents, solving-rational-exponent-equations]
---

# Module 2: Algebraic Expressions and Equations

**By the end of this module you can:** turn a word problem into an expression, pull perfect squares and cubes out of roots, and solve equations where the variable has a fractional exponent.

> [!info] Why this matters
> Real problems never show up as $3x + 7$. They show up as sentences - a phone plan, a savings goal, a recipe. Translating words into math is the bridge between "I know the rules" and "I can actually use them."

---

## 1. Translating Words into Math

Think of this like learning vocabulary in a new language. Certain words almost always point to the same operation.

| Operation | Signal words | Example phrase | Expression |
|---|---|---|---|
| **Add** | plus, sum, total, more than, increased by, added to, grew by | a number grew by 12 | $x + 12$ |
| **Subtract** | minus, difference, less than, fewer than, decreased by, subtracted from | 9 fewer than a number | $x - 9$ |
| **Multiply** | times, product, of, per, twice, double, triple | three quarters of a number | $\frac{3}{4}x$ |
| **Divide** | quotient, ratio, divided by, per, half, out of, percent | a number split 4 ways | $\frac{x}{4}$ |

A few that are worth memorizing on their own:

- **twice / double** → $\times 2$, **triple** → $\times 3$
- **half of** → $\div 2$ (or $\times \frac{1}{2}$)
- **percent** → $\div 100$, so 15% of a number is $\frac{15}{100}x = 0.15x$
- **of** after a fraction or percent → multiply ($\frac{2}{5}$ of $x$ is $\frac{2}{5}x$)

### Does order matter?

**Commutative** means "you can swap the order and get the same answer."

| | Swap it | Same result? |
|---|---|---|
| Addition | $2 + 7 = 9$ and $7 + 2 = 9$ | Yes - commutative |
| Multiplication | $4 \cdot 5 = 20$ and $5 \cdot 4 = 20$ | Yes - commutative |
| Subtraction | $10 - 2 = 8$ but $2 - 10 = -8$ | **No** |
| Division | $12 \div 4 = 3$ but $4 \div 12 = \frac{1}{3}$ | **No** |

So with addition and multiplication you can relax. With subtraction and division, you have to get the order right.

> [!warning] The "less than" trap
> "10 less than a number" is $x - 10$, **not** $10 - x$. The words come in the opposite order from the math.
> Same with "**subtracted from**": "4 subtracted from a number" is $x - 4$.

> [!tip] Sanity check with a real number
> If you're not sure about the order, plug in something easy. "10 less than a number" - if the number is 30, then 10 less is 20. Which expression gives 20? $30 - 10$. So it's $x - 10$.

> [!example] A 50-foot rope is cut into two pieces. One piece is $x$ feet. How long is the other?
> The pieces add up to 50, so the other is what's left: $50 - x$ feet.

> [!example] Concert tickets cost \$12 each plus a \$5 booking fee. Write the total cost for $t$ tickets.
> "\$12 each" → $12t$, "plus a \$5 fee" → $+5$
> $$12t + 5$$

### Practice

**1.** Translate "a number decreased by 7."

> [!check]- Answer
> $x - 7$

**2.** Translate "15 subtracted from a number."

> [!check]- Answer
> $x - 15$ (not $15 - x$)

**3.** Translate "40 percent of a number."

> [!check]- Answer
> $\frac{40}{100}x = 0.4x$

**4.** A pizza is cut into 8 slices and you eat $s$ of them. How many slices are left?

> [!check]- Answer
> $8 - s$

**5.** Match each phrase to an expression: "double a number," "the ratio of two numbers," "the sum of a number and 10," "a third of a number."

> [!check]- Answer
> - double a number → $2x$
> - the ratio of two numbers → $\frac{x}{y}$
> - the sum of a number and 10 → $x + 10$
> - a third of a number → $\frac{x}{3}$

---

## 2. Phrases with More Than One Operation

When a phrase has several operations, the hard part is figuring out **what gets grouped together**. Commas and phrases like "the quantity," "the sum of... and...," or "the difference of... and..." tell you where the parentheses go.

> [!example] Same words, different meaning
> - "Twice a number, decreased by 4" → double first, then subtract: $2x - 4$
> - "Twice the difference of a number and 4" → subtract first, then double: $2(x - 4)$
>
> Check with $x = 10$: the first gives $16$, the second gives $12$. Different expressions, different answers.

> [!tip] Build it in pieces
> Translate the smaller chunks first, then connect them.
> "The ratio of a number and 7 more than that number":
> - "a number" → $x$
> - "7 more than that number" → $x + 7$
> - "the ratio of [first] and [second]" → $\dfrac{x}{x + 7}$

> [!example] "The sum of a number and 6, divided by the number"
> The comma tells you the whole sum gets divided:
> $$\frac{x + 6}{x}$$

> [!example] Real-world: a gym membership
> There's a \$40 signup fee and then \$25 per month. Total cost after $m$ months:
> $$40 + 25m$$

> [!example] Real-world: spending down savings
> You have \$250 saved and spend \$15 each week. Amount left after $w$ weeks:
> $$250 - 15w$$

### Practice

**1.** "5 more than the product of 4 and a number"

> [!check]- Answer
> $4x + 5$

**2.** "The product of 4 and the sum of a number and 5"

> [!check]- Answer
> $4(x + 5)$ - compare with question 1. Same numbers, different grouping.

**3.** "The difference of two numbers, divided by their sum"

> [!check]- Answer
> $\dfrac{x - y}{x + y}$

**4.** "6 less than half a number"

> [!check]- Answer
> $\dfrac{x}{2} - 6$

**5.** "The quotient of a number and 3, increased by twice the number"

> [!check]- Answer
> $\dfrac{x}{3} + 2x$

**6.** A phone plan costs \$30 plus \$0.10 per text. Write the cost for $t$ texts.

> [!check]- Answer
> $30 + 0.10t$

**7.** "A number subtracted from 20, with the result multiplied by 3"

> [!check]- Answer
> $3(20 - x)$

---

## 3. Simplifying Roots with Rational Exponents

The exponent rules from Module 1 work exactly the same with fractional exponents. The big one here is $(ab)^n = a^nb^n$ - it lets you split a root into pieces and simplify the pieces you can.

### Numbers: pull out a perfect power

For a square root (exponent $\frac{1}{2}$), look for a **perfect square** factor. For a cube root (exponent $\frac{1}{3}$), look for a **perfect cube** factor.

> [!tip] Keep these lists handy
> **Perfect squares:** $4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144$
> **Perfect cubes:** $8, 27, 64, 125, 216, 1000$
> Always pull out the **largest** one that divides evenly.

> [!example] Simplify $72^{1/2}$
> Largest perfect square factor of 72 is 36:
> $$72^{1/2} = (36 \cdot 2)^{1/2} = 36^{1/2} \cdot 2^{1/2} = 6\sqrt{2}$$
> (Using $4 \cdot 18$ works too, but then $18$ still has a 9 inside it and you'd have to go again.)

> [!example] Simplify $54^{1/3}$
> Largest perfect cube factor of 54 is 27:
> $$54^{1/3} = (27 \cdot 2)^{1/3} = 27^{1/3} \cdot 2^{1/3} = 3\sqrt[3]{2}$$

### Variables: divide the exponent by the root

Here's a shortcut for variables. Divide the variable's exponent by the root's index:
- the **whole-number part** comes out of the root
- the **remainder** stays inside

> [!example] Simplify $(2x^5)^{1/2}$
> For $x^5$ under a square root: $5 \div 2 = 2$ remainder $1$. So $x^2$ comes out and $x^1$ stays in.
> The $2$ has no perfect square, so it stays in too.
> $$(2x^5)^{1/2} = x^2\sqrt{2x}$$
> Why it works: $x^5 = x^4 \cdot x$, and $(x^4)^{1/2} = x^2$.

> [!example] Simplify $(a^7b^3)^{1/3}$
> $a^7$: $7 \div 3 = 2$ remainder $1$ → $a^2$ out, $a$ in
> $b^3$: $3 \div 3 = 1$ remainder $0$ → $b$ out, nothing in
> $$(a^7b^3)^{1/3} = a^2b\sqrt[3]{a}$$

### Combining different roots

Roots with different indexes can't be combined directly - but as exponents, they're just fractions to add.

> [!example] Simplify $\sqrt[3]{x} \cdot \sqrt[4]{x}$
> 1. Convert: $x^{1/3} \cdot x^{1/4}$
> 2. Same base, add exponents: $x^{\frac{1}{3} + \frac{1}{4}} = x^{\frac{4}{12} + \frac{3}{12}} = x^{7/12}$
> 3. Back to a radical ("power over root"): $\sqrt[12]{x^7}$

> [!warning] Common mistakes
> - **Roots don't split over addition:** $\sqrt{9 + 16} = \sqrt{25} = 5$, but $\sqrt{9} + \sqrt{16} = 7$. The $(ab)^n$ rule only works for multiplication.
> - **Don't forget the coefficient:** in $(8a^3)^{1/3}$, the $8$ becomes $2$ too, giving $2a$.
> - **Pull out the largest factor:** $(4 \cdot 18)^{1/2} = 2\sqrt{18}$ isn't finished.

### Practice

**1.** $50^{1/2}$

> [!check]- Answer
> $(25 \cdot 2)^{1/2} = 5\sqrt{2}$

**2.** $200^{1/2}$

> [!check]- Answer
> $(100 \cdot 2)^{1/2} = 10\sqrt{2}$

**3.** $40^{1/3}$

> [!check]- Answer
> $(8 \cdot 5)^{1/3} = 2\sqrt[3]{5}$

**4.** $250^{1/3}$

> [!check]- Answer
> $(125 \cdot 2)^{1/3} = 5\sqrt[3]{2}$

**5.** $(x^3y^4)^{1/2}$

> [!check]- Answer
> $x^3$: 1 out, 1 in. $y^4$: 2 out, 0 in. → $xy^2\sqrt{x}$

**6.** $(8a^4b^2)^{1/3}$

> [!check]- Answer
> $8 \to 2$. $a^4$: 1 out, 1 in. $b^2$: 0 out, 2 in. → $2a\sqrt[3]{ab^2}$

**7.** $\sqrt{x} \cdot \sqrt[5]{x^2}$

> [!check]- Answer
> $x^{\frac{1}{2} + \frac{2}{5}} = x^{\frac{5}{10} + \frac{4}{10}} = x^{9/10} = \sqrt[10]{x^9}$

**8.** $(m^5n^9p^2)^{1/3}$

> [!check]- Answer
> $m^5$: 1 out, 2 in. $n^9$: 3 out, 0 in. $p^2$: 0 out, 2 in. → $mn^3\sqrt[3]{m^2p^2}$

---

## 4. Solving Equations with Rational Exponents

An **equation** says two things are equal. Solving it means finding the value of the variable that makes the statement true. The tool is **inverse operations**: whatever is being done to $x$, undo it - and do the same thing to both sides to keep things balanced.

The inverse of a rational exponent is its **reciprocal**, because $\left(x^{a/b}\right)^{b/a} = x^1 = x$.

> [!abstract] The method
> 1. **Isolate** the power term (get $x^{p/q}$ alone on one side).
> 2. **Raise both sides** to the reciprocal exponent $\frac{q}{p}$.
> 3. **Evaluate** - and decide whether you need $\pm$ (see below).
> 4. **Check** by plugging your answer back in.

> [!example] Solve $x^{1/2} + 3 = 10$
> Isolate: $x^{1/2} = 7$
> Reciprocal of $\frac{1}{2}$ is $2$: $x = 7^2 = 49$
> Check: $\sqrt{49} + 3 = 10$ ✓

> [!example] Solve $2x^{1/3} = 10$
> Isolate (divide by 2): $x^{1/3} = 5$
> Cube both sides: $x = 125$

> [!example] Solve $x^{3/2} = 27$
> Reciprocal of $\frac{3}{2}$ is $\frac{2}{3}$: $x = 27^{2/3} = \left(\sqrt[3]{27}\right)^2 = 3^2 = 9$

> [!example] Solve $x^{2/3} - 4 = 0$
> Isolate: $x^{2/3} = 4$
> Raise to $\frac{3}{2}$: $4^{3/2} = \left(\sqrt{4}\right)^3 = 8$
> But $x^{2/3}$ means "cube root, then **square**" - and squaring hides the sign. So $-8$ works too:
> $$\left((-8)^{1/3}\right)^2 = (-2)^2 = 4 \;✓$$
> $$x = \pm 8$$

> [!tip] When do you need $\pm$?
> Look at the **numerator** of the exponent in the original equation:
> - **Even numerator** ($x^{2/3}$, $x^{4/3}$, $x^{2/5}$) → there's a hidden square, so the answer is **$\pm$**.
> - **Odd numerator** ($x^{1/3}$, $x^{3/2}$, $x^{3/4}$) → **one** answer.

> [!tip] Evaluate root first, power second
> $16^{3/4}$ is much easier as $\left(\sqrt[4]{16}\right)^3 = 2^3 = 8$ than as $\sqrt[4]{16^3} = \sqrt[4]{4096}$. Same answer, smaller numbers.

### Practice

**1.** $x^{1/2} - 6 = 0$

> [!check]- Answer
> $x^{1/2} = 6 \Rightarrow x = 36$

**2.** $x^{1/3} + 1 = 5$

> [!check]- Answer
> $x^{1/3} = 4 \Rightarrow x = 4^3 = 64$

**3.** $3x^{1/4} = 6$

> [!check]- Answer
> $x^{1/4} = 2 \Rightarrow x = 2^4 = 16$

**4.** $x^{2/3} = 25$

> [!check]- Answer
> Even numerator → $\pm$. $x = \pm 25^{3/2} = \pm\left(\sqrt{25}\right)^3 = \pm 125$

**5.** $x^{3/4} = 8$

> [!check]- Answer
> Odd numerator → one answer. $x = 8^{4/3} = \left(\sqrt[3]{8}\right)^4 = 2^4 = 16$

**6.** $(x^2)^{1/5} - 4 = 0$

> [!check]- Answer
> Simplify: $x^{2/5} = 4$. Even numerator → $x = \pm 4^{5/2} = \pm\left(\sqrt{4}\right)^5 = \pm 32$

**7.** $x^{4/3} - 3 = 78$

> [!check]- Answer
> $x^{4/3} = 81$. Even numerator → $x = \pm 81^{3/4} = \pm\left(\sqrt[4]{81}\right)^3 = \pm 27$

---

## Module Review Quiz

**1.** Translate "seven less than three times a number."

> [!check]- Answer
> $3x - 7$

**2.** Translate "the quotient of a number and the difference of that number and 2."

> [!check]- Answer
> $\dfrac{x}{x - 2}$

**3.** Simplify $98^{1/2}$.

> [!check]- Answer
> $(49 \cdot 2)^{1/2} = 7\sqrt{2}$

**4.** Simplify $(27x^6y^2)^{1/3}$.

> [!check]- Answer
> $3x^2\sqrt[3]{y^2}$

**5.** Solve $x^{1/3} - 4 = -1$.

> [!check]- Answer
> $x^{1/3} = 3 \Rightarrow x = 27$

**6.** Solve $x^{2/3} = 49$.

> [!check]- Answer
> $x = \pm 49^{3/2} = \pm 7^3 = \pm 343$
