# Pre-Upload Content SEO Audit
# Optimized for: Travel · Restaurant · Booking (Local Business / Vietnam)

Audit content files BEFORE publishing. Local files or staging URL.

---

## Step 1 — Gather Input

Use `AskUserQuestion`:
- Input type: local folder / single file / staging URL
- Content subtype (see table below)
- Primary keyword (optional free text)

### Content Subtype & Word Count Targets

| Subtype | Code | Min Words | ToC | Notes |
|---------|------|-----------|-----|-------|
| Recipe / Công thức | `recipe` | 800 | ✗ | Step-by-step, read linearly |
| Travel guide / Hướng dẫn địa điểm | `travel-guide` | 1,000 | ✓ if >1,200 | Multi-section, reference doc |
| Destination review / Review địa điểm | `destination-review` | 600 | ✗ | Personal tone, short read |
| Restaurant review / Review nhà hàng | `restaurant-review` | 500 | ✗ | Menu, atmosphere, price |
| Activity / Trải nghiệm | `activity` | 600 | ✗ | What to expect, how to book |
| Landing page / Trang giới thiệu | `landing` | 600 | ✗ | CTA-focused |
| Service page / Dịch vụ | `service` | 800 | ✗ | Benefits, pricing, CTA |
| Booking/Event announcement | `booking` | 400 | ✗ | Date, price, CTA only |
| News / Tin tức | `news` | 400 | ✗ | Timely, factual |

For local: `Glob` + `Read`. For URL: `WebFetch`.

---

## Step 2 — 8-Point Audit

### 1. Heading Hierarchy (15%)
H1 exactly 1 with primary keyword. H2–H6 in logical order, no skipped levels.
- Recipe: H2 = Nguyên liệu / Cách làm / Lưu ý; H3 = sub-sections & steps
- Travel/Restaurant: H2 = major sections; H3 = sub-points
- Landing/Booking: H1 + H2 only, keep shallow

### 2. Readability (15%)
- Word count vs subtype minimum (see table above)
- Sentence avg 15–20 words
- Paragraph 2–4 sentences
- Vietnamese-specific: natural conversational tone ("cô bác", "bạn") preferred over formal

### 3. Image SEO (10%)
- Alt text: descriptive, include location + keyword (e.g., "bánh xèo Nha Trang giòn tan")
- Format: WebP/AVIF, compress to <200KB per image
- Dimensions: always set width + height to prevent CLS
- For restaurant/travel: minimum 3 images recommended (dish/scene, detail, ambiance)

### 4. Keyword Analysis (20%)
- Density 1–3%
- Primary keyword in: H1, first paragraph, at least 1 H2, meta description
- Semantic variations: 3–5 related terms
- Local keyword check: include city/area (e.g., "Nha Trang", "xứ Trầm") where relevant
- Generate: title tag (50–60 chars), meta description (150–160 chars)

### 5. E-E-A-T Signals (15%)
*Lower weight than generic blogs — travel/food/booking content is not YMYL.
Focus on trust signals that matter for local discovery.*

| Signal | Recipe | Travel/Review | Landing/Booking |
|--------|--------|---------------|-----------------|
| Author name | Recommended | Recommended | Optional |
| Author credentials | Optional | Optional | Not needed |
| Publication date | Recommended | Recommended | Required |
| First-hand experience | Implied via photos | Required | N/A |
| Original photos | Required | Required | Required |
| Sources/references | Not needed | Optional | Not needed |

### 6. Local SEO (10%) ← NEW — critical for this niche
- Business name consistent across page (match Google Business Profile exactly)
- Address / phone number present if service/landing page
- City/district/region keyword in H1 or first paragraph
- LocalBusiness or TouristAttraction or Restaurant schema — see Schema section
- Internal link to Google Maps or booking page
- Check: does content mention opening hours, price range, reservation method?

### 7. Schema Suggestion (10%)
Auto-detect subtype → recommend schema type → generate JSON-LD snippet.

| Subtype | Schema Type |
|---------|-------------|
| recipe | `Recipe` |
| restaurant-review / landing | `Restaurant` + `LocalBusiness` |
| travel-guide / destination-review | `TouristAttraction` or `TouristDestination` |
| activity | `Event` or `ExperienceActivity` |
| booking / event | `Event` |
| service | `LocalBusiness` + `Service` |

Also generate:
- OG tags (og:title, og:description, og:image, og:url, og:locale = vi_VN)
- Twitter Card tags

### 8. Content Structure (10%)
- ToC: only for `travel-guide` >1,200 words — skip for all other subtypes
- Internal links: 2–5 links to related content (other recipes, nearby attractions, booking page)
- CTA placement: must appear at end; for landing/booking also above the fold
- Ingredients/items: use proper HTML unordered lists, not inline text
- For restaurant/activity: include price range, hours, how-to-book info

---

## Step 3 — Score & Report

```
Content SEO Score: XX/100  [Grade]

Heading:     XX/100  ████████░░
Readability: XX/100  ██████████
Images:      XX/100  ███████░░░
Keywords:    XX/100  █████░░░░░
E-E-A-T:     XX/100  ████████░░
Local SEO:   XX/100  ██████░░░░
Schema:      XX/100  ██████░░░░
Structure:   XX/100  ███████░░░
```

### Copy-Paste Snippets
- Title tag + meta description
- OG tags (og:title, og:description, og:image, og:url, og:locale)
- Twitter Card tags
- JSON-LD schema (type auto-detected from subtype)

### Grade Scale
A (90–100) publish-ready | B (70–89) minor tweaks | C (50–69) needs work
D (30–49) significant issues | F (0–29) major rewrite

---

## Re-score: Bánh Xèo Xứ Trầm (with corrected targets)

Using subtype `recipe` (min 800 words, no ToC required):

```
Content SEO Score: 56/100  [Grade C — Needs Work]

Heading:     35/100  ███▌░░░░░░  (same — structure still broken)
Readability: 65/100  ██████▌░░░  (upgraded: 891w vs 800 target = 91% ✓)
Images:      45/100  ████▌░░░░░  (same — alt text missing)
Keywords:    70/100  ███████░░░  (same)
E-E-A-T:     40/100  ████░░░░░░  (upgraded: non-YMYL, photos present)
Local SEO:   30/100  ███░░░░░░░  (NEW — no address, no LocalBusiness schema)
Schema:      40/100  ████░░░░░░  (same — JSON-LD not implemented)
Structure:   65/100  ██████▌░░░  (same)
```

**Priority changes vs original report:**
- Readability: ~~❌ 609 từ thiếu~~ → ⚠️ Gần đủ, thêm ~100–200 từ FAQ là ổn
- ToC: ~~Recommended~~ → Không cần cho recipe
- E-E-A-T: giảm penalty vì đây không phải YMYL
- Local SEO mới: cần bổ sung địa chỉ Nha Trang Xưa + LocalBusiness schema