# A-015 — Duplicate SEO Owners / Output Audit

**Task:** A-015 · **Program:** FOUNDATION / STORE-FIRST · **Framework/schema:** v1.0 (frozen)  
**Audit date:** 2026-09-24 · **Lifecycle:** `CODEX_AUDITED`  
**Authority:** Round-1 evidence and initial recommendations only. No Second Review, approval, implementation, or Production change.

## Scope and evidence contract

This is the paired synthesis with A-014, using normalized Round-1 evidence and targeted A-010/A-013 excerpts. It does not recrawl, refetch, join separate GSC exports, inspect Production configuration, or edit raw data.

The deterministic summary reports 501 entities, 289 missing meta descriptions, 271 missing H1s, 286 `noindex` observations, 2 canonical differences, and no parsed schema types. These are output observations, not proof of a particular generator or duplicate owner. Public sitemap output is attributed to Rank Math, but its internal configuration and competing code paths are unavailable. `/shop/` is present in both page and product sitemaps; this is a measurable duplicate sitemap membership, not proof of duplicate sitemap generators.

## Concern-by-concern determination

| Output / control | Duplicate owner result | Evidence status | Required next evidence |
|---|---|---|---|
| Title / meta | Not proven; ownership unknown | `UNKNOWN_NEEDS_VERIFICATION` | Initial and rendered head; Rank Math fields/settings; theme/plugin filters and emitted tags |
| Canonical | Not proven; duplicate or conflicting emitters unknown | `UNKNOWN_NEEDS_VERIFICATION` | Complete head capture on representative families; source attribution for every canonical tag; Rank Math and platform hooks |
| Robots / noindex | Not proven; 286 noindex outputs are not owner attribution | `UNKNOWN_NEEDS_VERIFICATION` | Representative HTML plus response headers; per-type Rank Math settings; theme/plugin/platform emitters |
| Schema | Duplicate output not proven; parser found no schema types | `UNKNOWN_NEEDS_VERIFICATION` | Raw initial/rendered JSON-LD/microdata capture; schema generator inventory; visible-data consistency |
| Sitemap | Duplicate generator not proven; `/shop/` appears in two observed sitemap files | `OBSERVED` for membership only | Sitemap settings/module state, filters, generation logs/config, and whether the two memberships are intentional |
| Redirects | Not assessable; redirect table/server owner inaccessible | `BLOCKED_BY_ACCESS` | Rank Math redirection module state, server/CDN rules, web-app redirects, and exact chain samples |

No Page+Query attribution is used. **Page-query relationship is not proven by the current export.**

## Finding

### A-015-F001 — Duplicate SEO owner/output risk remains unclosed

```yaml
id: A-015-F001
severity: P1
scope: SITEWIDE
status: BLOCKED
evidence_class: INFERRED
confidence: MEDIUM
source_refs:
  - data/normalized/round1-foundation-context.json
  - data/normalized/round1-evidence-summary.json
  - audits/sitewide/A-010-inventory-notes.md:34,140-147
  - audits/sitewide/A-013-technical-baseline.md:34,39,44,50-70
impact: Without source attribution, future edits could create or preserve parallel title/meta, canonical, robots, schema, sitemap, or redirect output; current duplication cannot be confirmed or ruled out.
recommendation: INITIAL — create a concern-by-concern ownership matrix from accessible configuration and representative public output. Keep Rank Math as target owner wherever its verified capability supports the concern; remove or disable no competing output only after an approved change dossier, canary, rollback, and regression set.
acceptance_criteria: For each concern, one current owner, one target owner, emitted location, Rank Math capability/module path, conflict status, and representative before/after tests are recorded; sitemap membership and redirect chains are separately validated; no duplicate output remains in the approved regression set.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH where capability is verified; PLATFORM for server-only redirect behavior; otherwise UNKNOWN_NEEDS_VERIFICATION
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Installed modules, settings, hooks, theme/custom-plugin code, redirect table, and server configuration are hidden by isolated runtime; no broader Production access requested.
```

## Initial recommendations and limits

1. Preserve the public sitemap attribution as evidence, not as proof of exclusive Rank Math ownership.
2. Do not add a custom SEO snippet, second schema emitter, alternate canonical/robots emitter, sitemap generator, or redirect layer while ownership is unresolved.
3. Validate representative indexable products, shop/category, article, academy, homepage/entity, taxonomy, parameter, and redirect cases before any approved change.
4. Missing schema output and missing meta/H1 output require source-level diagnosis; they do not justify claiming a duplicate or a ranking/rich-result effect.

The result remains `CODEX_AUDITED`; it is not `SECOND_REVIEWED`, `APPROVED`, `IMPLEMENTING`, or a Production change.

