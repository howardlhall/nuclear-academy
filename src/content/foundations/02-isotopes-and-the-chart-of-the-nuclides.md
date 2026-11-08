---
title: "Isotopes and the chart of the nuclides"
description: "Same element, different neutrons: what an isotope is, how to write one down, which ones are stable, and how to read the chart that nuclear scientists use instead of the periodic table."
order: 2
status: draft
lastReviewed: "2026-09-22"
before: ["Unit 1: Atoms and the periodic table"]
tool: "/tools/nuclide-chart/"
---

## 1. Same element, different neutrons

Unit 1 ended with a puzzle. The number of protons, Z, decides which element an atom is. But
nothing says how many neutrons have to come along. Carbon always has 6 protons; it can have 6
neutrons, or 7, or 8. All three are carbon. All three make the same molecules, burn the same way,
and end up in the same box on the periodic table.

Atoms of the same element with different numbers of neutrons are called **isotopes** of that
element. The word comes from Greek for "same place" — same place on the periodic table.

- Carbon-12 (6 protons, 6 neutrons) makes up about 99 percent of the carbon in your body.
- Carbon-13 (6 protons, 7 neutrons) is most of the rest.
- Carbon-14 (6 protons, 8 neutrons) is a trace — about one atom in a trillion — and it is
  radioactive. That is what makes carbon dating possible.

Chemistry cannot tell these apart, because chemistry is done by the electrons, and all three have
six of them. What sets them apart happens in the nucleus.

## 2. Writing an isotope down

You met the notation in Unit 1. Here it is again, because you will see all four forms:

| Form | Example | Reads as |
|---|---|---|
| Name and mass number | uranium-235 | "uranium two thirty-five" |
| Symbol and mass number | U-235 | same |
| Mass number raised in front | ²³⁵U | same |
| Full form, with Z as well | ²³⁵₉₂U | same (the 92 is redundant — "U" already means 92 protons) |

Whichever form you meet, the recipe is the same: the symbol tells you Z, the raised number is A,
and N = A − Z. For U-235: Z = 92, A = 235, so N = 143. For U-238: N = 146. Three neutrons is the
whole difference between the isotope that can sustain a chain reaction and the one that mostly
cannot — and that difference is what much of nuclear security is about.

One more word: a **nuclide** is any particular combination of Z and N — any one kind of nucleus.
"Isotope" is a comparison word (carbon-14 is an isotope *of carbon*); "nuclide" just names the
thing. Nuclear scientists mostly say nuclide.

## 3. Stable and unstable

Some nuclides last forever. Carbon-12 atoms in you were made inside stars billions of years ago
and have not changed since. These are **stable**.

Others fall apart on their own, sooner or later, into a different nuclide. These are
**radioactive** (or **unstable**), and the falling-apart is called **radioactive decay**. "Sooner
or later" covers an enormous range. Some nuclides last a fraction of a second; carbon-14 has a
half-life of about 5,700 years; uranium-238's is about 4.5 billion years, which is why there is
still plenty of it in the ground. Unit 3 explains half-life properly. For now, the one idea to
keep is that *stable versus unstable is a property of the nuclide, not the element.* Every
element has unstable isotopes; most of the light elements also have stable ones; above lead
(Z = 82) nothing is stable at all.

Why? Very roughly: protons repel each other (like charges push apart), and something has to hold
the nucleus together against that. The something is a short-range attraction between all nucleons
called the **strong nuclear force**, and neutrons add to it without adding repulsion. So a nucleus
needs a certain balance of neutrons to protons. Too few neutrons, or too many, and it is unstable.
For light nuclei the balance is about one to one (carbon-12: 6 and 6). For heavy nuclei it takes
extra neutrons to hold all those protons together (uranium-238: 146 to 92). Past a certain size
even the extra neutrons are not enough, and every nuclide is unstable.

## 4. A map with a box for every nuclide

The periodic table has one box per element. The **chart of the nuclides** has one box per
nuclide — thousands of boxes instead of a hundred.

Here is how it is laid out:

- Going **up** the chart, each row adds one proton. Z is the vertical axis. Every row is one
  element: hydrogen at the bottom, then helium, and so on.
- Going **across** the chart to the right, each column adds one neutron. N is the horizontal axis.
- So every box is one (Z, N) pair — one nuclide. All the isotopes of carbon sit in one horizontal
  row (Z = 6), side by side.
- The boxes are usually **colored by what the nuclide does**: one color for stable, and other
  colors for each kind of radioactive decay.

If you color it that way, a pattern jumps out. The stable nuclides form a narrow band running
from the bottom left toward the upper right — the **valley of stability** (or line of stability).
Close to the bottom, the band runs along the diagonal where N = Z. As it climbs it bends to the
right, toward more neutrons than protons, for the reason in section 3. Everything off the band is
radioactive, and — this is the useful part — the *kind* of decay depends on which side of the
band a nuclide is on. Nuclides with too many neutrons decay one way; nuclides with too few decay
another way; the very heavy ones at the top often do something else again. Unit 3 is about those
three ways.

The band stops at lead and bismuth. Above that, in the top right corner, there are no stable
boxes at all — only radioactive ones, some very long-lived. Uranium is up there.

## 5. Reading the chart

Three things you can do with the chart that you cannot do with the periodic table:

1. **Count neutrons at a glance.** Find the row for the element, then count boxes from the left,
   or read N off the bottom axis.
2. **See what a nuclide turns into.** When a nuclide decays, it moves to a nearby box — one row
   down and one column across, say, or two rows down and two columns across. Decay is a short hop
   on the chart, and a chain of decays is a path. Uranium-238 takes fourteen hops to reach lead-206,
   where it stops.
3. **See how many isotopes there are.** The row for tin (Z = 50) has ten stable boxes, the most of
   any element. Some rows have one. The heavy rows have none.

The explorer linked below draws the chart from the same data that professionals use — the
evaluated nuclear data files kept by the U.S. National Nuclear Data Center — and lets you click
any box to see how long that nuclide lasts and where it goes.

## Try it

- Open the [nuclide chart explorer](/tools/nuclide-chart/). Find carbon (Z = 6). Which boxes are
  stable? Click carbon-14. What does it turn into, and how long does it take?
- Find the row for uranium. How many boxes are there? Are any of them stable?
- Starting from U-238, follow the hops until you reach a stable box. Count them.
- Pick any element in the middle of the chart. Notice that its stable boxes are usually near the
  band and its radioactive boxes are off to either side.

## Where this comes from

Isotopes, nuclides and the neutron–proton balance are in every introductory nuclear physics or
chemistry text. Carbon-14's half-life is about 5,700 years and U-238's about 4.47 billion years,
from the National Nuclear Data Center's evaluated data (the same data this site's tools use). Tin
has ten stable isotopes; no element above bismuth has a stable one, and bismuth-209 itself was
found in 2003 to be very slightly radioactive, with a half-life far longer than the age of the
universe. The chart of the nuclides in printed form is published by several laboratories; the
Karlsruhe chart and the Knolls Atomic Power Laboratory chart are the best known.
