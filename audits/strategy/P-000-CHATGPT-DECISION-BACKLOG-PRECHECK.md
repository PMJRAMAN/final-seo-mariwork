# P-000 — ChatGPT Decision Backlog Precheck

**Date:** 2026-09-25  
**Baseline before P-001:** Decision Backlog contains 73 decisions (`DEC-001`–`DEC-073`)  
**Mode:** repository review only  
**Production writes:** 0  
**Authority:** preliminary coverage check; not a backlog freeze and not an implementation authorization

## Executive result

The current 73-item Decision Backlog is a strong first structure but is **not yet ready to be frozen as the exhaustive implementation-governance source**.

A second independent coverage audit is warranted before collaborative decision sessions begin in earnest.

The reason is not that the existing decisions are wrong. The problem is that several repository workstreams contain material choices that are either:

- only implicit inside a broad Decision item;
- represented in MASTER-TODO / strategy/spec documents but not obviously mapped to an atomic Decision;
- currently represented only as a future QA item even though a target-state policy must exist before QA;
- or spread across technical/content/media strategy documents without a single traceable decision mapping.

## Preliminary material gaps / atomicity risks observed

These are **areas to challenge**, not final missing-decision conclusions.

### Technical crawl / URL controls

Current backlog should be checked for explicit enough coverage of:

- HTTP/HTTPS/www preferred-host normalization;
- trailing-slash / future URL normalization;
- sitewide canonical architecture beyond individual Store parameters;
- robots.txt crawl-control policy;
- meta robots versus X-Robots-Tag ownership/policy;
- blocked-but-indexable prevention;
- HTTP status lifecycle including 404 / 410 / soft-404 / 5xx;
- redirect quality rules beyond redirect technical ownership;
- sitemap hygiene / lastmod policy beyond family membership;
- JS/AJAX critical-content and crawlable-link discoverability;
- visible breadcrumb/navigation hierarchy versus Breadcrumb structured data;
- global header/footer/navigation link policy;
- crawler access/WAF treatment for Googlebot and OAI-SearchBot, distinct from GPTBot/ChatGPT-User;
- mobile/Page Experience/Core Web Vitals strategy;
- final concern-by-concern SEO ownership matrix.

### WooCommerce / Product data

Check explicit policy coverage for:

- SKU / brand / GTIN / MPN / identifier source of truth;
- price / sale / discount / availability source of truth;
- visible Woo facts versus Product/Offer schema consistency;
- shipping/returns data and schema where applicable;
- reviews/ratings/social-proof schema boundaries;
- out-of-stock versus discontinued product lifecycle;
- future product URL/slug policy.

### Editorial / trust

Check atomic coverage for:

- H2/H3 and content hierarchy by family;
- article author/reviewer/datePublished/dateModified policy;
- factual source/citation/trust policy for technical or safety claims;
- FAQ visible-content versus FAQ schema policy;
- Stores-address/local-search/location/NAP role;
- cannibalization resolution policy;
- commercial CTA policy inside informational Article/Academy content.

### Images

`DEC-058` is video-related, while image strategy still needs checking for atomic decisions around:

- filename/media naming;
- primary/representative image;
- product gallery consistency;
- duplicate/reused image handling;
- captions/surrounding context/linked-image behavior;
- dimensions/formats/srcset/lazy loading/LCP;
- image discovery/sitemap where applicable.

### Video

Current `DEC-058` appears intentionally broad and should be tested for possible split into:

- title/description/naming;
- thumbnail;
- transcript/summary/key text;
- player/embed/fetchability/prominence;
- duplicate/orphan handling;
- host-page relationship.

`DEC-038` already covers VideoObject eligibility/ownership and should not be duplicated.

### Brand / Entity

Current `DEC-053` is broad. Check whether separate decisions are needed for:

- canonical brand facts registry;
- branded query/landing-page map;
- brand spelling/naming consistency;
- Organization/logo/site-name/contact facts;
- founder/history/person entity treatment;
- off-site entity references.

### Deferred expansion programs

`DEC-071`, `DEC-072` and `DEC-073` are umbrella/deferred decisions.

Check whether they may safely remain umbrellas until their program begins or whether child decisions must already be represented for governance completeness:

- External PR / paid link attributes / publisher / landing-page policy;
- Merchant Center / feed route;
- feed product identity and variant mapping;
- feed price/availability/image/landing consistency;
- genuine reviews/social-proof collection/display/schema.

### Monitoring / maintenance

Check whether `DEC-069` is sufficiently atomic for:

- change annotations/release isolation;
- monitoring cadence;
- success/iterate/rollback interpretation;
- plugin/Rank Math regression after updates;
- Google documentation change review;
- content freshness queue;
- new URL/404/systemic-finding discovery.

## Why P-001 is necessary

The project owner intends the final Decision Backlog to be the basis from which the Execution Backlog and Codex Production tasks are derived.

Because of that authority, a false negative (missing decision) is more costly than doing one additional repository-only coverage audit now.

P-001 therefore asks Codex to independently map:

- MASTER-TODO;
- SYS findings;
- SR-004/SR-005;
- technical audit spec;
- strategy documents;
- current families;
- page dossiers;
- Execution Backlog dependencies

against every Decision ID.

Codex must not edit the authoritative Decision Backlog. ChatGPT P-002 will independently review its proposed gaps before any new authoritative DEC IDs are created.

## Current gate

- Decision Backlog freeze: **NO**
- Execution Backlog unlock: **NO**
- Broad Production implementation: **NO**
- Next step: execute `tasks/P-001-DECISION-BACKLOG-COVERAGE-AUDIT.md`, then ChatGPT P-002 review.
