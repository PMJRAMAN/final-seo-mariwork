---
framework_version: "1.0"
dossier_schema_version: "1.0"
entity_id: "TERM-product_cat-1991"
wp_id: "NOT_APPLICABLE"
type: "taxonomy"
family: "product_cat"
current_url: "https://www.mariwork.ir/product/fabric-color-set/fabric-color-set-30-ml/"
canonical_url: "https://www.mariwork.ir/product/fabric-color-set/fabric-color-set-30-ml/"
workflow_status: CODEX_AUDITED
final_disposition: NOT_DECIDED
blocked: false
blockers: []
---

# Page Dossier — TERM-product_cat-1991

## 0. State

- Workflow status: CODEX_AUDITED
- Final disposition: NOT_DECIDED

## 1. Identity

- Entity: TERM-product_cat-1991; WP ID: NOT_APPLICABLE; type/family: taxonomy/product_cat
- Current URL: https://www.mariwork.ir/product/fabric-color-set/fabric-color-set-30-ml/
- Canonical: https://www.mariwork.ir/product/fabric-color-set/fabric-color-set-30-ml/ (self-referential)
- Intended indexability: UNKNOWN_NEEDS_VERIFICATION; actual signals: 200, `index, follow`; sitemap: NOT_PRESENT_IN_OBSERVED_SITEMAPS

## 2. URL History

Round-1 evidence only; no legacy URL supplied.

## 3. Baseline

Search Console metrics: NOT_AVAILABLE in supplied evidence. Page+Query: NO — Page-query relationship is not proven by the current export. Coverage: NOT_AVAILABLE; sitemap: NOT_PRESENT_IN_OBSERVED_SITEMAPS.

## 4. Current Page Snapshot

- HTTP 200, no redirect, X-Robots empty, `index, follow`, self-canonical. Title: `ست‌های ۳۰ میل - رنگ پارچه ماری ورک`; H1: `ست‌های ۳۰ میل`; meta description supplied and includes an extended FAQ block. OG: NOT_AVAILABLE.
- Initial HTML exposes 11 bundle products and prices; 13 images/0 missing ALT/11 lazy; 133 internal links. Schema extraction: `[]`.

## 5. Search / Content Research

- Primary intent: transactional bundle/category browsing (INFERRED from taxonomy and listing); exact query ownership: UNKNOWN_NEEDS_VERIFICATION.
- The supplied meta description contains multiple FAQ answers; whether this is useful snippet text or duplicated visible content needs independent review. No final metadata is drafted.

## 6. Codex Audit

- Mode: READ-ONLY

### Findings

#### TERM-product_cat-1991-F001 — Meta description contains extended FAQ text

```yaml
severity: P2
scope: PAGE
status: CONFIRMED
evidence_class: OBSERVED
confidence: HIGH
source_refs: ["INPUT:evidence.meta_description"]
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/appearance/snippet
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH where capability is verified
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Current Rank Math configuration unavailable.
```
**Evidence:** Supplied meta description includes the category description followed by three FAQ questions and answers.
**Impact:** The description may be less focused as a search snippet; Google may generate a different snippet. No CTR/ranking causation is claimed.
**Recommendation:** INITIAL — review the intended snippet message and visible/metadata consistency; if changed, use Rank Math after capability and ownership verification.
**Acceptance criteria:** Approved description is concise, accurate, non-duplicative, and its owner is recorded.

#### TERM-product_cat-1991-F002 — Batch-level structured data and sitemap verification gaps

```yaml
severity: P1
scope: FAMILY
status: BLOCKED
evidence_class: MEASURED
confidence: HIGH
source_refs: ["INPUT:evidence.schema_types", "INPUT:inventory.sitemap", "SYS-001", "SYS-004"]
google_basis: GOOGLE_CONSISTENT
google_reference: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
seo_owner_current: UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: RANK_MATH where capability is verified
rank_math_capability_checked: BLOCKED_BY_ACCESS
rank_math_path_or_reason_not_used: Installed modules/settings unavailable.
```
**Evidence:** `schema_types: []`; sitemap is not present in observed sitemaps; page is 200/index-follow.
**Impact:** Family policy and structured-data ownership cannot be concluded.
**Recommendation:** INITIAL — resolve via family-level validation and Rank Math capability audit; do not add competing schema or alter sitemap in Round 1.
**Acceptance criteria:** Family regression set verifies rendered schema, taxonomy policy, canonical and sitemap state.

## 7. ChatGPT Independent Second Review

Pending.

## 8. Final Approved Findings

Pending.

## 9. Target State

NOT APPROVED in Round 1.

## 10. Implementation Plan

Not authorized.

## 11. Implementation Result

Not started.

## 12. Codex QA

Not started.

## 13. ChatGPT Final Acceptance QA

Not started.

## 14. Monitoring

Not started.

## 15. Change Log

Pending.

## 16. SEO Basis / Ownership Record

Round-1 only. Rank Math capability/current owner: BLOCKED_BY_ACCESS; see SYS-001. No Production change authorized.
