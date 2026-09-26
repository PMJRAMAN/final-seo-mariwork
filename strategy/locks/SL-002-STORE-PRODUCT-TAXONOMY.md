# SL-002 — Store / Product / Taxonomy

**Status:** STRATEGY_LOCKED  
**Locked:** 2026-09-26  
**Baseline repository HEAD:** `486abc31d66910d8b0f7323b25954b79d49134e6`

## Accepted Decision IDs

Primary:
- DEC-003, DEC-006
- DEC-007 through DEC-011
- DEC-015, DEC-016, DEC-020, DEC-021
- DEC-025, DEC-026, DEC-027
- DEC-035, DEC-036, DEC-039
- DEC-056
- DEC-076, DEC-077
- DEC-081, DEC-082, DEC-083, DEC-084, DEC-113
- DEC-115, DEC-116, DEC-117, DEC-130

Dependencies:
- DEC-030, DEC-059–061, DEC-067
- DEC-068, DEC-069, DEC-102–104, DEC-112
- DEC-121–125 where content/value claims are involved

## Exact target state

- Shop remains the broad commercial discovery hub.
- Durable Product Categories remain intentional indexable commercial browse hubs.
- `pa_volume` 30/60/250 pages remain distinct durable cross-family commercial browse pages.
- Product Tags are transitional and are decommissioned under verified mapping rules.
- Product visible identity follows accepted family naming standards.
- Rank Math Product SEO title default target is `%title%`, with justified exceptions only.
- Product metas are factual/page-specific; no blanket excerpt strategy.
- Product content is family-specific and useful, not filler.
- ProductGroup/variant and Bundle schema follow actual Woo/YITH identity.
- Product price/currency/sale/availability come from authoritative Woo state.
- Product identifiers/brand come only from verified source data.
- temporary Out of Stock differs from permanent Discontinued.
- Product URL history is preserved; no cosmetic slug migrations.
- Product Category and pa_volume archives receive concise unique content blocks under DEC-130.
- shipping/returns structured facts must match real business rules.

## Evidence / research gates

- DEC-081 exact identifier/brand field coverage;
- DEC-082 current price/availability ownership and edge cases;
- DEC-113 actual shipping/returns policy;
- exact Product meta/copy and archive copy;
- Product/Category/volume representative QA;
- YITH/Woo component/variant reconciliation where required.

## Exclusions

- Merchant Center / Google Shopping feed remains deferred.
- Review/rating program remains deferred.
- No third-party Product is relabeled Mariwork.

## Dependencies

- SL-000
- SL-001 for canonical/sitemap/redirect/system behavior
