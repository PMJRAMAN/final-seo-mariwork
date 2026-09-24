# Codex Audit Task Template

## Mode

**AUDIT ONLY — PRODUCTION READ-ONLY**

قبل از شروع:
- `MANIFEST.md`
- `AGENTS.md`
- `docs/WORKFLOW.md`
- `docs/AUDIT-SPEC.md`
- `docs/DATA-SOURCES.md`
- پرونده هر صفحه

را بخوان.

## Batch

Batch ID:  
Pages:

1.
2.
3.
4.
5.

## هدف

برای هر صفحه audit فنی و داده‌ای مستقل انجام بده و نتیجه را در پرونده همان page ثبت کن.

هیچ تغییر Production انجام نده.

## منابع اجباری

برای هر page در صورت دسترسی:

- URL عمومی
- HTML عمومی بدون login
- WordPress/WooCommerce read-only data
- JSON-LD/microdata
- metadata
- media/images
- internal links
- Search Console snapshot
- Coverage snapshot
- legacy URL records
- relevant code responsible for output

## Search Console Rule

وجود جداگانه یک query و یک page رابطه آن‌ها را اثبات نمی‌کند.

اگر Page+Query dataset نداریم، این limitation را ثبت کن و query را به URL نسبت نده.

## خروجی هر صفحه

پرونده را تکمیل کن:

- Identity
- URL history
- baseline
- current snapshot
- Codex Audit findings

هر finding:
- evidence
- severity
- scope PAGE/FAMILY/SITEWIDE
- impact
- recommendation
- acceptance criteria

را داشته باشد.

## Shared Findings

اگر یک finding در بیش از یک page ریشه مشترک دارد:
- برای هر page اشاره مختصر ثبت کن؛
- یک finding FAMILY/SITEWIDE واضح تعریف کن؛
- منشأ احتمالی مشترک را بررسی کن؛
- پنج اصلاح دستی مشابه پیشنهاد نده.

## Stop Conditions

اگر برای نتیجه نیاز به write، خرید واقعی، تغییر config یا اقدام مخرب است:
- انجام نده؛
- آن را BLOCKED/NEEDS_EXECUTION_TEST ثبت کن.

## Completion

در پایان:
- status صفحات audited را `CODEX_AUDITED` کن؛
- summary batch بنویس؛
- هیچ page را APPROVED نکن.
