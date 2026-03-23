# Rewrite Strategies by Dimension

Fix strategies for each of the 7 SEO audit dimensions. Apply only to dimensions scoring < 70.

## 1. Heading Hierarchy (target: 90+)

**Diagnosis:** Count H1/H2/H3 tags. Check for skipped levels, duplicate H1, untagged sections.

**Fixes:**
- Exactly 1× H1 containing primary keyword
- Every major section → H2 (ingredients, steps, tips, FAQ)
- Every subsection → H3 (individual steps, ingredient groups)
- Never skip levels (H1 → H3 without H2)
- Include keyword variations in H2s naturally

**Pattern:**
```
H1: [Primary keyword + compelling modifier]
  H2: [Section with keyword variation]
    H3: [Subsection detail]
    H3: [Subsection detail]
  H2: [Next section]
```

## 2. Readability (target: 80+)

**Diagnosis:** Word count vs page type minimum. Sentence length. Paragraph density.

**Word count targets:**
| Page Type | Minimum | Ideal |
|-----------|---------|-------|
| Blog | 1,500 | 2,000-2,500 |
| Landing | 600 | 800-1,200 |
| Product | 400 | 600-800 |
| Service | 800 | 1,000-1,500 |

**Expansion strategies (add, don't replace):**

1. **Expand intro** — add context, history, cultural significance, why this topic matters
2. **Add "Mẹo/Tips" section** — common mistakes, pro tips, troubleshooting
3. **Add FAQ section** — 3-5 questions readers commonly ask (long-tail keyword capture)
4. **Add comparison/variation** — regional variations, alternatives, customization options
5. **Add nutrition/specs** — factual data section (calories, dimensions, specifications)
6. **Expand existing steps** — add "why" explanations, not just "how"
7. **Add "Lưu ý/Notes" section** — storage tips, shelf life, reheating instructions

**Readability rules:**
- Sentences: avg 15-20 words, max 30
- Paragraphs: 2-4 sentences
- Use transition words between sections
- Break walls of text with lists, subheadings, bold key phrases

## 3. Image SEO (target: 75+)

**Diagnosis:** Count images, check alt text, format, dimensions.

**Alt text formula:**
```
[Descriptive action/subject] + [relevant detail] + [context keyword]
```

**Examples:**
- "Đĩa bánh xèo vàng giòn với nhân tôm thịt" (not "hình 1" or "banh-xeo.jpg")
- "Dashboard showing monthly revenue chart" (not "screenshot" or "image")

**Rules:**
- 10-125 characters per alt text
- Include keyword naturally in 1-2 image alts (not all)
- Decorative images: suggest `alt=""`
- Suggest WebP/AVIF format, <200KB, explicit width/height

**Output:** Table of image references → suggested alt text.

## 4. Keyword Analysis (target: 85+)

**Diagnosis:** Keyword in H1, first paragraph, density, semantic variations.

**Placement checklist:**
- [ ] Primary keyword in H1
- [ ] Primary keyword in first 100 words
- [ ] Primary keyword in at least 1 H2
- [ ] 3-5 semantic variations throughout
- [ ] Density 1-3% (count occurrences / total words)
- [ ] No keyword stuffing (reads naturally)

**Title tag formula (50-60 chars):**
```
[Action/How-to] + [Primary Keyword] + [Compelling Modifier]
```

**Meta description formula (150-160 chars):**
```
[Hook/Promise] + [Primary Keyword] + [Key Detail] + [CTA or Benefit]
```

**Long-tail expansion:** Add 2-3 long-tail variations naturally in content body, FAQ answers, and H3 headings.

## 5. E-E-A-T Signals (target: 80+)

**Diagnosis:** Check for author info, dates, sources, first-hand experience signals.

**Required additions:**

### Author Attribution (Critical)
```markdown
---
**Tác giả:** [Tên] — [Chức danh], [Tổ chức]
**Ngày đăng:** [DD/MM/YYYY]
**Cập nhật lần cuối:** [DD/MM/YYYY]
---
```

### Experience Signals
- Add first-person experience statement in intro ("Sau 10 năm...", "Qua kinh nghiệm...")
- Reference specific details only someone with experience would know
- Mention original photos/testing/methodology

### Expertise Signals
- Add "Về tác giả" section at bottom with credentials
- Reference sources (cite 2-3 authoritative links)
- Use precise, technical language appropriate for topic

### Trust Signals
- Publication date visible
- "Last updated" date if content revised
- Link to author profile page
- Contact information or organization reference

**Ask user for:** Author name, title, credentials, organization. Never fabricate.

## 6. Schema Markup (target: 90+)

**Diagnosis:** Check if JSON-LD, OG tags, Twitter Card exist.

**Auto-detect schema type:**
| Content Pattern | Schema Type |
|----------------|-------------|
| Ingredients + steps | Recipe |
| How-to steps (non-food) | Article (HowTo deprecated) |
| Product description + price | Product |
| Business info + location | LocalBusiness |
| Blog post / article | Article or BlogPosting |
| FAQ section | Article (FAQPage restricted) |
| Event details | Event |

**Generate all three:**
1. JSON-LD (primary — in `<script type="application/ld+json">`)
2. OG tags (og:title, og:description, og:image, og:url, og:type, og:locale)
3. Twitter Card (twitter:card, twitter:title, twitter:description, twitter:image)

**Validation:** @context = "https://schema.org", @type valid (non-deprecated), all required props present, URLs absolute, dates ISO 8601.

## 7. Content Structure (target: 85+)

**Diagnosis:** Check logical flow, lists, ToC, internal links, CTA.

**Fixes:**

### Table of Contents
Add if word count > 1,500:
```markdown
## Mục lục
- [Section 1](#section-1)
- [Section 2](#section-2)
...
```

### Internal Links
- Add 3-5 per 1,000 words
- Use descriptive anchor text (not "click here")
- Mark with `[INTERNAL_LINK: topic]` placeholder if URLs unknown

### Lists & Formatting
- Ingredients → unordered list (bullet points)
- Steps → ordered list (numbered)
- Comparisons → table
- Key points → bold or callout

### FAQ Section
Add 3-5 questions:
- Use natural question phrasing ("Làm sao...?", "Có thể...?", "Tại sao...?")
- Answer in 2-4 sentences each
- Include long-tail keywords in questions
- Place after main content, before conclusion

### CTA
- Verify CTA exists (subscribe, share, comment, buy, visit)
- Place primary CTA after conclusion
- Optional secondary CTA mid-content
