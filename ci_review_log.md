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
