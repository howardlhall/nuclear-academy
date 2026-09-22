---
title: "Nuclear reactions"
description: "What happens when something hits a nucleus: neutron capture, fission and the chain reaction, fusion, and the one graph — binding energy — that explains why the heaviest nuclei split and the lightest ones join."
order: 4
status: draft
lastReviewed: "2026-09-22"
before: ["Unit 3: Radioactive decay"]
tool: "/tools/nuclide-chart/"
---

## 1. Decay versus reaction

Decay (Unit 3) is something a nucleus does on its own. A **nuclear reaction** is something that
happens when a nucleus is *hit* — by a neutron, a proton, an alpha particle, a gamma ray, or
another nucleus — and comes out changed. The difference matters in practice: you cannot speed up
or slow down decay, but you can make reactions happen on purpose by arranging for the collisions,
and that is what a reactor does.

The bookkeeping rules from Unit 3 still hold. Nucleons are conserved: add up the mass numbers on
each side. Charge is conserved: add up the atomic numbers. If a reaction equation does not
balance, it is wrong.

## 2. The neutron is the key

Protons and alpha particles carry positive charge, and so does every nucleus. Fire one at the
other and they repel; only a fast, energetic particle gets close enough to react. A **neutron has
no charge**, so nothing pushes it away. Even a slow neutron drifts straight into a nucleus. That
is why nearly everything in a reactor is about neutrons.

**Neutron capture** is the simplest reaction: a nucleus absorbs a neutron and becomes the next
isotope up, with A + 1.

> uranium-238 + n → uranium-239
> (Z: 92 → 92; A: 238 → 239)

Uranium-239 is radioactive. It β⁻-decays (Unit 3: a neutron becomes a proton, Z goes up one) to
neptunium-239, which β⁻-decays again to **plutonium-239**. That two-step is how every gram of
plutonium on Earth was made — there is essentially none in nature. Keep this reaction in mind
when you reach the modules on safeguards: it is why a reactor is a plutonium factory whether or
not anyone wants it to be.

Capture is also how radioactive nuclides are made to order. Cobalt-59, which is stable, captures a
neutron and becomes cobalt-60, the gamma source used in cancer therapy and industrial radiography.

## 3. Fission

A few very heavy nuclides do something different when they absorb a neutron. Instead of settling
down as the next isotope, the nucleus wobbles, stretches, and splits into two pieces of unequal
size, plus two or three loose neutrons, plus a great deal of energy. That is **fission**.

> uranium-235 + n → (two fragments) + 2 or 3 n + energy

The fragments are not always the same two; there are dozens of combinations, with mass numbers
clustered around 95 and 140. Almost all of them have far too many neutrons for their size
(Unit 2: the valley of stability bends right, and a fragment inherits uranium's neutron-heavy
ratio), so they are strongly radioactive β⁻ emitters. That radioactivity is what makes spent
reactor fuel dangerous for a long time, and it is the reason the fragments are called
**fission products** and treated with such care.

Only some nuclides fission readily when hit by a *slow* neutron. The important ones are
**uranium-235**, **plutonium-239**, and **uranium-233**. These are called **fissile**. Uranium-238,
which is 99.3 percent of natural uranium, does not — a slow neutron is simply captured (section 2).
That single difference between two isotopes of the same element drives the whole business of
**enrichment**: separating the 0.7 percent of U-235 from the U-238 so that a fuel or a weapon has
enough of it. Chemistry cannot do the separation, because the two isotopes are chemically
identical; it has to be done by their 1 percent difference in mass, which is slow and expensive.
Module 1 explains why that difficulty is the main thing standing between the world and more
nuclear weapons.

## 4. The chain reaction

Each fission releases two or three neutrons. If, on average, **at least one** of them goes on to
cause another fission, the process keeps itself going: a **chain reaction**. If fewer than one
does, it dies out. If more than one does, it grows — each generation of fissions larger than the
last.

Engineers describe this with one number, **k**, the average number of fissions each fission
causes in the next generation:

- **k < 1** — subcritical: the reaction dies away.
- **k = 1** — critical: steady, self-sustaining. This is a running reactor.
- **k > 1** — supercritical: growing. A reactor starting up is slightly supercritical for a
  moment; a weapon is very supercritical for a few millionths of a second.

"Critical" sounds alarming but just means "steady." A reactor operates at k = 1 and is adjusted by
control rods, which are made of materials that absorb neutrons without fissioning; pushing them in
lowers k, pulling them out raises it.

What decides k? How much fissile material there is, how it is arranged, and what is around it to
absorb or reflect neutrons. The smallest amount that can sustain a chain reaction in a given
arrangement is the **critical mass**. Below it, too many neutrons escape through the surface
before they find a nucleus. For a bare sphere of U-235 metal it is on the order of tens of
kilograms; surrounding it with a neutron reflector, or compressing it, lowers the number. Those
are the two knobs that weapon design turns and that safeguards inspectors care about, and this
site does not go further into them than that.

## 5. Fusion

At the other end of the chart, the *lightest* nuclei release energy by **joining**. Two hydrogen
isotopes — deuterium (H-2) and tritium (H-3) — can fuse into helium-4 and a neutron:

> H-2 + H-3 → He-4 + n + energy
> (Z: 1 + 1 → 2 + 0; A: 2 + 3 → 4 + 1)

The catch is that both nuclei are positively charged and repel each other. To fuse they must be
slammed together fast, which means very hot — tens of millions of degrees, hotter than the center
of the Sun, which is where fusion happens naturally. Making that happen in a machine on Earth and
getting more energy out than in is the fusion-power problem, and it has been "twenty years away"
for seventy years. Fusion reactions produce no fission products, but the neutron in the equation
above makes the surrounding structure radioactive, and tritium is itself radioactive; so fusion
is not free of the concerns on this site, only different in them.

## 6. Why: the binding-energy curve

One picture explains fission and fusion at once.

Weigh a helium-4 nucleus and it comes out *lighter* than two protons plus two neutrons weighed
separately. The missing mass was turned into energy when the nucleus was assembled — Einstein's
E = mc², with c² so large that a tiny bit of mass is an enormous amount of energy. That energy is
the **binding energy**: what it would cost to pull the nucleus apart again. Divide by the number
of nucleons and you get **binding energy per nucleon** — how tightly each particle is held, on
average.

Plot that number against mass number A for every nuclide and you get the binding-energy curve.
It rises steeply from hydrogen, peaks around **iron and nickel (A ≈ 56–62)**, and then slopes
gently downward all the way to uranium. Iron is the most tightly bound nucleus there is.

Now read the curve as a hill with iron at the top:

- **Light nuclei fusing** move up the hill toward iron: the product is more tightly bound than the
  pieces, so the difference comes out as energy. Fusion of hydrogen releases energy.
- **Heavy nuclei splitting** also move up the hill toward iron from the other side: the two
  fragments are each more tightly bound per nucleon than the uranium they came from. Fission of
  uranium releases energy.
- **Iron itself** can do neither. You cannot get energy out of iron by splitting it or fusing it,
  which is why stars die when their cores turn to iron.

The amounts are large because binding energies are measured in **millions of electron-volts
(MeV)** per nucleon, while chemical bonds are a few electron-volts. Fissioning one uranium
nucleus releases about 200 MeV — roughly fifty million times the energy of burning one carbon
atom. That ratio is the reason a few kilograms of fuel can run a city, and the reason the same
few kilograms need guarding.

## 7. Putting a number on it: Q-values

The hill picture tells you *whether* a reaction gives off energy. To find out *how much*, you
weigh both sides. The energy released by a reaction is called its **Q-value**, and the recipe is
the same for every reaction and every decay:

> **Q = (mass of what goes in − mass of what comes out) × c²**

If Q is positive, mass has disappeared and that mass came out as energy — kinetic energy of the
products, gamma rays, or both. If Q is negative, the reaction cannot happen unless the incoming
particle brings at least that much energy with it.

**A warning about signs.** If you have taken chemistry, this is backwards from what you learned
there. In thermodynamics a reaction is favored when ΔG (or ΔH) is *negative* — energy leaves the
system, so the system's energy goes down, so the sign is minus. Nuclear physics counts the same
event from the other side: Q is the energy *released*, so a reaction that gives off energy has a
*positive* Q. Same physics, opposite bookkeeping. An exothermic chemical reaction has ΔH < 0; an
exothermic nuclear reaction has Q > 0. Scientific conventions grew up in different rooms at
different times, and nobody went back to make them agree — so check which one a table is using
before you trust a sign.

Three things make the arithmetic easy:

1. **Use atomic masses in atomic mass units (u).** Tables of nuclear data list the mass of each
   *atom* — nucleus plus electrons — to nine or ten figures. As long as you use atomic masses on
   both sides, the electrons cancel out (the same number of electrons goes in and comes out,
   because charge is conserved), so you can ignore them.
2. **Convert with one number.** One atomic mass unit is worth **931.494 MeV** of energy. So
   Q (in MeV) = (mass in − mass out, in u) × 931.494. You never need c² itself.
3. **Only the last few decimal places matter.** The masses are all close to whole numbers; the
   energy is hiding in the fifth and sixth decimal places. Keep all the digits until the
   subtraction is done.

**Example 1: fusion.** Deuterium and tritium fuse to make helium-4 and a neutron (section 5).

| in | u | out | u |
|---|---|---|---|
| ²H | 2.014102 | ⁴He | 4.002603 |
| ³H | 3.016049 | n | 1.008665 |
| total | 5.030151 | total | 5.011268 |

Mass in − mass out = 0.018883 u. Times 931.494 gives **Q = +17.6 MeV**. That is the energy every
D–T fusion releases, most of it carried off by the neutron.

**Example 2: neutron capture.** A neutron hits uranium-235 and sticks (section 2):
n + ²³⁵U → ²³⁶U.

Mass in = 1.008665 + 235.043928 = 236.052593 u. Mass out = 236.045566 u. Difference 0.007027 u,
so **Q = +6.5 MeV**. This is the energy that arrives *inside* the new nucleus the instant the
neutron is absorbed, before anything else happens — and 6.5 MeV is more than enough to make
uranium-236 split. Do the same sum for n + ²³⁸U → ²³⁹U and you get only 4.8 MeV, which is not
enough. That two-MeV difference is the whole reason U-235 is a fuel and U-238 is not
(section 3).

**Example 3: fission.** One of the many ways uranium-235 can split:
n + ²³⁵U → ¹⁴¹Ba + ⁹²Kr + 3n.

Mass in = 236.052593 u. Mass out = 140.914404 + 91.926173 + 3 × 1.008665 = 235.866572 u.
Difference 0.186021 u, so **Q ≈ +173 MeV** for this split. Different fragment pairs give
slightly different numbers, and the fragments' later beta decays add more; the average over all
of them is the ~200 MeV per fission quoted in section 6.

**Example 4: binding energy from the same recipe.** Treat "assembling helium-4 from its parts" as
a reaction: 2 protons + 2 neutrons → ⁴He. Using the hydrogen-atom mass for the proton (so the
electrons cancel): 2 × 1.007825 + 2 × 1.008665 = 4.032980 u in, 4.002603 u out. Difference
0.030377 u → **28.3 MeV**. That is the binding energy of helium-4, and 28.3 ÷ 4 = **7.07 MeV per
nucleon** — exactly the number the curve in section 6 plots for helium. Every point on that curve
is this calculation done for one nuclide.

**A negative one, to see what it means.** Protons hitting lithium-7 to make beryllium-7 and a
neutron: mass in 8.023828 u, mass out 8.025594 u. The products are *heavier*, so
**Q = −1.64 MeV**. This reaction runs only if the proton arrives with more than 1.64 MeV of
kinetic energy (a little more, in fact, because some energy has to go into the recoil). Physicists
use exactly this reaction as a laboratory neutron source, with an accelerator to supply the
energy.

The same recipe gives the energy of any decay from Unit 3. Tritium → helium-3 + β⁻: the atomic
masses differ by 0.0000200 u, so Q = 18.6 **keV** — a thousand times less than a typical
reaction, which is why tritium's beta particles cannot get through skin. Alpha decay, gamma
decay, spontaneous fission: weigh in, weigh out, multiply by 931.494.

## Try it

- In the [explorer](/tools/nuclide-chart/), find U-238, then look one box to the right (U-239).
  Follow its decays: does it reach Pu-239 in two hops as section 2 says?
- Find a typical fission product — strontium-90 or cesium-137 — and check that it sits on the
  neutron-rich side of the valley and decays by β⁻.
- Pick any nuclide and write a balanced neutron-capture equation for it. Then find the product on
  the chart and see what it does next.
- Look up the atomic masses of plutonium-239, uranium-235 and helium-4 (the IAEA Live Chart
  lists them) and compute the Q-value of the alpha decay ²³⁹Pu → ²³⁵U + ⁴He. You should get about
  5.2 MeV. Then find Pu-239 in the explorer and see how its half-life compares with a nuclide
  whose alpha Q-value is 8 or 9 MeV — the pattern you notice has a name (the Geiger–Nuttall rule).

## Where this comes from

Neutron capture, fission, fusion and the binding-energy curve are in every introductory nuclear
physics text. Natural uranium is 0.72 percent U-235 by atom count (IAEA and NRC glossaries). The
fission-product mass distribution peaks near A = 95 and A = 140 for thermal fission of U-235
(evaluated fission-yield data). The ~200 MeV energy release per U-235 fission and the location of
the binding-energy peak near iron-56 and nickel-62 are standard. The atomic masses in section 7
are the AME2020 values as served by the IAEA Live Chart of Nuclides (retrieved 2026-09-22, in the
site's data pipeline), rounded to six decimals; 1 u = 931.494 MeV (CODATA 2018). The Q-values were
recomputed from the unrounded masses: D–T 17.589 MeV; n + U-235 6.546 MeV; n + U-238 4.806 MeV;
the Ba-141/Kr-92 split 173.28 MeV; He-4 binding 28.296 MeV; p + Li-7 −1.644 MeV; tritium decay
18.59 keV. The critical-mass statement is
kept deliberately at the level found in public encyclopedias; this site does not carry weapon-design
detail (see the site's [about page](/about/)).
