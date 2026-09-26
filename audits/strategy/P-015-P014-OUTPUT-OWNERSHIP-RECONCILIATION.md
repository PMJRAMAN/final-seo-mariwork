# P-015 — P-014 Output-Ownership Reconciliation

**Date:** 2026-09-26  
**Mode:** repository planning reconciliation only  
**Production writes:** 0  
**Production implementation tasks issued:** 0  
**Source audit:** `audits/strategy/P-014-FINAL-POST-P013-INTEGRITY-GATE.md`  
**P-014 audited HEAD:** `faa8e429fd387b549203134d52b3ced47dd1a0c6`  
**P-014 verdict:** `FAIL_STAGE_6_NOT_SAFE`

## Purpose

Resolve the three HIGH duplicate-write boundaries and one MEDIUM field-boundary ambiguity identified by P-014 without changing accepted SEO strategy, package readiness, or Production state.

## Source findings

P-014 reported:

- `NEW-P014-01` HIGH — EXE-011 vs EXE-024/025/031 XML sitemap membership writes.
- `NEW-P014-02` HIGH — EXE-008 vs EXE-022 Bundle component rendering.
- `NEW-P014-03` HIGH — EXE-042 vs EXE-018/032/033 contextual body-link insertion.
- `NEW-P014-04` MEDIUM — EXE-023 vs EXE-026 factual Woo availability/stock field ownership unclear.

P-014 otherwise confirmed:
- 129 Decisions, DEC-126 unused;
- 58 EXEs;
- 17 READY / 41 BLOCKED;
- zero accepted-Decision coverage gaps;
- zero Backlog↔Final-TODO semantic drift;
- P-013 Academy and brand/entity ownership fixes resolved;
- provenance chain valid.

## Reconciliation

### NEW-P014-01 — XML sitemap membership

**Resolved.**

#### EXE-011
Is now the **sole XML sitemap membership writer**.

It owns:
- sitemap include/exclude membership mutation;
- sitewide sitemap reconciliation;
- sitemap QA after family rollout.

Its first Stage-6 task remains read-only evidence. Mutation still requires:
- exact family/URL manifest;
- verified Rank Math ownership;
- separately authorized write scope.

#### EXE-024 / EXE-025 / EXE-031
Continue to own their family-specific:
- taxonomy/term decommission;
- assignment cleanup where applicable;
- URL disposition;
- redirect/404/410 behavior;
- dependency verification.

They explicitly **must not mutate XML sitemap membership**.

They hand final family disposition to EXE-011 and verify the sitemap result there.

This preserves DEC-030's sitewide sitemap authority while keeping family decommission logic in family packages.

### NEW-P014-02 — Bundle component rendering

**Resolved.**

#### EXE-008
May:
- inspect initial HTML;
- inspect rendered DOM;
- inspect network/AJAX behavior;
- diagnose generic/sitewide JS/AJAX discoverability;
- own generic JS/AJAX remediation only where no dedicated family package exists.

For Bundle/set component rendering, EXE-008 is explicitly **evidence/diagnosis only**.

#### EXE-022
Is the **sole Bundle/set component-render writer**.

It owns any Bundle/set component-list rendering correction in:
- initial HTML;
- rendered DOM;
- YITH/Woo/custom-code path needed to satisfy DEC-036/080.

It consumes EXE-008 diagnosis where useful.

### NEW-P014-03 — contextual body links

**Resolved.**

#### EXE-042
Now owns only:
- cross-family source→destination mapping;
- approved anchor/context plan;
- link architecture coordination;
- rollout QA.

EXE-042 **does not insert page-body links**.

Actual contextual body-link insertion is owned by the source-family package:

- Product page → EXE-018
- Product Category page → EXE-019
- Article → EXE-032
- Guide/Course → EXE-033

Global/navigation/component link concerns remain under EXE-041/043 according to component ownership.

This prevents a cross-family link-planning package from editing the same body content as a page-family content package.

### NEW-P014-04 — factual Woo fields vs lifecycle disposition

**Resolved.**

#### EXE-023
Is the **sole factual Woo commercial-field writer** for:

- price;
- sale price;
- currency;
- stock;
- availability;
- authoritative mappings of those fields.

#### EXE-026
Owns Product lifecycle disposition after a Product is factually classified:

- retain current Product page;
- redirect to a genuine successor;
- proper 404/410 where appropriate;
- supporting lifecycle content state.

EXE-026 must **not** directly rewrite factual Woo price/sale/currency/stock/availability fields.

If lifecycle review reveals a factual commercial-field correction, that correction is handed to EXE-023.

## Readiness impact

No readiness state changed.

Current inventory remains:

- **58 EXEs**
- **17 READY_FOR_TASK**
- **41 BLOCKED**

No affected BLOCKED package was promoted.

EXE-011 remains READY only under its evidence-first initial-task rule.

## Files changed

- `tasks/EXECUTION-BACKLOG.md`
- `tasks/FINAL-EXECUTION-TODO.md`
- `MASTER-TODO.md`
- this P-015 reconciliation report

No Decision, Strategy Lock, Production, server, WordPress, Rank Math or application file was modified.

## Stage-6 gate

P-015 does not declare Stage 6 safe by itself.

`P-016` is opened for an independent full post-P-015 integrity re-audit.

Broad Stage-6 Production implementation task generation remains blocked until P-016 returns:

- `PASS`, or
- `PASS_WITH_NON_BLOCKING_FINDINGS`.
