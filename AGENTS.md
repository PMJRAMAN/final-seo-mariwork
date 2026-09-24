# AGENTS.md — Codex Rules for Final SEO Mariwork

این فایل برای Codex/Agent روی سرور و repository است.

قبل از هر task بخوان:
1. `MANIFEST.md`
2. آخرین تصمیم مرتبط در `docs/DECISIONS.md`
3. این فایل
4. سند workflow/spec مرتبط
5. dossier/change dossier مربوطه

## 1. Default Mode = AUDITOR / READ-ONLY

مگر task صریحاً `IMPLEMENTATION` باشد، Production فقط خواندنی است.

در Audit ممنوع:
- edit فایل Production
- DB write
- wp option/meta/content write
- slug/canonical/redirect change
- plugin/theme/config change
- cache purge
- checkout/order test واقعی
- bulk action
- schema modification

نوشتن گزارش در این repo مجاز است.

## 2. Production Safety

مسیر فعلی معمولاً:
`/home/mariwork/web/mariwork.ir/public_html`

اما قبل از استفاده verify کن.

قبل از هر implementation:
- environment/path را verify کن؛
- تغییرات unrelated را لمس نکن؛
- اگر git موجود است `git status`/وضعیت معادل را بررسی کن؛
- backup/rollback متناسب تهیه کن؛
- برای bulk operation در صورت امکان dry-run/sample اجرا کن؛
- secret/credential/PII را log یا commit نکن.

اگر `MARIWORK_CORE_ARCHITECTURE.md` مرتبط است، قبل از تغییر کد کامل خوانده شود.

## 3. Data Privacy

برای SEO معمولاً customer/order PII لازم نیست.

ممنوع در repo:
- نام/شماره/آدرس مشتری
- سفارش فردی
- password
- API key/token
- private key
- DB credential
- session/cookie secret

اگر داده خام به‌طور ناخواسته شامل PII شد، آن را commit نکن و blocker را گزارش کن.

## 4. Audit Sequence — Page

1. dossier را پیدا/از template بساز.
2. framework/schema version را ثبت کن.
3. identity:
   - entity ID
   - WP ID
   - page type/family
   - current URL
   - canonical
   - legacy URLs
4. HTTP status + redirect chain.
5. robots/noindex/X-Robots/canonical/sitemap.
6. public initial HTML بدون login.
7. metadata/H1/headings/OG.
8. JSON-LD/microdata و consistency با visible page.
9. current WP/Woo data read-only.
10. image/alt/dimensions/lazy behavior.
11. internal links/breadcrumbs/related links.
12. JS/AJAX dependence برای critical content.
13. GSC/Coverage snapshot + legacy URL metrics.
14. content usefulness/template similarity/contradictions.
15. related systemic findings registry را بررسی کن.
16. findings با ID یکتا ثبت کن.
17. Production را تغییر نده.
18. status = `CODEX_AUDITED`.

## 5. Finding Contract

Page finding ID:
`{entity_id}-F001`

Systemic:
`SYS-001` از registry.

حداقل:

```yaml
id:
severity: P0|P1|P2|P3
scope: PAGE|FAMILY|SITEWIDE
status: OPEN|CONFIRMED|HYPOTHESIS|BLOCKED|RESOLVED
evidence_class: OBSERVED|MEASURED|INFERRED|HYPOTHESIS
confidence: HIGH|MEDIUM|LOW
source_refs:
impact:
recommendation:
acceptance_criteria:
```

ادعاهای «پنالتی»، «حتماً رتبه بهتر» یا causation بدون مدرک ممنوع.

## 6. Search Console

`docs/DATA-SOURCES.md` الزامی.

ممنوع:
- join معنایی `Queries.csv` و `Pages.csv`
- مخلوط کردن date range/dimension متفاوت بدون disclosure
- نسبت دادن legacy URL به current URL بدون redirect/canonical verification

اگر Page+Query نداریم:
`Page-query relationship is not proven by the current export.`

## 7. Content Rules

در audit:
- fact اختراع نکن؛
- word count target نساز؛
- keyword stuffing پیشنهاد نده؛
- competitor copy بازنویسی نکن؛
- FAQ مصنوعی برای حجم متن نساز؛
- مشترک/اختصاصی خانواده را جدا کن؛
- Information Gain را بررسی کن؛
- تکرار template را در صورت امکان اندازه بگیر.

اگر task draft content می‌خواهد، خروجی `DRAFT — NOT APPROVED FOR PRODUCTION` است مگر متن از Target State تأییدشده عیناً اعمال شود.

## 8. Structured Data

بررسی consistency:
- name
- description
- Product/ProductGroup relationship
- unique variant IDs
- price/currency
- availability
- brand
- SKU/identifier
- images
- reviews/ratings واقعی
- shipping/returns فقط واقعی

Structured data نباید محتوای misleading یا غیرقابل‌مشاهده را جعل کند.

## 9. URL / Crawl / Migration

هر legacy URL:
- current status
- redirect destination
- redirect chain
- canonical destination
- entity

ثبت شود.

URL change فقط با task صریح + migration plan + rollback.

robots.txt را ابزار noindex تلقی نکن.

## 10. FAMILY / SITEWIDE Findings

اگر مشکل مشترک است:
- finding systemic را در registry ثبت/ارجاع کن؛
- root cause را بررسی کن؛
- change dossier پیشنهاد کن؛
- regression set تعریف کن؛
- ده‌ها تغییر دستی مشابه نساز.

## 11. Implementation Mode

فقط با `templates/IMPLEMENTATION-TASK.md` یا task هم‌ارز.

Preconditions:
- dossier = APPROVED
- finding IDs مشخص
- current state rechecked
- backup/rollback
- scope دقیق
- no conflicting recent change

برای FAMILY/SITEWIDE:
- Change Dossier
- canary/sample اگر عملی
- regression set
- rollout/rollback trigger

اصل اجرا:
- smallest necessary change
- no unrelated refactor
- no silent semantic change
- preserve URLs unless task says otherwise
- log exact changed objects

## 12. Codex QA

بعد از implementation:
- public output
- HTTP/canonical/indexability
- title/meta/H1
- visible content
- schema consistency
- price/availability if applicable
- variants/purchase path if applicable
- images/alt
- links
- mobile output
- regression set for systemic change

اگر پاس:
`IMPLEMENTED → CODEX_QA_PASSED`

Codex حق `FINAL_QA_PASSED` دادن ندارد.

## 13. Authority Limits

Codex حق ندارد:
- page را APPROVED کند؛
- Final Acceptance QA را امضا کند؛
- Playbook rule را خودسرانه ACCEPTED کند؛
- framework structure را بدون Decision تغییر دهد؛
- raw datasets را edit کند؛
- Production تغییر خارج task انجام دهد.

## 14. Missing Data Values

برای consistency از این مقادیر استفاده کن:
- `NOT_AVAILABLE`
- `NOT_APPLICABLE`
- `UNKNOWN_NEEDS_VERIFICATION`
- `BLOCKED_BY_ACCESS`

فیلد مهم را بی‌دلیل خالی نگذار.
