# Output Format Templates
# Optimized for: Travel · Restaurant · Booking (Local Business / Vietnam)

---

## Rewritten Content File ({filename}-seo-optimized.md)

```markdown
---
title: "[Title Tag — 50-60 chars, keyword + location near start]"
description: "[Meta Description — 150-160 chars]"
author: "[Author Name]"
author_title: "[Author Title/Credentials]"
date_published: "YYYY-MM-DD"
date_modified: "YYYY-MM-DD"
primary_keyword: "[keyword]"
content_subtype: "[recipe|travel-guide|destination-review|restaurant-review|activity|landing|service|booking|news]"
language: "vi"
---

# [H1 — Single, with primary keyword + location where relevant]

[Intro paragraph — keyword + city/area in first 100 words, hook reader, state what they'll learn]

**Tác giả:** [Tên] — [Chức danh], [Tổ chức] | **Ngày đăng:** DD/MM/YYYY

---

## [H2 Section 1 — keyword variation]

### [H3 Subsection]

[Content with proper formatting: lists, bold key phrases, short paragraphs]

## [H2 Section 2]
...

## Câu hỏi thường gặp (FAQ)
*(Add for recipe, travel-guide, restaurant-review — skip for landing/booking/news)*

### [Question 1 — long-tail keyword phrase?]
[Answer 2-4 sentences]

### [Question 2?]
[Answer]

## Kết luận

[Summary + CTA]

[INTERNAL_LINK: related-topic-1]
[INTERNAL_LINK: related-topic-2]
[INTERNAL_LINK: booking-page or google-maps]

---

### Về tác giả
*(Recommended for recipe/travel-guide, optional for review)*
**[Tên]** — [Credentials, experience, organization]. [1-2 sentences bio].
```

---

## SEO Metadata File ({filename}-seo-metadata.md)

```markdown
# SEO Metadata

## Title Tag
`[50-60 chars, keyword + location near start]`

## Meta Description
`[150-160 chars, keyword + location + CTA]`

## JSON-LD Schema
​```json
{ ... }
​```

## Open Graph Tags
​```html
<meta property="og:title" content="..." />
<meta property="og:description" content="..." />
<meta property="og:type" content="article" />
<meta property="og:image" content="[URL]" />
<meta property="og:url" content="[URL]" />
<meta property="og:locale" content="vi_VN" />
​```

## Twitter Card
​```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="..." />
<meta name="twitter:description" content="..." />
<meta name="twitter:image" content="[URL]" />
​```

## Local SEO Block
*(Include for restaurant-review, landing, service, activity subtypes)*
​```html
<!-- NAP Block — keep consistent with Google Business Profile -->
<p>
  <strong>[Tên doanh nghiệp]</strong><br>
  📍 [Địa chỉ], [Quận], [Thành phố]<br>
  📞 <a href="tel:[SĐT]">[SĐT]</a><br>
  🕐 [Giờ mở cửa]<br>
  🔗 <a href="[URL đặt chỗ]">Đặt bàn / Đặt tour</a> |
      <a href="[Google Maps URL]">Xem bản đồ</a>
</p>
​```

## Image Alt Text
| Image | Suggested Alt Text |
|-------|--------------------|
| [ref] | [subject + detail + location keyword] |

## Internal Link Opportunities
| Anchor Text | Suggested Target |
|-------------|-----------------|
| [text] | [topic/page] |
| Đặt bàn tại [tên] | [booking page] |
| Xem bản đồ | [Google Maps listing] |
```

---

## Score Comparison (seo-rewrite-{date}-{slug}.md)

```
## SEO Score: Before → After

Before: XX/100 [Grade X]  →  After: XX/100 [Grade X]

Dimension    Before  After  Change
─────────────────────────────────────
Heading:     XX  →  XX    (+XX)  ████████████░░░░░░░░
Readability: XX  →  XX    (+XX)  ██████████████░░░░░░
Images:      XX  →  XX    (+XX)  ████████████░░░░░░░░
Keywords:    XX  →  XX    (+XX)  ████████████████░░░░
E-E-A-T:     XX  →  XX    (+XX)  ██████████████░░░░░░
Local SEO:   XX  →  XX    (+XX)  ████████████████░░░░
Schema:      XX  →  XX    (+XX)  ██████████████████░░
Structure:   XX  →  XX    (+XX)  █████████████████░░░
─────────────────────────────────────
Weighted:    XX  →  XX    (+XX)

Changes Applied:
- [Heading] Restructured H1/H2/H3 hierarchy
- [Readability] Added FAQ section (+XXX words)
- [E-E-A-T] Added author byline and publication date
- [Keywords] Optimized title tag, meta description, local keyword layer
- [Local SEO] Added NAP block, city keyword in H1/intro, maps link
- [Schema] Generated [type] JSON-LD + OG + Twitter Card
- [Structure] [ToC added / skipped per subtype rule]
```

---

## Word Count Tracking

Always report:
```
Word count: XXX → XXX (+XXX)
Target: X,XXX (subtype: [code])
Status: ✅ Met / ⚠️ Close (within 10%) / ❌ XXX words short
```

## Subtype Quick Reference (for report)

| Subtype | Min | ToC rule |
|---------|-----|----------|
| `recipe` | 800 | Never |
| `travel-guide` | 1,000 | Only if >1,200 words |
| `destination-review` | 600 | Never |
| `restaurant-review` | 500 | Never |
| `activity` | 600 | Never |
| `landing` | 600 | Never |
| `service` | 800 | Never |
| `booking` | 400 | Never |
| `news` | 400 | Never |