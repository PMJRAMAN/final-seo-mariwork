# P-002 — ChatGPT Independent Review of Decision Backlog Coverage Audit

**Date:** 2026-09-25  
**Review type:** Independent governance/strategy coverage review  
**Input baseline:** `5bd0d8561cac330128351a6d8669c3f6642843cf`  
**Reviewed:** P-001 coverage audit, candidate changes, dependency graph, current Decision Backlog and Execution Backlog  
**Production writes:** 0  
**Decision authority:** ChatGPT review only; target-state decisions remain owner approval items

## 1. Executive verdict

P-001 is materially correct:

**Decision Backlog is NOT READY FOR FREEZE.**

However, P-001's proposed changes need reconciliation before they become authoritative.

ChatGPT review outcome:

- Most missing-decision candidates are confirmed in principle.
- Several candidate titles are too broad and should be split before authoritative IDs are created.
- A few concerns should remain evidence/QA rather than Strategy Decisions.
- Existing broad DEC IDs should be preserved for traceability, but may be narrowed, reworded or marked SUPERSEDED instead of renumbered.
- Three additional material governance gaps should be added beyond P-001's 27 ADD candidates:
  1. search-crawler access policy (Googlebot/OAI-SearchBot and distinction from training crawlers);
  2. mobile/CWV/page-experience remediation policy;
  3. concern-by-concern SEO technical-owner target matrix / ownership-change policy.

P-003 should now reconcile the authoritative backlog.

---

## 2. Candidate-by-candidate review

### Confirm as authoritative new decision topics

The following P-001 candidates are **CONFIRMED**, subject only to final wording:

- CAND-001 — preferred host/protocol/trailing-slash/future URL normalization.
- CAND-002 — sitewide canonical and duplicate-URL architecture.
- CAND-003 — critical JS/AJAX content/link discoverability.
- CAND-004 — Product identity source of truth: SKU/GTIN/MPN/brand.
- CAND-005 — Product commercial facts: price/currency/sale/availability source of truth.
- CAND-006 — out-of-stock vs discontinued Product lifecycle.
- CAND-008 — editorial provenance: author/reviewer/date/source/citation.
- CAND-009 — FAQ visible-content/schema boundary.
- CAND-010 — Stores/location/NAP/local-trust role.
- CAND-011 — informational Article/Academy commercial CTA policy.
- CAND-012 — image filename/media naming for new assets.
- CAND-013 — representative/primary image, gallery consistency and duplicate/reuse policy.
- CAND-015 — image technical delivery, subject to separation from the sitewide page-experience decision.
- CAND-016 — video host-page/fetchability/prominence/player policy.
- CAND-019 — canonical Mariwork facts and naming-consistency registry.
- CAND-021 — verified off-site entity references / entity-evidence boundary; keep DEFERRED.
- CAND-022 — release isolation, change annotation and measurement baseline.
- CAND-023 — monitoring success/iterate/rollback interpretation.
- CAND-024 — maintenance triggers.
- CAND-025 — Merchant Center / Free Listings program entry and eligibility; keep DEFERRED.

### Confirm with modification / split

#### CAND-007 — MODIFY

Do not combine future Product slug/URL policy with variant-preselection behavior.

Authoritative child decision should be:

**Future Product URL/slug change policy and history preservation.**

Variant-preselection URLs stay governed by the Product variant/schema/parameter architecture decisions.

#### CAND-014 — SPLIT

"Image context, linked-image behavior and discovery/sitemap policy" combines two independently selectable concerns.

Create:
- image context/caption/linked-image behavior;
- image discovery/indexability/sitemap treatment where applicable.

#### CAND-017 — SPLIT

Video metadata, thumbnail and transcript are independently meaningful.

Create at least:
- video title/description/naming standard;
- video thumbnail policy;
- video transcript/summary/key-text policy.

#### CAND-018 — MODIFY

Create a decision for:

**Video duplicate/orphan/weak-context lifecycle.**

Do not duplicate general cross-family internal-link policy. Video-specific linking requirements should reference the existing Internal Link architecture decisions.

#### CAND-020 — MODIFY

Create:

**Branded query/landing-page role strategy.**

Do not create a separate branded-monitoring decision here; monitoring is governed through the measurement decisions and can carry brand-specific metrics as an application.

#### CAND-026 — MODIFY / KEEP DEFERRED

Create one deferred **Product feed architecture/data-contract** decision separate from Merchant Center program entry.

It may remain an umbrella while deferred, but must be split further before feed implementation if one discussion cannot unambiguously decide identity, variant, price/availability, image and landing-page behavior.

#### CAND-027 — SPLIT

Create:
- genuine reviews/social-proof collection and visible-display policy;
- review/rating structured-data eligibility and ownership policy.

Both remain DEFERRED until real review data is audited.

---

## 3. Review of 9 over-broad current decisions

### DEC-004 — MODIFY, do not simply delete

P-001 correctly identifies endpoint differences.

Preserve DEC-004 for **Cart / Checkout transactional utility policy**.

Add children for:
- Login / My Account auth/account policy;
- Fast Buy utility/landing policy.

This preserves the referenced ID while separating state/privacy and search-role choices.

### DEC-016 — SPLIT

Preserve DEC-016 for **Shop metadata strategy**.

Add:
- Product Category metadata strategy;
- `pa_volume` metadata strategy.

### DEC-053 — NARROW + children

Preserve DEC-053 for **canonical Mariwork facts and naming registry**.

Separate:
- brand/trust site-content and entity-supporting page strategy;
- branded query/landing-page strategy;
- verified off-site entity-reference boundary.

### DEC-055 — RECLASSIFY

P-001 is correct that "sampling" is evidence/QA, not target-state strategy.

Mark DEC-055 `SUPERSEDED` as a Decision item and move its practical requirement into visual evidence/QA planning.

Do not create a replacement DEC solely for sample size; rollout/canary governance is already DEC-068.

### DEC-058 — SUPERSEDE / split

Current DEC-058 is too broad and overlaps DEC-038.

Keep DEC-038 as the sole VideoObject/schema eligibility/ownership decision.

Mark DEC-058 `SUPERSEDED` and replace it with atomic video decisions for:
- host-page/fetchability/player/prominence;
- title/description/naming;
- thumbnail;
- transcript/summary;
- duplicate/orphan lifecycle.

Video inventory itself is evidence collection, not a target-state decision.

### DEC-062 — NARROW + split

Preserve DEC-062 for **author/date archive public/indexability policy**.

Add separate decisions for:
- feed URL policy;
- general internal-search result policy;
- 404/soft-404/error-lifecycle policy.

Product Search remains DEC-061 and should not be duplicated.

### DEC-069 — NARROW + children

Preserve DEC-069 for **monitoring windows and metrics**.

Add:
- release/change annotation and comparable baseline policy;
- success/iterate/rollback interpretation;
- maintenance-trigger policy.

### DEC-072 — NARROW + child

Preserve DEC-072 for **Merchant Center / Free Listings program entry and eligibility** and keep it DEFERRED.

Add separate deferred Product Feed architecture/data-contract decision.

### DEC-073 — NARROW + child

Preserve DEC-073 for **genuine review/social-proof collection and visible display policy**, DEFERRED.

Add separate deferred review/rating structured-data eligibility/ownership decision.

---

## 4. Duplicate / overlap review

P-001's single explicit overlap is confirmed:

- DEC-038 remains VideoObject eligibility/ownership.
- DEC-058 must no longer contain VideoObject ownership.

Other cited parent/child pairs should remain distinct.

---

## 5. Additional material gaps found by P-002

### P2-ADD-001 — Search crawler access policy

Current documents correctly distinguish:
- Googlebot;
- OAI-SearchBot;
- GPTBot;
- ChatGPT-User.

But a durable target-state decision is still needed for Mariwork's own crawler-access policy where control is available.

It should cover:
- Googlebot search access;
- OAI-SearchBot search/discovery access;
- separation from AI training-crawler choices;
- WAF/CDN/server equivalence checks;
- no accidental blocking of desired search crawlers.

Initial status: `NEEDS_TARGETED_EVIDENCE`.

This is not a full security audit.

### P2-ADD-002 — Mobile / CWV / Page Experience remediation policy

The technical audit explicitly lacks current field/lab evidence and MASTER-TODO requires representative validation.

Create a decision defining:
- representative templates;
- field vs lab evidence hierarchy;
- when an issue becomes an SEO/performance remediation item;
- interaction with image/lazy-load/LCP decisions;
- no ranking guarantee.

Initial status: `NEEDS_TARGETED_EVIDENCE`.

Do not invent numerical performance targets beyond documented web-vitals thresholds and project performance requirements.

### P2-ADD-003 — SEO concern ownership target matrix

The project has the Rank-Math-first accepted rule, but implementation readiness still needs a concern-by-concern target decision when ownership can vary.

Create a decision for the final target owner matrix covering at least:
- title/meta;
- robots;
- canonical;
- sitemap;
- schema;
- redirects;
- robots.txt/server crawl controls.

This is not a replacement for `docs/SEO-OWNERSHIP.md`; it applies the accepted ownership rule to Mariwork's actual current stack.

Initial status: `OPEN` / evidence-backed by current ownership matrices.

---

## 6. Topics that should NOT become new Strategy Decisions now

The following should stay as evidence, QA or implementation mechanics unless a future conflict creates a genuine target-state choice:

- sitemap `lastmod` checking by itself;
- deterministic backup commands;
- exact visual sample count;
- raw crawl batch size;
- individual before/after checks;
- PageSpeed/Lighthouse tooling choice;
- per-page implementation order;
- generic "fix all 404s";
- exhaustive parameter generation;
- one Decision per historical URL;
- one Decision per image/video.

The backlog must be exhaustive in **policy choices**, not bloated with operational mechanics.

---

## 7. Content coverage review

P-001 correctly found the main missing editorial policies.

In P-003 ensure explicit traceability for:

- page/family intent and content role;
- title/H1;
- metadata;
- visible content architecture;
- factual accuracy/freshness;
- author/reviewer/date/source/citation;
- commercial CTA boundary;
- FAQ semantics;
- location/NAP facts;
- Article vs Academy;
- Product vs Category vs Article;
- cannibalization resolution path;
- internal links and anchor text;
- image/video policy.

A separate universal H2/H3 Decision is **not required** if family content-architecture decisions explicitly define heading structure where needed.

---

## 8. Technical coverage review

Before P-005 freeze, the authoritative backlog must explicitly cover or map to an accepted rule:

- URL normalization;
- canonical architecture;
- robots/indexability by relevant URL family;
- sitemap membership by family;
- redirects / 404 / 410 / soft-404;
- facets/parameters/pagination/search/feed/attachments;
- JS/AJAX critical-content discoverability;
- structured-data ownership;
- Woo Product facts and lifecycle;
- crawler access;
- mobile/CWV/page experience;
- concern-by-concern technical ownership.

No new separate decision is needed for HTTPS as a generic best practice if preferred-host/protocol policy records HTTPS + canonical host as the project target.

---

## 9. Image / Video / Brand coverage review

### Images

Required target-state decisions after reconciliation:

- ALT by image role;
- filename/new-media naming;
- primary/gallery/reuse;
- context/caption/linked-image behavior;
- discovery/sitemap;
- technical delivery/performance;
- family exceptions for Product and Article/Academy.

Sampling is evidence/QA.

### Video

Required target-state decisions:

- VideoObject eligibility/owner;
- host page/fetchability/prominence/player;
- title/description/naming;
- thumbnail;
- transcript/summary;
- duplicate/orphan lifecycle;
- cross-family links through the common internal-link architecture.

Inventory is evidence collection.

### Brand

Required target-state decisions:

- canonical verified brand facts/naming;
- brand/trust site-content role;
- branded query/landing-page role;
- homepage/Organization schema (already DEC-032);
- verified off-site entity-reference boundary;
- PR remains deferred until site architecture stabilizes.

---

## 10. Deferred programs

The backlog may freeze with some items `DEFERRED`.

Freeze does not require deciding future optional programs now.

It requires that deferred programs have a clear future decision gate and cannot silently unlock implementation.

Therefore:

- External PR may remain DEC-071 umbrella DEFERRED.
- Merchant Center entry and Product Feed architecture should be separate DEFERRED decisions.
- Review collection/display and Review schema should be separate DEFERRED decisions.

---

## 11. Execution Backlog review

P-001's 15 EXE dependency gaps are credible, but they should not be repaired against candidate IDs.

First complete P-003 authoritative DEC reconciliation.

Then P-006 must rebuild EXE dependencies using the final DEC IDs.

No EXE item should be unlocked during P-002/P-003.

---

## 12. P-002 outcome

### Confirmed

- P-001 freeze verdict: `NOT_READY_FOR_FREEZE`.
- Need for authoritative backlog reconciliation.
- Need to preserve existing DEC IDs.
- Need to split media/brand/monitoring/product-data decisions.
- Need to repair EXE dependencies after DEC reconciliation.

### Modified

- Some of the 27 candidate additions should become multiple atomic Decisions.
- Future Product URL policy should not absorb variant-preselection.
- Video linking should use the general Internal Link architecture rather than duplicate it.
- Branded monitoring should use the global measurement framework.
- Image sampling should not remain a Decision.

### Additional gaps

Three new decision domains beyond P-001:
- crawler access;
- mobile/CWV/page experience;
- concern-by-concern SEO owner target matrix.

### Rejected as standalone Decision concepts

- visual sample count;
- inventory collection itself;
- generic QA mechanics;
- sitemap lastmod checking by itself.

## 13. Next step

Proceed to P-003/P-004:

1. reconcile `strategy/DECISION-BACKLOG.md` using this review;
2. preserve all existing DEC IDs;
3. append new atomic DEC IDs;
4. mark superseded/reclassified IDs explicitly;
5. create a canonical Decision Coverage Matrix mapping source → authoritative DEC/rule;
6. do not edit EXE dependencies yet except to note they await P-006;
7. keep Production writes = 0.

Decision Backlog freeze remains **NO** until P-004 confirms zero unexplained material gaps.
