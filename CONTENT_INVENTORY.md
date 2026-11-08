# Content inventory

One row per page or tool. Status: `draft` → `reviewed` (editor read) → `screened` (self-audit, cold
read, CI screen logged) → `live` (merged to `main`). Sources column lists source-library keys.

| Path | Title | Type | Status | Sources | Owner | Last reviewed |
|---|---|---|---|---|---|---|
| `/` | Home | page | draft | — | HLH | — |
| `/about` | About | page | draft | — | HLH | — |
| `/modules/nuclear-security-why-it-matters` | Module 1: Nuclear Security — Why It Matters | module | draft — 4,100 words, 8 sections, drafted 2026-09-22 from the NE 200 deck; **self-audit, cold read and CI screen owed**; two deck errors corrected (Arabic 1973; Goldsboro) | 17 sources (SIPRI YB 2025, IAEA PR 21/2026, WNA 2026 verified 2026-09-22; others from the deck, links to verify) | HLH (author); assistant drafted | — |
| `/tools/decay-chain` | Decay-chain calculator (branched Bateman network, ENSDF data) | tool | draft — built 2026-09-22, tests pass, on `dev` | ENSDF ensdf_260901 (DOI 10.18139/nndc.ensdf/1845010); Bateman 1910 | assistant | — |
| `/atlas` | Atlas: civil fuel cycle diagram, weapons-routes diagram, explainer, facilities map (first cut) | tool + explainer | draft — built 2026-09-22 on `dev`; CI screen owed | IAEA Safeguards Glossary 2022 §§ 3.14, 4.24; WNA fuel cycle; NRC fuel-cycle stages; NAS 1994; Wikidata; OpenFreeMap | assistant (text: HLH to edit) | — |
| `/glossary` | Glossary (14 terms) | index | draft | IAEA glossaries, DoDD 3150.02, NRC | researcher | — |
| `/sources` | Source library (16 entries) | index | draft | — | researcher | — |
