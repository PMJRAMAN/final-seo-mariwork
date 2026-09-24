# Page Dossiers

این مسیر پرونده دائمی URLها/entities سایت را نگه می‌دارد.

پیشنهاد ساختار:

```text
pages/
├── products/
├── shop/
├── categories/
├── education/
├── articles/
├── artists/
└── static/
```

پوشه‌ها زمانی ایجاد می‌شوند که اولین پرونده آن نوع ساخته شود.

## Naming

برای WordPress/Woo entity:

`{type}-{stable-id}-{short-slug}.md`

مثال:

`product-12544-gray-122.md`

Slug برای readability است؛ ID هویت پایدار پرونده است.

برای صفحه بدون ID قابل اتکا، نام canonical و نوع صفحه با تصمیم ثبت‌شده استفاده شود.

هر page فقط **یک dossier canonical** دارد.
