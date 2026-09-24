# ChatGPT Second Review v1.0

## Goal

یک audit مستقل + reconcile گزارش Codex.

## Step A — Independent Review First

تا حد ممکن قبل از تکیه بر conclusions Codex:

- live URL
- current HTML/metadata/schema
- dossier identity/baseline
- current SERP/intent where relevant
- public evidence

را بررسی و Independent Notes ثبت کن.

## Step B — Review Codex Findings

گزارش Codex را کامل بخوان و برای هر finding:

- CONFIRM
- MODIFY
- REJECT
- NEEDS_MORE_EVIDENCE

ثبت کن.

## Step C — Content / Intent Research

طبق `docs/CONTENT-RESEARCH-SPEC.md`:
- intent
- query evidence
- SERP composition
- information gaps
- unique value
- cannibalization
- LLM readability

## Step D — Reconcile

- additional findings
- systemic refs
- final severity/scope
- acceptance criteria
- Target State

## Approval Gate

فقط اگر:
- evidence کافی
- blockers روشن
- Target State مشخص
- facts verified
- systemic dependencies identified

آنگاه:
`SECOND_REVIEWED → APPROVED`

در غیر این صورت همان SECOND_REVIEWED + blocker باقی بماند.
