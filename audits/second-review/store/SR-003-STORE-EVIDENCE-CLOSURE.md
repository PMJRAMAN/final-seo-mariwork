# SR-003 — Store Evidence Closure

Read-only current Store evidence. Original Round-1 evidence/dossiers remain immutable; WP-27727 is a post-Round-1 coverage addition.

## Classification correction
- Before: {'CURRENTLY_SUPPORTED': 1, 'HISTORICAL_ONLY': 114, 'NEEDS_TARGETED_REVIEW': 132, 'PARTIALLY_SUPPORTED': 15, 'STALE_EVIDENCE_DEPENDENCY': 62}
- After: {'NEEDS_TARGETED_REVIEW': 236, 'CURRENTLY_SUPPORTED': 15, 'STALE_EVIDENCE_DEPENDENCY': 71, 'HISTORICAL_ONLY': 2}
- Current entities are evaluated before migration context; Yoast → Rank Math does not make current entities historical.

## Blog categories
- Current categories checked: 12
- Empty 200/noindex: 9
- 404: 1
- Non-empty/indexable records are retained in current-blog-category-matrix.json.

## WP-27727
- Supplemental dossier: pages/products/WP-27727.md
- Status: CODEX_AUDITED; final_disposition remains NOT_DECIDED.

## Store matrices
- Variable schema: 60 parents in current-variable-schema-matrix.json.
- Bundle components: 22 parents; mappings obtained for 22.
- Product title/H1 matrix: 84 products, Shop and Product Categories.
- Internal-link graph: 157 entities, 16656 edges, 13668 unresolved destinations.
- Parameter families: filter_volume, orderby, pagination, per_page, per_row, product-page, product_search, shop_view, variation_selection.

## Remaining blockers
- Variant URL stability is PARTIAL and is recorded without transactional testing.
- Accessory/tool representative was not deterministically identified; no claim is made.
- Page+Query remains NOT_AVAILABLE.
