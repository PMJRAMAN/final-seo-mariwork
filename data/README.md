# Data

این مسیر برای داده‌های SEO پروژه است.

## قانون

- raw = immutable
- derived = reproducible/documented
- snapshot date اجباری
- date range اجباری
- dimension اجباری

Exportهای فعلی Search Console و Coverage هنوز در پوشه‌های اولیه ریشه repository قرار دارند و raw محسوب می‌شوند.

جابجایی آن‌ها فقط با حفظ تاریخچه، عدم تغییر محتوا و ثبت تصمیم انجام می‌شود.

داده‌های آینده ترجیحاً:

```text
data/
└── search-console/
    └── YYYY-MM-DD-range/
        ├── raw/
        ├── derived/
        └── README.md
```
