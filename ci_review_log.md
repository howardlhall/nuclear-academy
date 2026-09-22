# CI review log — nuclear.academy

One line per screened page version, newest last. Required by § 4a of the authoring quality protocol
(kept in the editor's planning folder). This log is a decision record, not a gate [HLH 2026-09-01]:
most lines should read `clear`. Clear findings are logged too — a missing line is indistinguishable
from a skipped screen. Never record here anything the screen flagged as classified, UCNI, SGI, CUI or
export-controlled; log that a finding was made, its disposition, and where the detail is held.

## Standing proximity (baseline) — set 2026-09-22, re-derive at any structural change

| Trigger class | Why it is inherent here | Level of treatment judged acceptable |
|---|---|---|
| Subject matter (nuclear security, safeguards, fuel cycle) | The site's purpose | Open-literature, textbook level; no facility-specific protection detail; no UCNI/SGI-adjacent content |
| Aggregation / compilation (facilities atlas) | A geolocated, categorized dataset of world nuclear facilities is the textbook compilation case (10 CFR 1045.130) | Civil fuel cycle first, from IAEA PRIS/RRDB/NFCIS, NRC and comparable public compilations; the **dataset schema is screened as its own versioned product**; the military-cycle layer is designed last, screened before any row, and built only from already-published compilations (IPFM, SIPRI, FAS) cited row by row |
| Automated content (daily feed) | A scheduled task drafts news/regulatory items | Drafts go to a review queue; nothing goes live without a human merge |
| Weapons basics (Module 1 § 4) | The seed lecture covers the fissile-material barrier at the public-lecture level | Stays at the level of the public record it cites; no design detail beyond the two-path statement already in the open literature |

## Per-version screens

| Date | Version | Sources refreshed (checked) | Movement vs. baseline | Finding | Action / where detail is held |
|---|---|---|---|---|---|
| 2026-09-22 | scaffold v0.1 (no content) | n/a — no outbound content | baseline set | n/a | none |
| 2026-09-22 | atlas v0.1 (diagrams, explainer, facilities schema v1) + decay-chain calculator v0.1 | 10 CFR 1017, 1045.130, 73.22, 810; 15 CFR 734.7; DOE S&T Risk Matrix (Apr 2026) — checked 2026-09-22; not reached: DOE O 471.7 text, NCSC (archived site), OSTP CETL, UTK page | baseline set: subject matter (C2 general) + aggregation (civil layer, public registers) | items 1–4 clear; item 5 revise-and-publish → clear | Generic Wikidata class dropped (mixed defense sites into civil layer); two misclassifications corrected via overrides. Full block below. |
| 2026-09-22 | Module 1 v3 (post cold review + diff-zone) + situation page v3 (new) + glossary/source additions | 10 CFR 1045.130 and 1045.65 re-read from eCFR (page current as of 2026-09-10; both sections last amended 83 FR 66007, 2018); part 1045 shows 2026 amendments (5/29, 7/09) in other sections — **not read this run**; other basis items as 13:20 run, not re-fetched | movement: Module 1 now names state attacks on facilities, the Iran verification gap, and the transport-theft pattern; situation page adds dated Iran/testing/ZNPP status | items 1–6 clear; item 7 (isotope list) removed | Full block below. |
| 2026-09-22 | Foundations F1–F5 (draft) + nuclide chart explorer v0.1 | as the 15:15 run (same day; not re-fetched) | none — textbook-level content (atoms, isotopes, chart of the nuclides, decay modes, capture/fission/fusion, half-life arithmetic); explorer re-serves the same ENSDF table already screened with the calculator, adds no selection | clear (screened at draft stage; re-screen with the § 0 cycle before `main`). **Note for the DC:** F4 § 4 states critical mass at the public-encyclopedia level ("on the order of tens of kilograms" for bare U-235; reflector/compression lower it) and says the site goes no further; F4 § 2 states the U-238 → Pu-239 capture chain. Both are in every textbook; C5 — no sentence characterizes accuracy of any open-literature figure. | HLH reads F4 before `main` |
| 2026-09-22 | Module 2 (fuel cycle) draft + situation page `us-spent-fuel-and-the-back-end` | as the 15:15 run (same day) | movement: first treatment of enrichment/reprocessing as safeguards subject matter; SWU ratio, SQ, MUF arithmetic — all IAEA-glossary/textbook level; no process parameters, no facility detail beyond public dockets | clear (draft stage). C3 note: the "most of the SWU is spent reaching LEU" statement is the standard public explanation (NRC/IAEA outreach) and states no parameters. | HLH reads §5–6 as DC before `main` |
| 2026-09-22 | Modules 3 (safeguards), 4 (forensics), 5 (fusion) drafts + 12 glossary entries | as the 15:15 run (same day) | movement: forensics module describes signature families, MS technique families and chronometry at textbook/ITWG-guideline level; fusion module states breeding and tritium pathways at the Goldston–Glaser (open) level; safeguards module at glossary level. No process parameters, no library contents, no post-detonation method. | clear (draft stage). C5 note: Module 4 makes no statement about the accuracy of any open-literature technical claim; Module 5 cites the CATF lecture, which HLH gave publicly. | HLH reads M4 §§3–5 and M5 §3 as DC before `main` |
| 2026-09-22 | Modules 6 (reactor types), 7 (enrichment), 8 (reprocessing options), 9 (treaties) drafts + teachers' notes | as the 15:15 run (same day) | **movement: enrichment and reprocessing are now described as technologies**, at the level of the NRC backgrounder and the NEA/INL public reports — principles of each method, no rotor, stage, cascade, flowsheet or throughput parameters; "re-piping to feed product back" stated only as the generic reason 20 % is a bright line. Reactor module names fuel/moderator/coolant classes and the plutonium-quality ranking found in every textbook. | clear (draft stage); **C3/C5 attention items for the DC: M7 §§2–3 and §5; M8 §2 (PUREX outline) and §5.** | HLH reads M7 and M8 in full as DC before `main` |

### CI screen — atlas v0.1 and decay-chain calculator v0.1, 2026-09-22 (run 13:20–13:35 local)

**Sources refreshed (checked 2026-09-22):** 10 CFR 1017 (eCFR current as of 2026-09-17; § 1017.11(b) basic-scientific-information exemption confirmed); 10 CFR 1045.130 (eCFR 2026-09-18; association/compilation); 10 CFR 73.22(a) SGI categories (eCFR 2026-09-18 — no category covers the existence or location of a licensed facility); 10 CFR 810 (eCFR 2026-09-18; § 810.2(c)(2)/§ 810.3 exclude publicly available information); 15 CFR 734.7 "published" (eCFR 2026-09-17; posting on a public website qualifies); DOE S&T Risk Matrix (energy.gov document, effective April 2026: six domains, countries China/Russia/Iran/Belarus/North Korea — none of the six domains touched). **Not reached:** DOE O 471.7 text (not fetched this run); NCSC Safeguarding Science site (dni.gov redirects to an archive that states it is no longer updated — recorded as archived, no newer advisory found); OSTP Critical and Emerging Technologies List (not located on OSTP news page this run; last known Feb 2024 list); UTK Office of Research export-control page (not fetched).

**Delta screened:** everything — first screen of both products.

**Items and findings.**
1. *Civil fuel-cycle diagram* — generic stage overview; enrichment stated as 0.7 → 3–5 %; no parameters, no facility. C2 general treatment. **Clear.**
2. *Weapons-routes diagram* — states that HEU is uranium enriched to ≥ 90 %, that a plutonium route uses short irradiation and reprocessing, and the IAEA significant quantities (25 kg U-235 in HEU, 8 kg Pu). All from the IAEA Safeguards Glossary and NRC/NAS public overviews; weaponization boxed as out of scope and not depicted; no process parameters, no design detail. C2 general treatment; C5 — no sentence characterizes the accuracy of any open-literature claim. **Clear.** Note for the author as a derivative classifier: the figure text stays at glossary level by design; any future annotation must not confirm or expand on technical specifics in the open literature (10 CFR 1045.65(a)).
3. *Explainer* — capability-vs-use framing; names France's civil reprocessing and HALEU < 20 %. Public. **Clear.**
4. *Decay-chain calculator page and method text* — Bateman mathematics; ENSDF data re-served with attribution (public-domain disposition [HLH 2026-09-22]); no facility, no inventory. Aggregation: ENSDF is itself a public compilation; the site adds no selection. Actinide half-lives and branching are in every nuclear data handbook. **Clear.**
5. *Facilities layer schema and dataset v1* — C1 aggregation trigger fires by construction (geolocated, categorized compilation). Screened: sources are Wikidata only; every field is a public-register field (name, location, country, operator, dates, status, capacity); existence/location is not SGI (§ 73.22 checked today); comparable compilations are published by IAEA (PRIS/RRDB/NFCIS), GEM and NTI, so the selection adds no new public picture. **Finding on first pass: revise-and-publish.** The generic Wikidata class "nuclear facility" (27 items) mixed defense-program sites (Mayak, Savannah River, Negev NRC, Yongbyon, Taechon, Sellafield/THORP, Z machine) into a layer the page describes as civil, and carried two misclassifications (a concentration camp as a repository; Fordow as "other"). **Revision applied same session:** class dropped from the pipeline; Fordow reclassified as enrichment and Leitmeritz excluded through `pipelines/overrides/facilities.json` with reasons; page text and filters updated; dataset rebuilt (500 features). **After revision: clear.** Baseline recorded: civil layer, public registers, no military layer; any military layer is movement and gets its own schema screen before a single row.

**Aggregation check:** the site's public picture after this version = two textbook diagrams + a civil-facility map equivalent in content to PRIS/RRDB/Wikipedia. Nothing joins previously unjoined sources.

**Movement vs. baseline:** baseline set this screen (see header); none beyond it.

**Finding:** clear (items 1–4); revise-and-publish → clear after revision (item 5).
**Action:** none further before merge to `main`; HLH's editorial read of the explainer is a separate (non-CI) gate.

### CI screen — Module 1 v3 and situation page v3, 2026-09-22 (run 15:15–15:25 local)

**Sources refreshed (checked 2026-09-22, this run):** 10 CFR 1045.130 (eCFR; text unchanged, last amended 83 FR 66007) and 10 CFR 1045.65 (same) re-read in full. eCFR shows part 1045 amended 2026-05-29 and 2026-07-09 in sections not read this run — **recorded as a gap; HLH to confirm those amendments do not touch the no-comment or compilation rules.** Other basis items (10 CFR 1017, 73.22, 810; 15 CFR 734.7; DOE S&T Risk Matrix Apr 2026) as the 13:20 run today; not re-fetched.

**Delta screened:** v1→v3 diff of Module 1 (`Nuclear_Academy_Website/reviews_20260922/module1_v1_to_v2.diff`, `module1_v2_to_v3.diff`); the whole situation page; four glossary entries; sixteen source-library entries.

**Items and findings.**
1. *Definitions (§ 2)* — verbatim IAEA glossary text; multilingual usage. **Clear.**
2. *§ 4 weapons basics* — unchanged two-path statement from v1 (gun-type/implosion at encyclopedia level); new text adds no technical detail; the "limits of the consensus" paragraph is argumentative, not technical. C5: no sentence characterizes the accuracy of any open-literature technical claim; the Oppenheimer remark is marked "attributed." **Clear.**
3. *§ 4 Additional Protocol / Iran* — safeguards-policy content from IAEA public reports and press; no facility detail beyond public names. **Clear.**
4. *§ 6 non-state threat* — "gun-type requires HEU" retained (open literature, NSS-level, unchanged from v1); **the four-isotope RDD list removed** (uncited in v1; its removal also answers the reviewers' pairing concern — the module no longer lists preferred source isotopes next to an atlas link). The transport-theft pattern (55 % / 70 %) is the IAEA's own headline finding, published for that purpose. **Clear after removal.**
5. *§ 6 legal framework, § 7 trends, "States as attackers"* — policy and public-event content; the module states that it does not adjudicate the attacks. **Clear.** Institutional note (C6): the passage on DOE-authorized demonstration reactors and "whose security rules apply" is a public regulatory question, stated neutrally; HLH to read as the NNSA-funded author before `main`.
6. *Situation page* — SIPRI table (published dataset), treaty status, IAEA Board actions, Chernobyl NSC status, ITDB counts — all from the cited public reports; no facility-protection detail. C1: re-serving SIPRI's table is not a new compilation. **Clear.**
7. *Glossary/source entries* — bibliographic. **Clear.**

**Aggregation check:** the site's public picture after this version adds a dated policy page and a longer module; nothing joins previously unjoined sources. The atlas is unchanged since the 13:20 screen.

**Movement vs. baseline:** the "weapons basics" row of the baseline is unchanged in technical content. New subject matter (state attacks; Iran) is policy-level and public. Recorded, no baseline change.

**Finding:** clear (items 1–3, 5–7); revise → clear (item 4).
**Action:** none further for CI before merge to `main`. Separate non-CI gates still open: HLH editorial pass; award-terms check for DE-NA0004197 (reviewer flag); the § 0 gate is **not** satisfied for v3 (no cold read of v3 exists yet — see reviews folder).
