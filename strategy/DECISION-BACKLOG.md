# SEO Decision Backlog

**Purpose:** canonical queue of strategy/target-state decisions before Production implementation  
**Authority:** owner + ChatGPT  
**Codex authority:** evidence collection only; Codex cannot mark decisions `ACCEPTED`  
**Baseline:** SR-004 + SR-005 and current audit repository  
**Production implementation authorized by this file:** NO
**Freeze state:** FROZEN_V1_COVERAGE — decision-domain structure complete; target-state decisions remain unresolved

See: `docs/DECISION-TO-EXECUTION-GOVERNANCE.md`.

## Coverage Freeze v1

As of 2026-09-25, P-001 through P-004 found **zero unexplained material decision-domain gaps** after reconciliation.

This freeze applies only to the **coverage/structure of the decision queue**.

It does not accept any OPEN / PROPOSED / NEEDS_TARGETED_EVIDENCE item.

Current authoritative range: `DEC-001`–`DEC-120`.

If future site discovery, product architecture or platform changes introduce a genuinely new material choice, a new Decision ID may be appended through the existing governance process. Existing IDs are never renumbered.

Coverage evidence:
- `audits/strategy/P-002-CHATGPT-DECISION-COVERAGE-REVIEW.md`
- `audits/strategy/P-003-DECISION-BACKLOG-RECONCILIATION.md`
- `audits/strategy/P-004-CANONICAL-DECISION-COVERAGE-MATRIX.json`
- `audits/strategy/P-004-DECISION-COVERAGE-CLOSURE.md`


## Status legend

- `OPEN` — requires discussion.
- `DISCUSSING` — currently under owner + ChatGPT review.
- `NEEDS_TARGETED_EVIDENCE` — requires a narrow evidence check first.
- `PROPOSED` — Second Review has a target direction; owner approval pending.
- `ACCEPTED` — owner-approved target state.
- `DEFERRED` — intentionally postponed; does not block unrelated scopes.
- `REJECTED`
- `SUPERSEDED`

## Working method

We will work through this backlog topic by topic over multiple sessions.

After each discussion:
1. record the decision;
2. update status;
3. record exact target state and exceptions;
4. identify implementation dependencies;
5. do **not** send a Production task to Codex until the required Decision IDs are accepted and an Execution Backlog item becomes `READY_FOR_TASK`.

---

# Session 1 — Site roles, indexability and architecture

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-001 | Approve durable site-family roles: Homepage, Shop, Product Categories, Products, Academy, Magazine/Articles, durable Blog Categories, Static trust/support | ACCEPTED | SR-005 §4–15; CONTENT-ARCHITECTURE | Accepted target: Homepage=brand/navigation root; Shop= broad commercial discovery hub; durable Product Categories=commercial category hubs; Products=transactional entities; Academy=structured learning; Magazine/Articles=informational/reference; durable Blog Categories=editorial hubs only where useful; Static=trust/support. Transitional/utility/legacy spaces remain governed by dedicated decisions. |
| DEC-002 | Decide final Homepage role and whether current title/H1/meta remain the baseline | ACCEPTED | WP-63; SR-005 §4 | Accepted: Homepage remains Brand/Entity + top-level navigation page; keep current Title, H1 and Meta as baseline; no extra keyword expansion without stronger evidence or verified brand-fact/content changes. |
| DEC-003 | Decide Shop target state: H1, visible role, title/meta and relationship to Product Categories | ACCEPTED | SR-004 SR-ST-001; WP-30918 | Accepted: /shop/ remains indexable + self-canonical broad commercial discovery hub and primary all-products listing; add H1 `فروشگاه ماری‌ورک`; SEO title `فروشگاه ماری‌ورک | رنگ پارچه، مدیوم، ست و ابزار`; replace broken archive meta with factual Shop-specific description; Shop supports discovery into durable Product Categories and Products without replacing category-specific landing pages; no layout redesign required by this decision. |
| DEC-004 | Cart / Checkout transactional utility-page policy | ACCEPTED | SR-005 §6; WP-10/WP-30919 | Accepted: retain transactional utility treatment; Cart noindex/follow; Checkout remains non-search transactional endpoint and may redirect to Cart in empty state; keep out of sitemap; no SEO copy/schema optimization; no crawl blocking that would prevent intended noindex from being seen; no change required where current behavior already matches this policy. |
| DEC-005 | Decide public role of current LearnDash Course Categories currently returning 404 | ACCEPTED | SR-005 §11; current SEO output | Accepted: Free/Paid LearnDash Course Categories are not durable public SEO entities; keep out of index/sitemap/navigation; current 404 behavior is acceptable while empty; internal retention is allowed if LearnDash needs them; no redirect without proven semantic replacement. |
| DEC-006 | Decide durable vs transitional taxonomy architecture at site level | ACCEPTED | SR-005; tag/category reconciliation | Accepted: taxonomy architecture is selective; only taxonomies with a durable, distinct user-facing browse/content role may become public SEO landing pages. Durable Product Categories and useful populated Blog Categories form part of the final architecture. pa_volume remains conditional under DEC-026. Product Tags, Blog Tags, migration-era Product Categories, empty LearnDash categories and other transitional/empty taxonomies are not durable SEO entities and must not be promoted through sitemap, navigation or SEO content merely because they exist in WordPress. |

# Session 2 — Titles, H1s and naming standards

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-007 | Product Title Naming Standard — fabric colors | ACCEPTED | SR-004 SR-ST-002; current-title-h1-matrix | Accepted visible Product title/H1 pattern: `رنگ پارچه [Color Name] ماری ورک کد [NNN]`. Use exact factual color name, canonical Mariwork brand spelling, stable product code, Latin digits for code consistency, no decorative `|` or `-`, no 30/60/250 ml variant tokens in parent title, and no URL/slug changes solely from title normalization. SEO `<title>` behavior is DEC-011. Half-space usage is a writing/brand-consistency standard, not a standalone SEO requirement; do not bulk-edit URLs/content only for half-space normalization. |
| DEC-008 | Product Title Naming Standard — sets/bundles | DEFERRED | SR-004 SR-ST-002; bundle matrix | Owner paused this decision on 2026-09-25; return later. No target state accepted yet. |
| DEC-009 | Product Title Naming Standard — mediums/additives | ACCEPTED | SR-004 SR-ST-002 | Accepted visible Product title/H1 pattern: `[Exact Product Name] ماری ورک کد [NNN]`. Use exact factual identity; do not force generic `مدیوم`; preserve product-specific terms such as glitter/varnish/glue/shine/base coat/fixative where factual; include canonical Mariwork brand spelling; end with stable Product code; no decorative `|` or `-`; use Latin digits; do not include volume in this family under any circumstance; no URL/slug changes solely from title normalization; SEO `<title>` remains DEC-011. |
| DEC-010 | Product Title Naming Standard — tools/accessories | DISCUSSING | SR-004 SR-ST-002 | Owner clarification: do not append `ماری ورک` to third-party/generic tools or accessories. Brand may appear only when the product is factually Mariwork-branded/manufactured. Decide final code/specification rules before acceptance. |
| DEC-011 | Decide relationship between visible Product H1/title and Rank Math SEO title template | OPEN | SR-004 SR-ST-002; Rank Math ownership | Template decision must follow visible-title standard |
| DEC-012 | Static/Core title and H1 policy | OPEN | SR-005 §5; current SEO output | Includes About, Contact, Stores, FAQ, Magazine, Why Mariwork |
| DEC-013 | Article title/H1 conventions | OPEN | 12 article dossiers; current output | Preserve natural informational titles; avoid mechanical keyword repetition |
| DEC-014 | Academy course/lesson title/H1 conventions | OPEN | course + 37 lesson dossiers | Keep instructional clarity; decide brand suffix/template behavior |

# Session 3 — Meta descriptions and visible content

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-015 | Product meta-description strategy | PROPOSED | SR-004 SR-ST-003 | Proposed: explicit factual descriptions; no Yoast reconstruction; prioritize broken/repeated/long descriptions |
| DEC-016 | Shop metadata strategy | OPEN | SR-004 SR-ST-001; WP-30918 | Decide explicit title/meta source and template behavior for Shop only |
| DEC-017 | Static/Core meta-description strategy | PROPOSED | SR-005 §5 | Magazine missing; several pages have weak generic descriptions |
| DEC-018 | Article meta-description update rule | OPEN | current article output | Decide when to retain, shorten, fact-check or rewrite |
| DEC-019 | Academy course/lesson meta-description rule | OPEN | current course/lesson output | Decide family template vs page-specific copy |
| DEC-020 | Product-page visible content architecture by family | OPEN | CONTENT-ARCHITECTURE; product dossiers | Decide required facts/modules for colors, sets, mediums, tools |
| DEC-021 | Product Category visible intro/content policy | OPEN | SR-004 SR-ST-006 | No word-count padding; define useful minimum role |
| DEC-022 | Static/trust page content policy | OPEN | static dossiers | Decide what About/Why/Contact/Stores/FAQ should contain and what not to expand |
| DEC-023 | Article update/freshness/fact-check policy | PROPOSED | SR-005 §7; article dossiers | Includes safety/technical claims such as WP-13295 |
| DEC-024 | Academy lesson/course content standard | OPEN | education dossiers | Decide instructional structure, prerequisites/materials, summary/transcript where useful |

# Session 4 — Taxonomies, sitemap and lifecycle

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-025 | Durable Product Category set and sitemap/index policy | PROPOSED | SR-004 SR-ST-006; taxonomy reconciliation | Durable categories proposed indexable; migration categories 20/27 decommission candidates |
| DEC-026 | `pa_volume` 30/60/250 archive role, indexability and sitemap policy | NEEDS_TARGETED_EVIDENCE | SR-005 §13; current-volume-architecture | Must prove distinct user value/navigation role before sitemap approval |
| DEC-027 | Product Tags decommission policy and mapping rule | PROPOSED | SR-004 SR-ST-010; 275 zero assignments | Controlled migration; no per-tag optimization |
| DEC-028 | Blog Categories lifecycle | PROPOSED | SR-005 §8; current-blog-category-matrix | Articles + History durable; empty categories need individual lifecycle |
| DEC-029 | Blog Tags decommission policy and mapping rule | PROPOSED | SR-005 §9; tag reconciliation | Six assigned terms / 39 assignments require cleanup first |
| DEC-030 | Sitewide sitemap membership policy by family | OPEN | current sitemap evidence; SR-004/SR-005 | Must follow accepted family/indexability decisions |
| DEC-031 | Attachment/media URL public/index policy | NEEDS_TARGETED_EVIDENCE | SYSTEM-URL-SPACES-CLOSURE; image summary | Current attachment count discrepancy requires representative verification |

# Session 5 — Structured data / technical ownership

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-032 | Homepage Organization/WebSite/WebPage schema target | PROPOSED | SR-005 §4; current SEO output | Keep one owner; SearchAction low priority / retired sitelinks-search-box relevance |
| DEC-033 | Static/Core WordPress Page schema policy | PROPOSED | SYS-016; SR-005 §5 | Proposed: remove generic Article default where semantics do not fit |
| DEC-034 | Article schema policy | PROPOSED | SR-005 §7; current BlogPosting output | Current BlogPosting generally coherent |
| DEC-035 | Product variation ProductGroup/variant schema architecture | PROPOSED | SR-004 SR-ST-004; variable-schema matrix | Canary required; Rank Math extension only if Free lacks capability |
| DEC-036 | Bundle/set schema and visible component representation | PROPOSED | SR-004 SR-ST-005; bundle matrix | Bundle remains Product/Offer, not ProductGroup |
| DEC-037 | Academy/LearnDash schema owner and canary | PROPOSED | SYS-017; SR-005 §10 | One course + two representative video lessons proposed |
| DEC-038 | VideoObject eligibility/ownership policy for lessons and other videos | NEEDS_TARGETED_EVIDENCE | SR-005 §10; MASTER-TODO M | Requires video inventory/fetchability facts before broad rule |
| DEC-039 | Breadcrumb structured-data policy across Store/Academy/content | OPEN | current output + hierarchy | Use only where visible hierarchy is accurate |

# Session 6 — Internal-link architecture

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-040 | Approve CORE_MANDATORY / FAMILY_SPECIFIC / CONTEXTUAL_OPTIONAL model | PROPOSED | SR-005 §17; link matrix draft | Framework approved in Second Review; owner approval pending |
| DEC-041 | Exact mandatory parent/hub links by family | OPEN | INTERNAL-LINK-REQUIREMENT-MATRIX-DRAFT | Requires exact durable destinations |
| DEC-042 | Product → Academy/Article rules | OPEN | SR-004 SR-ST-009; current graph | Only real preparation/technique/care relevance |
| DEC-043 | Academy/Lesson → Product/Category rules | OPEN | SR-004 SR-ST-009 | Only when material/tool is actually used |
| DEC-044 | Article → Product/Category rules | OPEN | SR-005 §17 | Commercial next step only when useful/contextual |
| DEC-045 | Article → Article / Article → Academy relationship | PROPOSED | SR-005 §17 | Related Article should not be mandatory on every Article |
| DEC-046 | Category → education/reference links | OPEN | SR-004/SR-005 | Define selected hubs, not generic footer duplication |
| DEC-047 | Anchor-text policy | OPEN | CONTENT-RESEARCH-SPEC; Page+Query limitation | Natural descriptive anchors; no invented query-target anchors |
| DEC-048 | Orphan/underlinked thresholds and approved exceptions | OPEN | current graph | Resolver gaps are not broken-link count |

# Session 7 — Content-family boundaries and information architecture

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-049 | Article vs Academy intent boundary | OPEN | article + Academy dossiers; CONTENT-ARCHITECTURE | Decide when content stays reference vs structured lesson |
| DEC-050 | Product vs Category vs Article query/content role boundary | OPEN | CONTENT-ARCHITECTURE; SR-004 | Page+Query unavailable; use user intent + SERP research where needed |
| DEC-051 | Magazine hub and Blog Category hierarchy | OPEN | WP-70; categories 71/142 | Decide Magazine role and category visibility/navigation |
| DEC-052 | History / Artists content strategy | NEEDS_TARGETED_EVIDENCE | legacy map; category state; current census | Current historical Artist URLs are not current public entities |
| DEC-053 | Canonical Mariwork facts and naming-consistency registry | NEEDS_TARGETED_EVIDENCE | BRAND-ENTITY-SEARCH; Homepage/About/Why Mariwork | Verify canonical brand facts/spelling before schema/content/entity changes |

# Session 8 — Images and video

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-054 | ALT policy by image role | PROPOSED | SYS-015; IMAGE-ALT-AUDIT-SUMMARY | Informative vs decorative first; no keyword stuffing |
| DEC-055 | SUPERSEDED — image sampling belongs to evidence/QA, not target-state strategy | SUPERSEDED | P-002; SR-005 §18 | Sampling remains required operationally; rollout governance is DEC-068 |
| DEC-056 | Product image/gallery SEO policy | NEEDS_TARGETED_EVIDENCE | Store evidence + MASTER-TODO L | Requires visual/primary-image review |
| DEC-057 | Article/Academy instructional image policy | NEEDS_TARGETED_EVIDENCE | SYS-010/011 | Visual-purpose review required |
| DEC-058 | SUPERSEDED — broad video policy replaced by atomic video decisions | SUPERSEDED | P-002; MASTER-TODO M; SYS-017 | Video inventory is evidence; VideoObject remains DEC-038; atomic video policies are separate |

# Session 9 — System URLs, facets and legacy migration

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-059 | Store facets/sort/display parameter policy | PROPOSED | SR-004 SR-ST-008; SR-005 §16 | Separate crawl traps from variant preselection before any blocking |
| DEC-060 | Shop pagination and legacy `product-page` policy | PROPOSED | parameter evidence | Keep normal pagination; stop/consolidate legacy alternate where approved |
| DEC-061 | Product search URL policy | PROPOSED | SR-004 | Keep noindex |
| DEC-062 | Author/date archive public/indexability policy | PROPOSED | SYSTEM-URL-SPACES-CLOSURE | Keep archive policy distinct from feed, internal search and 404/error lifecycle |
| DEC-063 | Legacy URL prioritization rule | PROPOSED | SR-005 §19; A-012 | Prioritize URLs with meaningful historical evidence/value |
| DEC-064 | Legacy product-volume mapping disposition | NEEDS_TARGETED_EVIDENCE | legacy-volume-url-map | 68 partial + 14 unknown remain |
| DEC-065 | Historical Education → Academy mappings | NEEDS_TARGETED_EVIDENCE | education-academy-migration-map | 36 partial + 5 unknown remain |
| DEC-066 | Historical Artist/other removed-content URL disposition | NEEDS_TARGETED_EVIDENCE | A-012 legacy map | Do not infer replacement by slug similarity |
| DEC-067 | Redirect technical owner and implementation path | OPEN | SEO-OWNERSHIP; legacy workstreams | Rank Math first where supported; platform only when justified |

# Session 10 — Measurement, rollout and later programs

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-068 | Canary size and rollout rules by change class | OPEN | M-15; change templates | Define practical samples for metadata/schema/content/link changes |
| DEC-069 | Monitoring windows and core success metrics | OPEN | M-18; MEASUREMENT-SPEC; MASTER-TODO J | Define 28/56-day defaults, comparable windows and core search/business metrics |
| DEC-070 | Strategy Lock scope for first implementation wave | OPEN | governance + accepted decisions | Decide which accepted decisions form first coherent rollout |
| DEC-071 | External PR / advertorial strategy | DEFERRED | MASTER-TODO K | Decide after internal architecture/landing pages stabilize |
| DEC-072 | Merchant Center / Free Listings program entry and eligibility | DEFERRED | MASTER-TODO O-001/O-003 | Keep separate from Product Feed architecture/data contract |
| DEC-073 | Genuine reviews/social-proof collection and visible-display policy | DEFERRED | MASTER-TODO O-007/O-009 | Genuine-data policy only; structured-data eligibility is a separate decision |


# Session 11 — System utility, metadata and URL architecture additions

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-074 | Login / My Account authentication/account-page policy | PROPOSED | SR-005 §5–6; current SEO output | Decide crawl/index role, privacy boundary and no-content-optimization policy |
| DEC-075 | Fast Buy utility/landing-page policy | PROPOSED | current SEO output; WP-30991 | Decide whether Fast Buy remains utility/noindex or becomes a deliberate landing page |
| DEC-076 | Durable Product Category metadata strategy | OPEN | SR-004 SR-ST-006; B7 | Separate from Shop and pa_volume metadata |
| DEC-077 | pa_volume metadata strategy | OPEN | SR-004 SR-ST-007; DEC-026 | Only relevant if volume archives remain durable public targets |
| DEC-078 | Preferred host/protocol, trailing-slash and future URL-normalization policy | OPEN | SITEWIDE-TECHNICAL-AUDIT-SPEC A/E; I-005/I-007 | Parent rule for future canonical/redirect consistency |
| DEC-079 | Sitewide canonical and duplicate-URL architecture | OPEN | SITEWIDE-TECHNICAL-AUDIT-SPEC E; SYS-006 | Parent for alternate URL spaces; family exceptions remain separate |
| DEC-080 | Critical JS/AJAX content and crawlable-link discoverability policy | NEEDS_TARGETED_EVIDENCE | SITEWIDE-TECHNICAL-AUDIT-SPEC G | Requires representative rendered/initial-HTML evidence before implementation |

# Session 12 — Product facts, lifecycle and commercial data

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-081 | Product identity source of truth for SKU / GTIN / MPN / brand | NEEDS_TARGETED_EVIDENCE | SR-004 SR-ST-004; MASTER-TODO O | Precedes ProductGroup/Offer/feed identity implementation |
| DEC-082 | Product commercial-fact source of truth for price / currency / sale / availability | NEEDS_TARGETED_EVIDENCE | SITEWIDE-TECHNICAL-AUDIT-SPEC H/I; Store evidence | Visible Woo facts and structured data must agree |
| DEC-083 | Out-of-stock versus discontinued Product lifecycle | OPEN | SYS-003; Store/Product architecture | Decide indexability, availability, links and eventual removal/redirect behavior |
| DEC-084 | Future Product URL/slug change and history-preservation policy | OPEN | SYS-003; B0-012 | Variant-preselection behavior is not part of this decision |
| DEC-113 | Shipping / returns source-of-truth and structured-data/feed policy | NEEDS_TARGETED_EVIDENCE | SITEWIDE-TECHNICAL-AUDIT-SPEC H; MASTER-TODO O | Only implement factual policies/data actually supported by Woo/business rules |

# Session 13 — Editorial trust and family-specific content semantics

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-085 | Editorial author / reviewer / date / source / citation provenance policy | OPEN | CONTENT-RESEARCH-SPEC §§8–9; E1/F1 | Applies where factual/technical claims need provenance; no invented credentials |
| DEC-086 | FAQ visible-content versus structured-data boundary | OPEN | WP-32895; SR-005 §5 | Semantic correctness first; no rich-result promise |
| DEC-087 | Stores/location/NAP and local-trust content role | NEEDS_TARGETED_EVIDENCE | WP-14760; BRAND-ENTITY-SEARCH | Requires verified store/address/contact facts |
| DEC-088 | Informational Article/Academy commercial CTA policy | OPEN | CONTENT-RESEARCH-SPEC §7; DEC-042–046 | Separate useful CTA policy from mechanical internal linking |
| DEC-114 | Homepage visible content and CTA structure | OPEN | C-009; WP-63; SR-005 §4 | Separate content/CTA structure from Homepage title/H1/meta baseline |
| DEC-115 | Durable Product Category title/H1 naming standard | OPEN | B7; SR-004 SR-ST-006 | Separate from metadata and visible intro/content |
| DEC-116 | pa_volume title/H1 naming standard | OPEN | DEC-026; SR-004 SR-ST-007 | Only relevant if archive role is retained |
| DEC-117 | pa_volume visible landing-content standard | OPEN | DEC-026; SR-005 §13 | No artificial text; define useful distinct value if retained indexable |
| DEC-118 | Durable Blog Category presentation/content standard | OPEN | DEC-028; current-blog-category-matrix | Covers title/H1/meta/visible hub treatment for durable categories only |
| DEC-119 | Content overlap/cannibalization resolution policy | OPEN | CONTENT-RESEARCH-SPEC §4; I-012; DEC-049/050 | Differentiate/merge/redirect only with evidence; no Page→Query inference |

# Session 14 — Image policy additions

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-089 | Image filename and media naming policy for new assets | OPEN | VISUAL-IMAGE-SEO; L-005 | No historical bulk rename implied |
| DEC-090 | Primary/representative image, gallery consistency and duplicate/reuse policy | NEEDS_TARGETED_EVIDENCE | VISUAL-IMAGE-SEO; L-002/L-006/L-008 | Requires representative visual review |
| DEC-091 | Image context, caption and linked-image behavior policy | OPEN | VISUAL-IMAGE-SEO; L-008 | Decide contextual text/link behavior separately from image discovery |
| DEC-092 | Image discovery/indexability/sitemap treatment | NEEDS_TARGETED_EVIDENCE | SITEWIDE-TECHNICAL-AUDIT-SPEC J; L-007 | Only where an image-discovery mechanism is actually relevant |
| DEC-093 | Image technical delivery policy: dimensions, formats, srcset, lazy loading and LCP interaction | NEEDS_TARGETED_EVIDENCE | VISUAL-IMAGE-SEO; L-009 | Coordinate with DEC-111; no performance claim without field/lab evidence |

# Session 15 — Atomic Video SEO decisions

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-094 | Video host-page, fetchability, prominence and player/embed policy | NEEDS_TARGETED_EVIDENCE | VIDEO-SEO; M-002/M-003; SR-005 §10 | Precedes broad video structured-data implementation |
| DEC-095 | Video title / description / reusable naming standard | OPEN | VIDEO-SEO; M-004/M-008 | Visible/contextual metadata, not VideoObject ownership |
| DEC-096 | Video thumbnail quality, uniqueness and representative-thumbnail policy | OPEN | VIDEO-SEO; M-006 | Factual/representative thumbnails only |
| DEC-097 | Video transcript / summary / key-text policy | OPEN | VIDEO-SEO; M-007 | Use when useful; no mandatory transcript for every video without reason |
| DEC-098 | Duplicate / orphan / weak-context video lifecycle | OPEN | VIDEO-SEO; M-010/M-011 | Cross-family linking remains governed by DEC-040–048 |

# Session 16 — Brand / Entity atomic decisions

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-099 | Brand/trust site-content and entity-supporting page strategy | OPEN | BRAND-ENTITY-SEARCH; Homepage/About/Why/Contact | Uses verified facts from DEC-053 |
| DEC-100 | Branded query and landing-page role strategy | OPEN | BRAND-ENTITY-SEARCH; N-002/N-007 | Query ownership requires joined evidence or direct research |
| DEC-101 | Verified off-site entity-reference and PR/entity evidence boundary | DEFERRED | BRAND-ENTITY-SEARCH; EXTERNAL-PR-STRATEGY | No invented relationships; coordinate with DEC-071 |

# Session 17 — Measurement, maintenance and deferred expansion

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-102 | Release isolation, change annotation and comparable measurement-baseline policy | OPEN | MEASUREMENT-SPEC §§1–3 | Required before meaningful causal interpretation |
| DEC-103 | Monitoring KEEP / ITERATE / ROLLBACK-CANDIDATE interpretation | OPEN | MEASUREMENT-SPEC §§4–7 | Separate from cadence and raw metrics |
| DEC-104 | Maintenance triggers for updates, Google changes, new URLs/404s and freshness | OPEN | MASTER-TODO J-003–J-009 | Recurring triage policy |
| DEC-105 | Product Feed identity/variant/data-contract architecture | DEFERRED | MASTER-TODO O-004–O-006; DEC-072 | Split further before implementation if one target state is still ambiguous |
| DEC-106 | Review/rating structured-data eligibility and ownership | DEFERRED | MASTER-TODO O-007–O-009; DEC-073 | Requires genuine review data; no fabricated ratings |

# Session 18 — System URL spaces, crawler access and page experience

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-107 | Feed URL crawl/index policy | OPEN | SYSTEM-URL-SPACES-CLOSURE; H-007 | Separate from author/date archives and internal search |
| DEC-108 | General internal-search result URL policy | PROPOSED | SYSTEM-URL-SPACES-CLOSURE; H-006 | Product Search remains DEC-061 |
| DEC-109 | 404 / soft-404 / error-page lifecycle policy | OPEN | SYS-003; SYSTEM-URL-SPACES-CLOSURE; I-004 | Separate source-level migration mapping from general error behavior |
| DEC-110 | Search-crawler access policy for Googlebot / OAI-SearchBot and training-crawler separation | NEEDS_TARGETED_EVIDENCE | SITEWIDE-TECHNICAL-AUDIT-SPEC L; I-014 | WAF/CDN/server evidence required; GPTBot and ChatGPT-User are separate concerns |
| DEC-111 | Mobile / Core Web Vitals / Page Experience remediation policy | NEEDS_TARGETED_EVIDENCE | SITEWIDE-TECHNICAL-AUDIT-SPEC K; I-013 | Field vs lab evidence hierarchy; no ranking guarantee |
| DEC-112 | Concern-by-concern SEO technical-owner target matrix | OPEN | SEO-OWNERSHIP; current ownership matrix; SYS-001/SYS-006 reconciliation | Apply Rank-Math-first rule to title/meta/robots/canonical/sitemap/schema/redirect/server controls |

# Session 19 — Navigation architecture completeness

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-120 | Global header/footer/navigation SEO link architecture | OPEN | current internal-link graph; Homepage navigation; INTERNAL-LINK-ARCHITECTURE | Define durable hub exposure separately from contextual body-link rules |


---

# Global constraints that apply to every decision

1. Repository evidence is the source of truth.
2. Current Production reality overrides stale Round-1 observations.
3. Google official documentation governs SEO basis.
4. Rank Math is the first technical owner where the installed version supports the concern.
5. No Page→Query attribution without joined evidence or explicit alternative research.
6. No invented product/content facts.
7. No mass implementation from a family recommendation before target state and exceptions are accepted.
8. No Codex Production task is generated directly from this file until the corresponding item(s) are `ACCEPTED` and represented in `tasks/EXECUTION-BACKLOG.md`.

# Strategy Lock checklist

For any scope proposed for implementation:

- [ ] all blocking DEC IDs = `ACCEPTED`
- [ ] exact target state written
- [ ] exact affected entity/family list known
- [ ] exceptions documented
- [ ] SEO owner known
- [ ] Google basis recorded
- [ ] content text approved where applicable
- [ ] canary/regression approach known
- [ ] unresolved dependencies are non-blocking and explicit
- [ ] Execution Backlog item created
