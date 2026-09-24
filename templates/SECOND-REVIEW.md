# ChatGPT Second Review Template

این review باید مستقل باشد و فقط خلاصه گزارش Codex نباشد.

## Inputs

- Page dossier
- Codex Audit
- Live URL
- Current Search Console/Coverage evidence
- Relevant public web/SERP/doc sources where useful

## Procedure

1. URL زنده را مستقیم بررسی کن.
2. metadata/content/schema visible را مستقل بخوان.
3. گزارش Codex را finding-by-finding بررسی کن.
4. برای هر finding یکی از این تصمیم‌ها:
   - CONFIRM
   - MODIFY
   - REJECT
   - NEEDS_MORE_EVIDENCE
5. Search intent را مستقلاً ارزیابی کن.
6. usefulness و Information Gain را بررسی کن.
7. LLM extractability را بررسی کن.
8. مواردی که Codex ندیده اضافه کن.
9. PAGE/FAMILY/SITEWIDE scope را بازبینی کن.
10. Final Approved Findings را فقط پس از reconcile بنویس.

## Required Notes

- چه چیزی مستقیم مشاهده شد؟
- چه چیزی از Codex تأیید شد؟
- چه چیزی رد شد و چرا؟
- چه finding جدیدی اضافه شد؟
- چه مواردی هنوز hypothesis است؟
- آیا systemic fix لازم است؟

## Gate

پس از تکمیل:
`CODEX_AUDITED → SECOND_REVIEWED`

فقط وقتی Final Findings و Target State به اندازه کافی روشن‌اند:
`SECOND_REVIEWED → APPROVED`
