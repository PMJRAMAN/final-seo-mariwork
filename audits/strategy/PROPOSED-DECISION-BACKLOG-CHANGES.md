# P-001 — Proposed Decision Backlog Changes

**Status:** `PROPOSAL ONLY — NOT AUTHORITATIVE`
**Date:** 2026-09-25
**Authority:** `CODEX_AUDITED`
**Production writes:** `0`
**Rule:** No new `DEC-###` IDs are allocated here. ChatGPT P-002 and the owner must accept, modify or reject every candidate.

## Candidate additions — 27 missing decision candidates

These `ADD` candidates are the missing-decision count reported by P-001. They are deliberately phrased as target-state questions, not implementation instructions.

| Candidate | Action | Proposed title | Source references | Suggested initial status | Dependency notes |
|---|---|---|---|---|---|
| CAND-001 | ADD | Preferred host/protocol, trailing-slash and future URL-normalization policy | `SITEWIDE-TECHNICAL-AUDIT-SPEC` A/E; P-000; MASTER-TODO I-005/I-007 | `OPEN` | Precedes canonical, redirect and sitemap implementation. |
| CAND-002 | ADD | Sitewide canonical and duplicate-URL architecture | `SITEWIDE-TECHNICAL-AUDIT-SPEC` E; MASTER-TODO I-005; `SYS-006` | `OPEN` | Parent for parameter, archive, variant and legacy canonical exceptions. |
| CAND-003 | ADD | Critical JS/AJAX content and crawlable-link discoverability | `SITEWIDE-TECHNICAL-AUDIT-SPEC` G; MASTER-TODO I-003/I-008 | `NEEDS_TARGETED_EVIDENCE` | Evidence/rendering sample must precede any implementation scope. |
| CAND-004 | ADD | Product identity source of truth for SKU/GTIN/MPN/brand | P-000; MASTER-TODO O-002/O-005; SR-004 `SR-ST-004` | `NEEDS_TARGETED_EVIDENCE` | Precedes Product/Offer, ProductGroup and feed decisions. |
| CAND-005 | ADD | Product commercial-fact source of truth for price/currency/sale/availability | P-000; `SITEWIDE-TECHNICAL-AUDIT-SPEC` H/I; MASTER-TODO B3/O-002 | `NEEDS_TARGETED_EVIDENCE` | Must reconcile visible Woo facts with structured data. |
| CAND-006 | ADD | Out-of-stock versus discontinued-product lifecycle | P-000; MASTER-TODO B2/B6/I-002; `SYS-003` | `OPEN` | Precedes product indexability, schema and migration dispositions. |
| CAND-007 | ADD | Future product slug/URL and variant-preselection lifecycle | P-000; MASTER-TODO B0-010/B0-012; `SYS-003` | `OPEN` | Must preserve URL history and remain distinct from current legacy mapping. |
| CAND-008 | ADD | Editorial author/reviewer/date/source/citation provenance policy | P-000; CONTENT-RESEARCH-SPEC §§8–9; MASTER-TODO E1 | `OPEN` | Supports Article and Academy trust decisions without inventing facts. |
| CAND-009 | ADD | FAQ visible-content versus structured-data boundary | P-000; SR-005 §5; MASTER-TODO D-003/I-009 | `OPEN` | Must remain semantically correct; not a rich-result promise. |
| CAND-010 | ADD | Stores/location/NAP and local-trust content role | P-000; MASTER-TODO D-004/N-004; `pages/static` dossiers | `NEEDS_TARGETED_EVIDENCE` | Requires verified address/contact facts before target state. |
| CAND-011 | ADD | Informational Article/Academy commercial CTA policy | P-000; CONTENT-RESEARCH-SPEC §7; `DEC-042`–`DEC-046`; SR-004 `SR-ST-009` | `OPEN` | Precedes broad contextual-link or CTA implementation. |
| CAND-012 | ADD | Image filename and media naming policy for new assets | VISUAL-IMAGE-SEO; MASTER-TODO L-005 | `OPEN` | Applies to future assets; no historical bulk rename implied. |
| CAND-013 | ADD | Representative image, gallery consistency and duplicate/reuse policy | VISUAL-IMAGE-SEO; MASTER-TODO L-002/L-006/L-008; `SYS-015` | `NEEDS_TARGETED_EVIDENCE` | Requires representative visual review by family. |
| CAND-014 | ADD | Image context, linked-image behavior and discovery/sitemap policy | VISUAL-IMAGE-SEO; MASTER-TODO L-007/L-008; `SITEWIDE-TECHNICAL-AUDIT-SPEC` J | `NEEDS_TARGETED_EVIDENCE` | Separate informative context from image-sitemap implementation. |
| CAND-015 | ADD | Image technical delivery policy: dimensions, formats, `srcset`, lazy loading and LCP | VISUAL-IMAGE-SEO; MASTER-TODO L-009; I-013 | `NEEDS_TARGETED_EVIDENCE` | Performance claims require representative field/lab evidence. |
| CAND-016 | ADD | Video host-page relationship, fetchability, prominence and player policy | VIDEO-SEO; MASTER-TODO M-002/M-003/M-009; SR-005 §10 | `NEEDS_TARGETED_EVIDENCE` | Precedes any VideoObject canary; no video implementation implied. |
| CAND-017 | ADD | Video title/description, thumbnail, transcript/summary and reusable metadata policy | VIDEO-SEO; MASTER-TODO M-004/M-006/M-007/M-008 | `OPEN` | Must be split from schema ownership and inventory evidence. |
| CAND-018 | ADD | Video duplicate/orphan/context and cross-family-link lifecycle | VIDEO-SEO; MASTER-TODO M-009/M-010/M-011 | `OPEN` | Precedes all-video implementation and final coverage QA. |
| CAND-019 | ADD | Canonical Mariwork facts and naming-consistency registry | BRAND-ENTITY-SEARCH; MASTER-TODO N-001/N-005/N-008; `DEC-053` | `NEEDS_TARGETED_EVIDENCE` | Facts must be verified before schema/content changes. |
| CAND-020 | ADD | Branded query, landing-page and branded-search monitoring policy | BRAND-ENTITY-SEARCH; MASTER-TODO N-002/N-007/N-012 | `OPEN` | Exact query ownership still requires joined evidence or direct research. |
| CAND-021 | ADD | Verified off-site entity references and PR/entity evidence boundary | BRAND-ENTITY-SEARCH; EXTERNAL-PR-STRATEGY; MASTER-TODO N-006/K-001 | `DEFERRED` | Must not invent relationships; coordinate with `DEC-071`. |
| CAND-022 | ADD | Release isolation, change annotation and measurement baseline policy | MEASUREMENT-SPEC §§1–3; MASTER-TODO J-001/J-002; P-000 | `OPEN` | Precedes meaningful rollout comparison. |
| CAND-023 | ADD | Monitoring success, iteration and rollback interpretation | MEASUREMENT-SPEC §§4–7; MASTER-TODO J-002/J-009; P-000 | `OPEN` | Distinct from monitoring window/cadence. |
| CAND-024 | ADD | Maintenance triggers for plugin/Rank Math updates, Google changes, new URLs/404s and freshness | MASTER-TODO J-003–J-008; P-000; `docs/WORKFLOW.md` | `OPEN` | Governs recurring triage, not a one-time QA checklist. |
| CAND-025 | ADD | Merchant Center / Free Listings program entry and eligibility | MASTER-TODO O-001/O-003; `DEC-072` | `DEFERRED` | No implementation until evidence and program decision. |
| CAND-026 | ADD | Product-feed identity, variant, price, availability, image and landing consistency | MASTER-TODO O-004–O-006; `DEC-035`; `DEC-072` | `DEFERRED` | Must remain coordinated with on-site schema without being identical to it. |
| CAND-027 | ADD | Genuine review/social-proof collection, display and schema eligibility | MASTER-TODO O-007–O-009; `DEC-073` | `DEFERRED` | No review markup or content is authorized without genuine data. |

## Atomicity / reclassification proposals — 9 over-broad decisions

| Candidate | Action | Affected decision | Proposed treatment | Why this is not a cosmetic split |
|---|---|---|---|---|
| CAND-028 | SPLIT | `DEC-004` | Separate utility/system policy for auth/fast-buy, cart/checkout state and account/privacy behavior, or define explicit child exceptions. | Current endpoints differ in HTTP/state/privacy behavior. |
| CAND-029 | SPLIT | `DEC-016` | Split Shop metadata, durable Product Category metadata and `pa_volume` metadata. | Each family has different role, content and sitemap dependencies. |
| CAND-030 | SPLIT | `DEC-053` | Separate canonical facts/naming, trust content/schema, branded landing/monitoring and off-site evidence. | Owner can accept one without accepting the others. |
| CAND-031 | RECLASSIFY / SPLIT | `DEC-055` | Move sampling to evidence/QA; keep rollout only if a distinct implementation policy is required. | Evidence sample selection is not a target-state image rule. |
| CAND-032 | SPLIT | `DEC-058` | Remove VideoObject ownership from this item; split inventory, host-page/media-text policy and lifecycle. | VideoObject eligibility is already `DEC-038`; the remaining choices are independent. |
| CAND-033 | SPLIT | `DEC-062` | Separate author/date, feed, search, archive and 404 policies. | Their indexability, privacy and lifecycle choices are not interchangeable. |
| CAND-034 | SPLIT | `DEC-069` | Separate baseline/cadence from success/iterate/rollback and maintenance triggers. | Monitoring can be accepted without accepting a rollback threshold. |
| CAND-035 | SPLIT | `DEC-072` | Separate Merchant eligibility/program gate from product-feed architecture. | External eligibility and feed data-contract decisions have different owners. |
| CAND-036 | SPLIT | `DEC-073` | Separate review-data availability, collection/display and structured-data eligibility. | Genuine-data policy and schema eligibility are distinct decisions. |

## Duplicate/merge/reword proposal — 1 candidate

| Candidate | Action | Affected decisions | Proposed treatment | Reason |
|---|---|---|---|---|
| CAND-037 | REWORD | `DEC-038`, `DEC-058` | Keep `DEC-038` as the sole VideoObject eligibility/ownership decision; remove that concern from `DEC-058`. | Prevents two decisions from unlocking competing video-schema interpretations. |

## Keep-as-is / intentionally deferred observations

- `DEC-025` and `DEC-030` should remain a family policy plus sitewide parent relationship, not be merged.
- `DEC-063` and `DEC-067` are distinct migration-priority and technical-owner decisions.
- `DEC-040` and `DEC-041` are distinct link framework and exact-destination decisions.
- `DEC-054` and `DEC-057` are a global image-role rule plus a family-specific policy, not duplicates.
- `DEC-071` may remain one deferred PR umbrella until the internal architecture and approved landing pages are stable; child decisions are required before PR implementation.

## Authority boundary

This proposal does not edit `strategy/DECISION-BACKLOG.md` or `tasks/EXECUTION-BACKLOG.md`, does not create authoritative IDs, and does not authorize any Production action.
