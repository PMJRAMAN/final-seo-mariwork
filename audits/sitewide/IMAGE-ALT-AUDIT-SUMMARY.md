# Image / ALT Audit Summary

**Date:** 2026-09-25
**Lifecycle:** `CODEX_AUDITED`
**Scope:** family/sitewide candidate inventory only
**Production writes:** `0`

## Evidence reused

- `registry/SYSTEMIC-FINDINGS.md` — SYS-010 and SYS-011.
- `handoff/round1/round1-repeated-findings.json` — representative image/ALT findings.
- `data/normalized/round1-page-evidence.jsonl` — supplied image counts and missing-ALT measurements.
- `strategy/VISUAL-IMAGE-SEO.md` — approved baseline against keyword-stuffed or invented ALT.
- `audits/second-review/store/SR-004-CHATGPT-STORE-SECOND-REVIEW.md` — Store ALT deferred to the image/content workstream.

## Current measured candidates

| Family | Measured evidence | Classification | Required human review |
|---|---|---|---|
| Articles | 83 missing ALT out of 133 reported images in SYS-010 | `NEEDS_TARGETED_REFRESH` | Determine informative vs decorative role and inspect repeated/template ALT |
| Academy / lessons | 74 missing ALT out of 170 reported images in SYS-011 | `NEEDS_TARGETED_REFRESH` | Sample instructional images, steps, product/material images and decorative assets |
| Homepage | Round-1 sample reported 12 images and 0 missing ALT | `CURRENT_EVIDENCE_COMPLETE` for sample only | Confirm representative/eager images and visual meaning; no mass write |
| Products / Store | Product evidence and current Store review defer ALT decisions | `NEEDS_TARGETED_REFRESH` | Review primary/gallery purpose and family/template repetition before any text decision |
| Static/trust/category pages | Page-level image observations exist in dossiers; no complete visual-purpose pass | `NEEDS_TARGETED_REFRESH` | Sample brand/trust/category images and decorative treatment |
| Attachments/media | 626 attachment IDs returned; 845 advertised; 219 difference is unknown | `BLOCKED_NEEDS_DECISION` | Reconcile only representative public media URLs; do not infer deletion/privacy |

## Audit rule

Missing ALT is a candidate issue, not an instruction to write text. For each image, the later approved work must determine whether it is informative or decorative. Informative images may receive factual descriptive ALT; decorative images may retain empty ALT. No keyword stuffing, invented visual facts, bulk write or Production content change is authorized here.

`google_basis=GOOGLE_RECOMMENDED` for useful image context/accessibility; `google_reference=https://developers.google.com/search/docs/appearance/google-images`.

## Finding

### SYS-015 — Image purpose and ALT quality are not closed by counts alone

```yaml
id: SYS-015
severity: P2
scope: FAMILY
status: OPEN
evidence_class: MEASURED
confidence: HIGH
source_refs:
  - registry/SYSTEMIC-FINDINGS.md#SYS-010
  - registry/SYSTEMIC-FINDINGS.md#SYS-011
  - data/normalized/round1-page-evidence.jsonl
impact: "Measured missing-ALT counts identify candidates but do not establish whether an image is informative, decorative, duplicated, or visually misdescribed."
recommendation: "Run a human visual review on representative high-value families and record role, factual description, repetition and delivery behavior before considering implementation."
acceptance_criteria: "A representative family matrix records image role and evidence-based ALT decision; no invented visual facts or keyword stuffing; implementation remains separately approved."
google_basis: GOOGLE_RECOMMENDED
google_reference: https://developers.google.com/search/docs/appearance/google-images
seo_owner_current: CONTENT/UNKNOWN_NEEDS_VERIFICATION
seo_owner_target: CONTENT for image purpose and ALT; RANK_MATH only for supported metadata concerns
rank_math_capability_checked: VERIFIED_INSTALLED_1.0.279; ALT ownership is not a Rank Math disposition
rank_math_path_or_reason_not_used: ALT requires image/content judgment and no Production write is authorized.
```
