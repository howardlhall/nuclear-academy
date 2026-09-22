# Content inventory

One row per page or tool. Status: `draft` → `reviewed` (editor read) → `screened` (self-audit, cold
read, CI screen logged) → `live` (merged to `main`). Sources column lists source-library keys.

| Path | Title | Type | Status | Sources | Owner | Last reviewed |
|---|---|---|---|---|---|---|
| `/` | Home | page | draft | — | HLH | — |
| `/about` | About | page | draft | — | HLH | — |
| `/modules/nuclear-security-why-it-matters` | Module 1: Nuclear Security — Why It Matters | module | draft (stub) | — | HLH | — |
| `/tools/decay-chain` | Decay-chain calculator (branched Bateman network, ENSDF data) | tool | draft — built 2026-09-22, tests pass, on `dev` | ENSDF ensdf_260901 (DOI 10.18139/nndc.ensdf/1845010); Bateman 1910 | assistant | — |
| `/atlas` | Facilities atlas (first cut) | tool | draft (stub) | — | assistant | — |
| `/glossary` | Glossary | index | draft | — | researcher | — |
| `/sources` | Source library | index | draft | — | researcher | — |
