# Data

## Contract

- raw = immutable
- derived = reproducible/documented
- snapshot date = required
- date range = required
- dimensions/filters = required
- privacy minimization = required

Exportهای فعلی Search Console و Coverage/Indexing در پوشه‌های ریشه raw snapshot هستند.

داده آینده ترجیحاً:

```text
data/
└── search-console/
    └── YYYY-MM-DD-range/
        ├── raw/
        ├── derived/
        └── README.md
```

Derived README باید source، method، filters، row-limit/truncation و URL normalization را ثبت کند.

PII، credential و secret در data repository ممنوع است.
