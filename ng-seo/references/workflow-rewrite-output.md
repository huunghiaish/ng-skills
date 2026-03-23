# Output Format Templates

## Rewritten Content File ({filename}-seo-optimized.md)

```markdown
---
title: "[Title Tag — 50-60 chars]"
description: "[Meta Description — 150-160 chars]"
author: "[Author Name]"
author_title: "[Author Title/Credentials]"
date_published: "YYYY-MM-DD"
date_modified: "YYYY-MM-DD"
primary_keyword: "[keyword]"
language: "[vi/en]"
---

# [H1 — Single, with primary keyword]

[Intro paragraph — keyword in first 100 words, hook reader, state what they'll learn]

[Author byline: **Tác giả:** Name — Title, Organization | **Ngày đăng:** DD/MM/YYYY]

## Mục lục (if >1,500 words)
- [Section links]

## [H2 Section 1 — keyword variation]

### [H3 Subsection]

[Content with proper formatting: lists, bold, short paragraphs]

## [H2 Section 2]
...

## Câu hỏi thường gặp (FAQ)

### [Question 1 — long-tail keyword?]
[Answer 2-4 sentences]

### [Question 2?]
[Answer]

## Kết luận

[Summary + CTA]

[INTERNAL_LINK: related-topic-1]
[INTERNAL_LINK: related-topic-2]

---

### Về tác giả
**[Name]** — [Credentials, experience, organization]. [1-2 sentences bio].
```

## SEO Metadata File ({filename}-seo-metadata.md)

```markdown
# SEO Metadata

## Title Tag
`[50-60 chars, keyword near start]`

## Meta Description
`[150-160 chars, with CTA]`

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

## Image Alt Text
| Image | Suggested Alt Text |
|-------|--------------------|
| [ref] | [descriptive alt] |

## Internal Link Opportunities
| Anchor Text | Suggested Target |
|-------------|-----------------|
| [text] | [topic/page] |
```

## Score Comparison (console output)

```
## SEO Score: Before → After

Before: XX/100 [Grade X]  →  After: XX/100 [Grade X]

Dimension    Before  After  Change
─────────────────────────────────────
Heading:     XX  →  XX    (+XX)  ██████████░░░░░░░░░░
Readability: XX  →  XX    (+XX)  ████████████░░░░░░░░
Images:      XX  →  XX    (+XX)  ██████████████░░░░░░
Keywords:    XX  →  XX    (+XX)  ████████████████░░░░
E-E-A-T:     XX  →  XX    (+XX)  ██████████████░░░░░░
Schema:      XX  →  XX    (+XX)  ██████████████████░░
Structure:   XX  →  XX    (+XX)  █████████████████░░░
─────────────────────────────────────
Weighted:    XX  →  XX    (+XX)

Changes Applied:
- [List each change made with dimension tag]
- [Heading] Restructured H1/H2/H3 hierarchy
- [Readability] Added FAQ section (+300 words)
- [E-E-A-T] Added author byline and credentials
- [Keywords] Optimized title tag and meta description
- [Schema] Generated Recipe JSON-LD
- [Structure] Added table of contents
```

## Word Count Tracking

Always report:
```
Word count: XXX → XXX (+XXX)
Target: X,XXX (page type: blog)
Status: ✅ Met / ❌ XXX words short
```
