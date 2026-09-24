# Data Sources & Evidence Rules v1.0

## 1. Evidence Hierarchy — Current State

1. public URL behavior
2. initial HTML/rendered visible output
3. current WP/Woo data
4. code/template responsible
5. current measured tooling
6. Search Console/Coverage snapshots
7. historical reports

برای historical performance، snapshot تاریخی خودش source اصلی آن بازه است.

## 2. Current Search Console Performance Snapshot

Path:
`httpswww.mariwork.ir-Performance-on-Search-2026-09-24/`

- Search type: Web
- Date: Last 16 months
- Export: 2026-09-24

Files include:
- Pages.csv
- Queries.csv
- Devices.csv
- Search appearance.csv
- Countries.csv
- Chart.csv
- Filters.csv

### Critical limitation

`Pages.csv` و `Queries.csv` مستقل‌اند.

از شباهت معنایی query و URL join نساز.

Page+Query relation نیازمند:
- Search Analytics API dimensions/filter
- export ترکیبی
- یا evidence مستقیم معادل

است.

Search Console API نیز ممکن است همه rows را برنگرداند و top rows را در محدودیت‌های داخلی ارائه کند؛ این limitation در derived dataset ثبت شود.

## 3. Coverage / Indexing Snapshot

Path:
`httpswww.mariwork.ir-Coverage-2026-09-24/`

Filename تاریخی حفظ می‌شود. از آن برای snapshot indexing issues استفاده می‌شود؛ جای URL Inspection زنده را نمی‌گیرد.

## 4. Raw / Derived Contract

### Raw
- immutable
- no normalization in-place
- no overwrite
- checksum/commit history preserved by repo

### Derived
هر derived output باید metadata داشته باشد:
- source path/snapshot
- generated date
- method/script
- filters
- dimensions
- assumptions
- row limits/truncation
- URL normalization rule

## 5. Standard Missing Values

- `NOT_AVAILABLE`
- `NOT_APPLICABLE`
- `UNKNOWN_NEEDS_VERIFICATION`
- `BLOCKED_BY_ACCESS`

## 6. URL History

برای legacy URL:
- historical metrics حفظ
- current status verify
- redirect chain
- current entity mapping
- canonical destination
- mapping confidence

Metrics URL قدیمی پاک یا به شکل خام merge نمی‌شود.

## 7. Date Context

هر metric:
- date range
- snapshot date
- dimension
- search type
- device/filter if any

مقایسه بدون این metadata معتبر نیست.

## 8. Server / Logs

Server evidence می‌تواند شامل:
- WP/Woo values
- responsible code
- access logs
- bot crawl evidence

باشد.

فقط داده لازم استخراج شود؛ PII/credentials وارد repo نشود.

## 9. Public Web / SERP

برای current intent و استاندارد:
- Google Search Central و Search Console docs اولویت
- schema.org برای vocabulary
- Woo/WordPress/Rank Math official docs برای رفتار platform
- competitor pages فقط برای مشاهده SERP/content gap، نه کپی متن

## 10. Analytics / Business Data

اگر Umami/Woo organic conversion data قابل‌اتکا و مجاز باشد، می‌تواند supplementary metric باشد.

نباید بدون attribution درست با Search Console یکی فرض شود.
