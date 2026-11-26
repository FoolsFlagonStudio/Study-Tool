---
title: Preparing for Trigonometry
section: 4 - Trigonometry - Functions, Graphs, and Applications
module: 11
status: draft
topics: [angle-quadrants, degree-radian-conversion, angle-types, coterminal-angles, complements-supplements, arc-length, sector-area, sector-applications]
---

# Module 11: Preparing for Trigonometry

**By the end of this module you can:** place an angle in standard position and name its quadrant, convert between degrees and radians, classify angles, find coterminal, complementary, and supplementary angles, and use radians to find arc length, sector area, and sector perimeter in real problems.

> [!info] Why this matters
> Trigonometry is the math of angles and circles - wheels, orbits, clocks, sound waves, and anything that repeats. Before the trig functions arrive in Module 12, you need a solid way to measure and describe angles. The big new idea is the **radian**, which measures an angle by the arc it cuts off. It makes circle formulas collapse into one-liners like $s = r\theta$.

---

## 1. Angles in Standard Position

An **angle** is formed by two rays sharing an endpoint, the **vertex**. The rotation goes from the **initial side** to the **terminal side**.

**Standard position:** vertex at the origin, initial side on the positive $x$-axis.
- **Counterclockwise** rotation → **positive** angle.
- **Clockwise** rotation → **negative** angle.

In $\angle ABC$, the middle letter $B$ is always the vertex.

The quadrant is wherever the **terminal side** lands. Quadrants are numbered I to IV going counterclockwise from the upper right.

| Terminal side between | Quadrant |
|---|---|
| $0°$ and $90°$ | I |
| $90°$ and $180°$ | II |
| $180°$ and $270°$ | III |
| $270°$ and $360°$ | IV |

An angle whose terminal side lands **exactly on an axis** ($0°$, $90°$, $180°$, $270°$, ...) is **quadrantal** - it isn't in any quadrant.

> [!abstract] Naming the quadrant of any angle
> 1. Add or subtract $360°$ until the angle is between $0°$ and $360°$.
> 2. Read the quadrant from the table.

> [!example] Quadrants
> - $200°$: Quadrant III
> - $-45°$: $-45° + 360° = 315°$, Quadrant IV (rotating 45° clockwise lands below the positive $x$-axis)
> - $480°$: $480° - 360° = 120°$, Quadrant II
> - $270°$: on the negative $y$-axis - quadrantal

### Practice

**1.** Which quadrant is $-150°$ in?

> [!check]- Answer
> $-150° + 360° = 210°$: Quadrant III.

**2.** Which quadrant is $400°$ in?

> [!check]- Answer
> $400° - 360° = 40°$: Quadrant I.

**3.** In $\angle PQR$, which point is the vertex?

> [!check]- Answer
> $Q$, the middle letter.

---

## 2. Degrees and Radians

One full turn is $360°$. In radians, one full turn is $2\pi$ - the circumference of a circle with radius 1. So:

$$180° = \pi \text{ radians}$$

That one fact gives both conversions:

| Converting | Multiply by |
|---|---|
| degrees → radians | $\dfrac{\pi}{180°}$ |
| radians → degrees | $\dfrac{180°}{\pi}$ |

Think of it as canceling units: you want the unit you're leaving to be on the bottom.

An angle written **without** a degree symbol is in radians.

> [!example] Degrees to radians
> $150° \cdot \frac{\pi}{180°} = \frac{150\pi}{180} = \frac{5\pi}{6}$
> $-210° \cdot \frac{\pi}{180°} = -\frac{7\pi}{6}$

> [!example] Radians to degrees
> $\frac{7\pi}{4} \cdot \frac{180°}{\pi} = 315°$
> $2.5 \cdot \frac{180°}{\pi} \approx 143.24°$ (no $\pi$ to cancel, so use the calculator)

**Worth memorizing:**

| $30°$ | $45°$ | $60°$ | $90°$ | $180°$ | $270°$ | $360°$ |
|---|---|---|---|---|---|---|
| $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ | $\frac{3\pi}{2}$ | $2\pi$ |

Every other common angle is a multiple of these: $120° = 2 \cdot 60° = \frac{2\pi}{3}$, $225° = 5 \cdot 45° = \frac{5\pi}{4}$.

> [!warning] Simplify the fraction
> $\frac{150\pi}{180}$ is correct but not finished. Divide the top and bottom by their GCF (30): $\frac{5\pi}{6}$.

### Practice

**1.** Convert $225°$ to radians.

> [!check]- Answer
> $\frac{225\pi}{180} = \frac{5\pi}{4}$

**2.** Convert $\frac{11\pi}{6}$ to degrees.

> [!check]- Answer
> $330°$

**3.** Convert $-\frac{3\pi}{4}$ to degrees.

> [!check]- Answer
> $-135°$

---

## 3. Classifying Angles

| Type | Degrees | Radians |
|---|---|---|
| Acute | between $0°$ and $90°$ | between $0$ and $\frac{\pi}{2}$ |
| Right | exactly $90°$ | $\frac{\pi}{2}$ |
| Obtuse | between $90°$ and $180°$ | between $\frac{\pi}{2}$ and $\pi$ |
| Straight | exactly $180°$ | $\pi$ |
| Quadrantal | any multiple of $90°$ | any multiple of $\frac{\pi}{2}$ |

Negative angles and angles of $180°$ or more are never acute or obtuse.

> [!example] Classify
> - $\frac{3\pi}{4} = 135°$: obtuse
> - $\frac{\pi}{12} = 15°$: acute
> - $\frac{3\pi}{2} = 270°$: quadrantal
> - $\pi$: straight (and quadrantal)

### Practice

**1.** Classify $\frac{5\pi}{9}$.

> [!check]- Answer
> $\frac{5\pi}{9} = 100°$: obtuse

**2.** Classify $\frac{2\pi}{5}$.

> [!check]- Answer
> $72°$: acute

---

## 4. Coterminal Angles

Angles are **coterminal** if they end on the same terminal side. Adding or subtracting full turns gets you there:

$$\theta + 360°k \qquad\text{or}\qquad \theta + 2\pi k \qquad (k \text{ any integer})$$

> [!example] Two coterminal angles for $75°$
> $75° + 360° = 435°$ and $75° - 360° = -285°$.

> [!example] The coterminal angle between $0°$ and $360°$
> - $-100°$: add $360°$ to get $260°$.
> - $1{,}000°$: subtract $2 \cdot 360° = 720°$ to get $280°$.
> - $\frac{17\pi}{6}$: subtract $2\pi = \frac{12\pi}{6}$ to get $\frac{5\pi}{6}$.

> [!abstract] Are two angles coterminal?
> Subtract them. If the difference is a whole number of turns ($360°k$ or $2\pi k$), yes.
> Example: $\frac{5\pi}{3} - \left(-\frac{\pi}{3}\right) = 2\pi$, so they're coterminal.

### Practice

**1.** Find the coterminal angle between $0°$ and $360°$ for $-500°$.

> [!check]- Answer
> $-500° + 720° = 220°$

**2.** Is $890°$ coterminal with $170°$?

> [!check]- Answer
> $890° - 170° = 720° = 2(360°)$. Yes.

**3.** Find a negative angle coterminal with $\frac{\pi}{4}$.

> [!check]- Answer
> $\frac{\pi}{4} - 2\pi = -\frac{7\pi}{4}$

---

## 5. Complementary and Supplementary Angles

| | Adds to | Find it |
|---|---|---|
| Complementary | $90°$ $\left(\frac{\pi}{2}\right)$ | $90° - x$ |
| Supplementary | $180°$ $(\pi)$ | $180° - x$ |

Both angles must be **positive**. An angle of $90°$ or more has no complement; an angle of $180°$ or more has no supplement.

> [!example] $38°$
> Complement: $52°$. Supplement: $142°$.

> [!example] $95°$
> Complement: $90° - 95° = -5°$, which is negative, so there's **no** complement. Supplement: $85°$.

> [!example] In radians
> The complement of $\frac{\pi}{6}$ is $\frac{\pi}{2} - \frac{\pi}{6} = \frac{\pi}{3}$. The supplement of $\frac{2\pi}{3}$ is $\pi - \frac{2\pi}{3} = \frac{\pi}{3}$.

### Practice

**1.** Supplement of $27°$?

> [!check]- Answer
> $153°$

**2.** Complement of $\frac{\pi}{5}$?

> [!check]- Answer
> $\frac{\pi}{2} - \frac{\pi}{5} = \frac{3\pi}{10}$

---

## 6. Arc Length

A central angle of $\theta$ **radians** in a circle of radius $r$ cuts off an arc of length

$$s = r\theta$$

That's what a radian **is**: an angle of 1 radian cuts off an arc exactly one radius long. Rearranged, $\theta = \frac{s}{r}$ and $r = \frac{s}{\theta}$.

> [!warning] Radians only
> Convert degrees to radians before using $s = r\theta$. Plugging in $150$ instead of $\frac{5\pi}{6}$ gives a wildly wrong answer.

> [!example] $r = 9$, $\theta = \frac{5\pi}{6}$
> $s = 9 \cdot \frac{5\pi}{6} = 7.5\pi \approx 23.56$

> [!example] $s = 15$, $r = 6$: find $\theta$
> $\theta = \frac{15}{6} = 2.5$ radians

> [!example] $s = 12$, $\theta = 150°$: find $r$
> $\theta = \frac{5\pi}{6}$. $r = \frac{12}{5\pi/6} \approx 4.58$

### Practice

**1.** $r = 8$, $\theta = 240°$. Arc length?

> [!check]- Answer
> $\theta = \frac{4\pi}{3}$. $s = \frac{32\pi}{3} \approx 33.51$

**2.** $s = 20$ cm, $r = 4$ cm. Find $\theta$.

> [!check]- Answer
> $5$ radians

---

## 7. Area of a Sector

A **sector** is a pizza slice: two radii and the arc between them. Its area is the same fraction of $\pi r^2$ as its angle is of $2\pi$:

$$A = \frac{\theta}{2\pi} \cdot \pi r^2 = \frac{1}{2}r^2\theta$$

($\theta$ in radians, answer in square units.)

> [!example] $r = 10$, $\theta = \frac{\pi}{5}$
> $A = \frac{1}{2}(100)\frac{\pi}{5} = 10\pi \approx 31.42$

> [!example] $r = 4$, $\theta = 135°$
> $\theta = \frac{3\pi}{4}$. $A = \frac{1}{2}(16)\frac{3\pi}{4} = 6\pi \approx 18.85$

> [!example] $A = 50$, $\theta = 2$: find $r$
> $50 = \frac{1}{2}r^2(2) = r^2$, so $r = \sqrt{50} \approx 7.07$

### Practice

**1.** $r = 6$, $\theta = \frac{\pi}{3}$. Area?

> [!check]- Answer
> $\frac{1}{2}(36)\frac{\pi}{3} = 6\pi \approx 18.85$

**2.** $A = 27$, $\theta = 1.5$. Find $r$.

> [!check]- Answer
> $r^2 = \frac{2(27)}{1.5} = 36$, so $r = 6$.

---

## 8. Sector Problems in the Real World

| Question asks for... | Use |
|---|---|
| distance along a curve (a wheel, a clock tip, an orbit) | $s = r\theta$ |
| region covered (sprinklers, sensors, slices) | $A = \frac{1}{2}r^2\theta$ |
| fencing or edging around a slice | $P = r\theta + 2r$ |

> [!abstract] Getting $r$ and $\theta$ from a story
> - A diameter? Halve it.
> - Something orbiting above a surface? $r$ = planet radius + height.
> - Clock hands: 60 minutes is $2\pi$, so $m$ minutes is $\frac{m}{60} \cdot 2\pi$.
> - Evenly spaced stops: each gap is $\frac{2\pi}{\text{number of stops}}$.

> [!example] A clock's minute hand is 6 in. How far does its tip move in 20 minutes?
> $\theta = \frac{20}{60} \cdot 2\pi = \frac{2\pi}{3}$. $s = 6 \cdot \frac{2\pi}{3} = 4\pi \approx 12.57$ in.

> [!example] Perimeter of a slice with $r = 12$, $\theta = \frac{\pi}{3}$
> $12 \cdot \frac{\pi}{3} + 24 = 4\pi + 24 \approx 36.57$

> [!example] A sprinkler reaches 30 ft over $120°$. Area watered?
> $\frac{1}{2}(900) \cdot \frac{2\pi}{3} = 300\pi \approx 942.48$ ft²

> [!example] A satellite orbits 300 km above Earth (radius 6,400 km) and is tracked over $30°$. Distance?
> $r = 6{,}700$. $s = 6{,}700 \cdot \frac{\pi}{6} \approx 3{,}508.1$ km

### Practice

**1.** A wheel has a 30 cm diameter. How far does a point on its rim travel in a quarter turn?

> [!check]- Answer
> $r = 15$, $\theta = \frac{\pi}{2}$: $7.5\pi \approx 23.56$ cm

**2.** A garden slice has a $60°$ angle and 8 ft sides. How much edging goes around it?

> [!check]- Answer
> $8 \cdot \frac{\pi}{3} + 16 \approx 24.38$ ft

---

## Module Review Quiz

**1.** Which quadrant is $-300°$ in?

> [!check]- Answer
> $60°$: Quadrant I

**2.** Convert $210°$ to radians and $\frac{5\pi}{12}$ to degrees.

> [!check]- Answer
> $\frac{7\pi}{6}$ and $75°$

**3.** Classify $\frac{7\pi}{12}$.

> [!check]- Answer
> $105°$: obtuse

**4.** Find the coterminal angle between $0$ and $2\pi$ for $-\frac{\pi}{6}$.

> [!check]- Answer
> $\frac{11\pi}{6}$

**5.** Complement and supplement of $64°$?

> [!check]- Answer
> $26°$ and $116°$

**6.** $r = 12$, $\theta = 45°$. Arc length?

> [!check]- Answer
> $3\pi \approx 9.42$

**7.** $r = 9$, $\theta = \frac{2\pi}{9}$. Sector area?

> [!check]- Answer
> $\frac{1}{2}(81)\frac{2\pi}{9} = 9\pi \approx 28.27$

**8.** A security camera sees 40 m over $75°$. Area?

> [!check]- Answer
> $\frac{1}{2}(1{,}600)\frac{5\pi}{12} \approx 1{,}047.20$ m²

