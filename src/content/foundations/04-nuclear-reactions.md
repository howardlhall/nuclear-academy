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

## Try it

- In the [explorer](/tools/nuclide-chart/), find U-238, then look one box to the right (U-239).
  Follow its decays: does it reach Pu-239 in two hops as section 2 says?
- Find a typical fission product — strontium-90 or cesium-137 — and check that it sits on the
  neutron-rich side of the valley and decays by β⁻.
- Pick any nuclide and write a balanced neutron-capture equation for it. Then find the product on
  the chart and see what it does next.

## Where this comes from

Neutron capture, fission, fusion and the binding-energy curve are in every introductory nuclear
physics text. Natural uranium is 0.72 percent U-235 by atom count (IAEA and NRC glossaries). The
fission-product mass distribution peaks near A = 95 and A = 140 for thermal fission of U-235
(evaluated fission-yield data). The ~200 MeV energy release per U-235 fission and the location of
the binding-energy peak near iron-56 and nickel-62 are standard. The critical-mass statement is
kept deliberately at the level found in public encyclopedias; this site does not carry weapon-design
detail (see the site's [about page](/about/)).
