---
title: Sequences and Series
section: 3 - Exponentials, Logarithms, and Sequences
module: 10
status: draft
topics: [sequence-terms, arithmetic-sequences, geometric-sequences, summation-notation, arithmetic-series, geometric-series]
---

# Module 10: Sequences and Series

**By the end of this module you can:** find terms of a sequence from its formula (and a formula from its terms), recognize arithmetic and geometric sequences, write their $n$th-term formulas (even from just two terms), read and evaluate sigma notation, and add up arithmetic and geometric series - including money and growth problems.

> [!info] Why this matters
> A sequence is just a numbered list: savings each month, seats in each row, a population each year. Arithmetic sequences are the list version of linear functions (add the same amount). Geometric sequences are the list version of exponential functions (multiply by the same amount). A series adds the list up - total savings, total seats, total earnings.

---

## 1. Sequences and Their Terms

A **sequence** is an ordered list that keeps going: $a_1, a_2, a_3, \ldots$ Formally it's a function whose inputs are the positive integers $1, 2, 3, \ldots$. The **$n$th term**, $a_n$, is the output for input $n$.

**From formula to terms:** substitute $n$.

> [!example] $a_n = 4n - 3$
> $a_1 = 1$, $a_2 = 5$, $a_3 = 9$, $a_4 = 13$, $a_5 = 17$, and $a_{10} = 37$.

**From terms to formula:** compare each term with its position.

| $n$ | 1 | 2 | 3 | 4 | Pattern | $a_n$ |
|---|---|---|---|---|---|---|
| | 3 | 6 | 9 | 12 | 3 times the position | $3n$ |
| | 2 | 5 | 10 | 17 | one more than a square | $n^2 + 1$ |
| | 0 | 2 | 6 | 12 | product of consecutive numbers | $n(n - 1)$ |
| | $\frac{1}{2}$ | $\frac{1}{4}$ | $\frac{1}{8}$ | $\frac{1}{16}$ | halving | $\left(\frac{1}{2}\right)^n$ |

> [!warning] Check more than one term
> $2, 4, \ldots$ could be $2n$ or $2^n$ - they split at the 3rd term (6 vs. 8). Always test your formula on several terms.

### Practice

**1.** $a_n = n^2 - 2n$. Find $a_6$.

> [!check]- Answer
> $36 - 12 = 24$

**2.** Formula for $5, 10, 15, 20, \ldots$?

> [!check]- Answer
> $a_n = 5n$

**3.** Formula for $0, 3, 8, 15, 24, \ldots$?

> [!check]- Answer
> $a_n = n^2 - 1$

---

## 2. Arithmetic Sequences

**Add the same number $d$ each time.** $d$ is the **common difference** - subtract any term from the next one.

$$a_n = a_1 + (n - 1)d$$

Why $n - 1$? To get from the 1st term to the $n$th, you add $d$ only $n - 1$ times.

> [!example] $7, 11, 15, 19, \ldots$
> $d = 4$. $a_n = 7 + 4(n - 1) = 4n + 3$. The 50th term is $203$.

### From two terms

> [!abstract] Given $a_j$ and $a_k$
> 1. $d = \dfrac{a_k - a_j}{k - j}$ (change in value over change in position)
> 2. $a_1 = a_j - (j - 1)d$
> 3. Write $a_n = a_1 + (n - 1)d$ and simplify.

> [!example] The 4th term is 17 and the 13th term is 53
> $d = \frac{53 - 17}{13 - 4} = \frac{36}{9} = 4$; $a_1 = 17 - 3(4) = 5$.
> $a_n = 5 + 4(n - 1) = 4n + 1$

> [!example] Saving for a guitar
> Alex has $40 and saves $15 every week. When does he reach $250?
> $250 = 40 + 15(n - 1) \Rightarrow 210 = 15(n - 1) \Rightarrow n = 15$. The 15th term - that's after 14 weeks of saving.

> [!warning] Off by one
> $a_1$ is the starting value, before any changes. After $k$ changes you're at $a_{k + 1}$.

### Practice

**1.** Is $10, 7, 4, 1, \ldots$ arithmetic? Give $d$ and $a_n$.

> [!check]- Answer
> Yes, $d = -3$. $a_n = 10 - 3(n - 1) = 13 - 3n$.

**2.** The 3rd term is 12 and the 10th is 47. Find $a_n$.

> [!check]- Answer
> $d = 5$, $a_1 = 2$: $a_n = 5n - 3$

**3.** Is $1, 4, 9, 16, \ldots$ arithmetic?

> [!check]- Answer
> No - the differences are 3, 5, 7, which aren't constant.

---

## 3. Geometric Sequences

**Multiply by the same number $r$ each time.** $r$ is the **common ratio** - divide any term by the one before it.

$$a_n = a_1 r^{n - 1}$$

> [!example] $2, 6, 18, 54, \ldots$
> $r = 3$. $a_n = 2 \cdot 3^{n - 1}$. The 6th term is $2 \cdot 3^5 = 486$.

> [!example] $48, 24, 12, \ldots$
> $r = \frac{1}{2}$. $a_6 = 48\left(\frac{1}{2}\right)^5 = 1.5$

A negative ratio makes the signs alternate: $3, -6, 12, -24, \ldots$ has $r = -2$.

### From two terms

> [!abstract] Given $a_j$ and $a_k$
> 1. Divide: $\dfrac{a_k}{a_j} = r^{k - j}$. Take the $(k - j)$th root to get $r$.
> 2. $a_1 = \dfrac{a_j}{r^{j - 1}}$
> 3. Write $a_n = a_1 r^{n - 1}$.

> [!example] The 3rd term is 18 and the 6th is 486
> $r^3 = \frac{486}{18} = 27$, so $r = 3$. $a_1 = \frac{18}{3^2} = 2$. $a_n = 2 \cdot 3^{n - 1}$.

### Growth and decay

A change of $p\%$ per step is a geometric sequence:
- growth: $r = 1 + \frac{p}{100}$
- decay: $r = 1 - \frac{p}{100}$

> [!example] A $12,000 machine loses 15% of its value a year. Value after 6 years?
> $r = 0.85$. After 6 years of decay, it's the 7th term: $12{,}000(0.85)^6 \approx \$4{,}525.79$.

> [!example] $500 at 3% interest, compounded yearly, for 8 years
> $500(1.03)^8 \approx \$633.39$ - the same answer as the Module 8 formula $P(1 + r)^t$.

### Practice

**1.** Is $5, -10, 20, -40, \ldots$ geometric? Give $r$ and $a_n$.

> [!check]- Answer
> Yes, $r = -2$, $a_n = 5(-2)^{n - 1}$.

**2.** The 2nd term is 6 and the 5th term is 162. Find $a_n$.

> [!check]- Answer
> $r^3 = 27$, $r = 3$; $a_1 = 2$: $a_n = 2 \cdot 3^{n - 1}$

**3.** A town of 200 people grows 6% a year. Population after 10 years?

> [!check]- Answer
> $200(1.06)^{10} \approx 358$

---

## 4. Summation Notation

A **series** is the sum of the terms of a sequence. $S_n$, the **$n$th partial sum**, adds the first $n$ terms.

**Sigma notation** writes a sum compactly:

$$\sum_{i = 1}^{n} a_i = a_1 + a_2 + \cdots + a_n$$

| Part | Meaning |
|---|---|
| $\Sigma$ | "add up" |
| $i = 1$ (bottom) | where to start (lower limit) |
| $n$ (top) | where to stop (upper limit) |
| $a_i$ | the formula for each term |

> [!abstract] Evaluating
> Plug in every whole number from the bottom limit to the top limit, then add. The number of terms is $\text{top} - \text{bottom} + 1$.

> [!example] $\displaystyle\sum_{i = 1}^{4} (i^2 + 1)$
> $2 + 5 + 10 + 17 = 34$

> [!example] $\displaystyle\sum_{i = 2}^{6} (5 - i)$
> $3 + 2 + 1 + 0 + (-1) = 5$ (five terms: 2 through 6)

> [!example] Writing a sum in sigma notation
> $\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots + \frac{1}{2^n} = \displaystyle\sum_{i = 1}^{n} \frac{1}{2^i}$

### Practice

**1.** $\displaystyle\sum_{i = 1}^{5} 2^i$

> [!check]- Answer
> $2 + 4 + 8 + 16 + 32 = 62$

**2.** $\displaystyle\sum_{i = 3}^{6} 2i$

> [!check]- Answer
> $6 + 8 + 10 + 12 = 36$

**3.** Write $1 + 8 + 27 + \cdots + n^3$ in sigma notation.

> [!check]- Answer
> $\displaystyle\sum_{i = 1}^{n} i^3$

---

## 5. Arithmetic Series

To add $1 + 2 + 3 + \cdots + 100$, pair the ends: $1 + 100$, $2 + 99$, $3 + 98$, ... Every pair is 101, and there are 50 pairs: $5{,}050$.

That's the whole idea:

$$S_n = n\left(\frac{a_1 + a_n}{2}\right)$$

**The number of terms times the average of the first and last.**

> [!abstract] Method
> 1. Find $a_1$, $d$, and the number of terms $n$.
> 2. Find the last term $a_n = a_1 + (n - 1)d$ (if it isn't given).
> 3. $S_n = n \cdot \frac{a_1 + a_n}{2}$.

> [!example] The first 20 terms of $6, 10, 14, \ldots$
> $a_{20} = 6 + 19(4) = 82$. $S_{20} = 20 \cdot \frac{6 + 82}{2} = 880$.

> [!example] A theater has 15 rows, 40 seats in the front row, and 2 fewer seats in each row behind it. Total seats?
> $a_{15} = 40 - 14(2) = 12$. $S_{15} = 15 \cdot \frac{40 + 12}{2} = 390$.

### Practice

**1.** The sum of the first 50 even numbers, $2 + 4 + \cdots + 100$?

> [!check]- Answer
> $50 \cdot \frac{2 + 100}{2} = 2{,}550$

**2.** The first 12 terms of $20, 17, 14, \ldots$?

> [!check]- Answer
> $a_{12} = 20 - 33 = -13$. $S_{12} = 12 \cdot \frac{20 - 13}{2} = 42$.

---

## 6. Geometric Series

$$S_n = \frac{a_1(1 - r^n)}{1 - r} \qquad (r \ne 1)$$

**Where it comes from:** write $S_n$, then $rS_n$ (every term shifted one step). Subtracting them cancels everything except the first and last pieces: $S_n - rS_n = a_1 - a_1 r^n$.

> [!example] 8 terms of $4, 12, 36, \ldots$
> $\frac{4(1 - 3^8)}{1 - 3} = \frac{4(1 - 6{,}561)}{-2} = 13{,}120$

> [!example] 10 terms of $1{,}000, 500, 250, \ldots$
> $\frac{1{,}000(1 - 0.5^{10})}{0.5} \approx 1{,}998.05$ - close to 2,000 and never reaching it.

> [!example] Total pay: $40,000 a year with a 3% raise each year, over 5 years
> $\frac{40{,}000(1 - 1.03^5)}{1 - 1.03} \approx \$212{,}365.43$

> [!warning] Common slips
> - The exponent is $n$, the number of terms - not $n - 1$.
> - With a negative ratio, use parentheses: $(-3)^6 = 729$.
> - Arithmetic or geometric? Check whether consecutive terms **differ** by a constant or **divide** to a constant before choosing a formula.

### Practice

**1.** 6 terms of $2, -6, 18, \ldots$

> [!check]- Answer
> $r = -3$: $\frac{2(1 - 729)}{1 + 3} = -364$

**2.** A penny on day 1, doubling daily for 20 days. Total?

> [!check]- Answer
> $\frac{0.01(1 - 2^{20})}{1 - 2} = \$10{,}485.75$

---

## Module Review Quiz

**1.** $a_n = 3n^2 - n$. Find $a_4$.

> [!check]- Answer
> $48 - 4 = 44$

**2.** The 5th term of an arithmetic sequence is 23 and the 12th is 58. Find $a_n$.

> [!check]- Answer
> $d = 5$, $a_1 = 3$: $a_n = 5n - 2$

**3.** The 2nd term of a geometric sequence is 12 and the 4th is 108 ($r > 0$). Find $a_n$.

> [!check]- Answer
> $r^2 = 9$, $r = 3$, $a_1 = 4$: $a_n = 4 \cdot 3^{n - 1}$

**4.** Evaluate $\displaystyle\sum_{i = 1}^{6} (3i - 2)$.

> [!check]- Answer
> $1 + 4 + 7 + 10 + 13 + 16 = 51$

**5.** Sum of the first 30 terms of $5, 9, 13, \ldots$?

> [!check]- Answer
> $a_{30} = 121$. $S_{30} = 30 \cdot \frac{126}{2} = 1{,}890$.

**6.** Sum of the first 7 terms of $3, 6, 12, \ldots$?

> [!check]- Answer
> $\frac{3(1 - 128)}{-1} = 381$

**7.** A $25,000 car loses 10% a year. Value after 4 years?

> [!check]- Answer
> $25{,}000(0.9)^4 = \$16{,}402.50$

