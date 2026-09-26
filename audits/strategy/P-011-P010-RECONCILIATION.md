# P-011 — P-010 Integrity Findings Reconciliation

**Date:** 2026-09-26  
**Mode:** repository planning reconciliation only  
**Production writes:** 0  
**Production implementation tasks issued:** 0  
**Source audit:** `audits/strategy/P-010-FINAL-DECISION-TO-EXECUTION-INTEGRITY-AUDIT.md`  
**P-010 verdict:** `FAIL_STAGE_6_NOT_SAFE`  
**P-011 starting planning baseline:** post-P-010 main  
**Authority:** owner + ChatGPT reconciliation of audit findings; no new Production target state invented

## Purpose

Resolve the repository-integrity findings that made broad Stage-6 task generation unsafe, while preserving accepted Decision meaning and keeping unresolved factual/content/entity gates blocked.

## Reconciliation summary

### F-01 — stale EXE-013–015 spelling blocker
**Resolved.**

DEC-007–009 and DEC-053 already contain canonical `ماری‌ورک`. The stale spelling prerequisite was removed from EXE-013–015. These packages remain BLOCKED on their real factual/canary prerequisites:
- EXE-013: named five-URL canary + verified color names/codes;
- EXE-014: verified bundle identity/composition + named canary;
- EXE-015: verified Product identity/name/code + named canary.

No package was promoted by this correction.

### F-02 — EXE-034 / EXE-048 VideoObject ownership collision
**Resolved.**

- EXE-034 owns Academy/LearnDash schema ownership and video-host eligibility/canary mapping.
- EXE-034 is explicitly prohibited from writing VideoObject.
- EXE-048 is the sole VideoObject technical/schema write owner.
- EXE-048 depends on EXE-047 inventory and, for Academy hosts, the EXE-034 host/schema-owner output.

### F-03 — archive/hub content-block overlap
**Resolved.**

DEC-130 write ownership is now singular by family:
- Shop → EXE-012
- Product Category → EXE-019
- pa_volume → EXE-020
- Blog Category → EXE-030
- Academy / Magazine / other residual durable hubs not assigned above → EXE-035

EXE-035 is coordination + residual-hub implementation and may not duplicate the family-owned writes above.

### F-04 — EXE-009 / EXE-049 crawler overlap
**Resolved.**

- EXE-009 is the sole owner for robots/WAF/server crawler-control mutations.
- EXE-049 is read-only AI-search eligibility verification and cannot mutate robots/WAF/server controls.

### F-05 — broad READY reconciliation scopes
**Resolved through task-boundary hardening.**

EXE-005, EXE-007, EXE-009 and EXE-011 retain READY_FOR_TASK only for explicitly bounded evidence-first initial tasks.

Their first Stage-6 task must be read-only. Any Production mutation requires:
- exact affected-entity/URL/family manifest;
- single write owner;
- capability/ownership revalidation;
- exact change scope;
- separate authorization under governance.

The governance document now explicitly distinguishes evidence-ready from mutation-authorized work.

### F-06 — stale Decision range
**Resolved.**

Current Decision Backlog authority now states DEC-001–DEC-130, with DEC-126 intentionally unused/reserved. The historical P-004 range in the Decision Log is preserved as historical rather than represented as current.

### F-07 — DEC-126
**No correction required.**

DEC-126 remains an intentionally unused/reserved stable ID. No renumbering.

### F-08 — repeated historical Decision headings
**Resolved as authority/parsing clarification.**

`docs/DECISIONS.md` now explicitly states that it preserves historical proposals/amendments and may repeat DEC headings. Current machine parsing and target-state authority belong to:
- `strategy/DECISION-BACKLOG.md`
- `strategy/ACCEPTED-DECISIONS.md`

### F-09 — MASTER stale naming + non-pa_volume attribute gap + D-005
**Resolved / disposition recorded.**

- B0-022 is marked resolved by DEC-007–011 + DEC-053.
- B0-023 now uses canonical `ماری‌ورک` and points to EXE-013–016 implementation/verification.
- New EXE-058 provides read-only discovery for all non-`pa_volume` Product attribute archives.
- EXE-058 may inventory current robots/sitemap/internal-link/public-use state and create per-family decision dossiers, but cannot choose or implement index/noindex/redirect/canonical policy without a later accepted Decision.
- D-005 is now an explicit discovery trigger: if a current public policy/terms/privacy entity is found, an indexability Decision + EXE must be opened before mutation.

### F-10 — Wave closure vs implementation ambiguity
**Resolved.**

The Final Execution TODO now has an explicit milestone boundary:
- Waves 2/3 are blocker-closure/design/mapping lanes;
- blocked packages do not become executable merely by appearing there;
- Wave-4 admission requires gate closure, READY_FOR_TASK reconciliation in both authorities, and an unambiguous write owner.

### F-11 — EXE-057 generic final regression manifest
**Resolved.**

EXE-057 remains terminal/BLOCKED and now requires a frozen, versioned completed-package + Decision + Lock regression manifest before activation.

### F-12 — EXE-054 before EXE-052
**Resolved.**

EXE-054 may run a read-only verification task before EXE-052 is complete. Any redirect mutation requires:
- EXE-052 baseline complete;
- URL-specific identity/disposition;
- separately authorized write scope.

### F-13 — EXE-046 implementation path
**Clarified; BLOCKED correctly retained.**

The gate now requires an owner-approved non-destructive upload-workflow enforcement design, implementation owner and rollback. Codex cannot choose the path.

### F-14 — malformed Decision table rows
**Resolved without changing accepted target-state meaning.**

Literal pipe characters inside the accepted target text of DEC-003, DEC-007, DEC-009, DEC-014 and DEC-016 were escaped so Markdown/table parsers no longer shift/truncate cells.

## New evidence-only package

### EXE-058
**Non-pa_volume Product-attribute archive inventory + decision dossier (read-only)**

Purpose:
- close MASTER B8-008–010 traceability;
- discover every attribute archive besides `pa_volume`;
- record current public/nonpublic state, Rank Math robots/sitemap ownership, internal-link exposure and actual use;
- produce a per-family decision dossier.

It does **not** authorize an indexability, redirect, canonical, sitemap or content change.

## Current authoritative execution inventory after P-011

- EXE packages: **58**
- READY_FOR_TASK: **17**
- BLOCKED: **41**
- Production writes: **0**
- Production implementation tasks issued: **0**
- Accepted-Decision coverage gaps introduced: **0**

EXE-057 remains terminal by lifecycle even though EXE-058 is numerically higher.

## Files reconciled

- `strategy/DECISION-BACKLOG.md`
- `docs/DECISIONS.md`
- `docs/DECISION-TO-EXECUTION-GOVERNANCE.md`
- `tasks/EXECUTION-BACKLOG.md`
- `tasks/FINAL-EXECUTION-TODO.md`
- `MASTER-TODO.md`

## Stage-6 gate

Broad Stage-6 implementation must not begin solely on this reconciliation.

`P-012` is opened in MASTER-TODO for an independent post-P-011 integrity re-audit. It must return `PASS` or `PASS_WITH_NON_BLOCKING_FINDINGS` before broad Stage-6 Production implementation task generation.

Narrow read-only evidence tasks may still be written for packages whose current scope explicitly permits them.
