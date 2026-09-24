# Manifest — Final SEO Mariwork

**Framework version: 1.0**  
**State: FROZEN BEFORE PAGE AUDITS**  
**Frozen: 2026-09-24**

## 1. مأموریت

این پروژه برای SEO اصولی، مستند، قابل‌اندازه‌گیری و بلندمدت کل ماری‌ورک است.

هدف پروژه:
- شناخت وضعیت واقعی سایت؛
- ساخت پرونده دائمی برای هر entity مهم؛
- تحقیق فنی و محتوایی با شواهد؛
- تبدیل یافته‌های تکراری به اصلاح سیستماتیک؛
- تولید محتوای مفید، دقیق و متمایز؛
- سازگاری داده visible، WooCommerce و structured data؛
- قابل‌فهم بودن اطلاعات برای کاربر، Search و سیستم‌های AI/LLM؛
- ثبت تأثیر واقعی تغییرات.

هدف پروژه «امتیاز افزونه SEO»، «تعداد کلمه» یا «تولید انبوه صفحه برای keyword» نیست.

## 2. قواعد غیرقابل‌مذاکره

### M-01 — Dual Audit
هیچ صفحه‌ای با یک audit نهایی نمی‌شود.

**Audit 1 — Codex:** تحقیق فنی/داده‌ای read-only بر اساس task ChatGPT.

**Audit 2 — ChatGPT:** بررسی مستقل URL زنده و intent/content/SEO و سپس reconcile با گزارش Codex.

Second Review باید یافته‌های Codex را `CONFIRM / MODIFY / REJECT / NEEDS_MORE_EVIDENCE` کند و یافته مستقل اضافه کند.

### M-02 — Analysis Before Write
تا قبل از `APPROVED` شدن dossier و صدور Implementation Task هیچ تغییر SEO روی Production مجاز نیست.

### M-03 — Stable Page Dossier
هر entity مهم فقط یک dossier canonical دارد. تغییر slug/URL باعث ساخت dossier جدید نمی‌شود مگر entity واقعاً عوض شده باشد.

### M-04 — Immutable Raw Data
Search Console، Coverage/Indexing، crawl export، log extract و سایر raw snapshotها ویرایش نمی‌شوند. Derived data باید منبع، تاریخ و transformation را ثبت کند.

### M-05 — No False Page/Query Attribution
Query و Page مستقل Search Console به هم نسبت داده نمی‌شوند مگر relation با Page+Query dataset/filter یا شواهد مستقیم اثبات شده باشد.

### M-06 — Production Reality Wins
HTML، HTTP behavior، current WP/Woo data و code فعلی نسبت به گزارش تاریخی اولویت دارند. اختلاف باید ثبت شود، نه پنهان.

### M-07 — Systemic Problems Get Systemic Fixes
هر finding باید PAGE/FAMILY/SITEWIDE باشد. مشکلات FAMILY/SITEWIDE قبل از تکرار دستی به ریشه مشترک، change dossier و regression set تبدیل می‌شوند.

### M-08 — No Invented Facts
هیچ spec، پوشش، دوام، زمان، دما، نتیجه آزمایش، SKU، GTIN، availability، review، rating یا ادعای محصول برای SEO اختراع نمی‌شود.

### M-09 — People-First, Evidence-Rich Content
طول متن هدف نیست. محتوا باید intent را حل کند، Information Gain داشته باشد و تا حد ممکن از تجربه/شواهد واقعی ماری‌ورک استفاده کند.

تولید انبوه متن template/AI با ارزش کم ممنوع است.

### M-10 — LLM/AI Visibility Is Built on Search Fundamentals
برای AI/LLM فایل یا schema خیالی ساخته نمی‌شود. اولویت:
- crawl/index eligibility؛
- محتوای متنی قابل‌دسترسی؛
- entity واضح؛
- داده دقیق و سازگار؛
- internal links؛
- structured sections؛
- شواهد واقعی.

### M-11 — Traceability
هر write روی Production باید به finding پذیرفته‌شده، Implementation Task، change reference، QA و تاریخ متصل باشد.

### M-12 — URL History Is Preserved
legacy URL، redirect chain و canonical history حفظ می‌شود تا داده تاریخی GSC از entity جدا نشود.

### M-13 — Sitewide Technical Baseline Before Page Batches
قبل از audit گسترده صفحه‌ها، baseline سراسری حداقل برای crawl/indexation، URL spaces، facets، sitemap، redirects، canonical patterns، schema system، internal linking و performance/mobile ایجاد می‌شود.

استثنا فقط task اضطراری مستندشده است.

### M-14 — Independent Final QA
`IMPLEMENTED` پایان کار نیست. Codex QA و سپس ChatGPT Final Acceptance Review اجباری است. فقط بعد از آن `FINAL_QA_PASSED`.

### M-15 — Controlled Systemic Rollout
تغییر FAMILY/SITEWIDE باید:
- Change Dossier
- exact scope
- backup/rollback
- canary یا نمونه محدود در صورت عملی
- regression set
- acceptance criteria
- rollout result

داشته باشد.

### M-16 — Framework Freeze
بعد از Framework v1.0 تغییر ساختار workflow یا schema پرونده‌ها فقط طبق `docs/CHANGE-CONTROL.md` مجاز است. تغییرات باید تا حد ممکن backwards-compatible باشند.

### M-17 — Content Authority
Final content target توسط ChatGPT در Second Review/Target State تأیید می‌شود.

Codex می‌تواند فقط اگر task صریحاً خواست draft بسازد. Draft Codex قبل از approval محتوای قابل اجرا نیست و حق افزودن fact تأییدنشده ندارد.

### M-18 — Measurement Discipline
هر implementation باید تاریخ، baseline و change scope داشته باشد. رشد یا افت پس از تغییر بدون کنترل seasonality، query mix، قیمت/موجودی و تغییرات دیگر به‌عنوان causation قطعی گزارش نمی‌شود.

### M-19 — Evidence Classes
در گزارش‌ها تفاوت این موارد روشن است:
- `OBSERVED` — مستقیم دیده شده
- `MEASURED` — از داده/اندازه‌گیری
- `INFERRED` — استنباط مستدل
- `HYPOTHESIS` — نیازمند آزمایش
- `DECISION` — تصمیم پروژه

### M-20 — Data Minimization & Security
SEO audit نباید customer PII، order details، credential، token، private key یا secret را وارد repo کند. فقط کمترین داده لازم خوانده/ثبت شود.

## 3. نقش‌ها

### ChatGPT — SEO Lead / Independent Reviewer
- طراحی task
- انتخاب batch
- تحقیق SERP/intent
- Second Review مستقل
- reconcile findings
- تعیین Target State
- تأیید محتوای نهایی
- توسعه Playbook
- نوشتن Implementation Task
- Final Acceptance QA
- اولویت‌بندی

### Codex — Technical Auditor / Controlled Executor
- read-only server/page audit
- extraction و measurement
- WordPress/WooCommerce/code analysis
- schema/metadata/media/link analysis
- ثبت finding
- implementation فقط با task صریح
- backup/rollback متناسب
- Codex QA و مستندسازی

### Repository
حافظه رسمی پروژه است. تصمیم مهمی که فقط در chat مانده، تا وقتی در repo ثبت نشده تصمیم پایدار پروژه محسوب نمی‌شود.

## 4. Definition of Ready

### برای Codex Audit
- entity/URL مشخص
- dossier یا template مشخص
- snapshotهای داده موجود مشخص
- mode = READ-ONLY
- scope و batch روشن

### برای APPROVED
- Codex Audit کامل
- Second Review مستقل
- findings reconcile شده
- blockerها مشخص
- intent و Target State به اندازه کافی روشن
- اگر rewrite بر query intent متکی است: Page+Query data موجود یا limitation + جایگزین پژوهشی ثبت شده

### برای Implementation
- dossier = APPROVED
- exact approved finding IDs
- exact write scope
- backup/rollback
- acceptance criteria
- برای FAMILY/SITEWIDE: change dossier و rollout strategy

## 5. Definition of Done

صفحه زمانی `COMPLETE` است که:
- baseline دارد؛
- دو audit کامل است؛
- target state ثبت شده؛
- تغییرات لازم اجرا شده؛
- Codex QA پاس شده؛
- Final Acceptance QA پاس شده؛
- monitoring انجام یا نتیجه/عدم امکان آن ثبت شده؛
- blocker بحرانی باز ندارد.

## 6. اصل احتیاط

هیچ best practice به‌تنهایی رتبه یا نمایش rich result/AI citation را تضمین نمی‌کند. پروژه تفاوت مشاهده، فرضیه، تصمیم و نتیجه اندازه‌گیری‌شده را حفظ می‌کند.
