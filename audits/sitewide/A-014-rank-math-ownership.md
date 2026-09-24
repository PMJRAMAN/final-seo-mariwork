# A-014 — Rank Math Configuration & Ownership Audit

**Task:** A-014 · **Program:** FOUNDATION / STORE-FIRST · **Framework/schema:** v1.0 (frozen)  
**Audit date:** 2026-09-24 · **Lifecycle:** `CODEX_AUDITED`  
**Authority:** Round-1 evidence and initial recommendations only. No Second Review, approval, implementation, or Production change.

## Scope and evidence

This audit uses the compact Round-1 inputs and targeted existing notes only. No recrawl, refetch, database/WP command, configuration write, or raw-export edit was performed.

- `data/normalized/round1-foundation-context.json`: 555 inventory rows; 388 policy/system rows; 167 model-page candidates; six observed child sitemaps with 147 entries / 146 unique URLs.
- `data/normalized/round1-evidence-summary.json`: 501 deterministic entities; 440 HTTP 200, 58 HTTP 404, 3 `SKIPPED_SAFETY`; 289 missing meta descriptions; 271 missing H1s; 286 `noindex`; 2 canonical differences; no parsed schema types.
- `audits/sitewide/A-010-inventory-notes.md:140-147`: access and ownership blockers; public sitemap generator attribution.
- `audits/sitewide/A-013-technical-baseline.md:22,34,39,44,50-70`: baseline and existing systemic finding.
- `docs/SEO-OWNERSHIP.md`, `docs/DECISIONS.md` SEO-013/SEO-014, and `MASTER-TODO.md` A-014/A-015.

## Result

The public sitemap index/output contains a generator marker attributing sitemap output to Rank Math. This is evidence of public output attribution only; it does **not** verify the installed Rank Math version, Free/Pro status, mode, active modules, per-type settings, hooks, custom filters, or exclusive ownership of any other SEO output.

The isolated runtime could not verify the Production path or access WP/database/configuration. Therefore capability and current ownership for title, meta description, robots, canonical, schema, sitemap, taxonomy SEO, and redirects remain `BLOCKED_BY_ACCESS` / `UNKNOWN_NEEDS_VERIFICATION`. No substitute owner is inferred from public HTML, and no duplicate owner is asserted from missing or empty parsed output.

| Concern | Public evidence | Current owner | Capability check | Initial target owner |
|---|---|---|---|---|
| Title/meta | Titles were not missing in the normalized summary; 289 meta descriptions were missing | `UNKNOWN_NEEDS_VERIFICATION` | `BLOCKED_BY_ACCESS` | `RANK_MATH` if installed capability is verified |
| Robots/noindex | 286 entities expose `noindex` in deterministic evidence | `UNKNOWN_NEEDS_VERIFICATION` | `BLOCKED_BY_ACCESS` | `RANK_MATH` if capability/settings are verified |
| Canonical | 2 canonical differences; sampled parameter canonicals exist | `UNKNOWN_NEEDS_VERIFICATION` | `BLOCKED_BY_ACCESS` | `RANK_MATH` if capability is verified; otherwise documented platform owner |
| Schema | No parsed schema types in normalized summary | `UNKNOWN_NEEDS_VERIFICATION` | `BLOCKED_BY_ACCESS` | `RANK_MATH` where supported; otherwise one documented central integration |
| Sitemap | Six public child maps, 147 entries / 146 unique; generator marker says Rank Math; `/shop/` appears in page and product maps | `RANK_MATH` for public marker only; exclusive pipeline `UNKNOWN_NEEDS_VERIFICATION` | `BLOCKED_BY_ACCESS` | `RANK_MATH` if settings/module ownership is verified |
| Redirects / 404 | A-012 records redirect evidence; redirect table/server config inaccessible | `UNKNOWN_NEEDS_VERIFICATION` | `BLOCKED_BY_ACCESS` | `RANK_MATH` only if the installed redirect module is verified and suitable; otherwise `PLATFORM` |

## Finding

### A-014-F001 — Rank Math capability and exclusive SEO ownership are not verifiable

```yaml
id: A-014-F001
severity: P1
scope: SITEWIDE
status: BLOCKED
evidence_class: OBSERVED
confidence: HIGH
source_refs:
  - data/normalized/round1-foundation-context.json
  - data/normalized/round1-evidence-summary.json
  - audits/sitewide/A-010-inventory-notes.md:140-147
  - audits/sitewide/A-013-technical-baseline.md:44,50-70
impact: The project cannot identify the verified current owner, active capability, settings, or duplicate-output boundary for core SEO concerns.
recommendation: INITIAL — when authorized and accessible, record the installed Rank Math version/mode/modules, relevant settings and hooks, and inspect theme/custom-plugin/platform output. Use Rank Math for every supported concern; use one documented central extension or platform owner only where Rank Math is insufficient.
acceptance_criteria: Version/modules/settings and current owner are evidenced for each concern; one owner is recorded; conflicts and output locations are enumerated; any later approved change has rollback and a family/sitewide regression set.
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH where capability is verified; otherwise UNKNOWN_NEEDS_VERIFICATION or PLATFORM for server redirect behavior
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Production filesystem/WP/database/configuration and internal hooks are inaccessible in the isolated runtime; no broader access requested and no SEO setting change proposed.
```

## Handoff

This result updates/refines existing `SYS-001`; it does not close it. The sitemap marker is not evidence that Rank Math exclusively owns canonical, robots, schema, metadata, or redirects. This report does not grant `SECOND_REVIEWED`, `APPROVED`, `IMPLEMENTING`, or any Production authority.

