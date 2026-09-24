# Final SEO Mariwork

این مخزن **مرجع اصلی (Source of Truth)** پروژه SEO ماری‌ورک است. هدف آن فقط نگهداری گزارش نیست؛ بلکه ثبت کامل وضعیت هر صفحه، داده‌های تصمیم‌گیری، دو مرحله audit، تصمیم‌های استانداردسازی، تسک‌های اجرایی، نتیجه اجرا و پایش بعد از تغییر است.

## اصل مرکزی پروژه

هیچ صفحه‌ای صرفاً بر اساس یک audit بهینه‌سازی نمی‌شود.

برای هر صفحه دو بررسی مستقل الزامی است:

1. **Codex Audit** — بر اساس تسکی که ChatGPT برای Codex تعریف می‌کند؛ با بررسی داده‌های سرور، HTML، ساختار وردپرس/ووکامرس، اسکیما، تصاویر، لینک‌ها، Search Console و سایر شواهد.
2. **ChatGPT Second Review** — ChatGPT گزارش Codex را می‌خواند، همان صفحه را مستقلاً بررسی می‌کند، یافته‌ها را تأیید/رد/تکمیل می‌کند و نتیجه نهایی را در پرونده صفحه ثبت می‌کند.

تا زمانی که مرحله دوم انجام نشده و نتیجه به وضعیت `APPROVED` نرسیده باشد، پیشنهادهای audit مجوز اجرا روی Production نیستند.

## اسناد حاکم

به ترتیب اهمیت:

1. [MANIFEST.md](MANIFEST.md) — هدف، اصول و قواعد غیرقابل‌مذاکره پروژه
2. [AGENTS.md](AGENTS.md) — دستور کار Codex/Agent روی سرور
3. [docs/WORKFLOW.md](docs/WORKFLOW.md) — چرخه کامل تحلیل تا اجرا و پایش
4. [docs/AUDIT-SPEC.md](docs/AUDIT-SPEC.md) — استاندارد بررسی هر صفحه
5. [docs/DATA-SOURCES.md](docs/DATA-SOURCES.md) — قوانین استفاده از داده و Search Console
6. [docs/SEO-PLAYBOOK.md](docs/SEO-PLAYBOOK.md) — استانداردهای پذیرفته‌شده SEO سایت
7. [docs/DECISIONS.md](docs/DECISIONS.md) — تصمیم‌های رسمی و تاریخچه آن‌ها

در صورت تناقض، سند بالاتر اولویت دارد.

## ساختار مخزن

```text
.
├── README.md
├── MANIFEST.md
├── AGENTS.md
├── STATUS.md
├── docs/
│   ├── WORKFLOW.md
│   ├── AUDIT-SPEC.md
│   ├── DATA-SOURCES.md
│   ├── SEO-PLAYBOOK.md
│   └── DECISIONS.md
├── templates/
│   ├── PAGE-DOSSIER.md
│   ├── CODEX-AUDIT-TASK.md
│   ├── SECOND-REVIEW.md
│   ├── IMPLEMENTATION-TASK.md
│   └── BATCH.md
├── pages/
│   └── README.md
├── batches/
│   └── README.md
├── data/
│   └── README.md
├── httpswww.mariwork.ir-Performance-on-Search-2026-09-24/
└── httpswww.mariwork.ir-Coverage-2026-09-24/
```

خروجی‌های فعلی Search Console در ریشه مخزن داده خام محسوب می‌شوند و **نباید ویرایش شوند**. مهاجرت یا سازمان‌دهی مجدد آن‌ها فقط با حفظ نسخه خام و ثبت تصمیم انجام می‌شود.

## پرونده هر صفحه

هر URL مهم یک پرونده دائمی در `pages/` دارد، نه مجموعه‌ای از گزارش‌های پراکنده. نام فایل برای صفحات دارای WordPress/Product ID باید شناسه پایدار را نگه دارد:

```text
pages/products/product-12544-gray-122.md
pages/products/product-12471-redbrown-105.md
```

تغییر slug یا URL باعث ساخت پرونده جدید نمی‌شود؛ URLهای قبلی در همان پرونده به‌عنوان `legacy_urls` ثبت می‌شوند.

## طبقه‌بندی یافته‌ها

هر finding باید دارای `scope` باشد:

- `PAGE` — مختص همان صفحه
- `FAMILY` — مربوط به یک خانواده صفحه، مثل همه رنگ‌های پارچه
- `SITEWIDE` — مشکل یا قاعده سراسری

و severity:

- `P0` — خطای بحرانی/ریسک جدی
- `P1` — اولویت بالا
- `P2` — بهبود مهم
- `P3` — بهبود کم‌ریسک/کم‌اولویت

یافته‌های FAMILY و SITEWIDE باید قبل از ساخت ده‌ها تسک تکراری، به راهکار سیستماتیک تبدیل شوند.

## وضعیت پرونده

```text
DISCOVERED
→ CODEX_AUDITED
→ SECOND_REVIEWED
→ APPROVED
→ IMPLEMENTING
→ IMPLEMENTED
→ QA_PASSED
→ MONITORING
→ COMPLETE
```

## فلسفه اجرا

- داده و شواهد مقدم بر حدس هستند.
- تغییر سیستماتیک مقدم بر اصلاح دستی تکراری است.
- محتوای بیشتر لزوماً محتوای بهتر نیست.
- اطلاعات محصول باید برای انسان، موتور جست‌وجو و LLM قابل‌استخراج، دقیق و سازگار باشد.
- هیچ schema، review، rating، مشخصه فنی یا ادعای محصولی نباید ساخته یا حدس زده شود.
- حفظ URL، تاریخچه و داده‌های قبلی اهمیت دارد.
- هر تغییر باید قابل QA و در صورت نیاز قابل rollback باشد.

برای شروع پروژه، ابتدا [STATUS.md](STATUS.md) و سپس [docs/WORKFLOW.md](docs/WORKFLOW.md) خوانده شود.
