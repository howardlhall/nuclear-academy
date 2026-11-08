---
layout: ../../layouts/Page.astro
title: "For teachers: using the Foundations units"
kicker: "Foundations · Teacher's notes"
description: "What each unit covers, how long it takes, which standards it touches, the misconceptions it is written to catch, discussion prompts, and answer notes for every 'Try it' task."
---

The five Foundations units are written for readers at a nominal tenth-grade level with no
prior chemistry or physics. Each is 1,100–1,500 words, reads in 15–25 minutes, and ends with
"Try it" tasks that send students to the site's own tools — the
[nuclide chart explorer](/tools/nuclide-chart/) and the
[decay-chain calculator](/tools/decay-chain/) — so that every abstract statement can be checked
against real evaluated data. The tools run in the browser, need no account, and work on a phone.

Everything here is licensed [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/):
copy and distribute it for teaching with attribution; do not sell it or produce altered
versions. Corrections and suggestions are welcome through the site's GitHub repository.

## Sequence and time

| Unit | Prerequisite | Class time | Home reading |
|---|---|---|---|
| 1 Atoms and the periodic table | none | one period | 15 min |
| 2 Isotopes and the chart of the nuclides | Unit 1 | one period + explorer time | 20 min |
| 3 Radioactive decay | Unit 2 | one to two periods | 25 min |
| 4 Nuclear reactions | Unit 3 | one to two periods | 25 min |
| 5 The math you need | Unit 3 (can run alongside 4) | two periods with practice | 25 min |

Units 1–3 stand alone as a three-lesson introduction to isotopes and radioactivity. Units 4–5
are the bridge to the site's modules and to a chemistry or physics course's nuclear chapter.

## Standards

**Next Generation Science Standards.** The units map most directly to two high-school
performance expectations, quoted from nextgenscience.org:

- **HS-PS1-1** — "Use the periodic table as a model to predict the relative properties of
  elements based on the patterns of electrons in the outermost energy level of atoms."
  Unit 1, section 4 (rows, columns, and why they predict behavior).
- **HS-PS1-8** — "Develop models to illustrate the changes in the composition of the nucleus of
  the atom and the energy released during the processes of fission, fusion, and radioactive
  decay." Clarification: "Emphasis is on simple qualitative models, such as pictures or
  diagrams, and on the scale of energy released in nuclear processes relative to other kinds of
  transformations." Assessment boundary: "Assessment does not include quantitative calculation
  of energy released. Assessment is limited to alpha, beta, and gamma radioactive decays."
  Units 2–4 throughout; the chart of the nuclides is the model, and Unit 4 section 6 gives the
  energy-scale comparison (about fifty million to one) without calculation.

Unit 5 goes past the HS-PS1-8 assessment boundary on purpose, for classes that want the
quantitative half-life work; it is optional for meeting the standard.

**Common Core mathematics** (codes only; consult your state's adoption):

- 8.EE.A.3 and 8.EE.A.4 — scientific notation and operations with it (Unit 5, section 1).
- HSN-Q.A.1 — units as a way to guide the solution of problems (Unit 5, section 2).
- HSF-LE.A.1 and HSF-LE.A.2 — recognizing and constructing exponential functions (Unit 5,
  sections 3–4).
- HSF-LE.A.4 — using logarithms to solve exponential equations (Unit 5, section 5).
- HSF-IF.C.7e — graphing exponential and logarithmic functions (Unit 5, section 7).

Other frameworks (state standards, IB, A-level) are not mapped here; the unit contents are
conventional enough that the mapping is usually obvious.

## Misconceptions each unit is written to catch

- **"Radioactive" describes an element.** It describes a nuclide. Carbon is not radioactive;
  carbon-14 is. (Unit 2, section 3; Unit 3 throughout.) Students who leave with this
  distinction have the main thing.
- **Decay is like a countdown.** It is not; each nucleus has a fixed chance per unit time and no
  memory. The dice model in Unit 5, section 6 is the corrective; running it with real dice in
  class (start with 100, remove the sixes each round, plot what is left) takes ten minutes and
  is worth it.
- **After two half-lives everything is gone.** A quarter is left. The table in Unit 3, section 4
  is designed to be read aloud.
- **Fission and fusion are opposites, so one must absorb energy.** Both release it, because of
  where iron sits on the binding-energy curve (Unit 4, section 6). The "hill with iron on top"
  picture is the single most useful thing in the unit.
- **Alpha, beta, and gamma are three kinds of "rays" from the same thing.** They are different
  particles doing different things to the nucleus; the bookkeeping rule (Unit 3, section 2)
  lets students derive the daughter instead of memorizing it.
- **"Critical" means "about to explode."** It means steady (Unit 4, section 4).
- **"Negative means favorable."** Chemistry students carry ΔG < 0 into Unit 4 and read a
  positive Q-value as unfavorable. Unit 4, section 7 flags the sign flip explicitly; it is worth
  saying aloud that Q counts energy released, ΔH counts energy change of the system, and that the
  conventions were simply never reconciled.
- **Chemistry can change one element into another.** It cannot; the nucleus is untouched by
  chemistry (Unit 1, section 2; Unit 2, section 1).

## Discussion prompts

- After Unit 2: *Why does the periodic table have about 100 boxes and the chart of the nuclides
  about 3,000?* (Same Z, different N; the periodic table is a projection of the chart onto one
  axis.)
- After Unit 3: *A smoke detector, a banana, a PET scan, and a basement with radon all involve
  radioactive decay. Rank them by how worried you should be, and say what number you would want
  to know to decide.* (Activity, dose, and where the material is — inside or outside the body.)
- After Unit 4: *A reactor makes plutonium whether anyone wants it to or not. What follows?*
  (This is the bridge to Module 1 and the safeguards system.)
- After Unit 5: *If carbon dating works by measuring what is left, why can't it date something a
  million years old?* (After 175 half-lives there is nothing left to measure; the practical limit
  is about 50,000 years, roughly nine half-lives.)

## Answer notes for the "Try it" tasks

Answers are from the ENSDF evaluated data as served by the site's tools; students using the
explorer should get exactly these.

**Unit 1.** (1) Any three elements: for carbon Z = 6, A ≈ 12, N = 6; for iron Z = 26, A ≈ 56,
N = 30; for uranium Z = 92, A ≈ 238, N = 146. (2) Uranium and plutonium are in the actinide row,
which belongs to row 7 of the table.

**Unit 2.** (1) Carbon has two stable boxes, C-12 and C-13. C-14 decays by β⁻ to N-14 with a
half-life of 5,700 years. (2) The explorer draws about forty uranium ground states; none is
stable — the longest-lived are U-238 (4.47 billion years) and U-235 (704 million years). (3)
From U-238 to Pb-206 is fourteen hops (eight alpha, six β⁻). (4) Open-ended; any mid-chart
element shows stable boxes on the band and colored boxes either side.

**Unit 3.** (1) K-40 decays by β⁻ to Ca-40 (89.3 percent) and by electron capture to Ar-40
(10.7 percent). (2) Am-241 → Np-237 by alpha: Z 95 → 93, A 241 → 237. (3) Tc-99m lasts
6.0 hours and decays to Tc-99 by isomeric transition (a gamma). (4) Any β⁻ emitter hops up-left,
any β⁺ emitter down-right; both toward the band.

**Unit 4.** (1) U-239 → Np-239 (β⁻, 23.5 minutes) → Pu-239 (β⁻, 2.36 days): two hops. (2) Sr-90
and Cs-137 both sit to the right of the band and decay by β⁻ (Sr-90 → Y-90; Cs-137 → Ba-137m,
mostly). (3) Open-ended; check that A goes up by one and Z is unchanged. (4) Q(²³⁹Pu → ²³⁵U + ⁴He)
= (239.052162 − 235.043928 − 4.002603) u × 931.494 = 0.005631 u × 931.494 ≈ 5.24 MeV. Pu-239's
half-life is 24,100 years; an alpha emitter with Q near 8–9 MeV (e.g. Po-212, 8.95 MeV) lives
microseconds — higher Q, shorter half-life, steeply (Geiger–Nuttall). Section 7 is the natural
place to use the mass–energy equivalence students meet in physics; the arithmetic is only
subtraction and one multiplication, but insist on carrying six decimals.

**Unit 5.** (1) At 12 h the calculator gives 2.0 GBq of Tc-99m; at 30 h, 0.25 GBq. (2) On a log
vertical axis the C-14 line is straight; the fraction at 20,000 years is 0.088. (3) In the U-238
preset with log axes the daughters rise to meet the parent and then run parallel to it — secular
equilibrium.

## Safety and sensitivity note

Nothing in the Foundations units or the tools goes beyond what is in a standard high-school or
first-year university textbook, and the site's editorial rules keep it that way: no facility
detail, no weapon-design detail beyond the two-sentence public description in Unit 4, and no
statement that could confirm or deny anything in the open literature beyond what its cited
sources say. Teachers are welcome to use the units to discuss nuclear weapons and their
control; the site's [Module 1](/modules/nuclear-security-why-it-matters/) is the natural next
step for that discussion.
