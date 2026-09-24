# QA Specification v1.0

QA دو مرحله دارد.

## 1. Codex Implementation QA

بلافاصله بعد از write.

### Technical
- expected HTTP
- redirect chain
- canonical
- indexability
- title/meta/H1
- initial HTML
- schema syntax/consistency
- price/currency/availability
- variant/bundle behavior
- links
- image/ALT
- cache/public output

### Content
- exact approved meaning
- no missing sections
- no invented facts
- formatting/mobile readability
- links point correctly

### Regression
برای FAMILY/SITEWIDE:
- canary pages
- representative affected pages
- unaffected control where useful
- template exceptions

اگر fail:
- rollback یا remediation مطابق task
- status `IMPLEMENTED` باقی می‌ماند
- PASS فقط با evidence

اگر pass:
`CODEX_QA_PASSED`.

## 2. ChatGPT Final Acceptance QA

مستقل از executor.

بررسی:
- approved findings واقعاً resolved؟
- target state visible؟
- live page matches intended content؟
- Codex QA شواهد کافی دارد؟
- مشکل جدید ایجاد نشده؟
- برای systemic change regression sample قابل‌قبول است؟

ChatGPT می‌تواند PASS یا FAIL کند.

PASS:
`FINAL_QA_PASSED`

FAIL:
remediation task و بازگشت به implementation.

## 3. External Validation When Relevant

- Rich Results Test
- Search Console URL Inspection
- PageSpeed/Lighthouse/CrUX
- mobile browser check

عدم دسترسی = `BLOCKED_BY_ACCESS`، نه PASS فرضی.

## 4. QA Evidence

پرونده باید تاریخ، URL، output و نتیجه را ثبت کند. فقط checkbox بدون evidence برای موارد بحرانی کافی نیست.
