# Mariwork SEO Strategy Lock Index

**Status:** ACTIVE LOCK SET  
**Lock-set date:** 2026-09-26  
**Common baseline repository HEAD:** `486abc31d66910d8b0f7323b25954b79d49134e6`

## Purpose

These locks are the formal bridge from accepted strategy decisions to execution planning.

They do not authorize Production writes by themselves.

## Locks

1. `SL-000-GOVERNANCE-MEASUREMENT.md` — rollout, measurement, change isolation, ownership
2. `SL-001-TECHNICAL-SYSTEM-URLS.md` — canonical/indexability/system URLs/crawlers/CWV
3. `SL-002-STORE-PRODUCT-TAXONOMY.md` — Shop, Products, Categories, pa_volume, Product schema/content
4. `SL-003-EDITORIAL-ACADEMY-BRAND-CONTENT.md` — Homepage, Static, Magazine, Academy, brand/content strategy
5. `SL-004-INTERNAL-LINKS-NAVIGATION-HUBS.md` — internal-link classes, hierarchy, navigation, hub relationships
6. `SL-005-VISUAL-VIDEO-PERFORMANCE-AI.md` — image/video/performance/AI-answer discoverability
7. `SL-006-LEGACY-MIGRATION.md` — historical URL mapping, redirects, 404/410, migration evidence

## Deferred programs excluded from current lock set

- DEC-071 External PR / advertorial
- DEC-072 Merchant Center / Free Listings
- DEC-073 Reviews/social proof
- DEC-101 off-site entity/PR evidence program
- DEC-105 Google Merchant Product Feed
- DEC-106 review/rating structured-data program

## Next gate

P-006 must reconcile `tasks/EXECUTION-BACKLOG.md` against these locks and the accepted decisions.

P-007 must confirm that only packages with:
- accepted blocking decisions;
- exact scope;
- required evidence/input;
- technical owner;
- canary/rollback/regression;
- approved copy where applicable

can become `READY_FOR_TASK`.

No Production task may bypass these gates.
