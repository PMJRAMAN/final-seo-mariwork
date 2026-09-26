# Decision-to-Execution Governance

**Status:** ACCEPTED PROCESS RULE  
**Effective date:** 2026-09-25  
**Applies after:** Full-site Audit + ChatGPT Second Review  
**Current baseline:** SR-005  
**Production writes authorized by this document:** NO

## 1. Purpose

Mariwork SEO does not move directly from an audit finding to a Production change.

After Audit and Second Review, the project enters a deliberate **Strategy / Decision Phase**. During this phase the owner and ChatGPT review the recorded evidence topic by topic — for example titles, taxonomy policy, metadata, content structure, schema, internal links, images, video and legacy URLs — and explicitly decide the target state.

Only after the required decisions for a scope are accepted may implementation work be converted into an executable backlog and delegated to Codex.

This process exists to prevent:
- contradictory page-by-page changes;
- local optimizations that later conflict with site architecture;
- repeated rework after internal-link/content decisions change;
- Codex inferring business/editorial decisions from audit findings;
- large Production changes before the target state is stable.

## 2. Three planning authorities

### A. Coverage authority — `MASTER-TODO.md`

Answers:

> What areas of the SEO project must eventually be covered?

It controls program completeness and sequencing.

A checked/unchecked MASTER-TODO item does **not by itself authorize a Production write**.

### B. Decision authority — `strategy/DECISION-BACKLOG.md`

Answers:

> What choices must the owner + ChatGPT make before we know the correct target state?

This is the canonical queue for unresolved strategy/target-state decisions.

Every material technical/content decision must be recorded here before implementation when the answer is not already an accepted project decision.

### C. Execution authority — `tasks/EXECUTION-BACKLOG.md`

Answers:

> Which approved changes are now ready to be turned into Codex implementation tasks?

An item may enter the executable state only after all blocking Decision IDs are `ACCEPTED`.

A finding, recommendation, audit checkbox, or Second Review note alone is not an implementation authorization.

## 3. Decision Phase workflow

Work through the Decision Backlog in small coherent topics over multiple sessions.

Recommended session pattern:

1. Select one decision topic or tightly related group.
2. Read the relevant current evidence from GitHub.
3. Re-check current Google/vendor documentation where the decision is time-sensitive.
4. Discuss options, tradeoffs and dependencies.
5. Record the agreed target state.
6. Change the Decision item status.
7. Record consequences and affected families.
8. Do not create a Codex Production task yet unless the required decision set for that implementation scope is complete.

Examples of topics that should normally be decided separately:

- Product title naming standard.
- Rank Math title template.
- Product meta-description strategy.
- Product Category and `pa_volume` index/sitemap policy.
- Product Tags and Blog Tags lifecycle.
- Static-page schema.
- ProductGroup / variation schema.
- Academy / LearnDash schema and video policy.
- Internal-link rules and exact destinations.
- Article vs Academy content roles.
- Image / ALT policy.
- Legacy URL disposition.

The purpose is not to decide everything in one chat. The repository preserves each accepted decision between sessions.

## 4. Decision item lifecycle

Allowed statuses:

- `OPEN` — decision is required and discussion has not reached a target state.
- `DISCUSSING` — actively being worked on by owner + ChatGPT.
- `NEEDS_TARGETED_EVIDENCE` — a small specific evidence gap must be closed before deciding.
- `PROPOSED` — a concrete target state exists but owner approval is pending.
- `ACCEPTED` — owner-approved target state; may unlock execution.
- `DEFERRED` — intentionally postponed and does not currently block unrelated work.
- `REJECTED` — proposed direction was explicitly rejected.
- `SUPERSEDED` — replaced by a later decision.

Codex may collect targeted evidence for an `OPEN`/`NEEDS_TARGETED_EVIDENCE` item only through a read-only task.

Codex cannot set `ACCEPTED`.

## 5. Required fields for every material decision

Each Decision item should identify, where applicable:

- Decision ID.
- Topic.
- Scope: PAGE / FAMILY / SITEWIDE / PROCESS.
- Current status.
- Why a decision is required.
- Evidence references.
- Related finding IDs.
- Current state.
- Options considered.
- ChatGPT recommendation.
- Owner decision.
- Exact target state.
- Affected entities/families.
- SEO owner: RANK_MATH / RANK_MATH_EXTENSION / PLATFORM / CONTENT.
- Google basis and current official reference where applicable.
- Dependencies.
- Exceptions.
- Implementation implications.
- QA / regression implications.

A decision is not `ACCEPTED` if the target state remains ambiguous.

## 6. Strategy lock

When all decisions required for a coherent implementation scope are accepted, create a **Strategy Lock** for that scope.

A Strategy Lock records:

- accepted Decision IDs;
- exact target state;
- unresolved non-blocking items;
- scope boundaries;
- dependencies;
- latest repository HEAD.

The Strategy Lock is the bridge between discussion and implementation planning.

It may cover one family first; the project does not need every future optional workstream decided before an independent approved scope can proceed.

However, cross-family changes such as internal linking must wait until all dependent families have sufficiently stable decisions.

## 7. Execution Backlog generation

The Execution Backlog is generated from accepted decisions, not directly from findings.

Each execution item must include:

- Execution ID.
- Accepted Decision IDs.
- related finding IDs;
- MASTER-TODO references;
- exact affected scope;
- exact intended change;
- technical owner;
- dependencies;
- canary requirement;
- backup/rollback requirement;
- acceptance criteria;
- Codex QA requirement;
- ChatGPT Final Acceptance requirement;
- rollout status.

Allowed execution states:

- `LOCKED_BY_DECISIONS`
- `READY_FOR_TASK`
- `TASK_ISSUED`
- `IMPLEMENTING`
- `CODEX_QA`
- `CHATGPT_FINAL_QA`
- `COMPLETE`
- `BLOCKED`

Only `READY_FOR_TASK` items may be converted into a Codex Production implementation task.

## 8. Codex implementation gate

Before any Codex task with Production writes:

1. The task must reference one or more `ACCEPTED` Decision IDs.
2. It must reference an Execution Backlog item in `READY_FOR_TASK`.
3. Relevant dossier/target state must be approved.
4. FAMILY/SITEWIDE changes require a Change Dossier.
5. Rank Math capability/ownership must be verified for the exact concern.
6. Backup/rollback and acceptance criteria must be explicit.
7. Canary/regression scope must be explicit where applicable.
8. Current Production state must be rechecked immediately before write.

If any blocking decision is still `OPEN`, `DISCUSSING`, `PROPOSED`, or `NEEDS_TARGETED_EVIDENCE`, Codex must not implement that scope.

### Evidence-first READY packages

A `READY_FOR_TASK` package may be ready only for a bounded **read-only evidence task** when current-state evidence is the package's immediate prerequisite.

In that case:

- the task must explicitly say `READ-ONLY / NO PRODUCTION MUTATION`;
- Codex may collect current output, inventory, rendered behavior, configuration evidence and exact affected entities;
- Codex must not convert the same task into an implementation task merely because the evidence reveals a fix;
- any Production mutation requires an exact affected-entity manifest, one unambiguous write owner, capability/ownership verification, rollback/acceptance criteria, and a separately authorized write scope;
- if evidence materially changes the implementation boundary or reveals a new strategy choice, reconcile the Execution Backlog state/gate before a write task is issued;
- two EXEs must never be simultaneous write owners for the same output/concern. Shared evidence is allowed; write ownership must be singular and explicit.

This rule preserves the distinction between `task-ready for evidence` and `authorized for mutation`.

## 9. Content gate

Final visible text is a decision artifact.

Titles, meta descriptions, H1 changes, category introductions, rewritten article sections, product copy and important anchor text must be approved before implementation.

Codex may not turn an audit recommendation into final copy by itself unless the explicit task asks only for a draft; a draft is never automatically executable.

## 10. Internal-link gate

Internal links are not a mechanical post-processing step.

Before large-scale internal-link implementation:

- source/target family roles must be accepted;
- CORE/FAMILY_SPECIFIC/CONTEXTUAL rules must be accepted;
- exact durable destinations must be known;
- mandatory-link exceptions must be defined;
- query anchors must not be invented from unjoined GSC data.

Only then can exact link additions become Execution items.

## 11. No forced all-at-once approval

The Decision Phase is intentionally incremental.

Independent scopes may be strategy-locked and implemented while later independent topics are still being discussed, provided there is no unresolved dependency that can materially change the approved scope.

Example:

- a confirmed Shop H1/meta fix may be ready before historical Artist URL cleanup;
- sitewide contextual internal linking should wait for relevant content-family decisions.

## 12. Repository update rule

A material decision discussed in chat is not durable until it is committed to GitHub.

After each decision session, ChatGPT should update the Decision Backlog and, when appropriate:

- `docs/DECISIONS.md`;
- relevant strategy document;
- page/family target state;
- systemic finding;
- Execution Backlog dependency state.

The repository remains the source of truth.

## 13. Final transition to implementation

Before broad implementation begins:

1. Required Decision items for the chosen rollout scope are `ACCEPTED`.
2. Strategy Lock is recorded.
3. Execution Backlog is populated and ordered.
4. Systemic Change Dossiers are created where required.
5. Exact Codex tasks are generated from `READY_FOR_TASK` items.
6. Implementation proceeds canary-first.
7. Codex QA is performed.
8. ChatGPT Final Acceptance QA is performed.
9. Only then is rollout expanded.

## 14. Relationship to existing framework

This rule is a backwards-compatible clarification of:

- M-02 Analysis Before Write;
- M-07 Systemic Problems Get Systemic Fixes;
- M-11 Traceability;
- M-14 Independent Final QA;
- M-15 Controlled Systemic Rollout;
- M-17 Content Authority;
- SEO-002 Repository as Source of Truth;
- SEO-010 Systemic Changes Need Change Dossier;
- SEO-012 Final Content Requires ChatGPT Approval;
- SEO-015 MASTER-TODO Is the Execution Authority.

It does not change existing lifecycle statuses or human/Codex authority. It separates **coverage**, **decision-making**, and **execution planning** so they cannot be confused.
