---
title: "The math you need"
description: "Scientific notation, exponents, the half-life formula worked by hand, logarithms as 'how many halvings', a little probability, and how to read a log-scale graph — everything the site's tools assume, with nothing harder than algebra."
order: 5
status: draft
lastReviewed: "2026-09-22"
before: ["Unit 3: Radioactive decay"]
tool: "/tools/decay-chain/"
---

Nuclear numbers are awkward: atoms are counted in the trillions of trillions, half-lives run from
nanoseconds to billions of years, and the interesting question is usually "how much is left after
this long?" Five ideas handle all of it. None of them needs more than the algebra in a first
high-school course.

## 1. Scientific notation

Writing 602,000,000,000,000,000,000,000 is a good way to lose a zero. Scientific notation moves the
decimal point and keeps count of how far it moved:

> 602,000,000,000,000,000,000,000 = 6.02 × 10²³

The **exponent** (the 23) is the number of places the decimal point moved to the left. A negative
exponent means it moved to the right — a small number:

> 0.000 000 000 000 000 000 16 = 1.6 × 10⁻¹⁹

Two rules do most of the work:

- **To multiply**, multiply the front numbers and *add* the exponents:
  (2 × 10⁵) × (3 × 10⁴) = 6 × 10⁹.
- **To divide**, divide the front numbers and *subtract* the exponents:
  (6 × 10⁹) ÷ (2 × 10⁵) = 3 × 10⁴.

Calculators write 6.02 × 10²³ as `6.02E23`. The site's tools accept that form too.

**Two numbers worth knowing.** One **mole** of anything is 6.02 × 10²³ of it (Avogadro's number).
One mole of carbon-12 weighs 12 grams; one mole of uranium-238 weighs 238 grams — the mass number
in grams, near enough. So a gram of U-238 contains (1 ÷ 238) × 6.02 × 10²³ ≈ 2.5 × 10²¹ atoms.
That is how the calculator turns "1 gram" into a number of atoms.

## 2. Units and prefixes

Nuclear quantities come with prefixes that are just powers of ten:

| Prefix | Symbol | Means | Example |
|---|---|---|---|
| kilo | k | 10³ | 1 kBq = 1,000 decays per second |
| mega | M | 10⁶ | 1 MBq = a million per second |
| giga | G | 10⁹ | 1 GBq — a typical medical-imaging dose |
| tera | T | 10¹² | 1 TBq |
| milli | m | 10⁻³ | 1 mCi = 0.001 curie |
| micro | μ | 10⁻⁶ | 1 μg = a millionth of a gram |
| nano | n | 10⁻⁹ | 1 ns = a billionth of a second |

For time, the site uses seconds, minutes, hours, days, and years. One year is about
3.156 × 10⁷ seconds — useful when a half-life is given in one unit and the time you care about
in another. Always get both into the same unit before you divide one by the other.

## 3. Exponents and "how many halvings"

Unit 3 showed that after each half-life, half of what was there remains. After two half-lives,
half of a half: a quarter. After three, an eighth. The pattern is a power of one-half:

> after *k* half-lives, the fraction left is (½)ᵏ

| k | (½)ᵏ | as a decimal |
|---|---|---|
| 1 | ½ | 0.5 |
| 2 | ¼ | 0.25 |
| 3 | ⅛ | 0.125 |
| 5 | 1/32 | 0.031 |
| 10 | 1/1,024 | ≈ 0.001 |
| 20 | 1/1,048,576 | ≈ 0.000 001 |

Ten half-lives is the rule of thumb for "about a thousandth left"; twenty for "about a millionth."
The exponent *k* does not have to be a whole number. (½)^0.5 is the square root of one-half, about
0.71 — what is left after half a half-life. Any calculator with a `xʸ` or `^` key will do it:
`0.5 ^ 0.5`.

## 4. The half-life formula

Put the last two sections together and you have the one formula on this page:

> **N = N₀ × (½)^(t / T½)**

- **N₀** is how much you started with (atoms, grams, or becquerels — it works for all three).
- **t** is the time that has passed.
- **T½** is the half-life, *in the same unit as t*.
- **t / T½** is the number of half-lives that have passed, whole or not.
- **N** is how much is left.

**Worked example 1 — whole number of half-lives.** A hospital receives 8 GBq of technetium-99m
(half-life 6.0 hours) at 6 a.m. How much is left at 6 p.m.?

t = 12 h, T½ = 6 h, so t / T½ = 2. N = 8 × (½)² = 8 × ¼ = **2 GBq**.

**Worked example 2 — not a whole number.** Same shipment; how much is left at noon the next day
(30 hours later)?

t / T½ = 30 ÷ 6 = 5. N = 8 × (½)⁵ = 8 ÷ 32 = **0.25 GBq**. Now try 3 p.m. the same day, 9 hours:
t / T½ = 1.5. (½)^1.5 = 0.354, so N = 8 × 0.354 = **2.8 GBq**. That is between the 4 GBq you would
have at one half-life and the 2 GBq at two — as it should be.

**Worked example 3 — mixed units.** How much of a sample of carbon-14 (half-life 5,700 years) is
left after 20,000 years? t / T½ = 20,000 ÷ 5,700 = 3.51. (½)^3.51 = 0.088, so about **9 percent**
remains. Check it against Unit 3's table: after 3 half-lives, 12.5 percent; after 4, 6.25 percent;
3.51 half-lives should land between, and it does.

The fraction left, N / N₀, is the same whether you count atoms or measure activity in becquerels,
because activity is just the number of atoms times a constant. That is why the decay calculator
lets you type either.

## 5. Logarithms: running the formula backwards

The formula answers "how much is left after time t?" Carbon dating asks the reverse: "how much
time has passed, if this much is left?" That means solving for the exponent, and the tool for
pulling a number out of an exponent is the **logarithm**.

You do not need the theory. You need one fact: **a logarithm answers the question "what exponent
gets me here?"** log₂(8) = 3 because 2³ = 8. log₁₀(1,000) = 3 because 10³ = 1,000. And for
half-lives, the number of halvings *k* that takes you from N₀ down to N is

> k = log₂(N₀ / N)

Most calculators have `log` (base 10) and `ln` (base *e*) but not log₂. Either one works if you
divide by the same kind of log of 2:

> k = log(N₀ / N) ÷ log(2)

**Worked example 4 — carbon dating.** A piece of wood has 23 percent of the carbon-14 that living
wood has. N₀ / N = 1 ÷ 0.23 = 4.35. log(4.35) ÷ log(2) = 0.638 ÷ 0.301 = 2.12 half-lives. Age =
2.12 × 5,700 = about **12,000 years**. Sanity check: 25 percent would be exactly two half-lives,
11,400 years; 23 percent is a little less, so a little older. Good.

**Worked example 5 — how long until it is "gone"?** A radiation safety rule of thumb says a
short-lived source can be treated as ordinary waste after ten half-lives. For iodine-131 (half-life
8.0 days) that is 80 days; the fraction left is (½)¹⁰ ≈ 0.001. If instead you asked "how long until
only one part in a million is left?": k = log(1,000,000) ÷ log(2) = 6 ÷ 0.301 = 19.9 half-lives,
about 160 days.

## 6. A little probability

Unit 3 said you cannot predict when one nucleus will decay, only the odds. Here is the whole of
what "odds" means here.

Imagine 1,000 dice, each rolled once a second. A die "decays" when it shows a six. Each second,
about one-sixth of the remaining dice decay and are taken away. You cannot say which die will go
next, but you can say with confidence that after one second about 833 remain, after two about
694, and so on. The "half-life" of a die is the time for half to be gone — about 3.8 rolls.

A nucleus is a die with a very lopsided chance per second. For carbon-14 the chance that any
given nucleus decays in a given second is about 4 × 10⁻¹² — four in a trillion. That sounds like
nothing, but a gram of carbon has 5 × 10²² atoms, of which about 6 × 10¹⁰ are carbon-14, and four
in a trillion of those is about 0.2 decays per second. Multiply tiny odds by an enormous number of
atoms and you get a steady, measurable rate. That is the whole trick.

Two consequences. First, **the curve is smooth only because the numbers are huge**; with a few
atoms, decay is jerky and random, and the site's calculator will happily show you a network with
three atoms of polonium-214 in it — treat the fractional atom counts it prints as averages.
Second, **a nucleus has no memory.** A carbon-14 atom that has survived 20,000 years is no more
"due" than one made yesterday. Its odds for the next second are exactly the same.

## 7. Reading a log-scale graph

The decay calculator's plots have a check-box for **log axes**. On an ordinary axis, equal
distances mean equal *amounts*: 0, 100, 200, 300. On a **logarithmic** axis, equal distances mean
equal *multiples*: 1, 10, 100, 1,000. Each step is ten times the last.

Why bother? Two reasons.

- **Range.** A uranium-238 decay chain contains U-238 with a half-life of billions of years and
  polonium-214 with a half-life of 0.16 milliseconds. On one ordinary time axis you would see
  either the U-238 or the Po-214 and never both. A log time axis shows nanoseconds and eons on the
  same picture.
- **Shape.** Exponential decay — the curve from section 4 — is a **straight line** on a log
  vertical axis. Each half-life drops the line by the same distance. So on a log plot, a steeper
  straight line means a shorter half-life, and a curve that bends means something is being added
  (a daughter growing in from its parent) as well as decaying.

Reading tip: on a log axis the tick marks between the big labels are not evenly spaced. Between
10 and 100 the marks are at 20, 30, 40 … 90, and they bunch up toward the top. Halfway across the
decade is not 50 — it is about 32 (the square root of 10, times 10).

## Try it

- Open the [decay calculator](/tools/decay-chain/) with Tc-99m, 8 GBq, 30 hours. Read the activity
  off the table at 12 h and 30 h and check them against worked examples 1 and 2.
- Set up carbon-14, any amount, 20,000 years. Switch the vertical axis to log. Is the line
  straight? Read off the fraction at 20,000 years and compare it with worked example 3.
- Run the U-238 series preset with log axes on. Find the flat stretch where U-238 has not changed
  and the daughters have all grown in to match it — that is called *secular equilibrium*, and the
  math of why it happens is the next thing to learn after this page.

## Where this comes from

The mathematics is standard; the half-life relation and its logarithmic inverse are in every
introductory chemistry and physics text. Avogadro's number is exactly 6.02214076 × 10²³ by the
2019 definition of the mole. Half-lives used in the examples (technetium-99m 6.0 h; carbon-14
about 5,700 y; iodine-131 8.0 d; polonium-214 0.16 ms) are from the evaluated nuclear data behind
the site's tools. The carbon-14 decay probability per second is the natural log of 2 divided by
the half-life in seconds, ln 2 / (5,700 × 3.156 × 10⁷ s) ≈ 3.9 × 10⁻¹² per second. The
carbon-14 abundance in living carbon, about 1.2 parts in 10¹², is the standard figure in
radiocarbon references. The dice model of decay is a common classroom demonstration.
