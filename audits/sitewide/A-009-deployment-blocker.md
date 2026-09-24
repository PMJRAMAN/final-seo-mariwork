# A-009 Deployment Check — Blocked by Runtime Isolation

**Date:** 2026-09-24  
**Result:** SETUP INCOMPLETE — autonomous execution was not started

## Verified setup state

- Repository: `/home/mariwork/Final-SEO-Codex`
- Branch and starting HEAD: `main`, `4f4f229eb7458407992b50ef0af39289c2458deb`
- Remote: `https://github.com/PMJRAMAN/final-seo-mariwork.git`
- Python: 3.10.12
- Codex CLI: 0.156.1
- Runner syntax: PASS (`python3 -m py_compile automation/seo_audit_runner.py`)
- Runner status: PASS; it read the plan and Master TODO. The URL inventory currently has a header only, so it reported zero page entities.
- Runtime directories were created at `/root/.local/state/mariwork-seo-runner/`, outside the repository.
- Git push authentication check: `git push --dry-run origin main` succeeded. No A-009 completion commit was pushed.

## CLI compatibility correction

The installed CLI rejects the runner's `--ask-for-approval never` argument with exit code 2. That obsolete argument was removed from `codex_args()`; the remaining `--json`, `--sandbox workspace-write`, and network configuration flags are accepted by the installed CLI's parser/help path. No Codex job was launched to test a real request.

## Blocking security evidence

- This process runs as UID 0 (`root`). The Production `public_html` directory is writable in this context.
- The `mariwork` account can also write to the Production directory.
- `public_html/wp-config.php` is readable by both `mariwork` and the unprivileged `nobody` account. Its contents were not read or copied. This means an unprivileged identity has not been demonstrated that is unable to obtain the site's database credentials.
- The runner launches Codex with network access and has no database-write denial, credential isolation, or secret/PII output scanner. Its prompt and changed-file allowlist do not technically prevent database writes or secret reads.

These conditions fail the A-009 requirements for no sudo/root authority, no Production file writes, and no DB-write credentials. Therefore the A-010 smoke test and autonomous queue were deliberately not run. Production files and the database were not modified.

## Safe remediation required

Provision a dedicated runtime identity with Codex and repository credentials kept in that identity's protected credential store, no sudo privileges, no write access to Production, and no read access to `wp-config.php` or other write-capable database credentials. Deny that identity access to the Production database over both socket and network. Keep Codex confined to its job worktree and pass only required non-secret environment variables. If safe WordPress evidence is unavailable, continue with public HTML and repository data and record `BLOCKED_BY_ACCESS` / `UNKNOWN_NEEDS_VERIFICATION`.

After those controls are independently verified, rerun A-010 smoke validation, changed-file checks, commit/push verification, and only then mark A-009 complete and start `auto --push`.
