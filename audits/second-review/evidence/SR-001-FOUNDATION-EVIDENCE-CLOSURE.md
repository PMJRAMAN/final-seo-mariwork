# SR-001 — Foundation Evidence Closure

This document records new read-only evidence for independent Second Review. It is not another SEO audit and does not change Round-1 dossiers or dispositions.

## Baseline

- Round-1 source handoff HEAD: `01b91a5a3a41bf7df45bd8fb5e35252beabeb61f`
- Round-1 page dossiers: 167/167 `CODEX_AUDITED`; model remaining 0; blocked 0.
- Production writes: none. Main Round-1 service remained inactive.

## Rank Math and ownership

- Rank Math: see `seo-ownership-matrix.json`; the active plugin is recorded with version, active modules, safe allowlisted settings, theme and relevant active plugins.
- Hook inspection is a path/concern matrix only; source code was not copied.

## Public SEO output

- Checked 167 of 167 current URLs with anonymous GET and at most two concurrent workers.
- JSON-LD was present on 162 entities; 5 had no JSON-LD script. Parsed types and errors are in `current-seo-output-summary.json`.
- `round1_parser_discrepancy` is `TRUE`. Original Round-1 evidence was not edited.
- Five URLs returned public HTTP errors; exact errors are retained in `current-seo-output.jsonl`.

## Sitemap and runtime evidence

- Sitemap walk saw 7 public sitemap documents with 145 URL memberships and no sitemap-fetch errors. Entity-level membership is in `sitemap-membership.json`.
- Sanitized aggregate Woo/WordPress architecture is in `store-runtime-architecture.json`; no customer/order/user data is included.

## GSC closure

- `gsc-foundation-summary.json` records the immutable Pages.csv/Chart.csv date range, row count, totals, weighted CTR, top pages, classifications and provenance. Pages and Queries remain separate.
- `PAGE_QUERY_DATASET = NOT_AVAILABLE`.

## Foundation artifacts

- A-018: `strategy/QUERY-MAP.md`
- A-019: `strategy/CONTENT-ARCHITECTURE.md`
- Sitewide/Foundation audit index remains in `handoff/round1/round1-sitewide-index.json`.

## Readiness

- SYS readiness counts: {'PARTIALLY_READY': 8, 'READY': 2, 'STILL_BLOCKED': 2}.
- These labels indicate evidence availability for ChatGPT Second Review only; they are not finding decisions.

## Migration reconciliation supplied by the project owner

- Product/volume architecture is TRANSITIONAL: 30ml is new, historical 60ml/250ml URLs must be reconciled to current parent/variation structure, and redirects prove transport only, not entity equivalence. Historical GSC metrics remain attached to their original URLs.
- Yoast to Rank Math is HISTORICAL_PRE_MIGRATION: the reset was intentional; missing current Rank Math fields are not automatically failed Yoast migration, and old Yoast metadata must not be restored solely because it existed.
- These labels are reconciliation aids for independent Second Review. They do not alter Round-1 findings or dispositions. Full machine-readable facts are in migration-reconciliation.json.
