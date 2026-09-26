# P-013 — P-012 Ownership / Provenance Reconciliation

**Date:** 2026-09-26  
**Mode:** repository planning reconciliation only  
**Production writes:** 0  
**Production implementation tasks issued:** 0  
**Source audit:** `audits/strategy/P-012-POST-P011-INTEGRITY-REAUDIT.md` (recovered provenance record on main)  
**P-012 audited HEAD:** `7118e87d12e06edfe4b1f016dc163a546b38fa4c`  
**P-012 verdict:** `FAIL_STAGE_6_NOT_SAFE`

## Purpose

Resolve the two remaining HIGH execution-ownership findings from P-012, restore durable audit provenance on `main`, and remove historical-counter ambiguity without changing accepted SEO strategy or performing Production work.

## Source findings

P-012 reported:

- `NEW-P012-01` HIGH — duplicate Academy Guide/Course collection DEC-130 write paths in EXE-033 and EXE-035.
- `NEW-P012-02` HIGH — duplicate brand/entity write paths across EXE-027/028/029.
- `NEW-P012-03` MEDIUM — P-010 source audit absent from audited main because the original report lived on divergent/local history.
- `NEW-P012-04` LOW — historical P-007 counters could be mistaken for current inventory by naive automation.

P-012 found no accepted-Decision coverage gaps, no orphan Decision, no orphan EXE, and no Backlog↔Final-TODO semantic drift.

## Reconciliation

### NEW-P012-01 — Academy Guide/Course collection ownership

**Resolved without changing Decision target state.**

#### EXE-033
Owns:

- Guide/Course entity identity;
- Guide/Course metadata;
- non-DEC-130 supporting content for Guide/Course entities;
- current Guide vs future Course entity mapping.

Explicit exclusion:

- EXE-033 must not write the Academy archive/current Guide-collection DEC-130 visible hub block.

#### EXE-035
Owns:

- coordination of the durable archive/hub DEC-130 content-block program;
- the DEC-130 visible hub block for Academy archive/current Guide collection;
- Magazine archive DEC-130 visible hub block;
- other residual durable hub blocks not already assigned to EXE-012/019/020/030.

Explicit exclusion:

- EXE-035 must not write Guide/Course entity metadata or non-hub supporting content owned by EXE-033.

This preserves DEC-037's semantic identity of the current guide collection while giving the DEC-130 visible hub block exactly one execution write owner.

### NEW-P012-02 — Homepage / Static / shared Organization ownership

**Resolved by concrete output ownership.**

#### EXE-027 — Homepage page-family owner

Sole write owner for:

- Homepage visible content / CTA;
- Homepage SEO metadata;
- Homepage WebSite/WebPage outputs.

Dependencies / exclusions:

- consumes verified canonical brand/entity facts from EXE-029;
- may not write the canonical/shared Organization/sameAs/contact registry;
- may not independently redefine shared Organization entity facts/schema.

#### EXE-028 — Static/Trust page-family owner

Sole write owner for:

- Static/Trust visible content;
- Static/Trust SEO metadata;
- role-appropriate page-local schema.

Dependencies / exclusions:

- consumes verified canonical contact/social/entity facts from EXE-029;
- may not write the canonical/shared Organization/sameAs/contact registry;
- may not independently redefine shared Organization entity facts/schema.

#### EXE-029 — shared entity owner

Sole write owner for:

- canonical Mariwork brand/entity registry;
- shared Organization entity facts;
- `sameAs` values;
- verified contact-channel entity data;
- shared Organization/sameAs/contact-channel schema/configuration.

Explicit exclusions:

- no Homepage or Static/Trust visible-content writes;
- no H1 writes;
- no page SEO metadata writes;
- no page-local WebSite/WebPage/CollectionPage content/schema owned by EXE-027/028/other page-family packages.

This lets page-family packages consume one verified entity source without becoming parallel owners of the shared Organization entity.

### NEW-P012-03 — audit provenance

**Resolved as an explicit provenance recovery, without history rewrite.**

The original P-010 and P-012 report commits reported by Codex were not reachable through the connected GitHub repository.

P-013 did **not** reset, force-move, cherry-pick fabricated SHAs, or rewrite `main`.

Instead, the expected durable paths were restored as explicit **Recovered provenance records**:

- `audits/strategy/P-010-FINAL-DECISION-TO-EXECUTION-INTEGRITY-AUDIT.md`
- `audits/strategy/P-012-POST-P011-INTEGRITY-REAUDIT.md`

Each record:
- identifies the original audited HEAD;
- preserves the reported unreachable/local commit SHA;
- records the material findings and verdict supplied by the owner;
- explicitly states that it is a provenance recovery summary rather than a claim that the old local commit was merged.

This restores a durable repository audit chain while preserving truthful Git history.

### NEW-P012-04 — historical counter ambiguity

**Resolved.**

The P-007 section in `tasks/EXECUTION-BACKLOG.md` is now explicitly labelled:

`HISTORICAL SNAPSHOT ONLY`

and states that its 57-package / 16-READY counters are not the current inventory.

Current inventory remains derived from live EXE rows and the latest reconciliation:

- **58 EXEs**
- **17 READY_FOR_TASK**
- **41 BLOCKED**

## Readiness effect

No readiness promotion or demotion was performed.

The five packages involved in the P-012 ownership findings remain BLOCKED:

- EXE-027
- EXE-028
- EXE-029
- EXE-033
- EXE-035

Their factual/content/query/entity gates remain in force.

## Files changed in P-013

- `tasks/EXECUTION-BACKLOG.md`
- `tasks/FINAL-EXECUTION-TODO.md`
- `MASTER-TODO.md`
- `audits/strategy/P-010-FINAL-DECISION-TO-EXECUTION-INTEGRITY-AUDIT.md` — recovered provenance record
- `audits/strategy/P-012-POST-P011-INTEGRITY-REAUDIT.md` — recovered provenance record
- this report

No Production/system/app files were changed.

## Post-reconciliation structural verification

- Execution Backlog EXEs: **58**
- Final TODO EXEs: **58**
- READY: **17**
- BLOCKED: **41**
- Backlog ↔ Final TODO semantic drifts: **0**
- P-010 provenance path present on main: YES
- P-012 provenance path present on main: YES
- EXE-033/035 mutual output exclusion: PRESENT
- EXE-027/029 mutual output exclusion: PRESENT
- EXE-028/029 mutual output exclusion: PRESENT
- P-012 closed in MASTER: YES
- P-013 closed in MASTER: YES
- P-014 independent re-audit opened: YES

## Stage-6 gate

P-013 does not itself declare Stage 6 safe.

`P-014` must independently re-audit the post-P-013 repository state.

Broad Stage-6 Production implementation task generation remains gated until P-014 returns either:

- `PASS`, or
- `PASS_WITH_NON_BLOCKING_FINDINGS`.

Bounded read-only evidence/research tasks remain governed by the existing evidence-first rules.
