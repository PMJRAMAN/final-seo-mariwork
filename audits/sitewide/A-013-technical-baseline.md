# A-013 — Sitewide Technical SEO Baseline

**Task:** A-013 · **Program:** FOUNDATION / STORE-FIRST  
**Framework/schema:** v1.0 (frozen)  
**Audit date:** 2026-09-24  
**Lifecycle:** `CODEX_AUDITED`  
**Authority:** Round-1 evidence and initial recommendations only. No Second Review, approval, final disposition, implementation, or Production change.

## Scope and evidence contract

This baseline reuses the deterministic Round-1 evidence. It does not recrawl, refetch, join separate GSC exports, or treat live content as instructions. Primary inputs:

- `data/normalized/round1-foundation-context.json` — 555 inventory rows, 388 policy/system rows, 167 model-page candidates.
- `data/normalized/round1-evidence-summary.json` — 501 deterministic evidence entities: 440 HTTP 200, 58 HTTP 404, 3 `SKIPPED_SAFETY`; issue summary: 289 missing meta descriptions, 271 missing H1s, 2 canonical differences; no parsed schema types.
- `data/normalized/round1-page-evidence.jsonl` — targeted representative page/tag/product examples only.
- `audits/sitewide/A-010-inventory-notes.md`, `A-011-content-types-taxonomies.md`, and `A-012-legacy-url-map.md` — targeted excerpts and existing evidence, not reinterpreted as final decisions.

GSC source is page-dimension history only. **Page-query relationship is not proven by the current export.** Historical clicks/impressions remain attached to their exact source URLs and are not transferred to redirects or current targets.

## Executive baseline

The site has a publicly observed HTTPS sitemap index with six child sitemaps and 147 sitemap entries representing 146 unique URLs. The index and public sitemap output are attributed to Rank Math, but the installed version, modules, settings, hooks, and complete owner pipeline are inaccessible. The product sitemap contains 83 product URLs plus `/shop/`; `/shop/` also occurs in the page sitemap.

The deterministic page evidence shows a mixed architecture: indexable 200 pages, many 200 `follow, noindex` archive/system candidates, and 404 historical/taxonomy URLs. The inventory contains 275 `product_tag` rows, 53 `post_tag` rows, three product-attribute rows, one sampled facet space, pagination/sort/search/feed/action spaces, and 25 policy/system rows. This is a crawl/index policy problem space, not evidence that every row should be indexed or removed.

The explicit Product Tag and Blog Tag decommission direction is therefore recorded as a **family candidate requiring migration evidence**, not as an approved deletion/noindex/redirect list. No production change is authorized by this report.

## Coverage matrix

| Area | Round-1 result | Confidence / limitation |
|---|---|---|
| robots.txt / crawl controls | A-010 collected public robots and retained route rules; this baseline has no Googlebot/OAI-SearchBot access-log validation. | Observed for collected output; crawler equivalence unknown. `robots.txt` is not treated as noindex. |
| HTTP, redirects, errors | 501 deterministic entities: 440×200, 58×404, 3 skipped for safety. A-012 observed 144 redirecting source URLs; 143 one-hop and one two-hop; two chains terminated at 404. | High for recorded samples/source set; not an exhaustive server log census. |
| sitemaps | Sitemap index plus six child maps observed HTTP 200; 147 entries / 146 unique URLs. Product sitemap 83 products + shop; shop duplicated across page/product maps. | High for fetched maps; sitemap membership does not prove indexing. |
| canonical / duplicate spaces | Product examples self-canonical with percent-encoding differences; sampled facet and sort URLs declared `/shop/` or category canonical. 2 canonical differences in normalized summary. | Observed declared canonicals only; Google-selected canonical and complete duplicate graph unavailable. |
| facets / parameters | Sample: `filter_volume=250ml&query_type_volume=or` → 200 and canonical `/shop/`; sort/per-page examples retained; combinations were not expanded. | Bounded evidence; no blanket facet policy. |
| internal links | Initial HTML link extraction exists; internal link count ranges from 0 to 162 in targeted JSONL, with 3 zero-link records. No rendered-JS link graph or complete orphan analysis. | Measured initial HTML only; orphan/depth conclusions blocked. |
| JS/AJAX | No rendered crawl or interaction/form submission was performed. | `BLOCKED_BY_ACCESS` / `UNKNOWN_NEEDS_VERIFICATION`; critical-content discoverability not proven. |
| structured data | Normalized summary reports no parsed schema types. Targeted evidence examples also report empty schema arrays. | Observed parser output, but generator/HTML coverage and duplicate ownership need targeted recheck. |
| Woo architecture | 83 public products; variation/bundle parent-child census, unpublished objects, price hooks, and complete attribute architecture blocked. | Public evidence only; DB/WP/Woo access unavailable. |
| images/media | Targeted evidence records 249 missing-alt instances and 1,279 lazy-image instances across the JSONL set; A-010 retained media/attachment spaces without downloading raw bodies. | Measured extraction; not a performance or visual-quality verdict. |
| performance/mobile | No PageSpeed/Lighthouse, field CWV, mobile usability, viewport, or lab/field split is available in the normalized evidence. | `NOT_AVAILABLE`. |
| crawler/security access | No bot access-log/WAF/CDN-equivalence evidence. HTTPS is the observed scheme for collected URLs. | Server security audit out of scope; crawler-specific access remains unknown. |
| Rank Math ownership | Public sitemap marker attributes output to Rank Math. Installed version, Free/Pro, Advanced mode, active modules, settings and hooks are blocked. | `BLOCKED_BY_ACCESS`; A-014/A-015 owners. |

## Sitewide findings

Findings are also registered in `registry/SYSTEMIC-FINDINGS.md`. All recommendations below are `INITIAL` and require Second Review and human approval.

### SYS-001 — Rank Math configuration and SEO ownership cannot be verified

```yaml
id: SYS-001
severity: P1
scope: SITEWIDE
status: BLOCKED
evidence_class: OBSERVED
confidence: HIGH
source_refs:
  - data/normalized/round1-foundation-context.json
  - audits/sitewide/A-010-inventory-notes.md:140-147
  - public sitemap generator marker recorded by A-010
impact: Current owner and configuration for robots, canonical, title/meta, schema, sitemap, redirects, and taxonomy controls cannot be confirmed; duplicate-owner risk cannot be closed.
recommendation: INITIAL — A-014/A-015 should inspect the installed Rank Math version, mode, active modules, per-type settings, hooks, theme/custom-plugin SEO output, and redirect/404 configuration. Where capability is verified, target owner is Rank Math; do not introduce parallel custom output.
acceptance_criteria: Version/modules/settings/current output owners are evidenced; one owner is recorded per concern; conflicts are enumerated; approved changes have rollback and a regression set.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH where installed capability is verified; otherwise UNKNOWN_NEEDS_VERIFICATION
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Installed configuration and code paths are inaccessible; no alternative owner selected.
```

### SYS-002 — Product Tag and Blog Tag archives are decommission candidates with unresolved migration risk

```yaml
id: SYS-002
severity: P1
scope: FAMILY
family: product_tag + post_tag
status: CONFIRMED
evidence_class: OBSERVED
confidence: HIGH
source_refs:
  - data/normalized/round1-foundation-context.json: family_counts
  - data/normalized/round1-page-evidence.jsonl: representative TERM-product_tag and TERM-post_tag records
  - audits/sitewide/A-010-inventory-notes.md:140-147
  - audits/sitewide/A-012-legacy-url-map.md: redirect/404 evidence
impact: Product tags occupy 275 inventory rows and sampled live 200 pages expose follow/noindex, no canonical, empty H1, and no product result text; sampled blog-tag URLs are 404. Historical value, internal-link sources, destination identity, and complete family behavior are not yet reconciled.
recommendation: INITIAL — treat both spaces as explicit decommission candidates. Before any noindex, redirect, removal, or taxonomy change, inventory exact live/legacy URLs, GSC source metrics, inbound links, current term assignments, semantic replacements, sitemap membership, and owner settings. Preserve source metrics and do not bulk redirect unrelated tags to home/shop.
acceptance_criteria: A family migration dossier has a complete URL/term set, status/canonical/robots/link evidence, historical-value review without Page+Query inference, destination mapping or explicit no-replacement decisions, rollback, canary/regression set, and Second Review approval.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/crawling/docs/faceted-navigation
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH for approved robots/canonical/sitemap controls; CONTENT/PLATFORM only where separately justified
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Taxonomy settings and installed capability not accessible; no production policy proposed.
```

The evidence does **not** establish that all 275 product tags share identical behavior or that all 53 post-tag rows should receive one outcome. Counts and representative pages are evidence for investigation, not a final decommission list.

### SYS-003 — Historical/error URL population requires source-level disposition

```yaml
id: SYS-003
severity: P2
scope: SITEWIDE
status: CONFIRMED
evidence_class: MEASURED
confidence: HIGH
source_refs:
  - data/normalized/round1-evidence-summary.json
  - audits/sitewide/A-012-legacy-url-map.md: initial findings and Appendix A
  - audits/sitewide/A-010-inventory-notes.md: redirect/error baseline
impact: 58 of 501 deterministic evidence entities returned 404; 67 GSC source URLs in A-012 ended at 404, and two recorded chains terminated at numeric-ID 404 destinations. Historical identity and appropriate replacements remain unproven.
recommendation: INITIAL — reconcile the highest-value exact source URLs with historical object identity and current intent before restoration, direct redirect, removal, or leave-as-404 decisions. Keep unrelated sources separate; do not infer replacement from slug similarity or transfer metrics.
acceptance_criteria: Every selected source has an evidence-backed disposition or explicit blocker; redirect destinations are direct, relevant, live and canonical-consistent; source metrics remain traceable; regression covers all approved mappings and 404 controls.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/crawling-indexing/301-redirects
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH if the approved redirect concern is supported; otherwise PLATFORM/server owner for HTTP behavior
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Redirect table/server ownership unavailable; A-014/A-015 and migration review required.
```

### SYS-004 — Initial-HTML SEO output has broad metadata/H1/schema evidence gaps

```yaml
id: SYS-004
severity: P1
scope: SITEWIDE
status: CONFIRMED
evidence_class: MEASURED
confidence: MEDIUM
source_refs:
  - data/normalized/round1-evidence-summary.json
  - data/normalized/round1-page-evidence.jsonl
impact: The deterministic set reports 289 missing meta descriptions, 271 missing H1s, and no parsed schema types. This can reduce clarity of page/entity output, but no ranking or rich-result causation is claimed; parser/owner coverage requires validation.
recommendation: INITIAL — segment by canonical page family and verify initial HTML plus rendered output. Audit Rank Math/theme/plugin generators for one owner per title/meta/H1-adjacent and schema concern; prioritize indexable products, shop/category, articles, academy and organization/entity templates.
acceptance_criteria: A representative regression set has measured title/meta/H1/schema output by family; visible content and structured data agree; duplicate/empty output is attributed to a verified owner; approved changes use Rank Math where capable and include before/after evidence.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH where capability supports metadata/schema; CONTENT for visible H1/content; otherwise UNKNOWN_NEEDS_VERIFICATION
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Installed modules and template ownership unavailable; no implementation proposed.
```

### SYS-005 — Facet, sort, pagination, and parameter URL policy is incomplete

```yaml
id: SYS-005
severity: P2
scope: SITEWIDE
status: BLOCKED
evidence_class: OBSERVED
confidence: HIGH
source_refs:
  - data/normalized/round1-foundation-context.json: representative_samples and family_counts
  - audits/sitewide/A-010-inventory-notes.md: machine-space coverage
  - audits/sitewide/A-012-legacy-url-map.md: canonical-only shop parameters
impact: Filter, sort/display, pagination, search, and transaction/action spaces create multiple URL forms. A sampled volume filter returned 200 and canonicalized to `/shop/`; combinations were not exhaustively tested, so crawl demand, indexability, and internal-link generation are not fully known.
recommendation: INITIAL — classify each parameter family by user value, crawlable-link generation, canonical/robots behavior, sitemap exclusion, and duplicate/content difference. Do not apply a blanket robots/noindex/canonical rule before architecture and Rank Math ownership are verified.
acceptance_criteria: A parameter policy covers observed and generated patterns, representative combinations, pagination, sort controls, canonical target status, internal links, and regression examples; no action or transaction URL is tested through a real checkout/order flow.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/crawling/docs/faceted-navigation
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH for supported canonical/robots/sitemap controls; PLATFORM for server crawl controls where required
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Settings unavailable; policy remains an investigation recommendation.
```

## Initial investigation order

1. A-014/A-015: verify Rank Math capability, current owners, and duplicate output before proposing SEO-control changes.
2. Resolve SYS-002 with a complete tag-family migration evidence set, keeping Product Tag and Blog Tag policies separate from one another and from product/category archives.
3. Reconcile SYS-003 historical 404/redirect sources, prioritizing exact GSC source evidence without Page+Query attribution.
4. Segment SYS-004 by canonical page family and validate schema/visible-output consistency.
5. Map SYS-005 generated parameter spaces and internal-link generation; then obtain targeted rendered-JS evidence.
6. Obtain performance/mobile and crawler-access evidence: field CWV where available, representative lab measurements, mobile output/usability, WAF/CDN/bot logs, and OAI-SearchBot separately from GPTBot. These are not available in Round-1 and must not be inferred.

## Safety and handoff

- Production remained read-only; no HTTP recrawl, DB/WP/Woo write, cache purge, redirect, taxonomy, sitemap, robots, schema, content, or configuration change was made.
- No PII, order data, credentials, cookies, tokens, keys, or secrets were read or written.
- `registry/URL-INVENTORY.csv` was not changed because no new entity or verified disposition was established.
- This report and the systemic registry entries are initial Codex evidence only. They do not confer `SECOND_REVIEWED`, `APPROVED`, `IMPLEMENTING`, `CODEX_QA_PASSED`, or final QA status.
