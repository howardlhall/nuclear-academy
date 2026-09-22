---
title: "Nuclear Forensics: Who Made This Material?"
description: "How scientists read the history of a piece of nuclear or radioactive material from its isotopes, its impurities, its shape, and whatever came with it — what the answers can and cannot establish, why the clock in every sample is a Bateman equation, and what a famous fingerprint error teaches the field."
order: 4
status: draft
lastReviewed: "2026-09-22"
objectives:
  - "State what nuclear forensics can and cannot conclude, and the difference between pre- and post-detonation work."
  - "Name the four families of signatures in a sample and give an example of each."
  - "Explain how a parent–daughter ratio gives a material's age, and why more than one chronometer is used."
  - "Know which measurement technique answers which question, at the level of choosing the right tool."
  - "Explain why forensic conclusions are probabilistic and what confirmation bias does to an expert."
---

*Adapted from the author's graduate course NE-635 at the University of Tennessee, at the level
of its open-literature sources. The field's standard texts are Moody, Hutcheon and Grant,
*Nuclear Forensic Analysis*, and Fedchenko (ed.), *The New Nuclear Forensics*; this module is a
door into them, not a substitute. The [decay-chain calculator](/tools/decay-chain/) on this site
does the arithmetic behind section 5.*

## 1. The question

After any nuclear incident — a seizure of smuggled material at a border, a radioactive source
found in a scrapyard, a detonation — the first question anyone asks is *who made this?* Nuclear
forensics is the discipline that tries to answer it from the material itself, by reading the
history written into a sample's isotopes, chemistry, and physical form, and combining that with
everything else the sample carries: the container, the packaging, the fingerprints on the bag.

It is forensic science in the ordinary sense — the scientific method applied to a past event,
constrained by evidence rules, aiming at conclusions a court or a government can act on — with
one unusual feature. The material in question is radioactive, sometimes intensely, and often
dangerous in other ways, so every step from the field to the laboratory has to preserve the
evidence and protect the people at once.

Two settings, two different jobs. **Pre-detonation** forensics works on intact material: an
interdicted package, an orphaned source, a swipe sample from a suspect facility. The bulk
material is the evidence, and the questions are *what is it, what process made it, where did it
come from, how did it get here.* **Post-detonation** forensics works on what a nuclear explosion
leaves — glass, fallout, activated debris — under intense time pressure, and asks about the
device and its origin from samples that have been melted, mixed, and fractionated. This module
is mostly about the first; the second is a subject of its own and this site stays at the level
of what it is, not how it is done.

And one caution at the outset, which section 7 makes concrete: nuclear forensics provides
*conclusions*, with stated confidence, not always *answers*. The right output of a forensic
analysis is "these observations are consistent with origin A and inconsistent with origins B and
C," not "it was A."

## 2. Four kinds of signature

A **signature** is any measurable property that narrows down where a material came from or what
was done to it. They fall into four families.

**Isotopic.** The ratios of isotopes in the sample. The uranium-235 fraction tells you the
enrichment — natural, reactor grade, HALEU, or weapons grade — and the minor isotopes
uranium-234 and uranium-236 say more: U-236 exists only in uranium that has been through a
reactor, so its presence means recycled material, and the U-234 ratio varies with the ore and
the enrichment process. In plutonium the ratio of Pu-240 to Pu-239 records how long the fuel
was irradiated. Isotopes are the most powerful signatures because chemistry cannot change them.

**Chemical.** Trace and minor elements carried along from the ore body, from the reagents used
in processing, or picked up in storage and transport. Rare-earth patterns point to the geology
of the source; process contaminants point to the extraction and refining chemistry; and
contamination is often the most variable but most distinctive of all. Organic residues —
solvents, lubricants, plasticizers — record handling and packaging, and have solved cases: a
pigmented paraffin wax in one European seizure pointed to a particular region's packaging
practice.

**Physical.** Shape, size, crystal structure, surface texture. A fuel pellet has a
manufacturer's dimensions; a powder has a particle-size distribution that reflects how it was
precipitated and calcined; a metal has a microstructure that reflects how it was cast and worked.
Under a microscope a sample tells you what kind of plant it came out of.

**Collateral.** Everything that is not the nuclear material: the container and its alloy (lead
shielding carries its own isotopic fingerprint from the ore it was smelted from), the paper the
material was wrapped in (pulp species, manufacturing process), the ink on the label,
fingerprints, DNA, hair and fibers. These are the province of conventional forensic laboratories,
which is why a nuclear case is worked jointly with them from the first hour — and why samples
have to be handled so that radiation does not destroy the DNA and the DNA swab does not
contaminate the isotopics.

No single signature identifies a source. The method is to assemble as many as the sample
offers and compare the pattern against reference materials and databases of known origin. The
strength of a conclusion is the number of independent signatures that agree.

## 3. Reading the sample: the tools

The measurements fall into two broad classes, and knowing which answers which question is most
of what a non-specialist needs.

**Radiation counting** measures the radiation a sample emits. Gamma spectroscopy identifies
radioactive nuclides by the characteristic energies of their gamma rays, non-destructively and
quickly — it is the first thing done to any unknown sample, often in the field with a portable
instrument. Alpha spectroscopy, after chemical separation, does the same for alpha emitters
such as plutonium and americium. Counting is limited by half-life: a nuclide that decays slowly
gives few counts, and uranium-235, with a half-life of 700 million years, is effectively stable
on the timescale of a measurement.

**Mass spectrometry** counts atoms directly rather than waiting for them to decay, and so
reaches sensitivities that counting cannot for long-lived isotopes. There is a family of
instruments, each with a job:

- **Thermal ionization mass spectrometry (TIMS)** gives the most precise isotope ratios —
  parts per million — and is the "court-quality" measurement for certifying the isotopics of a
  seized uranium or plutonium sample. It is slow and its sample preparation is exacting.
- **Inductively coupled plasma mass spectrometry (ICP-MS)** is the workhorse for trace-element
  profiling and, in its multi-collector form, approaches TIMS precision much faster.
- **Secondary ion mass spectrometry (SIMS)** measures single particles tens of nanometers
  across. Because bulk samples are mixtures, the rare anomalous particle in an environmental
  swipe is what SIMS finds — it has been the IAEA's standard tool for safeguards swipe samples
  since the 1990s, and it is how undeclared enrichment has been detected from dust.
- **Accelerator mass spectrometry (AMS)** reaches ultra-trace levels for long-lived nuclides
  such as uranium-236 and iodine-129.

Behind the instruments sits **radiochemistry**: the separations that isolate a trace daughter
from a bulk parent, or a picogram of plutonium from a gram of dirt, so that the spectrometer
sees what matters. Much of the skill of the field is there.

## 4. The age of a sample

Every radioactive sample carries a clock, and the clock is the decay chain you met in
[Foundations 3](/foundations/03-radioactive-decay/).

When uranium or plutonium is chemically purified — at the end of enrichment, or when metal is
cast — its decay daughters are removed. From that moment the daughters begin to grow back in at
a rate fixed by physics. Measure the ratio of a daughter to its parent, solve the Bateman
equations backwards, and you have the time since purification: the **model age** of the material.
Thorium-230 growing into uranium-234, or uranium-234 into plutonium-238, or americium-241 into
plutonium-241, each gives a chronometer; the one to use depends on the material and the age
range.

Two things make chronometry robust. First, the daughters are present in vanishingly small
amounts, which is where radiochemical separation and mass spectrometry come in. Second, a sample
has **several** chronometers, and they should agree. If the thorium clock and the protactinium
clock give different ages, either the purification was incomplete, the material has been mixed
from batches of different ages, or someone has tampered with it — all of which are themselves
findings. A single chronometer is an estimate; concordant chronometers are evidence.

You can run the forward problem yourself: put a gram of pure U-234 into the
[decay-chain calculator](/tools/decay-chain/), and watch Th-230 grow in. The forensic problem is
that curve read from right to left.

## 5. Putting it together: a case sketch

A composite, at the level of the published record.

Material is seized at a border crossing: a few grams of dark powder in a glass vial, inside a
lead container, wrapped in wax paper, in a briefcase. Gamma spectroscopy at the scene says
uranium, and says it is enriched — the U-235 lines are strong. The container, the wax and the
paper go to a conventional forensic laboratory; the powder goes to a nuclear one.

TIMS puts the enrichment at 72 percent, weapons-usable HEU, and the U-236 content says it has
been through a reactor. The U-234 ratio is compared with reference materials. ICP-MS trace
elements show a rare-earth pattern and a set of process contaminants; the physical form —
uranium oxide of a particular particle morphology — is consistent with a specific kind of fuel
fabrication. A chronometer puts the last purification decades in the past. Meanwhile the wax
turns out to contain a barium chromate pigment characteristic of one region's industrial
practice; the paper's pulp species narrows the region further; the lead shielding's antimony
content and isotopics match a particular smelter tradition.

None of those results names a facility. Together they say: HEU, of a fuel type used by a
particular class of research reactors, produced at a particular era, packaged in a particular
part of the world. That is enough to direct an investigation, to rule out several stories the
courier told, and to feed the international database that lets the next seizure be compared
with this one. The 1999 Bulgarian seizure, which this sketch draws on, was worked in essentially
this way and is one of the field's teaching cases.

## 6. The libraries, and the international system

A signature is only useful if it can be compared with something. Nuclear forensics therefore
depends on **reference materials** — certified samples of known origin — and on **libraries**
of signatures from known facilities and processes. Most of the libraries are national, held by
the states that own the facilities, and much of their content is sensitive; the international
system works by having each state able to say whether a sample is consistent with its own
holdings, rather than by pooling everything.

The Nuclear Forensics International Technical Working Group (ITWG), founded in 1995, is where
laboratories compare methods and run round-robin exercises on shared samples. The IAEA
publishes the guidance and maintains the Incident and Trafficking Database
([Module 1, section 6](/modules/nuclear-security-why-it-matters/)), and national laboratories in
the United States, Europe, Russia, and elsewhere do the analysis. The discipline is small — a
few hundred practitioners worldwide — and its casework is mostly unpublished, which is why the
open teaching cases are few and old.

## 7. The lesson of a fingerprint

In March 2004, after the Madrid train bombings, the FBI's automated fingerprint system returned a
partial print from a bag at the scene as a match to an Oregon lawyer named Brandon Mayfield.
Three FBI examiners and an independent expert confirmed it. Spanish authorities disputed the
match; the FBI arrested Mayfield anyway and held him for two weeks. The print belonged to an
Algerian national. The U.S. government apologized and paid a settlement, and the Department of
Justice's inspector general found that the examiners, having committed to a conclusion, had
explained away the differences that should have stopped them.

The lesson is not about fingerprints. It is that a well-established technique, applied by
experts, produced a confident wrong answer because the analysts saw what they expected to see.
Nuclear forensics is exposed to exactly the same failure: a signature library returns
candidates, not answers; an analyst under time pressure with a plausible story will find the
evidence fits it; and the more consequential the case, the greater the pressure. The defenses
are the ordinary ones of good science — independent review, an explicit search for
disconfirming evidence, stated uncertainties, and a culture in which the dissenting examiner
is heard — and the field teaches the Mayfield case for that reason.

That is also why the honest output of a nuclear forensic analysis is a set of observations with
their consistency and inconsistency with each hypothesis, and a confidence level, rather than a
name. The scientist's job ends there. What to do with the conclusion — a prosecution, a
diplomatic demarche, a strike — is a decision for others, made on more than the science.

**Explore.** (a) You are handed a gamma spectrum showing strong lines from cesium-137 and
nothing else. What can you say about the source, and what can you not? (b) Why is uranium-236
such a useful signature, and what would its complete absence tell you? (c) A sample's thorium
chronometer says 12 years and its protactinium chronometer says 30. List three explanations. (d)
Apply the Mayfield lesson to a hypothetical: a seized sample's rare-earth pattern is "consistent
with" a country the investigators already suspect. What should happen next?

---

### Sources

1. K. J. Moody, I. D. Hutcheon and P. M. Grant, *Nuclear Forensic Analysis*, 2nd ed. (CRC Press,
   2014).
2. V. Fedchenko (ed.), *The New Nuclear Forensics: Analysis of Nuclear Materials for Security
   Purposes* (SIPRI / Oxford University Press, 2015).
3. International Atomic Energy Agency, *Nuclear Forensics in Support of Investigations*, Nuclear
   Security Series No. 2-G (Rev. 1) (2015).
4. Nuclear Forensics International Technical Working Group (ITWG), guidelines and exercise
   reports (nf-itwg.org).
5. The 1999 Bulgarian HEU seizure as described in the open literature (e.g., Fedchenko, ed.,
   2015, and IAEA/ITWG case summaries); the Moldova 2011 case, Module 1.
6. U.S. Department of Justice, Office of the Inspector General, *A Review of the FBI's Handling of
   the Brandon Mayfield Case* (2006).
7. Varga et al., rapid plutonium age dating by MC-ICP-MS (2015), and the chronometry literature
   summarized in source 1.
8. H. L. Hall, NE-635 *Nuclear Forensics*, University of Tennessee, course modules 0, 4 and 6
   (Spring 2027 revision), at the level of their open sources.

*This material is based in part upon work supported by the Department of Energy National Nuclear
Security Administration through Defense Nuclear Nonproliferation's Enabling Capabilities in
Technology Consortium under Award Number DE-NA0004197. The views and opinions expressed are the
author's own and do not necessarily state or reflect those of the United States Government or any
agency thereof.*
