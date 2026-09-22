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
