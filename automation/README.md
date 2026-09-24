# Autonomous Round-1 SEO Runner v2.2 — Low Consumption

Round 1 remains strictly read-only on Production and can advance only to CODEX_AUDITED.

## Consumption model

The runner now separates deterministic collection from model reasoning:

- Python collects reusable public HTTP/HTML evidence once.
- The autonomous model defaults explicitly to `gpt-5.6-luna` instead of an account-default model; Foundation and page batches both use medium reasoning.
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
- All autonomous model calls use GPT-5.6 Luna with medium reasoning.

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


## Always load the latest runner before autonomous work

Use `automation/run_latest.sh` for `auto`, `resume`, and `prepare`. It fast-forwards `main`, validates the exact updated runner without creating bytecode artifacts, and only then starts Python. This avoids the self-update trap where a long-running Python process pulls a newer runner file but continues executing the old in-memory code.

Examples:

    automation/run_latest.sh prepare --push
    automation/run_latest.sh resume --push
    automation/run_latest.sh auto --push

The systemd oneshot ExecStart is also pinned to this launcher by the v2 installer.
