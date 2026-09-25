# SR-002 — Current-State Migration Reconciliation

Read-only reconciliation layer. Round-1 dossiers/evidence and Production were not changed.

## Current census
- Source HEAD: 78b8bc1939393f5f0a9afece7bbe1cf9f37ca3e9
- Current public post/taxonomy entities: 502
- Published products: 84; Round-1 reviewed: 83
- Current products missing from Round-1: [27727]

## Migration interpretation
- Product/volume: TRANSITIONAL. 30ml is new; historical 60ml/250ml URLs retain exact historical metrics and do not prove parent identity.
- Yoast to Rank Math: HISTORICAL_PRE_MIGRATION. The reset was intentional; missing Rank Math fields are not failed Yoast migration.
- Education to Academy: historical /education/ is HISTORICAL_PRE_MIGRATION; verified LearnDash destinations are CURRENT_VERIFIED; redirects alone prove transport.

## Education to Academy
- Historical URLs: 41; mapped: 36; verified: 0; partial: 36; unknown: 5
- Old draft records: 0; unexpectedly public: 0
- Current courses: 1; lessons: 37; hierarchy verified: True

## Finding dependency map
- Relationship counts: {'HISTORICAL_ONLY': 114, 'PARTIALLY_SUPPORTED': 15, 'NEEDS_TARGETED_REVIEW': 132, 'STALE_EVIDENCE_DEPENDENCY': 62, 'CURRENTLY_SUPPORTED': 1}
- Round-1 history remains immutable; no recommendation or disposition was decided.

## Tags, categories, attributes
- Product Tag, Blog Tag, Product Category and pa_volume matrices are in tag-category-attribute-reconciliation.json.
- Tags are recorded as TRANSITIONAL for the controlled decommission direction; no terms or redirects changed.

## Remaining gaps
- Page+Query dataset: NOT_AVAILABLE.
- Five SR-001 HTTP errors and targeted structured-data samples are in their dedicated JSON files.
