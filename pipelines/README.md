# Pipelines

Scripts that build `src/data/*` from public sources. Every script:

- records its source, URL, retrieval date, and the source's redistribution terms in `SOURCES.md`
  **before** any data is stored;
- writes machine-generated files only; hand corrections go in `overrides/*.json` with a `reason`;
- is re-runnable from a clean checkout.

Planned: `build_nuclides.py` (decay data for the Bateman calculator), `build_facilities.py`
(civil fuel-cycle facilities → `src/data/facilities.geojson`).
