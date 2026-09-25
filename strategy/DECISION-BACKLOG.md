# SEO Decision Backlog

**Purpose:** canonical queue of strategy/target-state decisions before Production implementation  
**Authority:** owner + ChatGPT  
**Codex authority:** evidence collection only; Codex cannot mark decisions `ACCEPTED`  
**Baseline:** SR-004 + SR-005 and current audit repository  
**Production implementation authorized by this file:** NO
**Freeze state:** FROZEN_V1_COVERAGE — decision-domain structure complete; target-state decisions remain unresolved

See: `docs/DECISION-TO-EXECUTION-GOVERNANCE.md`.

## Decision Discussion Pipeline

This section defines the mandatory owner + ChatGPT workflow for every unresolved `DEC-###` item. It exists so the same decision method can continue across different chat sessions without relying on conversational memory.

### Interaction format

For each Decision, ChatGPT must:

1. **Read current Mariwork evidence from this repository first.**
   - Use the relevant dossier, audit, reconciliation, matrix, current-output evidence, and previously accepted Decisions.
   - Do not infer current site state when repository evidence exists.

2. **Check current official Google Search documentation before making the recommendation when the Decision involves SEO behavior.**
   - Google Search Central / developers.google.com/search is the primary SEO authority.
   - Vendor documentation may be used only for implementation capability, not as a substitute for Google's SEO guidance.
   - If official Google documentation does not prescribe a specific choice, state that clearly and distinguish project judgment from Google requirements.

3. **Explain the Decision to the owner in Persian.**
   The explanation should normally include:
   - what this Decision controls;
   - current Mariwork state/evidence;
   - concrete examples from the site when useful;
   - relevant Google basis;
   - the recommended Target State;
   - important exceptions/dependencies;
   - what this Decision does *not* change.

4. **Provide the proposed GitHub Target State in English.**
   - Keep it precise enough to become a durable implementation constraint.
   - Preserve exact exceptions, dependencies, and boundaries.
   - Do not record a proposal as accepted before owner approval.

5. **Owner decision gate.**
   The owner may:
   - approve;
   - modify;
   - reject;
   - request more evidence/research;
   - defer the Decision for later.

6. **After explicit owner approval only:**
   - set the Decision to `ACCEPTED` in `strategy/DECISION-BACKLOG.md`;
   - append/record the full accepted target state in `docs/DECISIONS.md`;
   - update `strategy/ACCEPTED-DECISIONS.md`;
   - preserve unresolved dependencies and implementation blockers;
   - then move the next Decision to `DISCUSSING`.

7. **If the owner defers a Decision:**
   - set it to `DEFERRED`;
   - record that no target state has been accepted;
   - continue with the next independent Decision;
   - return to the deferred item later before any dependent implementation.

8. **No implementation during the strategy discussion phase.**
   - Acceptance defines target state only.
   - Production work waits for Strategy Lock, dependency reconciliation, Execution Backlog readiness, canary/rollback requirements, and the normal Codex + ChatGPT QA process.

### Communication rule

The user-facing explanation is in **Persian**.  
The durable GitHub decision text is in **English**.

### Default Decision response shape

1. Decision title / scope  
2. Current Mariwork state  
3. Official Google basis  
4. ChatGPT recommendation  
5. Concrete examples / edge cases when useful  
6. Persian Target State explanation  
7. English Target State for GitHub  
8. Owner approval / modification / defer gate

Do not skip directly from audit evidence to implementation. The purpose of this pipeline is deliberate, topic-by-topic strategy agreement before execution.

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
| DEC-010 | Product Title Naming Standard — tools/accessories | ACCEPTED | SR-004 SR-ST-002 | Accepted: Product naming must reflect actual brand ownership. Third-party/generic tools use `[Exact Product Name] [Code if factually applicable]`; Mariwork-branded/manufactured tools use `[Exact Product Name] ماری ورک کد [NNN]`. Do not append Mariwork merely because the item is sold on mariwork.ir. Include only real brands/codes, remove decorative separators, exclude volume, include model/size only for genuinely distinct products, and do not change URLs solely from title normalization. |
| DEC-011 | Decide relationship between visible Product H1/title and Rank Math SEO title template | ACCEPTED | SR-004 SR-ST-002; Rank Math ownership | Accepted: WooCommerce Product title/visible H1 is the primary Product identity source; default Rank Math Product SEO title template target is `%title%` rather than `%title% %sep% %sitename%`; page-specific SEO title exceptions require concise factual clarity, not keyword expansion or artificial branding. Global implementation remains blocked until DEC-008 is resolved; rollout requires regression checks for uniqueness, descriptiveness, and duplicate-brand removal. |
| DEC-012 | Static/Core title and H1 policy | ACCEPTED | SR-005 §5; current SEO output | Accepted: concise page-specific SEO titles and clear primary H1s; repetitive `- رنگ پارچه ماری ورک` suffix is not required. Approved targets: About `درباره ماری‌ورک` / H1 same; Contact `تماس با ماری‌ورک` / H1 `با ماری‌ورک در تماس باشید`; Magazine `مجله ماری‌ورک`; Why `چرا ماری‌ورک؟` / H1 `چرا رنگ پارچه ماری‌ورک؟`; Stores `فروشگاه‌های ماری‌ورک` / H1 `فروشگاه‌های ماری‌ورک نزدیک شما`; FAQ `سوالات متداول ماری‌ورک` / H1 `سوالات متداول`. Title/H1 may differ but must describe same page role. |
| DEC-013 | Article title/H1 conventions | ACCEPTED | 12 article dossiers; current output | Accepted: natural reader-facing Article titles based on actual subject; default Article SEO `<title>` = approved Article H1/title; remove repetitive `- رنگ پارچه ماری ورک` article suffix; use brand/product terms only when naturally relevant; no mechanical keyword/date/modifier injection; retain accurate existing titles; rewrite only when materially vague/inaccurate/misleading/verbose; no URL changes from title normalization; overlapping Articles handled separately by DEC-119. |
| DEC-014 | Academy course/lesson title/H1 conventions | ACCEPTED | course + 37 lesson dossiers; owner amendment 2026-09-25 | AMENDED: Academy is video-first. Course H1 remains the natural Course name; Course SEO `<title>` should explicitly communicate video format where useful, e.g. `[Course Name] | آموزش‌های ویدیویی`. Lesson H1 remains the natural instructional title; default Lesson SEO `<title>` = `[Lesson H1] | آموزش ویدیویی`. Do not append the old `- رنگ پارچه ماری ورک` suffix. Include Mariwork only when naturally part of the subject/identity. Preserve genuine sequence numbers only. No URL/slug changes from normalization. Video/schema naming must stay consistent with the visible Lesson identity; schema ownership/eligibility remains DEC-037/038. |

# Session 3 — Meta descriptions and visible content

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-015 | Product meta-description strategy | ACCEPTED | SR-004 SR-ST-003 | Accepted as a general policy: `%excerpt%` is not the final Product meta-description strategy. Product metas must be page-specific, factual, concise, based on verified Product data, avoid generic/history copy, duplicate text, keyword stuffing, unsupported claims, artificial Mariwork branding, and arbitrary fixed character limits. Manual or programmatic generation is allowed if output is accurate, human-readable and meaningfully page-specific. Exact per-product copy is deferred to implementation/content QA; do not restore historical Yoast metadata by default. |
| DEC-016 | Shop metadata strategy | ACCEPTED | SR-004 SR-ST-001; WP-30918 | Accepted: `/shop/` uses explicit Shop-specific Rank Math metadata rather than generic archive/excerpt templates. SEO title remains `فروشگاه ماری‌ورک | رنگ پارچه، مدیوم، ست و ابزار` per DEC-003. Meta target: `فروشگاه ماری‌ورک؛ خرید رنگ پارچه، مدیوم‌ها، ست‌های رنگ و ابزارهای مرتبط برای نقاشی و چاپ روی پارچه.` Do not derive from archive/%excerpt%; avoid keyword stuffing and volatile counts/prices/discounts/stock. Product Category metadata remains separate. |
| DEC-017 | Static/Core meta-description strategy | ACCEPTED | SR-005 §5 | Accepted: important Static/Core pages use explicit page-specific meta descriptions, not generic templates or `%excerpt%`. Each description must summarize the page's real role/content, avoid keyword stuffing and unsupported claims, need not repeat Title/H1, and has no fixed 150/160-character rule. Initial page-specific direction: About=story/activity/product focus; Contact=contact/support purposes; Magazine=editorial/educational scope; Why Mariwork=features/use cases; Stores=physical points of sale; FAQ=common Product/educational questions. Final copy must align with visible content and DEC-053 facts. |
| DEC-018 | Article meta-description update rule | ACCEPTED | current article output; owner amendment 2026-09-25 | AMENDED: classify each Article meta as KEEP, SHORTEN/REFINE, or REWRITE. Preserve accurate useful metas; no blanket rewrite; resolve duplicates; rewrite weak/generic/insufficient metas; refine introduction-like verbose metas; no fixed 150/160-character limit; summarize the Article rather than copy paragraph one; metadata only, not substantive Article changes; cannibalization remains DEC-119. Current Article fact-check has already been completed and is not a remaining requirement in this workflow. |
| DEC-019 | Academy course/lesson meta-description rule | ACCEPTED | current course/lesson output; owner amendment 2026-09-25 | AMENDED + ACCEPTED: every Academy Lesson is video-first and contains a primary video. Course/Lesson metas must be page-specific; Lesson metas should explicitly communicate that the page is a video lesson and describe the specific technique/task/learning outcome. Visible context near the primary video should also make the video format clear. Academy intent = practical/demo/video-first; Magazine intent = explanatory/reference/text-first. Classify existing metas as KEEP / REFINE / REWRITE / FACT-CHECK REQUIRED; resolve duplicates/mismatches; no raw `%excerpt%`, generic family meta, mechanical keyword/brand injection, or fixed character rule. DEC-024 governs visible supporting content; DEC-119 governs Academy↔Magazine overlap/cannibalization. |
| DEC-020 | Product-page visible content architecture by family | ACCEPTED | CONTENT-ARCHITECTURE; product dossiers | Accepted: people-first family-specific Product content architecture. Shared family templates define information structure, not duplicated prose. Common core covers Product identity, verified specs, variants, primary use, necessary usage/handling guidance, limitations/warnings where relevant, and useful contextual links. Colors prioritize verified color/surface/technique/volume/fixation/washing facts; mediums prioritize function/use/verified ratios/compatibility/limitations; sets prioritize current Woo/YITH-backed composition/count/volume/use/differentiation; tools prioritize factual identity/specs/use/compatibility without false Mariwork branding. No fixed word count, filler SEO copy, mandatory FAQ, or unsupported claims. Exact copy/layout remains implementation-level. |
| DEC-021 | Product Category visible intro/content policy | ACCEPTED | SR-004 SR-ST-006 | Accepted: durable Product Categories are commercial discovery/product-selection pages, not long-form editorial articles. Use concise useful intros, keep Product grid primary, add supplementary selection guidance only when useful, no fixed word count, no filler SEO copy, no duplicated Product descriptions or Magazine/Academy content, FAQ optional, no keyword stuffing, child volume-set Categories require genuinely distinct value, factual inventory/product distinctions only, and no false Mariwork branding for third-party tools. DEC-121–124 may later inform emphasis without creating artificial duplication; metadata/title/indexability remain DEC-076/115/025. |
| DEC-022 | Static/trust page content policy | ACCEPTED | static dossiers; owner approval 2026-09-25 | Accepted: Static/Trust pages remain purpose-specific people-first entities, not generic SEO-content containers. About=Who is Mariwork? verified identity/history/people/activity; Why Mariwork=verified user-relevant brand/Product differentiators; Contact=verified actionable contact/support information; Stores=verified physical purchase-location information; FAQ=concise genuine answers + routing layer to Academy for practical/video how-to, Magazine for explanatory/reference depth, and Product/Category for commercial detail. No fixed word count, no filler SEO copy, no unsupported superiority/safety/performance claims, no invented local/inventory claims, and no duplication across Static/Magazine/Academy/Commerce. Facts remain governed by DEC-053. |
| DEC-023 | Article update/freshness policy | ACCEPTED | SR-005 §7; article dossiers; owner amendment 2026-09-25 | Accepted without a remaining fact-check workstream: Article age alone is not a reason to update. Classify existing Articles as KEEP/CURRENT, TARGETED UPDATE, SUBSTANTIVE UPDATE/REWRITE, or OVERLAP REVIEW. Trigger updates when information materially changes, examples/sources become obsolete, a factual error is discovered, or the Article no longer adequately serves its intended informational/reference need. Prefer targeted correction over unnecessary full rewrites; preserve original datePublished; dateModified must reflect a real content modification and must not be manipulated for freshness. Magazine remains text-first explanatory/reference content; practical video demonstrations route to Academy. Per-Article body-content review is an implementation-stage content QA task after strategy, using DEC-013/018/023/044/045/049/050/085/119/123 as constraints. |
| DEC-024 | Academy lesson/course content standard | ACCEPTED | education dossiers; DEC-019 owner clarification | Accepted: Academy is video-first practical/instructional content. Each Lesson functions as a dedicated watch page with natural H1, clear visible video-lesson context, primary video as dominant content, concise Lesson-specific intro, and optional practical supporting modules only when useful (materials/tools, preparation, key steps, practical notes/warnings, genuinely used products/tools, relevant next Lesson/reference). Full transcripts are optional, not mandatory; default to concise summaries/notes for short videos. Academy owns practical/demo intent; Magazine owns explanatory/reference text-first intent. Course page is an educational hub that explains scope, video-learning format and organizes Lessons; no generic long SEO copy. Overlap remains DEC-119. |

# Session 4 — Taxonomies, sitemap and lifecycle

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-025 | Durable Product Category set and sitemap/index policy | ACCEPTED | SR-004 SR-ST-006; taxonomy reconciliation; owner approval 2026-09-25 | Accepted: durable Product Categories are 1902 Fabric Colors, 28 Mediums/Glitters, 82 Sets root, 220 Tools/Accessories, and child Set categories 1991/1992/1993 (30/60/250 ml). Durable categories target 200 + index/follow + self-canonical + Product Category sitemap + crawlable internal navigation, provided each retains a genuine commercial browse role. Historical Product Categories 20 (60 ml colors) and 27 (250 ml colors) are not durable and must be decommissioned: remove from SEO architecture/sitemap/navigation, preserve migration evidence, implement the verified consolidation/redirect to the main Fabric Colors Category, then delete the obsolete WooCommerce category terms only after confirming no operational dependency remains. pa_volume is separate under DEC-026. |
| DEC-026 | `pa_volume` 30/60/250 archive role, indexability and sitemap policy | ACCEPTED | SR-005 §13; current-volume-architecture; owner approval 2026-09-25 | Accepted: `pa_volume` 30ml/60ml/250ml are durable cross-family commercial browse landing pages for Products genuinely purchasable in the selected volume. Target: 200 + index/follow + self-canonical + XML sitemap + deliberate crawlable navigation/internal links. These pages are distinct from volume-specific Set Product Categories. Shop `?filter_volume=` states remain functional faceted/filter URLs, not independent search landing pages. Where reliable, Product links from volume pages should preserve/preselect the relevant variation. Title/H1 and visible copy remain separate under DEC-116/117. |
| DEC-027 | Product Tags decommission policy and mapping rule | ACCEPTED | SR-004 SR-ST-010; 275 zero assignments; owner amendment 2026-09-25 | AMENDED: decommission/delete all 275 current Product Tag terms. Product Tag archives are not durable SEO/navigation entities and remain out of sitemap/index targets. Historical tag URLs may permanently redirect only to a genuine semantic successor within the commerce/store architecture: Product, Product Category, approved `pa_volume` landing page, or exceptionally Shop when it is truly the closest valid commercial replacement. Do not redirect Product Tags to Magazine, Academy, Static pages, Homepage, or unrelated broad destinations. Do not map by slug/keyword similarity. Where no meaningful commerce replacement exists, return proper 404/410; standard 404 is the default unless deliberate 410 is operationally useful. Preserve important historical evidence before deletion and QA for soft 404s/chains/internal remnants. |
| DEC-028 | Blog Categories lifecycle | ACCEPTED | SR-005 §8; current-blog-category-matrix; owner approval/amendment 2026-09-25 | Accepted: Educational Articles (71) and History (142) remain durable Magazine hubs. Artists (18) is transitional migration infrastructure for the new Artists project and is not deleted as an ordinary empty category. When the new Artists system is public and stable, each historical Artist URL that can be identity-matched to a new Artist profile redirects one-to-one to that new profile; unmatched historical Artist URLs redirect to the main new Artists landing page. Do not redirect to draft/non-public targets. All other empty Blog Categories (including Education/video, Cultural, Guides, Literature, Uncategorized variants, Free, General, Paid, and other empty non-Artist terms) are approved for controlled deletion. Their URLs should redirect only if a genuine semantic successor exists; otherwise return proper 404. |
| DEC-029 | Blog Tags decommission policy and mapping rule | ACCEPTED | SR-005 §9; tag reconciliation; owner approval 2026-09-25 | Accepted: fully decommission and delete all 54 current Blog Tag terms. Remove all 39 current Article↔Tag assignments before/with deletion; Article content and durable Blog Category membership remain unaffected. Blog Tag archives are not durable SEO/navigation entities and remain out of sitemap/index targets. Historical Blog Tag URLs may permanently redirect only to a genuine editorial successor (durable Magazine Category, specific Magazine Article, or equivalent Magazine hub). Do not redirect Blog Tags to Store/Product destinations merely from keyword overlap. Do not map by name/slug similarity alone. URLs with no meaningful editorial replacement return proper 404/410; standard 404 is the default. Preserve relevant historical evidence and QA internal links, sitemap leakage, redirect chains and soft 404s. |
| DEC-030 | Sitewide sitemap membership policy by family | ACCEPTED | current sitemap evidence; SR-004/SR-005; owner approval 2026-09-25 | Accepted: XML sitemap must mirror approved canonical Search architecture, not every generated WordPress/WooCommerce/LearnDash URL. Include only intentional canonical indexable search targets: Homepage, Shop, indexable Products, durable Product Categories (DEC-025), durable `pa_volume` pages (DEC-026), durable Static/Trust pages, Articles, durable Blog Categories, public/indexable Academy Course/Lessons, and future public/indexable Artists hub/profiles after launch. Exclude utilities/noindex pages, Product Tags, Blog Tags, retired/empty taxonomies, deprecated categories, empty LearnDash categories, internal search/facet/sort/display/variation-query URLs, pagination, redirects, 404/410, legacy URLs, non-canonical duplicates, drafts/private content. Sitemap membership follows indexability/canonical decisions, never drives them. `<lastmod>` reflects meaningful changes only. Sitemap QA is a dedicated implementation/release gate: validate every emitted URL for 200 status, indexability, canonical self-consistency, family eligibility, absence of redirects/errors/retired entities, and expected sitemap family membership after each rollout. |
| DEC-031 | Attachment/media URL public/index policy | ACCEPTED | SYSTEM-URL-SPACES-CLOSURE; image summary; owner approval 2026-09-25 | Accepted: WordPress Attachment HTML pages are not durable Search landing pages. Keep public media asset files crawlable where needed for page rendering/Google Images; suppress Attachment HTML pages from index/sitemap and redirect them to a clear owning canonical page when one exists, otherwise to the retained media file when appropriate, otherwise 404/410. Do not delete Media Library records as part of this SEO decision. Operational follow-up is required to inventory and safely remove genuinely unused/orphaned media assets, but only after proving no references remain in post/page content, Product featured/gallery images, Academy content, taxonomy/static content, schema/metadata, CSS/JS/theme/plugin references, or other runtime dependencies. Current 626-returned vs 845-advertised attachment discrepancy blocks blind bulk deletion and requires targeted reconciliation first. |

# Session 5 — Structured data / technical ownership

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-032 | Homepage Organization/WebSite/WebPage schema target | DISCUSSING | SR-005 §4; current SEO output | Keep one owner; SearchAction low priority / retired sitelinks-search-box relevance |
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
| DEC-119 | Content overlap/cannibalization resolution policy | OPEN | CONTENT-RESEARCH-SPEC §4; I-012; DEC-049/050; DEC-019 owner clarification | Must explicitly protect the Academy↔Magazine boundary: Academy = video-first practical/demo intent; Magazine = text-first explanatory/reference intent. If two pages remain substantially same-intent/same-content despite format distinction, differentiate/merge/redirect only with evidence; no Page→Query inference. |

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

# Session 20 — Semantic positioning, topic clusters and claim evidence

| ID | Decision | Status | Primary evidence | Blocking / notes |
|---|---|---|---|---|
| DEC-121 | Semantic positioning and Product value pillars | OPEN | Product/content corpus; brand facts; owner positioning input; future search research | Define which concepts Mariwork deliberately wants to own/associate with (e.g. durability/stability, fabric suitability, application quality, efficiency/economic value, compatibility) and the intended angle of each. Owner input: “economic” must not mean lowest price; intended angle is economic value derived from quality/useful performance/reduced waste or rework. Exact supporting mechanisms require evidence before publication. |
| DEC-122 | Topic / keyword cluster research and prioritization | OPEN | DEC-121; GSC where query evidence exists; direct SERP/search research | Research how users search around approved value pillars and problems; group by intent/topic, not keyword variants alone; prioritize clusters by relevance, evidence, user value and realistic search opportunity. No Page→Query inference without joined evidence. |
| DEC-123 | Cluster-to-page-family ownership map | OPEN | DEC-121/122; DEC-001; DEC-049/050 | Assign each approved cluster to the right primary owner: Product, Product Category, Magazine Article, Academy, FAQ, Why Mariwork, Homepage or other durable family. Avoid duplicate ownership and doorway-like keyword-variant pages. |
| DEC-124 | Content journey and coverage strategy by cluster | OPEN | DEC-121–123; DEC-040–050; DEC-088 | Define how each priority cluster is covered across awareness → understanding → instruction/comparison → product/use/care, with useful cross-family handoffs rather than repeated copy. |
| DEC-125 | Product/brand claim evidence standard | OPEN | DEC-121; DEC-053; DEC-081/082/085; product instructions/tests/business facts | Define evidence required before claims such as economic/value, durability/stability, coverage/efficiency, compatibility, professional suitability, safety, performance or superiority can appear sitewide. Marketing attractiveness alone is insufficient evidence. |

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
