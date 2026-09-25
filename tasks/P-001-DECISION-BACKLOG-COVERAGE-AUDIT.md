# P-001 — Independent Decision Backlog Coverage Audit

## Mode

**REPOSITORY AUDIT / PRODUCTION READ-ONLY**

This is a decision-governance coverage audit.

The purpose is to determine whether `strategy/DECISION-BACKLOG.md` is complete, sufficiently atomic, correctly categorized and dependency-safe to become the basis for all future Mariwork SEO Production implementation.

This task does **not** make SEO decisions.
This task does **not** approve target states.
This task does **not** modify Production.

Maximum lifecycle authority: `CODEX_AUDITED`.

---

## 1. Primary question

Answer this rigorously:

> If Mariwork uses the current Decision Backlog as the only source from which future SEO implementation packages are unlocked, is every material technical, content, taxonomy, schema, media, crawl/index, migration, brand/entity and measurement decision represented at the correct level of granularity?

The answer must be based on the repository, not generic SEO checklists alone.

---

## 2. Mandatory reading

Read first:

- `MANIFEST.md`
- `AGENTS.md`
- `MASTER-TODO.md`
- `STATUS.md`
- `docs/DECISIONS.md`
- `docs/DECISION-TO-EXECUTION-GOVERNANCE.md`
- `docs/CHANGE-CONTROL.md`
- `docs/WORKFLOW.md`
- `docs/SEO-OWNERSHIP.md`
- `docs/SEO-PLAYBOOK.md`
- `docs/SITEWIDE-TECHNICAL-AUDIT-SPEC.md`
- `docs/CONTENT-RESEARCH-SPEC.md`
- `docs/MEASUREMENT-SPEC.md`
- `docs/QA-SPEC.md`

Current decision/execution authorities:

- `strategy/DECISION-BACKLOG.md`
- `tasks/EXECUTION-BACKLOG.md`

Current strategy documents:

- `strategy/CONTENT-ARCHITECTURE.md`
- `strategy/QUERY-MAP.md`
- `strategy/INTERNAL-LINK-ARCHITECTURE.md`
- `strategy/INTERNAL-LINK-REQUIREMENT-MATRIX-DRAFT.md`
- `strategy/VISUAL-IMAGE-SEO.md`
- `strategy/VIDEO-SEO.md`
- `strategy/BRAND-ENTITY-SEARCH.md`
- `strategy/EXTERNAL-PR-STRATEGY.md`

Second Review / closure:

- `audits/second-review/store/SR-004-CHATGPT-STORE-SECOND-REVIEW.md`
- `audits/second-review/sitewide/SR-005-CHATGPT-FULL-SITE-SECOND-REVIEW.md`
- `audits/sitewide/PRE-IMPLEMENTATION-AUDIT-CLOSURE.md`
- `audits/sitewide/PRE-IMPLEMENTATION-COVERAGE-MATRIX.json`
- `handoff/FULL-SITE-PRE-IMPLEMENTATION-SECOND-REVIEW-HANDOFF-2026-09-25.md`

Current evidence registries:

- `registry/SYSTEMIC-FINDINGS.md`
- `registry/URL-INVENTORY.csv`
- `audits/second-review/reconciliation/current-entity-census.json`
- `audits/sitewide/SYSTEM-URL-SPACES-CLOSURE.md`
- `audits/sitewide/IMAGE-ALT-AUDIT-SUMMARY.md`

Also scan all canonical page dossiers under `pages/**`, but do not re-audit every page manually. Use deterministic parsing/search to extract:
- unresolved findings;
- target-state/TBD statements;
- blockers;
- recurring decision topics;
- family-specific exceptions.

---

## 3. Repository baseline

Before work record:

```bash
git status -sb
git log -5 --oneline
git rev-parse HEAD
```

Expected current branch: `main`.

Do not reset, rebase or discard changes.

If remote has advanced, fast-forward only if safe and record the actual baseline.

---

## 4. Production safety

Expected Production path:

`/home/mariwork/web/mariwork.ir/public_html`

Production writes: **0**

Do not:

- edit WordPress;
- write database/options/meta/content;
- modify Rank Math;
- edit theme/plugin/server configuration;
- purge cache;
- create redirects;
- change sitemap/robots/canonical;
- test real cart/order/checkout/login state;
- collect PII/secrets.

Production should only be consulted read-only if a repository contradiction cannot be classified without a current-state verification.

This is primarily a repository governance audit.

---

## 5. Independent anti-anchoring rule

Do not assume the current 73 Decision IDs are complete merely because ChatGPT created them.

Do not assume every Decision ID is necessary merely because it exists.

Challenge the backlog in both directions:

1. **Missing decisions**
2. **Over-broad decisions**
3. **Duplicate/overlapping decisions**
4. **Items that are not decisions at all and belong to execution/QA/evidence collection**
5. **Dependencies not represented**
6. **Deferred decisions that would actually block earlier implementation**
7. **Existing accepted process rules that should not be duplicated as new decisions**

Do not edit the authoritative Decision Backlog in this task.

---

## 6. Build a source-to-decision coverage matrix

Create a machine-readable matrix mapping every material source requirement to zero or more Decision IDs.

Required source classes:

### A. MASTER-TODO

Map every material strategy/target-state item in Programs:

- B Store/WooCommerce
- C Homepage
- D Static/Core
- E Blog/Articles
- F Academy/Education
- G Artists/History/custom content
- H Taxonomies/Archives/System URLs
- I Final validation, where the item implies a prior policy decision
- J Monitoring, where the item implies a monitoring-policy decision
- K External PR
- L Visual/Image
- M Video
- N Brand/Entity
- O Merchant/feed/reviews
- P Strategy Decision Coverage / Freeze

Pure implementation/QA/checklist items should be classified as such rather than forced into a DEC ID.

### B. Systemic findings

Map every active/relevant:

- `SYS-001` through current latest SYS ID

For each finding determine whether it:
- already has an accepted framework rule;
- requires one or more target-state decisions;
- is execution-only;
- is evidence-only;
- is historical/superseded.

### C. Second Review target states

Map every material:

- `SR-ST-*` in SR-004
- section/target recommendation in SR-005

No Second Review recommendation may remain implementation-relevant but unmapped.

### D. Technical Audit Specification

Explicitly cover all domains in `SITEWIDE-TECHNICAL-AUDIT-SPEC.md`:

- robots.txt
- meta robots
- X-Robots-Tag
- blocked/indexable risk
- preferred host/protocol
- trailing-slash / URL normalization
- canonical architecture
- redirects
- 4xx/5xx
- soft-404
- sitemap membership
- sitemap lastmod where used
- facets
- parameters
- pagination
- search
- feeds
- attachments
- JS/AJAX discoverability
- structured data
- WooCommerce product/variation/bundle architecture
- identifiers
- price/currency
- availability
- reviews
- shipping/returns where applicable
- images/media
- mobile/CWV/page experience
- crawler/WAF access
- Googlebot
- OAI-SearchBot versus GPTBot/ChatGPT-User
- Rank Math ownership by concern

A technical domain may legitimately map to an accepted process rule rather than a new DEC, but this must be explicit.

### E. Content Research / Editorial

Check decision coverage for:

- intent/page role
- title
- H1
- H2/H3/content hierarchy
- meta description
- factual accuracy
- freshness
- author/reviewer/date
- sources/citations/trust
- CTA/commerciality on informational content
- Article vs Academy boundary
- Product vs Category vs Article boundary
- duplicate/cannibalization handling
- FAQ
- brand facts
- store/location content
- internal links
- anchor text
- external/outbound links where policy is material

### F. Visual/Image

Cross-check every Required Decision in `strategy/VISUAL-IMAGE-SEO.md` and MASTER-TODO L:

- informative/decorative role
- ALT
- filename/media naming
- representative/primary image
- gallery consistency
- duplicate/reused image
- captions/surrounding context
- linked-image behavior
- dimensions/formats/srcset
- lazy loading/LCP
- image discovery/sitemap if applicable
- family exceptions
- monitoring

### G. Video

Cross-check every area in `strategy/VIDEO-SEO.md` and MASTER-TODO M:

- inventory identity
- host-page relationship
- crawl/discoverability
- title/description/naming
- thumbnail
- surrounding text
- transcript/summary
- player/embed source
- prominence/fetchability
- VideoObject eligibility/ownership
- internal links
- duplicate/orphan video handling
- target state
- monitoring

### H. Brand / Entity

Cross-check `strategy/BRAND-ENTITY-SEARCH.md` and MASTER-TODO N:

- canonical brand name/spelling
- factual brand registry
- founder/history facts
- logo/site-name/contact facts
- branded query/landing-page strategy
- schema ownership
- naming consistency
- trust pages
- off-site references
- external PR relationship
- monitoring

### I. Store / Product data

Ensure explicit decision coverage, where applicable, for:

- visible product naming
- Rank Math title template
- product meta
- product content modules
- categories
- attributes
- product tags
- variations
- bundles
- Product/ProductGroup/Offer
- SKU/identifier/brand source
- price/availability/sale/discount source
- shipping/returns
- reviews/ratings
- product image/gallery
- out-of-stock versus discontinued-product lifecycle
- future product URL/slug policy
- variant/preselection URLs
- Store search/facets/pagination
- sitemap/canonical/indexability

### J. Migration / URL lifecycle

Check:

- 301 vs 404 vs 410 decision rules
- redirect semantic relevance
- direct redirect / no chain rule
- old Product volume URLs
- Education → Academy
- Artists/removed content
- future slug changes
- preserving historical metrics
- replacement mapping
- migration QA/monitoring

### K. Measurement / rollout

Check:

- canary scope
- release isolation/change annotations
- baseline windows
- 28/56-day monitoring
- success/iteration/rollback interpretation
- confounders
- new URL discovery
- new 404s
- Rank Math/plugin update regression
- Google documentation changes
- content freshness queue
- schema/price consistency sampling

### L. Expansion programs

Check whether broad deferred decisions are too coarse for future governance:

- External PR / advertorial
- Merchant Center / Free Listings
- product feed architecture
- reviews/social proof

It is valid to keep them deferred, but the audit should state whether one umbrella Decision ID is sufficient now or whether child decisions should already exist.

---

## 7. Coverage classifications

Each matrix row must use exactly one primary classification:

- `COVERED_EXACT`
- `COVERED_BY_ACCEPTED_RULE`
- `COVERED_BY_UMBRELLA_DECISION`
- `DECISION_TOO_BROAD`
- `MISSING_DECISION`
- `DUPLICATE_DECISION`
- `EXECUTION_ONLY`
- `QA_ONLY`
- `EVIDENCE_COLLECTION_ONLY`
- `HISTORICAL_SUPERSEDED`
- `INTENTIONALLY_DEFERRED`
- `NOT_APPLICABLE_TO_CURRENT_SITE`

Never call something covered merely because a vaguely related DEC exists.

---

## 8. Decision atomicity test

A Decision item is sufficiently atomic only if the owner and ChatGPT can discuss it and produce one unambiguous target state without silently making multiple unrelated choices.

Flag a Decision as `DECISION_TOO_BROAD` when, for example, it combines several independently selectable policies such as:

- filename + ALT + image performance;
- video thumbnail + transcript + host-page architecture;
- Merchant Center + product feed + variant identity;
- brand facts + branded SERP + external entity references;
- monitoring cadence + rollback threshold + technical regression policy.

Do not split items merely for cosmetic reasons.

---

## 9. Family completeness invariant

For every durable/current family, determine which of these dimensions are applicable and whether each maps to a Decision or accepted rule:

- role / intent;
- indexability;
- URL/canonical;
- sitemap;
- title;
- meta description;
- H1/headings;
- visible content architecture;
- structured data;
- technical owner;
- internal links;
- media/image;
- video where present;
- trust/factual-source requirements;
- lifecycle/migration;
- QA/monitoring.

Families include at least:

- Homepage
- Shop
- Fabric-color products
- Sets/Bundles
- Mediums/Additives
- Tools/Accessories
- other Products
- durable Product Categories
- `pa_volume`
- Product Tags
- Magazine
- Articles
- durable Blog Categories
- Blog Tags
- Academy Course
- Academy Lessons
- LearnDash taxonomies
- About / Why Mariwork
- Contact
- Stores address
- FAQ
- Login / Fast Buy
- Cart / Checkout / My Account
- system/archive/machine URL spaces
- historical/legacy URLs
- Images
- Videos
- Brand/Entity

Mark a dimension `NOT_APPLICABLE` instead of inventing work.

---

## 10. Decision dependency audit

Build a dependency graph for the current Decisions.

Identify:

- Decisions that must precede others.
- Circular dependencies.
- Decisions that can be made independently.
- Decisions that block cross-family Internal Linking.
- Decisions that block sitemap/indexability.
- Decisions that block schema.
- Decisions that block content writing.
- Decisions that block migration.
- Decisions that block the first Production canary.

Do not modify statuses.

---

## 11. Execution Backlog reconciliation

Review `tasks/EXECUTION-BACKLOG.md`.

For each EXE item determine:

- Are all material blocking decisions listed?
- Is it missing a decision dependency?
- Does it depend on an over-broad DEC?
- Is an EXE package too broad and likely to combine unrelated writes?
- Are there likely future implementation packages with no EXE placeholder at all?

Do not unlock any EXE item.

---

## 12. Do not create false decisions

Not every audit observation deserves a Decision ID.

Do not propose a new Decision for:

- deterministic QA steps;
- backup commands;
- simple before/after checks;
- an already accepted immutable project rule;
- purely historical evidence with no current/future target-state choice;
- a one-off implementation detail that belongs inside a future approved task.

The goal is **complete governance**, not maximum decision count.

---

## 13. Required outputs

Create directory if needed:

`audits/strategy/`

Create:

### A. `audits/strategy/DECISION-BACKLOG-COVERAGE-AUDIT.md`

Include:

1. Executive verdict:
   - `COMPLETE`
   - `COMPLETE_WITH_MINOR_GAPS`
   - `NOT_READY_FOR_FREEZE`

2. Current DEC count.

3. Source coverage summary.

4. Material missing decisions.

5. Over-broad decisions needing split.

6. Duplicate/merge candidates.

7. Decisions that are actually execution/QA/evidence items.

8. Deferred programs assessment.

9. Family completeness assessment.

10. Technical-domain completeness assessment.

11. Content/media completeness assessment.

12. Execution Backlog dependency findings.

13. Recommended session grouping.

14. Freeze blockers.

### B. `audits/strategy/decision-source-coverage-matrix.json`

Each row should include:

```json
{
  "source_type": "MASTER_TODO|SYS_FINDING|SECOND_REVIEW|TECH_SPEC|STRATEGY|FAMILY|PLAYBOOK|OTHER",
  "source_ref": "...",
  "topic": "...",
  "applicable": true,
  "decision_ids": ["DEC-..."],
  "classification": "COVERED_EXACT|...",
  "reason": "...",
  "materiality": "P0|P1|P2|P3",
  "notes": "..."
}
```

### C. `audits/strategy/decision-dependency-graph.json`

Record:

- Decision ID
- prerequisites
- unlocks
- family
- cross-family yes/no
- current status
- dependency issue if any

### D. `audits/strategy/PROPOSED-DECISION-BACKLOG-CHANGES.md`

This file is a proposal only.

Use candidate IDs:

- `CAND-001`
- `CAND-002`
- etc.

For each candidate:

- action: `ADD | SPLIT | MERGE | REWORD | RECLASSIFY | KEEP_AS_IS`
- affected DEC IDs if applicable
- proposed title
- reason
- source references
- suggested scope
- suggested initial status
- dependency notes
- why this is a real decision instead of execution/QA

Do **not** allocate new authoritative `DEC-###` IDs.

### E. `handoff/DECISION-BACKLOG-COVERAGE-HANDOFF-2026-09-25.md`

Keep concise.

Include:

- HEAD before
- HEAD after
- current DEC count
- exact-covered count
- umbrella-covered count
- missing decision candidate count
- over-broad decision count
- duplicate/merge candidate count
- execution-only/QA-only classifications
- freeze verdict
- top freeze blockers
- confirmation Production writes = 0
- recommended next step = ChatGPT P-002 review

---

## 14. Repository write boundaries

Allowed repository writes:

- the four audit/handoff artifacts above.

Do not modify:

- `strategy/DECISION-BACKLOG.md`
- `tasks/EXECUTION-BACKLOG.md`
- `docs/DECISIONS.md`
- `MANIFEST.md`
- `AGENTS.md`
- existing page dossiers
- existing Second Review files
- raw data
- Production

The point is to preserve independence before ChatGPT P-002 reconciliation.

---

## 15. Efficiency

Do not use one model call per dossier.

Prefer deterministic scripts to:

- enumerate files;
- extract headings/TBD/decision/finding references;
- enumerate MASTER-TODO items;
- enumerate SYS findings;
- enumerate SR-004/SR-005 recommendations;
- enumerate current DEC/EXE IDs;
- build the initial mapping.

Use reasoning for classification and gap analysis only.

Do not recrawl the whole live site.

---

## 16. Completion criteria

P-001 is complete only when:

- every material MASTER-TODO strategy/policy item has a classification;
- every current SYS finding has a classification;
- all SR-004/SR-005 target-state recommendations have a classification;
- all technical audit domains have a classification;
- all current durable families pass the applicable-dimension check or have explicit gaps;
- Image, Video, Brand, PR, Merchant/feed and Review programs are checked;
- over-broad DEC items are identified;
- missing decisions are proposed without editing the authoritative backlog;
- EXE dependency coverage is checked;
- no Production write occurred;
- the handoff is ready for ChatGPT P-002.

## 17. Final report

Return only a concise summary plus paths to the generated artifacts and:

- actual HEAD before;
- actual HEAD after;
- freeze verdict;
- number of missing decision candidates;
- number of over-broad decisions;
- number of duplicate/merge candidates;
- number of EXE dependency gaps;
- Production writes = 0.
