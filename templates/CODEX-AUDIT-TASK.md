# Codex Page Audit Task v1.0

## Mode
**AUDIT ONLY — PRODUCTION READ-ONLY**

## Required Reading
- MANIFEST.md
- docs/DECISIONS.md
- AGENTS.md
- docs/WORKFLOW.md
- docs/AUDIT-SPEC.md
- docs/DATA-SOURCES.md
- docs/SITEWIDE-TECHNICAL-AUDIT-SPEC.md
- registry/SYSTEMIC-FINDINGS.md
- relevant dossier(s)

## Batch
Batch ID:  
Type: PILOT / FAMILY / OPPORTUNITY / VALIDATION

Pages:
1.
2.
3.
4.
5.

## Planning Reference

Master TODO task/program ID:  

## Goal

برای هر page وضعیت واقعی را audit کن و dossier را تا `CODEX_AUDITED` تکمیل کن.

**No Production writes.**

## Mandatory Sources Where Available

- public URL + initial HTML
- redirect/canonical/index controls
- WP/Woo read-only data
- JSON-LD/microdata
- images/media
- internal links
- relevant server code
- GSC snapshot
- Coverage/Indexing snapshot
- legacy URL evidence
- sitewide systemic findings

## Data Rule

Queries.csv و Pages.csv را join معنایی نکن.

اگر Page+Query نداریم:
`Page-query relationship is not proven by the current export.`

## Findings

ID + severity + scope + evidence class + confidence + source refs + impact + recommendation + acceptance criteria.

اگر مشترک:
- systemic registry reference/create
- root cause candidate
- no repeated manual fix strategy

## Content

Audit کن، ولی Production copy ننویس/اعمال نکن مگر task جداگانه draft بخواهد.

Fact اختراع نکن.

## Stop Conditions

نیاز به write/purchase/destructive test → انجام نده؛ blocker/hypothesis ثبت کن.

## Completion

- dossier status = CODEX_AUDITED
- batch summary
- systemic findings update
- no APPROVED status
- no Production change


## Google / Rank Math Requirements

برای findings فنی/محتوایی مهم:
- Google basis/reference ثبت کن.
- توصیه vendor را به Google نسبت نده.
- Rank Math capability و owner را برای concerns مرتبط audit کن.
- اگر Rank Math capability دارد، recommendation باید Rank Math-first باشد.
- custom PHP پراکنده پیشنهاد نده.
