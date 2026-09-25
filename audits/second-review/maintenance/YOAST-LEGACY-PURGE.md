# DB-SEO-001 — Yoast Legacy Database Purge

## Decision

The project intentionally reset SEO ownership from Yoast SEO to Rank Math without importing Yoast metadata or configuration. Historical Round-1/GSC evidence remains immutable in Git and was not used as a migration source.

## Pre-flight

- Database: `mariwork_reco`, prefix `wp_`
- Rank Math: active, version `1.0.279`
- Yoast active: **NO**
- Yoast plugin files/extensions present: **NO**
- Repository HEAD before: `b82ee481e8e0458b44ce7bd54cd490f6d7fdb508`
- Production reachable: **YES**
- Concurrent SEO maintenance process: **NONE**

## Inventory and reviewed scope

- Dedicated Yoast tables: **0**
- Confirmed Yoast postmeta rows: **0**
- Confirmed Yoast termmeta rows: **0**
- Confirmed Yoast usermeta rows: **0**
- Confirmed Yoast options/transients: **0**
- Database size before: **495.19 MB**

The reviewed machine-readable plan is `yoast-purge-plan.json`. It contains zero destructive targets because no confirmed Yoast-owned database data remained. No `DELETE` or `DROP` statement was executed.

Six option names containing `wpseo_editor`/`wpseo_manager` were retained as `SKIP_UNKNOWN`: they are prefixed by Reward Points namespaces (`rewardpoints_` / `rs_reward_`) and represent capability-role settings, not confirmed Yoast ownership.

## Backup

A restricted Yoast-only logical backup was created before the maintenance decision:

- Path: `/home/mariwork/migration-audits/yoast-legacy-purge-20260925-114840/backup/yoast-owned-only.sql.gz`
- Size: 195 bytes
- SHA-256: `f93fccba6819073ffa9ee4e23d7e26c5439e214ae8b8b888fba48f09bbfee383`
- Confirmed Yoast rows included: 0

The SQL backup contains no credentials, private values, Rank Math data or ambiguous options.

## Code dependency review

No active custom-code dependency on Yoast runtime/data was found. Active Blocksy contains conditional Yoast breadcrumb compatibility branches; Duplicate Post and LearnDash contain generic `wpseo_editor`/`wpseo_manager` capability strings. These are retained as expected non-database references because Yoast is inactive and no data access dependency is active.

## Post-maintenance verification

- Dedicated Yoast tables: **0**
- Confirmed Yoast postmeta/termmeta/usermeta/options/transients: **0**
- Ambiguous retained records: **6**
- Unexpected Yoast leftovers: **0**
- Database size after: **495.19 MB**
- Tables dropped: **0**
- Rows removed: **0**

Representative public GET regression checked Homepage, Shop, variable Product, simple Product, Product Category, Article, Academy and Lesson. HTTP, final URL, title, meta description, canonical, robots and JSON-LD summaries were unchanged: **PASS**.

Rank Math data was not modified. No WordPress content, products, variations, terms, users, orders, customers, LearnDash data or Mariwork custom data was modified.

## Future policy

Yoast is `HISTORICAL_PRE_MIGRATION`. Rank Math is the current SEO owner and implementation layer where capability is appropriate. Missing Yoast metadata must not be treated as a current SEO defect or migration gap.
