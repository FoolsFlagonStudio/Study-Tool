---
title: Exponential Functions and Transformations
section: 3 - Exponentials, Logarithms, and Sequences
module: 8
status: draft
topics: [identifying-exponentials, evaluating-exponentials, exponential-graphs, logarithmic-form, evaluating-logarithms, solving-exponential-equations, compound-interest]
---

# Module 8: Exponential Functions and Transformations

**By the end of this module you can:** tell an exponential function apart from a power or linear one, evaluate and graph exponential functions (including shifted, stretched, and flipped ones), switch between exponential and logarithmic form, evaluate common and natural logs, solve exponential equations with logarithms, and use compound-interest and continuous-growth formulas.

> [!info] Why this matters
> A linear function adds the same amount each step. An exponential function **multiplies** by the same amount each step. That one change describes money earning interest, populations growing, medicine leaving the bloodstream, and radioactive material decaying. Logarithms are the tool that undoes exponentials, so you can answer questions like "how long until this doubles?"

---

## 1. What Makes a Function Exponential

$$f(x) = b^x \qquad b > 0,\ b \ne 1$$

In an exponential function, the **variable is in the exponent** and the base is a fixed number.

| Type | Form | Example | Each step of +1 in $x$... |
|---|---|---|---|
| Linear | $mx + b$ | $6x$ | **adds** the same amount (6) |
| Power | $x^a$ | $x^6$ | neither; the variable is the base |
| Exponential | $b^x$ | $6^x$ | **multiplies** by the same factor (6) |

> [!example] Linear vs. exponential, step by step
> | $x$ | 0 | 1 | 2 | 3 | 4 |
> |---|---|---|---|---|---|
> | $3x$ | 0 | 3 | 6 | 9 | 12 |
> | $3^x$ | 1 | 3 | 9 | 27 | 81 |
>
> The linear row goes up by 3 each time. The exponential row is multiplied by 3 each time, and it pulls away fast.

**Why the restrictions on $b$?** If $b = 1$, then $1^x = 1$ is just a flat line. If $b$ were negative, values like $(-4)^{1/2}$ wouldn't be real numbers.

**Growth or decay** depends only on the base:
- $b > 1$: **exponential growth** - increasing.
- $0 < b < 1$: **exponential decay** - decreasing.

> [!warning] Growth is $b > 1$, not $b > 0$
> Every exponential base is positive. A base of 0.3 is positive but gives decay.

> [!tip] Exponential beats power - eventually
> $x^6$ is bigger than $6^x$ for some small $x$ (at $x = 2$: 64 vs. 36). But by $x = 10$, $6^{10} \approx 60$ million and $10^6 = 1$ million. An exponential with $b > 1$ always wins in the long run.

### Practice

**1.** Classify: $f(x) = 6^x$, $g(x) = x^6$, $h(x) = 6x$.

> [!check]- Answer
> Exponential, power, linear.

**2.** Growth or decay: $f(x) = (0.3)^x$? $g(x) = 3(1.5)^x$?

> [!check]- Answer
> $0.3 < 1$: decay. $1.5 > 1$: growth (the 3 in front doesn't change that).

**3.** Is $f(x) = \left(\frac{7}{4}\right)^x$ growth or decay?

> [!check]- Answer
> Growth - $\frac{7}{4} = 1.75 > 1$.

---

## 2. Evaluating Exponential Functions

Substitute the input into the exponent and simplify. Two exponent rules do most of the work:

- $b^0 = 1$ for any allowed base.
- A negative exponent flips the base: $b^{-n} = \frac{1}{b^n}$, and $\left(\frac{p}{q}\right)^{-n} = \left(\frac{q}{p}\right)^n$.

> [!example] $f(x) = 3^x$ at $x = -2$
> $3^{-2} = \frac{1}{3^2} = \frac{1}{9}$

> [!example] $g(x) = \left(\frac{2}{5}\right)^x$ at $x = -2$
> Flip and square: $\left(\frac{5}{2}\right)^2 = \frac{25}{4} = 6.25$

> [!example] $h(x) = 4 \cdot 2^{x - 1} + 1$ at $x = 3$ and $x = 0$
> Order of operations: exponent first, then multiply, then add.
> $h(3) = 4 \cdot 2^2 + 1 = 17$
> $h(0) = 4 \cdot 2^{-1} + 1 = 2 + 1 = 3$

> [!warning] Don't multiply the base by the coefficient first
> $4 \cdot 2^2$ is $4 \cdot 4 = 16$, not $8^2 = 64$.

### Practice

**1.** $6^{-1}$

> [!check]- Answer
> $\frac{1}{6}$

**2.** $\left(\frac{1}{3}\right)^{-3}$

> [!check]- Answer
> $3^3 = 27$

**3.** $f(x) = 2 \cdot 3^x - 5$ at $x = 2$

> [!check]- Answer
> $2 \cdot 9 - 5 = 13$

**4.** $f(x) = 10^{x + 2}$ at $x = -4$

> [!check]- Answer
> $10^{-2} = 0.01$

---

## 3. Graphs and Key Points

Every basic exponential $f(x) = b^x$ has the same skeleton:

| Feature | Value |
|---|---|
| Domain | all real numbers |
| Range | $y > 0$ |
| Horizontal asymptote | $y = 0$ (the curve gets close, never touches) |
| $y$-intercept | $(0, 1)$ |
| Key points | $\left(-1, \frac{1}{b}\right)$, $(0, 1)$, $(1, b)$ |

$b^x$ and $\left(\frac{1}{b}\right)^x$ are mirror images across the $y$-axis, since $\left(\frac{1}{b}\right)^x = b^{-x}$.

### The transformed form

$$f(x) = a \cdot b^{x - h} + k$$

Each letter does one job, exactly like the transformations in Module 7:

| Letter | Effect | Changes |
|---|---|---|
| $k$ | shift up/down | asymptote $\to y = k$; range |
| $h$ | shift right/left (backwards from the sign) | where the key points sit on the $x$-axis |
| $a$ | stretch/compress; $a < 0$ flips over the asymptote | the $y$-values of key points; range direction if negative |

> [!abstract] Graphing $a \cdot b^{x - h} + k$
> 1. Draw the asymptote $y = k$.
> 2. Find the $x$-values that make the **exponent** $-1$, $0$, and $1$ (that's $x = h - 1$, $h$, $h + 1$).
> 3. Evaluate the function there to get three key points.
> 4. Sketch a smooth curve through them that hugs $y = k$.
> 5. Domain: all real numbers. Range: $y > k$ if $a > 0$, $y < k$ if $a < 0$.

> [!example] $f(x) = 2 \cdot 3^{x - 4} - 1$
> Asymptote $y = -1$. Exponent $x - 4$ is $-1, 0, 1$ at $x = 3, 4, 5$.
> $f(3) = 2 \cdot \frac{1}{3} - 1 = -\frac{1}{3}$, $f(4) = 2 - 1 = 1$, $f(5) = 6 - 1 = 5$.
> Key points $\left(3, -\frac{1}{3}\right)$, $(4, 1)$, $(5, 5)$. Range $y > -1$.

> [!example] $g(x) = -\left(\frac{1}{2}\right)^x + 6$
> Asymptote $y = 6$. $a = -1$ flips it below the asymptote.
> $g(-1) = -2 + 6 = 4$, $g(0) = -1 + 6 = 5$, $g(1) = -\frac{1}{2} + 6 = 5.5$.
> Range $y < 6$.

> [!tip] The asymptote is just $k$
> Horizontal shifts and stretches never move it. Only adding or subtracting outside does.

### Practice

**1.** $f(x) = 5^x + 2$: asymptote and key points?

> [!check]- Answer
> $y = 2$; $(-1, 2.2)$, $(0, 3)$, $(1, 7)$.

**2.** $f(x) = 3^{x + 2}$: key points?

> [!check]- Answer
> Exponent $-1, 0, 1$ at $x = -3, -2, -1$: $\left(-3, \frac{1}{3}\right)$, $(-2, 1)$, $(-1, 3)$. Asymptote $y = 0$.

**3.** $f(x) = -2 \cdot 4^x$: range and key points?

> [!check]- Answer
> Range $y < 0$. $(-1, -0.5)$, $(0, -2)$, $(1, -8)$.

**4.** $f(x) = (0.5)^{x - 1} - 3$: growth or decay, asymptote, key points?

> [!check]- Answer
> Decay. Asymptote $y = -3$. $(0, -1)$, $(1, -2)$, $(2, -2.5)$.

---

## 4. Logarithms: Asking for the Exponent

A logarithm answers one question: **what exponent turns the base into this number?**

$$\log_b(x) = y \quad\Longleftrightarrow\quad b^y = x$$

So $\log_2 32 = 5$ because $2^5 = 32$. The log's answer **is** the exponent.

Because they swap input and output, $y = \log_b x$ and $y = b^x$ are inverse functions.

> [!tip] Converting either way
> The base stays the base. The number by itself on one side of the exponential equation goes inside the log. The exponent becomes the answer of the log.

> [!example] Exponential → log
> $5^3 = 125 \;\Rightarrow\; \log_5 125 = 3$
> $2^{-4} = \frac{1}{16} \;\Rightarrow\; \log_2 \frac{1}{16} = -4$

> [!example] Log → exponential
> $\log_9 3 = \frac{1}{2} \;\Rightarrow\; 9^{1/2} = 3$

### Practice

**1.** Write $10^4 = 10{,}000$ in log form.

> [!check]- Answer
> $\log_{10} 10{,}000 = 4$, or $\log 10{,}000 = 4$.

**2.** Write $p^q = r$ in log form.

> [!check]- Answer
> $\log_p r = q$

**3.** Write $\log_3 \frac{1}{9} = -2$ in exponential form.

> [!check]- Answer
> $3^{-2} = \frac{1}{9}$

**4.** Write $\ln 7.389 \approx 2$ in exponential form.

> [!check]- Answer
> $e^2 \approx 7.389$

---

## 5. Evaluating Logarithms

**By recognizing a power:** $\log_5 125$ asks "5 to what power is 125?" $5^3 = 125$, so it's 3.

**With a shared base**, when the answer isn't a whole number: write both numbers as powers of one base and match exponents.

> [!example] $\log_8 4$
> $8^y = 4 \Rightarrow 2^{3y} = 2^2 \Rightarrow 3y = 2 \Rightarrow y = \frac{2}{3}$

> [!example] $\log_4 \frac{1}{64}$
> $\frac{1}{64} = 4^{-3}$, so the answer is $-3$.

### Two special logs

| Name | Written | Means | Undoes |
|---|---|---|---|
| Common log | $\log x$ | $\log_{10} x$ | $10^x$ |
| Natural log | $\ln x$ | $\log_e x$ ($e \approx 2.718$) | $e^x$ |

- $\log 10^n = n$: for powers of 10, count the places the decimal moves from 1. $\log 1{,}000 = 3$ and $\log 0.001 = -3$.
- $\ln e^n = n$: $\ln e^{-5} = -5$.
- The log of 1 is always 0 (in any base, $b^0 = 1$), so $\ln 1 = \log 1 = 0$.
- Anything else, use the calculator's LOG or LN key.

### Practice

**1.** $\log_9 27$

> [!check]- Answer
> $3^{2y} = 3^3$, so $y = \frac{3}{2}$.

**2.** $\log 0.001$ and $\log 100{,}000$

> [!check]- Answer
> $-3$ and $5$

**3.** $\ln e^{-5}$ and $\ln 1$

> [!check]- Answer
> $-5$ and $0$

**4.** On a calculator: $\ln 20$ and $\log 500$ (four decimal places).

> [!check]- Answer
> $2.9957$ and $2.6990$

---

## 6. Solving Exponential Equations

When the variable is stuck in an exponent, take a log of both sides and use the **power rule** to bring it down:

$$\log_b(M^n) = n \log_b(M)$$

> [!abstract] The method
> 1. Isolate the exponential part (divide away coefficients, move constants).
> 2. Take $\ln$ of both sides (or $\log$ if a base is 10).
> 3. Power rule: bring each exponent down in front as a multiplier.
> 4. Solve the linear equation for $x$: gather $x$-terms, factor out $x$, divide.
> 5. Calculator last.

> [!example] $3^x = 20$
> $x \ln 3 = \ln 20 \Rightarrow x = \frac{\ln 20}{\ln 3} \approx 2.727$

> [!example] $4^{x + 1} = 7^x$
> $(x + 1)\ln 4 = x \ln 7$
> $x \ln 4 + \ln 4 = x \ln 7$
> $\ln 4 = x(\ln 7 - \ln 4)$
> $x = \frac{\ln 4}{\ln 7 - \ln 4} \approx 2.477$

> [!example] $10^x = 6^{x - 2}$
> A base is 10, so use $\log$: $x = (x - 2)\log 6$
> $x - x\log 6 = -2\log 6 \Rightarrow x = \frac{-2\log 6}{1 - \log 6} \approx -7.015$

> [!warning] Isolate first
> For $3 \cdot 2^x = 48$, divide by 3 before taking logs: $2^x = 16$, so $x = 4$. Taking the log of $3 \cdot 2^x$ directly needs a rule from Module 9.

### Practice

**1.** $5^x = 40$

> [!check]- Answer
> $x = \frac{\ln 40}{\ln 5} \approx 2.292$

**2.** $2^{x - 3} = 9$

> [!check]- Answer
> $x - 3 = \frac{\ln 9}{\ln 2} \approx 3.170$, so $x \approx 6.170$

**3.** $6^x = 2^{x + 4}$

> [!check]- Answer
> $x(\ln 6 - \ln 2) = 4\ln 2 \Rightarrow x = \frac{4\ln 2}{\ln 6 - \ln 2} \approx 2.524$

**4.** $3 \cdot 2^x = 48$

> [!check]- Answer
> $2^x = 16$, $x = 4$

---

## 7. Compound Interest and the Number $e$

| Situation | Formula |
|---|---|
| Simple interest (no compounding) | $A = P + Prt$ |
| Compounded $n$ times a year | $A = P\left(1 + \frac{r}{n}\right)^{nt}$ |
| Compounded continuously / natural growth | $A = Pe^{rt}$ |
| Continuous decay | $A = Pe^{rt}$ with $r < 0$ |

$P$ = starting amount, $r$ = annual rate **as a decimal**, $t$ = years (or whatever time unit the rate uses), $n$ = compounding periods per year.

**Where $e$ comes from:** if $1 earns 100% a year, compounded $n$ times, you end with $\left(1 + \frac{1}{n}\right)^n$. As $n$ grows - monthly, daily, every second - the result levels off at $e \approx 2.71828$. That's why $e$ shows up for anything that grows continuously.

More compounding always earns more, but with diminishing returns.

> [!example] $2,000 at 4% for 5 years
> - Annually: $2{,}000(1.04)^5 \approx \$2{,}433.31$
> - Monthly: $2{,}000\left(1 + \frac{0.04}{12}\right)^{60} \approx \$2{,}441.99$
> - Continuously: $2{,}000e^{0.2} \approx \$2{,}442.81$

> [!example] Decay: 80 grams of a substance with $r = -0.05$ per year, after 10 years
> $A = 80e^{-0.05(10)} = 80e^{-0.5} \approx 48.52$ grams

> [!warning] Common mistakes
> - Using 6 instead of 0.06 for 6%.
> - Forgetting to multiply $t$ by $n$ in the exponent.
> - Mixing units: a rate per hour needs time in hours (one day = 24).

### Practice

**1.** $5,000 at 6% compounded quarterly for 8 years?

> [!check]- Answer
> $5{,}000(1.015)^{32} \approx \$8{,}051.62$

**2.** $1,200 at 3.5% compounded continuously for 10 years?

> [!check]- Answer
> $1{,}200e^{0.35} \approx \$1{,}702.88$

**3.** A town of 3,000 grows continuously at 2% per year. Population after 15 years?

> [!check]- Answer
> $3{,}000e^{0.3} \approx 4{,}050$

**4.** 500 mg of a drug leaves the body at a continuous rate of 12% per hour. How much is left after 6 hours?

> [!check]- Answer
> $500e^{-0.72} \approx 243.38$ mg

---

## Module Review Quiz

**1.** Is $f(x) = 0.9^x$ growth or decay?

> [!check]- Answer
> Decay

**2.** Evaluate $f(x) = 3 \cdot 2^{x + 1}$ at $x = -3$.

> [!check]- Answer
> $3 \cdot 2^{-2} = \frac{3}{4}$

**3.** $f(x) = 4^{x - 2} + 5$: asymptote, key points, range?

> [!check]- Answer
> $y = 5$; $(1, 5.25)$, $(2, 6)$, $(3, 9)$; $y > 5$.

**4.** Write $7^{-1} = \frac{1}{7}$ in log form.

> [!check]- Answer
> $\log_7 \frac{1}{7} = -1$

**5.** Evaluate $\log_{25} 125$.

> [!check]- Answer
> $5^{2y} = 5^3$, $y = \frac{3}{2}$

**6.** Evaluate $\log 0.0001$ and $\ln e^7$.

> [!check]- Answer
> $-4$ and $7$

**7.** Solve $2^{x + 2} = 5^x$.

> [!check]- Answer
> $x = \frac{2\ln 2}{\ln 5 - \ln 2} \approx 1.513$

**8.** $10,000 at 5% compounded monthly for 3 years?

> [!check]- Answer
> $10{,}000\left(1 + \frac{0.05}{12}\right)^{36} \approx \$11{,}614.72$

**9.** A sample of 200 bacteria grows continuously at 8% per hour. How many after 12 hours?

> [!check]- Answer
> $200e^{0.96} \approx 522$

