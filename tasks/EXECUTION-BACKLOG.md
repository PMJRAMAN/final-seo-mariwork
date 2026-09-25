# SEO Execution Backlog

**Status:** LOCKED — strategy decisions are being finalized  
**Authority:** generated only from `ACCEPTED` items in `strategy/DECISION-BACKLOG.md`  
**Production implementation authorized by this file now:** NO

See:
- `docs/DECISION-TO-EXECUTION-GOVERNANCE.md`
- `strategy/DECISION-BACKLOG.md`
- `MASTER-TODO.md`

## Rule

This file is **not** a second strategy document.

It contains implementation packages only after the target state is decided.

Audit findings, Second Review recommendations and MASTER-TODO checkboxes do not enter `READY_FOR_TASK` directly.

Each item must cite:
- accepted Decision IDs;
- related findings;
- MASTER-TODO task/program IDs;
- exact scope;
- exact intended writes;
- SEO owner;
- dependencies;
- canary;
- backup/rollback;
- acceptance criteria;
- Codex QA;
- ChatGPT Final QA.

## Status lifecycle

- `LOCKED_BY_DECISIONS`
- `READY_FOR_TASK`
- `TASK_ISSUED`
- `IMPLEMENTING`
- `CODEX_QA`
- `CHATGPT_FINAL_QA`
- `COMPLETE`
- `BLOCKED`

Only `READY_FOR_TASK` may become a Production Codex task.

---

# Candidate implementation packages

These packages are placeholders derived from SR-004/SR-005. They are deliberately locked until the referenced decisions are accepted.

| Execution ID | Candidate package | Blocking decisions | Current state |
|---|---|---|---|
| EXE-001 | Shop landing H1/title/meta canary | DEC-003, DEC-016 | LOCKED_BY_DECISIONS |
| EXE-002 | Fabric-color Product title normalization canary | DEC-007, DEC-011, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-003 | Sets/bundles title normalization canary | DEC-008, DEC-011, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-004 | Medium/tool title normalization canary | DEC-009, DEC-010, DEC-011, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-005 | Product meta-description remediation batch | DEC-015, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-006 | Durable Product Category metadata/content/sitemap canary | DEC-016, DEC-021, DEC-025, DEC-030 | LOCKED_BY_DECISIONS |
| EXE-007 | Migration-era Product Category 20/27 decommission | DEC-025, DEC-063, DEC-067 | LOCKED_BY_DECISIONS |
| EXE-008 | `pa_volume` archive policy implementation | DEC-026, DEC-030 | LOCKED_BY_DECISIONS |
| EXE-009 | Product Tags controlled decommission | DEC-027, DEC-063, DEC-067 | LOCKED_BY_DECISIONS |
| EXE-010 | Blog Categories lifecycle cleanup | DEC-028, DEC-030, DEC-067 | LOCKED_BY_DECISIONS |
| EXE-011 | Blog Tags controlled decommission | DEC-029, DEC-063, DEC-067 | LOCKED_BY_DECISIONS |
| EXE-012 | Static/Core schema canary | DEC-033, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-013 | Homepage schema cleanup if needed | DEC-032 | LOCKED_BY_DECISIONS |
| EXE-014 | ProductGroup/variant schema canary | DEC-035, DEC-039, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-015 | Bundle/set schema + visible composition canary | DEC-036, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-016 | Academy/LearnDash schema/video canary | DEC-037, DEC-038, DEC-039, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-017 | Store facets/parameter policy canary | DEC-059, DEC-060, DEC-061, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-018 | Homepage/Static metadata/content batch | DEC-002, DEC-012, DEC-017, DEC-022 | LOCKED_BY_DECISIONS |
| EXE-019 | Article factual/content refresh pilot | DEC-013, DEC-018, DEC-023, DEC-049, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-020 | Academy content/metadata pilot | DEC-014, DEC-019, DEC-024, DEC-049, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-021 | Cross-family internal-link pilot | DEC-040–DEC-048, DEC-049–DEC-051, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-022 | Image/ALT visual-review pilot and implementation | DEC-054–DEC-057, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-023 | Video SEO inventory/canary | DEC-038, DEC-058, DEC-068 | LOCKED_BY_DECISIONS |
| EXE-024 | Historical product-volume URL migration batch | DEC-063, DEC-064, DEC-067 | LOCKED_BY_DECISIONS |
| EXE-025 | Historical Education → Academy migration batch | DEC-063, DEC-065, DEC-067 | LOCKED_BY_DECISIONS |
| EXE-026 | Historical Artist/removed-content migration batch | DEC-052, DEC-063, DEC-066, DEC-067 | LOCKED_BY_DECISIONS |
| EXE-027 | Attachment/media URL policy implementation | DEC-031, DEC-062, DEC-067 | LOCKED_BY_DECISIONS |
| EXE-028 | Brand/entity consistency implementation | DEC-053 | LOCKED_BY_DECISIONS |
| EXE-029 | Sitewide sitemap reconciliation | DEC-025, DEC-026, DEC-028–DEC-031 | LOCKED_BY_DECISIONS |
| EXE-030 | Final sitewide technical/content/link/schema regression | all implemented scope decisions, DEC-069 | LOCKED_BY_DECISIONS |

## Promotion rule

To promote an item from `LOCKED_BY_DECISIONS` to `READY_FOR_TASK`:

1. every listed blocking Decision ID must be `ACCEPTED`;
2. exact scope and target state must be written;
3. active conflicting changes must be checked;
4. FAMILY/SITEWIDE work must have a Change Dossier;
5. canary/regression and rollback must be explicit;
6. final copy must be approved if the item writes visible content;
7. current Production state must be rechecked when the Codex task is issued.

## Task generation rule

When an item becomes `READY_FOR_TASK`, ChatGPT writes a Codex task that cites:

- `Execution ID`
- accepted `Decision IDs`
- finding IDs
- MASTER-TODO IDs
- current HEAD
- target entities
- allowed writes
- prohibited writes
- backup
- canary
- regression set
- acceptance criteria
- Codex QA report format
- ChatGPT Final QA gate

No Production task may be issued from a candidate package that is still `LOCKED_BY_DECISIONS`.
