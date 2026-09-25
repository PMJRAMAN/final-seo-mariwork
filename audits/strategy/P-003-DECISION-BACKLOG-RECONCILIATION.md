# P-003 — Authoritative Decision Backlog Reconciliation

**Date:** 2026-09-25  
**Input:** P-001 + P-002  
**Production writes:** 0  
**Result:** authoritative Decision Backlog reconciled; not yet an SEO target-state approval

## Summary

The authoritative backlog was reconciled from 73 to **120 stable Decision IDs**.

- Existing IDs preserved: `DEC-001`–`DEC-073`
- New IDs appended: `DEC-074`–`DEC-120`
- Existing IDs renumbered: **0**
- Existing IDs deleted: **0**
- Decisions reclassified as non-strategy: `DEC-055`, `DEC-058` → `SUPERSEDED`
- Production writes: **0**

## Major reconciliation actions

### Existing broad decisions narrowed

- `DEC-004` → Cart / Checkout transactional utility policy.
- `DEC-016` → Shop metadata strategy.
- `DEC-053` → canonical Mariwork facts/naming registry.
- `DEC-062` → author/date archive public/index policy.
- `DEC-069` → monitoring windows/core metrics.
- `DEC-072` → Merchant Center / Free Listings entry/eligibility.
- `DEC-073` → genuine review/social-proof collection and visible-display policy.

### Reclassified

- `DEC-055` sampling is evidence/QA, not target-state strategy.
- `DEC-058` broad Video policy is superseded by atomic Video decisions; `DEC-038` remains sole VideoObject eligibility/ownership gate.

### Added decision domains

New atomic decisions now explicitly cover:

- auth/account and Fast Buy utility roles;
- Product Category and `pa_volume` metadata;
- URL normalization and canonical architecture;
- JS/AJAX critical-content discoverability;
- Product identifiers/commercial facts/shipping/returns;
- out-of-stock/discontinued and future Product URL lifecycle;
- editorial provenance, FAQ semantics, Stores/NAP, informational CTA;
- Homepage content/CTA;
- Product Category / `pa_volume` presentation;
- Blog Category presentation;
- cannibalization resolution;
- image naming, gallery/reuse, context, discovery and technical delivery;
- atomic Video host/metadata/thumbnail/transcript/lifecycle policies;
- brand content, branded landing roles and off-site evidence;
- release annotation, monitoring interpretation and maintenance triggers;
- Product Feed and Review schema deferred child decisions;
- feed/search/404 system spaces;
- Googlebot/OAI-SearchBot access;
- mobile/CWV/Page Experience;
- concern-by-concern SEO ownership;
- global header/footer/navigation architecture.

## Status counts after reconciliation

- PROPOSED: 29
- NEEDS_TARGETED_EVIDENCE: 22
- OPEN: 61
- SUPERSEDED: 2
- DEFERRED: 6
- ACCEPTED: 0

This is expected. P-003 defines the complete decision queue; it does not make the owner's SEO decisions.

## Authority

The canonical source remains:

`strategy/DECISION-BACKLOG.md`

No Production implementation is unlocked by this reconciliation.
