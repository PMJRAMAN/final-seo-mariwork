# P-010 — Final Decision-to-Execution Integrity Audit

> **Recovered provenance record — 2026-09-26.**
> The original P-010 report was produced in a divergent/local history and its reported commit `c9b306061f8512d7cf0cda92dd9f2a0af64228b9` is not reachable through the connected GitHub repository. This file restores the durable audit path and the material findings from the owner-provided original report. It is a provenance recovery summary, not a claim that the unreachable original commit was merged or rewritten.

**Original audit mode:** repository-only, Production read-only  
**Original audited HEAD:** `8aa37b466186d748cae243225aed4f54537f99f8`  
**Original reported commit:** `c9b306061f8512d7cf0cda92dd9f2a0af64228b9` (unreachable in connected GitHub history)  
**Original verdict:** `FAIL_STAGE_6_NOT_SAFE`

## Original inventory

- Decision rows: **129**
- Decision range: `DEC-001`–`DEC-130`
- Unused ID: `DEC-126`
- EXE packages at audit baseline: **57**
- Repository labels: **16 READY_FOR_TASK / 41 BLOCKED**
- Confirmed accepted-Decision coverage gaps: **0**
- Orphan Decisions: **0**
- Orphan EXEs: **0**

## Material findings preserved from the original report

| ID | Severity | Finding |
|---|---|---|
| F-01 | HIGH | EXE-013–015 still carried a stale canonical-spelling prerequisite even though DEC-007–009/053 had already reconciled canonical `ماری‌ورک`; factual/canary gates remained real. |
| F-02 | HIGH | EXE-034 and EXE-048 both claimed VideoObject/schema implementation without a single per-output write owner. |
| F-03 | HIGH | DEC-130 archive/hub visible-content writes overlapped across EXE-012/019/020/030/035. |
| F-04 | HIGH | EXE-009 and EXE-049 overlapped on OAI-SearchBot/AI crawler eligibility/control and needed technical-control vs AI-eligibility separation. |
| F-05 | HIGH | READY EXE-005/007/009/011 were broad enough that an evidence task could drift into Production mutation without an explicit second gate. |
| F-06 | MEDIUM | Historical/current Decision range text still stated DEC-001–120 despite current rows extending through DEC-130. |
| F-07 | INFO | DEC-126 was never a real Decision row in available history and should remain unused/reserved; no renumbering. |
| F-08 | MEDIUM | `docs/DECISIONS.md` repeated several historical Decision headings and needed explicit current-authority parsing guidance. |
| F-09 | MEDIUM | MASTER contained stale Product naming text; non-pa_volume attribute discovery lacked a named EXE; D-005 needed a discovery disposition. |
| F-10 | MEDIUM | Wave 2/3 blocker-closure and Wave 4 implementation lanes lacked a sufficiently explicit milestone boundary. |
| F-11 | LOW | EXE-057 needed a versioned completed-package/Decision/Lock manifest before final regression. |
| F-12 | MEDIUM | EXE-054 verification could precede EXE-052, but redirect mutation needed the EXE-052 baseline and URL-specific disposition. |
| F-13 | MEDIUM | EXE-046 required an owner-approved future-upload implementation design; Codex could not choose the enforcement path. |
| F-14 | HIGH | DEC-003/007/009/014/016 contained unescaped pipes in Markdown table cells and could be misparsed. |

## Original readiness revalidation

The original independent review confirmed a subset of READY items, identified EXE-005/007/009/011 as requiring clarification/evidence-first boundaries, and found the EXE-013–015 spelling blocker stale while retaining their real factual/canary blockers.

## Original conclusion

No accepted Decision was an unexplained orphan. The failure was **execution-integrity**, not strategy coverage: overlapping write ownership, evidence-to-mutation ambiguity, stale gates and parser/documentation integrity made broad Stage-6 task generation unsafe.

P-011 was created to reconcile these findings.

## Provenance note

The owner later supplied the original report artifact in the ChatGPT project. P-013 restored this repository path without resetting, force-moving or rewriting `main`. For current planning authority use the authoritative Decisions/Locks/Execution Backlog; this file is audit evidence only.
