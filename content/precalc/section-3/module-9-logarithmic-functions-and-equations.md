---
title: Logarithmic Functions and Equations
section: 3 - Exponentials, Logarithms, and Sequences
module: 9
status: draft
topics: [log-graph-features, log-graph-points, change-of-base, inverse-properties, expanding-logs, condensing-logs, solving-log-equations, log-applications]
---

# Module 9: Logarithmic Functions and Equations

**By the end of this module you can:** graph logarithmic functions and their shifts, find their asymptotes, intercepts, domain and range, follow points through a shift, use change of base and the inverse properties, expand and condense logs with the product, quotient, and power rules, solve logarithmic equations (and spot extraneous solutions), and work with decibels, pH, and earthquake magnitudes.

> [!info] Why this matters
> Module 8 introduced the log as "the exponent you need." This module treats it as a full function with its own graph, rules, and equations. Logs compress huge ranges into small numbers: a sound a trillion times louder than silence is just 120 decibels, and an earthquake 1,000 times stronger is only 3 points higher on the Richter scale.

> [!tip] Quick review from Module 8
> $\log_b x = y$ means $b^y = x$. $\log x$ means base 10; $\ln x$ means base $e$.

---

## 1. Logarithms and Their Graphs

$y = \log_b x$ is the inverse of $y = b^x$, so its graph is the reflection of the exponential across the line $y = x$, and **domain and range swap**.

| | $y = b^x$ | $y = \log_b x$ |
|---|---|---|
| Domain | all real numbers | $x > 0$ |
| Range | $y > 0$ | all real numbers |
| Asymptote | horizontal, $y = 0$ | **vertical, $x = 0$** |
| Key points | $\left(-1, \frac{1}{b}\right)$, $(0, 1)$, $(1, b)$ | $\left(\frac{1}{b}, -1\right)$, $(1, 0)$, $(b, 1)$ |
| Intercept | $y$-intercept $(0, 1)$ | $x$-intercept $(1, 0)$ |

- $b > 1$: increasing. $0 < b < 1$: decreasing.
- You **can't take the log of zero or a negative number.** That's the domain restriction, and it's behind every "check your answer" step later.

**Graph a log by swapping coordinates:** if $(c, d)$ is on $y = b^x$, then $(d, c)$ is on $y = \log_b x$.

**Find the base from a point:** if $(x, y)$ is on $y = \log_b x$, solve $b^y = x$. Through $(8, 3)$: $b^3 = 8$, so $b = 2$.

### Shifted logs

$$f(x) = \log_b(x - h) + k$$

- **Inside** (horizontal): the asymptote moves to $x = h$ and the domain becomes $x > h$.
- **Outside** (vertical): everything moves up or down; the asymptote and domain don't change.
- The range is always all real numbers.

> [!abstract] Features of $\log_b(x - h) + k$
> - Vertical asymptote: set the inside equal to 0, giving $x = h$.
> - Domain: inside $> 0$, giving $x > h$.
> - A key point: inside $= 1$ gives $(h + 1, k)$, because $\log_b 1 = 0$.
> - $x$-intercept: set $f(x) = 0$ and solve.

> [!example] $f(x) = \log_3(x - 2) + 1$
> Asymptote $x = 2$. Domain $x > 2$. Key points $(3, 1)$ (inside = 1) and $(5, 2)$ (inside = 3).
> $x$-intercept: $\log_3(x - 2) = -1 \Rightarrow x - 2 = \frac{1}{3} \Rightarrow x = \frac{7}{3}$.

> [!example] $g(x) = \log_{1/2}(x + 4)$
> Decreasing (base less than 1). Asymptote $x = -4$. $x$-intercept $(-3, 0)$, where the inside equals 1.

### Practice

**1.** $f(x) = \log_5(x + 3)$: asymptote, domain, $x$-intercept?

> [!check]- Answer
> $x = -3$; $x > -3$; $(-2, 0)$

**2.** $f(x) = \log x - 2$: asymptote and $x$-intercept?

> [!check]- Answer
> $x = 0$ (a vertical shift doesn't move it). $\log x = 2 \Rightarrow x = 100$: $(100, 0)$.

**3.** An increasing log graph $y = \log_b x$ passes through $(8, 3)$. Find $b$.

> [!check]- Answer
> $b^3 = 8$, $b = 2$

**4.** A decreasing log graph passes through $(25, -2)$. Find $b$.

> [!check]- Answer
> $b^{-2} = 25 \Rightarrow b^2 = \frac{1}{25} \Rightarrow b = \frac{1}{5}$

---

## 2. Following Points Through a Shift

For $\log_b(x - h) + k$:
- Inside shift: add $h$ to the $x$-coordinate (right if $h > 0$).
- Outside shift: add $k$ to the $y$-coordinate.

> [!example] $(27, 3)$ is on $\log_3 x$. Where is it on $\log_3(x + 5) - 2$?
> Left 5, down 2: $(22, 1)$. Check: $\log_3(22 + 5) - 2 = 3 - 2 = 1$ ✓

> [!example] $\left(\frac{1}{4}, -2\right)$ is on $\log_2 x$. Where is it on $\log_2(x - 3) + 6$?
> $\left(\frac{13}{4}, 4\right)$

### Practice

**1.** $(49, 2)$ on $\log_7 x$ → $\log_7(x - 1)$?

> [!check]- Answer
> $(50, 2)$

**2.** $(100, 2)$ on $\log x$ → $\log x - 5$?

> [!check]- Answer
> $(100, -3)$

**3.** $(16, 4)$ on $\log_2 x$ → $\log_2(x + 10) + 1$?

> [!check]- Answer
> $(6, 5)$

---

## 3. Change of Base

Calculators only have LOG (base 10) and LN (base $e$). For any other base:

$$\log_a M = \frac{\log M}{\log a} = \frac{\ln M}{\ln a}$$

**The number you're taking the log of goes on top.** Either LOG or LN works - the answer is the same.

> [!example] $\log_3 50$
> $\frac{\ln 50}{\ln 3} \approx \frac{3.912}{1.099} \approx 3.561$. Sanity check: $3^3 = 27$ and $3^4 = 81$, so it should be between 3 and 4 ✓.

> [!example] $\log_{1/2} 10$
> $\frac{\log 10}{\log 0.5} = \frac{1}{-0.301} \approx -3.322$. Negative makes sense: a base below 1 needs a negative exponent to make a big number.

### Practice

**1.** $\log_7 2$ (three decimals)

> [!check]- Answer
> $\approx 0.356$

**2.** $\log_6 200$

> [!check]- Answer
> $\approx 2.957$

**3.** $\log_9 3$ - by change of base, then without a calculator.

> [!check]- Answer
> $\frac{\ln 3}{\ln 9} = 0.5$. Without one: $9^{1/2} = 3$.

---

## 4. Inverse Properties

A log and an exponential with the **same base** cancel:

$$b^{\log_b x} = x \qquad\qquad \log_b\left(b^x\right) = x$$

So $10^{\log 7} = 7$, $e^{\ln 2} = 2$, and $\log_5 5^9 = 9$.

To use the second one, rewrite the argument as a power of the base - including fractions and roots:
- $\frac{1}{b^n} = b^{-n}$
- $\sqrt[n]{b} = b^{1/n}$

> [!example] $\log_2\frac{1}{32}$
> $\frac{1}{32} = 2^{-5}$, so the answer is $-5$.

> [!example] $\log_5\sqrt{5}$
> $\sqrt{5} = 5^{1/2}$, so the answer is $\frac{1}{2}$.

### Practice

**1.** $7^{\log_7 11}$

> [!check]- Answer
> $11$

**2.** $e^{\ln 4.2}$ and $10^{\log 0.7}$

> [!check]- Answer
> $4.2$ and $0.7$

**3.** $\ln e^{-3}$

> [!check]- Answer
> $-3$

**4.** $\log_4\sqrt[3]{4}$

> [!check]- Answer
> $\frac{1}{3}$

---

## 5. Expanding Logarithms

Logs turn multiplication into addition, division into subtraction, and powers into multipliers:

| Rule | Formula |
|---|---|
| Product | $\log_b(MN) = \log_b M + \log_b N$ |
| Quotient | $\log_b\left(\frac{M}{N}\right) = \log_b M - \log_b N$ |
| Power | $\log_b(M^n) = n\log_b M$ |

These come straight from exponent rules ($b^m b^n = b^{m + n}$, and so on), because logs **are** exponents.

> [!abstract] Expanding
> 1. Rewrite roots as fractional exponents.
> 2. Quotient rule: numerator minus denominator.
> 3. Product rule: split each product into a sum.
> 4. Power rule: bring exponents to the front.
> 5. Evaluate any plain-number logs you can ($\log_2 8 = 3$).

> [!example] $\log_2\left(\frac{8x^3}{y}\right)$
> $\log_2 8 + \log_2 x^3 - \log_2 y = 3 + 3\log_2 x - \log_2 y$

> [!example] $\ln\left(\frac{x^2\sqrt{y}}{z^5}\right)$
> $2\ln x + \frac{1}{2}\ln y - 5\ln z$

> [!warning] The traps
> - $\log(x + y)$ **cannot** be split. There's no rule for the log of a sum.
> - $(\log x)^2$ is not $2\log x$. The power rule needs the exponent **inside** on the argument.
> - Everything in the denominator gets a minus sign: $\log\frac{x}{9y^2} = \log x - \log 9 - 2\log y$.

### Practice

**1.** $\log(100a^4)$

> [!check]- Answer
> $2 + 4\log a$

**2.** $\log_3\left(\frac{x}{9y^2}\right)$

> [!check]- Answer
> $\log_3 x - 2 - 2\log_3 y$

**3.** $\ln\left(\frac{\sqrt{x + 1}}{x^3}\right)$

> [!check]- Answer
> $\frac{1}{2}\ln(x + 1) - 3\ln x$

---

## 6. Condensing Logarithms

Run the rules backwards to make one log. The logs must have the **same base**.

> [!abstract] Condensing
> 1. Power rule first: move coefficients up into exponents ($2\log a = \log a^2$).
> 2. Then gather: added terms multiply in the numerator; subtracted terms go in the denominator.
> 3. Simplify the argument.

> [!example] $\log 5 + \log 20$
> $\log 100 = 2$

> [!example] $2\log_3 6 - \log_3 4$
> $\log_3\frac{36}{4} = \log_3 9 = 2$

> [!example] $3\ln x - \ln y + \frac{1}{2}\ln z$
> $\ln\left(\frac{x^3\sqrt{z}}{y}\right)$

### Practice

**1.** $\log 2 + \log 50$

> [!check]- Answer
> $\log 100 = 2$

**2.** $\log_2 48 - \log_2 3$

> [!check]- Answer
> $\log_2 16 = 4$

**3.** $2\log a + 3\log b$

> [!check]- Answer
> $\log(a^2 b^3)$

**4.** $\ln 12 - 2\ln 2$

> [!check]- Answer
> $\ln\frac{12}{4} = \ln 3$

---

## 7. Solving Logarithmic Equations

Three patterns cover almost everything:

| The equation looks like | Do this |
|---|---|
| $\log_b(\text{stuff}) = \text{number}$ | rewrite as $\text{stuff} = b^{\text{number}}$ |
| $\log_b(A) = \log_b(B)$ | set $A = B$ (one-to-one property) |
| several logs on a side | **condense first**, then use one of the above |

> [!warning] Always check
> Plug each answer back into the **original** equation. If any argument becomes zero or negative, that answer is **extraneous** - throw it out.

> [!example] $\log_3(4x - 1) = 2$
> $4x - 1 = 9$, $x = 2.5$. Check: $4(2.5) - 1 = 9 > 0$ ✓

> [!example] $\ln(x^2 - 4x) = \ln 5$
> $x^2 - 4x - 5 = 0 \Rightarrow x = 5$ or $x = -1$.
> Both make $x^2 - 4x = 5 > 0$, so **both** work.

> [!example] $\log(x + 3) + \log x = 1$
> Condense: $\log(x^2 + 3x) = 1 \Rightarrow x^2 + 3x = 10 \Rightarrow x^2 + 3x - 10 = 0 \Rightarrow x = 2$ or $x = -5$.
> $x = -5$ makes $\log x$ undefined. The only solution is $x = 2$.

> [!example] $\log_2(x + 6) - \log_2 x = 2$
> $\log_2\frac{x + 6}{x} = 2 \Rightarrow \frac{x + 6}{x} = 4 \Rightarrow x + 6 = 4x \Rightarrow x = 2$

### Practice

**1.** $\log_4(2x + 8) = 3$

> [!check]- Answer
> $2x + 8 = 64$, $x = 28$

**2.** $\log(x^2 - 15) = \log(2x)$

> [!check]- Answer
> $x^2 - 2x - 15 = 0$: $x = 5$ or $x = -3$. Only $5$ works.

**3.** $\log_2 x + \log_2(x + 2) = 3$

> [!check]- Answer
> $x^2 + 2x = 8$: $x = 2$ ($-4$ is extraneous).

**4.** $\ln(x + 1) - \ln 3 = \ln 6$

> [!check]- Answer
> $\frac{x + 1}{3} = 6$, $x = 17$

---

## 8. Logarithms in the Real World

Each of these scales uses the common log to squeeze a huge range into small numbers.

| Scale | Formula | One step means |
|---|---|---|
| Richter (earthquakes) | magnitude difference $d$ ⇒ $10^d$ times stronger | ×10 |
| Decibels (sound) | $\text{dB} = 10\log\left(\frac{I}{I_0}\right)$ | ×10 intensity = +10 dB |
| pH (acidity) | $\text{pH} = -\log[\text{H}^+] = \log\frac{1}{[\text{H}^+]}$ | ×10 acidity = −1 pH |

$I_0$ is the quietest sound people can hear, so $\frac{I}{I_0}$ is "how many times the threshold." For pH, below 7 is acidic and above 7 is alkaline.

> [!example] Earthquakes
> A magnitude 8.3 quake vs. a 6.3: $10^{8.3 - 6.3} = 10^2 = 100$ times stronger.

> [!example] A lawn mower at $10^9$ times the threshold
> $10\log 10^9 = 10(9) = 90$ dB

> [!example] pH of a solution with $[\text{H}^+] = 0.00032$
> $-\log(0.00032) \approx 3.49$, acidic.

### Practice

**1.** A sound $10^{11}$ times the threshold?

> [!check]- Answer
> $110$ dB

**2.** How many times stronger is a magnitude 7.5 quake than a 5.5?

> [!check]- Answer
> $10^2 = 100$

**3.** pH when $[\text{H}^+] = 10^{-8}$? Acidic or alkaline?

> [!check]- Answer
> $8$, alkaline

**4.** A magnitude 7 vs. a magnitude 4?

> [!check]- Answer
> $10^3 = 1{,}000$ times stronger

---

## Module Review Quiz

**1.** $f(x) = \log_2(x + 6) - 3$: asymptote and domain?

> [!check]- Answer
> $x = -6$; $x > -6$

**2.** $(9, 2)$ is on $\log_3 x$. Where is it on $\log_3(x - 4) + 1$?

> [!check]- Answer
> $(13, 3)$

**3.** $\log_5 80$ to three decimals.

> [!check]- Answer
> $\frac{\ln 80}{\ln 5} \approx 2.723$

**4.** $\log_6\frac{1}{36}$ and $8^{\log_8 3}$

> [!check]- Answer
> $-2$ and $3$

**5.** Expand $\log\left(\frac{10x^5}{\sqrt{y}}\right)$.

> [!check]- Answer
> $1 + 5\log x - \frac{1}{2}\log y$

**6.** Condense $2\log_4 8 - \log_4 2$.

> [!check]- Answer
> $\log_4\frac{64}{2} = \log_4 32 = \frac{5}{2}$

**7.** Solve $\log_5(x - 3) + \log_5(x + 1) = 1$.

> [!check]- Answer
> $(x - 3)(x + 1) = 5 \Rightarrow x^2 - 2x - 8 = 0 \Rightarrow x = 4$ or $x = -2$. Only $x = 4$ works.

**8.** A rock concert is 120 dB. How many times the threshold intensity is it?

> [!check]- Answer
> $10\log k = 120 \Rightarrow \log k = 12 \Rightarrow k = 10^{12}$

