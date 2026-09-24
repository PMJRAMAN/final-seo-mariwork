# Autonomous Round-1 SEO Runner v2.1 — Low Consumption

Round 1 remains strictly read-only on Production and can advance only to CODEX_AUDITED.

## Consumption model

The runner now separates deterministic collection from model reasoning:

- Python collects reusable public HTTP/HTML evidence once.
- The autonomous model defaults explicitly to `gpt-6-luna` instead of an account-default model; Foundation uses medium reasoning and page batches use low reasoning.
- A compact deterministic Foundation context pack prevents full rereads of the ~2.7MB inventory and large A-011/A-012 ledgers.
- Page-batch evidence is trimmed before prompting (representative links/images/headings/text only).
- Store-first priority is enforced after the five-page pilot.
- Codex network access is disabled during analysis.
- A-014 + A-015 are grouped into one model call.
- A-016 + A-017 use no model call.
- A-018 + A-019 + A-020 are grouped into one model call.
- A-021 uses no model call.
- The first page pilot is max 5 entities.
- Later page executions default to 15 entities, preferably from one family.
- Product Tags, Blog Tags, attributes, attachments and system/policy URL spaces are excluded from repetitive page-model calls where FAMILY/SITEWIDE policy is the correct coverage mechanism.
- Page batches use low reasoning; Foundation model synthesis uses medium reasoning.

## Commands

Status:

    python3 automation/seo_audit_runner.py status

Build deterministic evidence without consuming Codex model quota:

    python3 automation/seo_audit_runner.py prepare --push

After the Codex usage limit resets:

    python3 automation/seo_audit_runner.py resume --push

The runtime state remains outside Git at:

    ~/.local/state/mariwork-seo-runner/

Do not run the autonomous worker as root.
