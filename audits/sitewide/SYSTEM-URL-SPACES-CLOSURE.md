# System / Archive URL-Space Closure

**Date:** 2026-09-25
**Lifecycle:** `CODEX_AUDITED`
**Mode:** Production read-only
**Production writes:** `0`

This is a family-level policy artifact. It prevents meaningless one-file dossiers for machine-generated or transactional URL spaces. It does not approve any URL disposition or implementation.

## Evidence basis

- `registry/URL-INVENTORY.csv` — 25 URL-space rows covering 15 policy spaces.
- `audits/sitewide/A-010-inventory-notes.md` — bounded public crawl, redirect, sitemap and system-space evidence.
- `audits/sitewide/A-012-legacy-url-map.md` — current/legacy transport evidence.
- `audits/second-review/reconciliation/current-entity-census.json` — current public census and non-public classification.
- `audits/second-review/evidence/seo-ownership-matrix.json` — Rank Math Free `1.0.279` and active module evidence.
- Public read-only HTTP checks on 2026-09-25 for the three WooCommerce page entities.

## Policy matrix

| Space | Current evidence | Audit classification | Second Review need | Safety boundary |
|---|---|---|---|---|
| Cart `/cart/` | 200; `noindex, follow`; H1 `سبد خرید`; no canonical observed | `SYSTEM_POLICY_ONLY` | Confirm utility/noindex policy | No cart mutation or order test |
| Checkout `/checkout/` | 302 → `/cart/` in empty public state; final cart is 200/noindex | `SYSTEM_POLICY_ONLY` | Confirm transport and state policy | No checkout submission |
| My Account `/my-account/` | 200; `noindex, follow`; no canonical/H1 observed | `SYSTEM_POLICY_ONLY` | Confirm privacy/system policy | No login/account test |
| Login/auth return endpoints | Return/action patterns recorded in A-010; no authentication executed | `SYSTEM_POLICY_ONLY` | Confirm crawl exposure and parameter policy | No credentials/session handling |
| Internal search | Search form/parameter family recorded; no fabricated result URL | `SYSTEM_POLICY_ONLY` | Confirm noindex/canonical policy | No search action required |
| Author archives | No concrete current route proved; explicit unknown row retained | `BLOCKED_NEEDS_DECISION` | Verify route and policy if public | No invented URL |
| Date archives | No concrete current route proved; explicit unknown row retained | `BLOCKED_NEEDS_DECISION` | Verify route and policy if public | No invented URL |
| Feeds | Five feed policy rows recorded; not editorial landing pages | `SYSTEM_POLICY_ONLY` | Confirm exposure policy | No content rewrite |
| Attachments/media | 626 returned attachment IDs; 845 advertised; 219 difference unknown | `NEEDS_TARGETED_REFRESH` | Resolve sample and policy gaps | No media download/write |
| Pagination | `/shop/page/N/` and legacy `product-page` patterns sampled | `SYSTEM_POLICY_ONLY` | Confirm canonical/indexability rule | No blanket robots rule |
| Facets/sort/display | Nine Store parameter families evidenced in SR-003 | `CURRENT_EVIDENCE_COMPLETE` | Review target policy | No parameter bulk action |
| 404/soft-404 | Aggregate Coverage exists; URL-specific Coverage/Inspection unavailable | `NEEDS_TARGETED_REFRESH` | Review representative 404/soft-404 set | No redirect/410 write |
| Unexposed CPT/editor spaces | Registered but not public SEO targets; covered in A-011 | `NON_PUBLIC` | Only revisit if public exposure changes | No private data enumeration |

## Current WooCommerce page dossiers

- [WP-10](/home/mariwork/Final-SEO-Codex/pages/static/WP-10.md): checkout role; 302 to cart observed.
- [WP-11](/home/mariwork/Final-SEO-Codex/pages/static/WP-11.md): account role; 200/noindex observed.
- [WP-30919](/home/mariwork/Final-SEO-Codex/pages/static/WP-30919.md): cart role; 200/noindex observed.

## Findings

### SYS-013 — Transactional system pages require policy treatment, not editorial optimization

```yaml
id: SYS-013
severity: P2
scope: FAMILY
status: OPEN
evidence_class: OBSERVED
confidence: HIGH
source_refs:
  - pages/static/WP-10.md
  - pages/static/WP-11.md
  - pages/static/WP-30919.md
  - audits/sitewide/SYSTEM-URL-SPACES-CLOSURE.md
impact: "Cart, checkout and account endpoints are public utility pages with noindex/redirect behavior; treating them as normal SEO landing pages could create privacy, state or commerce regressions."
recommendation: "Keep them in a system-policy queue; obtain human Second Review of intended crawl/index behavior before any owner or output change."
acceptance_criteria: "Each endpoint has a recorded role, current HTTP/robots/canonical observation, owner boundary, non-mutating regression scope and explicit no-content-optimization disposition."
google_basis: GOOGLE_RECOMMENDED
google_reference: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
seo_owner_current: RANK_MATH for observed robots/title output; WORDPRESS/WooCommerce or PLATFORM for transport/state
seo_owner_target: RANK_MATH for supported metadata; WORDPRESS/WooCommerce or PLATFORM for system transport
rank_math_capability_checked: VERIFIED_INSTALLED_1.0.279; exact per-page setting path not read
rank_math_path_or_reason_not_used: No implementation or configuration write is authorized in this task.
```

### SYS-014 — URL-space evidence is bounded and must not be promoted to exhaustive crawl coverage

```yaml
id: SYS-014
severity: P2
scope: SITEWIDE
status: CONFIRMED
evidence_class: OBSERVED
confidence: HIGH
source_refs:
  - audits/sitewide/A-010-inventory-notes.md
  - registry/URL-INVENTORY.csv
  - audits/second-review/store/current-parameter-policy-evidence.json
impact: "Parameterized, attachment, feed, archive and authenticated spaces are bounded samples; absence of a discovered URL is not proof of absence or indexability."
recommendation: "Use family policy plus targeted representatives; do not invent URLs or apply bulk dispositions from samples alone."
acceptance_criteria: "Each machine space has a policy owner, sample evidence, explicit unknowns and a targeted next check where needed."
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/crawling/docs/faceted-navigation
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION by space
seo_owner_target: RANK_MATH for supported robots/canonical/sitemap controls; PLATFORM where server controls are required
rank_math_capability_checked: VERIFIED_INSTALLED_1.0.279; per-space capability/settings not fully read
rank_math_path_or_reason_not_used: No output change proposed; target owner remains conditional on Second Review and approval.
```

## Boundary

No redirect, canonical, robots, sitemap, taxonomy, content, cache, session, order or WooCommerce configuration was changed. These policy rows are ready for ChatGPT Second Review, not approval.
