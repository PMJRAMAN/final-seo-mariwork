# Workflow — چرخه استاندارد SEO ماری‌ورک

## Phase 0 — Foundation

اسناد حاکم، templateها، data rules و status lifecycle تثبیت می‌شوند.

خروجی: `FOUNDATION_READY`

## Phase 1 — Site Inventory

برای همه URLهای مهم:
- URL
- entity ID
- page type
- family
- canonical
- indexability
- legacy URL
- sitemap presence
- basic HTTP state

ثبت می‌شود.

در این مرحله audit محتوایی عمیق انجام نمی‌شود.

## Phase 2 — Data Baseline

برای هر entity، داده‌های تاریخی موجود از:
- Search Console Performance
- Coverage/Indexing
- legacy URLها
- redirectها

به پرونده متصل می‌شوند.

اگر داده Page+Query موجود نیست، این خلأ ثبت می‌شود و query به صفحه نسبت داده نمی‌شود.

## Phase 3 — Batch Selection

Batch اولیه معمولاً ۵ صفحه است.

انتخاب فقط random نیست. اولویت با ترکیبی از:
- اهمیت تجاری؛
- impression/click؛
- فرصت CTR/ranking؛
- legacy/migration risk؛
- نمایندگی خانواده‌های مختلف؛
- وجود anomaly.

هر batch در `batches/` ثبت می‌شود.

## Phase 4 — Codex Audit

ChatGPT تسک را با `templates/CODEX-AUDIT-TASK.md` می‌نویسد.

Codex:
- صفحه را روی Production read-only بررسی می‌کند؛
- داده سرور را می‌خواند؛
- datasetهای موجود را بررسی می‌کند؛
- پرونده را تکمیل می‌کند؛
- findings را PAGE/FAMILY/SITEWIDE می‌کند؛
- status = `CODEX_AUDITED`.

## Phase 5 — ChatGPT Second Review

ChatGPT برای **هر صفحه همان batch**:

1. گزارش Codex را کامل می‌خواند.
2. URL زنده را مستقلاً بررسی می‌کند.
3. در صورت نیاز SERP/منابع رسمی/رقبا را بررسی می‌کند.
4. Search intent را مستقل تحلیل می‌کند.
5. شواهد Codex را challenge می‌کند.
6. findingها را CONFIRM / MODIFY / REJECT می‌کند.
7. یافته‌های جدید اضافه می‌کند.
8. نتیجه را در بخش Second Review ثبت می‌کند.

status = `SECOND_REVIEWED`.

این مرحله check-box نیست و باید تحلیل مستقل داشته باشد.

## Phase 6 — Reconciliation

دو audit به Final Approved Findings تبدیل می‌شوند.

برای هر finding:
- واقعیت و evidence نهایی؛
- scope؛
- severity؛
- target state؛
- acceptance criteria

ثبت می‌شود.

اگر finding سیستماتیک باشد، به Playbook یا تصمیم architecture مرتبط می‌شود.

status = `APPROVED`.

## Phase 7 — Playbook Consolidation

پس از چند پرونده:
- patternهای عنوان؛
- meta؛
- schema؛
- content modules؛
- image/ALT؛
- variant؛
- internal links؛
- URL؛
- family rules

به `SEO-PLAYBOOK.md` منتقل می‌شوند.

قانون فقط زمانی وارد Playbook می‌شود که evidence کافی یا تصمیم صریح پروژه وجود داشته باشد.

## Phase 8 — Systemic Fixes First

قبل از page-by-page edits بررسی شود که مشکل از:
- template؛
- plugin؛
- Rank Math template؛
- Woo schema؛
- Blocksy component؛
- custom plugin؛
- content generator

نیامده باشد.

اگر منشأ مشترک است، یک اصلاح systemic با regression set اجرا می‌شود.

## Phase 9 — Page Implementation

ChatGPT بر اساس پرونده APPROVED تسک اجرایی می‌نویسد.

Codex فقط تغییرات تعیین‌شده را اجرا می‌کند.

status:
`IMPLEMENTING → IMPLEMENTED`

## Phase 10 — QA

حداقل:
- HTTP/canonical/robots
- title/meta/H1
- visible content
- schema consistency
- price/availability if commerce
- image/alt
- mobile presentation
- internal links
- no regression
- relevant cache behavior

پس از قبولی:
`QA_PASSED`.

## Phase 11 — Monitoring

baseline و تاریخ تغییر ثبت می‌شود.

بسته به page:
- 28 day comparison
- 56 day comparison
- دوره‌های طولانی‌تر در صورت seasonality

بررسی:
- clicks
- impressions
- CTR
- position
- relevant query mix اگر داده موجود باشد
- organic conversion در صورت وجود measurement

هم‌زمانی تغییر و رشد به‌عنوان causation قطعی گزارش نمی‌شود.

status:
`MONITORING → COMPLETE`

## Change Gate

هیچ اجرای Production قبل از این سه مورد:
- Second Review
- APPROVED findings
- Implementation Task

انجام نمی‌شود، مگر اصلاح اضطراری مستقل از SEO که خارج از این workflow است.
