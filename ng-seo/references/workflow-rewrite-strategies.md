# Rewrite Strategies by Dimension
# Optimized for: Travel · Restaurant · Booking (Local Business / Vietnam)

Fix strategies for each of the 8 SEO audit dimensions. Apply only to dimensions scoring < 70.

---

## 1. Heading Hierarchy (target: 90+)

**Diagnosis:** Count H1/H2/H3 tags. Check for skipped levels, duplicate H1, untagged sections.

**Fixes:**
- Exactly 1× H1 containing primary keyword
- Every major section → H2 (ingredients, steps, tips, FAQ)
- Every subsection → H3 (individual steps, ingredient groups)
- Never skip levels (H1 → H3 without H2)
- Include keyword variations in H2s naturally

**Pattern by subtype:**
```
recipe:
  H1: [Primary keyword + modifier]
    H2: Nguyên liệu
      H3: Phần bột / Phần nhân / Ăn kèm
    H2: Cách làm
      H3: Bước 1–N
    H2: Lưu ý / Mẹo

travel-guide:
  H1: [Destination + keyword]
    H2: Tổng quan
    H2: Địa điểm nổi bật
      H3: [Place 1], [Place 2]...
    H2: Kinh nghiệm di chuyển
    H2: Ăn uống / Lưu trú
    H2: FAQ

restaurant-review:
  H1: [Restaurant name + keyword]
    H2: Không gian & Vị trí
    H2: Thực đơn nổi bật
    H2: Giá cả & Đặt bàn
    H2: Nhận xét tổng thể
```

---

## 2. Readability (target: 80+)

**Diagnosis:** Word count vs subtype minimum. Sentence length. Paragraph density.

**Word count targets by subtype:**

| Subtype | Minimum | Ideal |
|---------|---------|-------|
| `recipe` | 800 | 900–1,100 |
| `travel-guide` | 1,000 | 1,200–1,800 |
| `destination-review` | 600 | 700–900 |
| `restaurant-review` | 500 | 600–800 |
| `activity` | 600 | 700–900 |
| `landing` | 600 | 800–1,000 |
| `service` | 800 | 1,000–1,400 |
| `booking` | 400 | 400–600 |
| `news` | 400 | 400–600 |

**Expansion strategies by subtype (add, don't replace):**

**recipe:**
1. Expand intro — history, cultural significance, regional variations
2. Add "Mẹo chọn nguyên liệu" — how to pick fresh ingredients
3. Add FAQ — "Làm sao giữ bánh giòn lâu?", "Có thể thay nước dừa bằng gì?"
4. Expand steps with "why" explanations, not just "how"
5. Add storage/reheating tips

**travel-guide / destination-review:**
1. Add destination overview — geography, best time to visit, vibe
2. Add "Cách di chuyển" section — transport options, distances, cost
3. Add "Kinh nghiệm thực tế" — first-person tips, common mistakes
4. Add FAQ — "Có nên đặt trước không?", "Mùa nào đẹp nhất?"
5. Add nearby attractions or day-trip suggestions

**restaurant-review:**
1. Expand atmosphere description — decor, noise level, seating
2. Add dish-by-dish breakdown of standouts
3. Add price range context — "ngon mà không đắt" framing
4. Add parking, booking, hours info
5. Compare to similar restaurants in the area

**landing / service / booking:**
1. Add social proof — testimonials, number of guests, ratings
2. Expand benefits section — what makes this experience unique
3. Add FAQ addressing objections
4. Add clear booking/contact process steps

**Readability rules (all subtypes):**
- Sentences: avg 15-20 words, max 30
- Paragraphs: 2-4 sentences
- Use transition words between sections
- Break walls of text with lists, subheadings, bold key phrases
- Vietnamese tone: conversational ("cô bác", "bạn") preferred over formal

---

## 3. Image SEO (target: 75+)

**Diagnosis:** Count images, check alt text, format, dimensions.

**Alt text formula:**
```
[Descriptive subject] + [relevant detail] + [location/context keyword]
```

**Examples for travel/restaurant niche:**
- "Bánh xèo xứ Trầm Nha Trang vàng giòn nhân tôm thịt"
- "Không gian nhà hàng Nha Trang Xưa mang phong cách cổ xứ Trầm"
- "Hồ bơi resort Nha Trang view biển"

**Rules:**
- 10–125 characters per alt text
- Include primary keyword naturally in 1-2 image alts (not all)
- Location keyword (e.g., "Nha Trang", "xứ Trầm") in at least 1 alt
- Decorative images: suggest `alt=""`
- Suggest WebP/AVIF format, <200KB, explicit width/height
- For restaurant/travel: recommend minimum 3 images (dish/scene, detail, ambiance)

**Output:** Table of image references → suggested alt text.

---

## 4. Keyword Analysis (target: 85+)

**Diagnosis:** Keyword in H1, first paragraph, density, semantic variations, local terms.

**Placement checklist:**
- [ ] Primary keyword in H1
- [ ] Primary keyword in first 100 words
- [ ] Primary keyword in at least 1 H2
- [ ] City/area keyword (e.g., "Nha Trang", "miền Trung") in H1 or first paragraph
- [ ] 3–5 semantic variations throughout
- [ ] Density 1–3% (count occurrences / total words)
- [ ] No keyword stuffing (reads naturally)

**Local keyword layer:**
- Always combine primary keyword + location for travel/restaurant content
- Example: "bánh xèo" → "bánh xèo Nha Trang", "bánh xèo xứ Trầm", "cách làm bánh xèo miền Trung"
- Add district/neighborhood if relevant: "Nha Trang", "Khánh Hòa", "xứ Trầm"

**Title tag formula (50-60 chars):**
```
[Action/Keyword] + [Location] + [Compelling Modifier]
```

**Meta description formula (150-160 chars):**
```
[Hook/Promise] + [Primary Keyword] + [Location detail] + [CTA or Benefit]
```

---

## 5. E-E-A-T Signals (target: 75+)

*Lower weight (15%) for travel/food/booking — not YMYL. Focus on trust signals
that matter for local discovery, not academic credentials.*

**Diagnosis:** Author info, dates, first-hand experience, original photos.

**Priority by subtype:**

| Signal | recipe | travel/review | restaurant | landing/booking |
|--------|--------|---------------|------------|-----------------|
| Author name | Recommended | Recommended | Recommended | Optional |
| Author credentials | Optional | Optional | Optional | Not needed |
| Publication date | Required | Required | Required | Required |
| First-hand experience | Implied via photos | Required | Required | N/A |
| Original photos | Required | Required | Required | Required |
| Sources/references | Not needed | Optional | Not needed | Not needed |

**Author attribution block:**
```markdown
**Tác giả:** [Tên] — [Chức danh], [Tổ chức]
**Ngày đăng:** DD/MM/YYYY | **Cập nhật:** DD/MM/YYYY
```

**Experience signals to add:**
- First-person statements: "Qua nhiều năm nấu ăn tại...", "Trong chuyến thăm gần nhất..."
- Specific details only someone with experience would know
- Reference original photos taken on-site

**"Về tác giả" section (recommended for blog/guide, optional for review):**
```markdown
### Về tác giả
**[Tên]** — [Chức danh]. [1-2 câu bio ngắn về kinh nghiệm liên quan].
```

Never fabricate credentials — ask user for real info.

---

## 6. Local SEO (target: 80+) ← NEW

*Critical for travel/restaurant/booking — this is how local customers find you.*

**Diagnosis:** Business name consistency, address/phone, city keyword, maps link, hours/booking info.

**Checklist:**
- [ ] Business name matches Google Business Profile exactly (no variations)
- [ ] City/district keyword in H1 or first 100 words
- [ ] Address present (if service/landing/restaurant page)
- [ ] Phone number or booking link present
- [ ] Opening hours mentioned (if applicable)
- [ ] Price range mentioned (if applicable)
- [ ] Link to Google Maps or booking platform
- [ ] LocalBusiness / Restaurant / TouristAttraction schema (see Schema section)

**NAP block (add to service/restaurant/landing pages):**
```markdown
**[Tên doanh nghiệp]**
📍 [Địa chỉ đầy đủ], [Quận/Huyện], [Thành phố]
📞 [Số điện thoại]
🕐 [Giờ mở cửa]
🔗 [Link đặt chỗ / Google Maps]
```

**City keyword integration:**
- Mention city/area in first paragraph naturally
- Use in at least 1 H2 (e.g., "Đặt bàn tại Nha Trang Xưa")
- Include in meta description and title tag
- Add to 1-2 image alt texts

**Internal link requirements:**
- Link to Google Maps listing
- Link to booking/reservation page
- Link to related content (other dishes, nearby attractions, cooking class page)

---

## 7. Schema Markup (target: 90+)

**Diagnosis:** Check if JSON-LD, OG tags, Twitter Card exist.

**Auto-detect schema type by subtype:**

| Subtype | Schema Type |
|---------|-------------|
| `recipe` | `Recipe` |
| `restaurant-review` / `landing` (restaurant) | `Restaurant` + `LocalBusiness` |
| `travel-guide` / `destination-review` | `TouristAttraction` or `TouristDestination` |
| `activity` | `ExperienceActivity` or `Event` |
| `booking` / event announcement | `Event` |
| `service` | `LocalBusiness` + `Service` |
| `news` | `NewsArticle` |

**LocalBusiness schema block (for restaurant/service/landing):**
```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "[Tên doanh nghiệp]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Địa chỉ]",
    "addressLocality": "Nha Trang",
    "addressRegion": "Khánh Hòa",
    "addressCountry": "VN"
  },
  "telephone": "[SĐT]",
  "url": "[URL trang chủ]",
  "servesCuisine": "Vietnamese",
  "priceRange": "$$"
}
```

**Generate all three outputs:**
1. JSON-LD (primary — in `<script type="application/ld+json">`)
2. OG tags (og:title, og:description, og:image, og:url, og:type, og:locale = vi_VN)
3. Twitter Card (twitter:card, twitter:title, twitter:description, twitter:image)

**Validation:** @context = "https://schema.org", @type valid, all required props present,
URLs absolute, dates ISO 8601.

---

## 8. Content Structure (target: 85+)

**Diagnosis:** Logical flow, lists, ToC, internal links, CTA.

**Table of Contents — subtype rules:**
- `travel-guide` >1,200 words → add ToC ✓
- All other subtypes → skip ToC ✗
- Never add ToC to recipe, review, booking, news

**Internal links (2-5 per post):**
- Use descriptive anchor text (not "click here" or "xem thêm")
- Mark with `[INTERNAL_LINK: topic]` placeholder if URLs unknown
- For restaurant/travel: always link to booking page + Google Maps

**Lists & Formatting:**
- Ingredients → unordered list (bullet)
- Steps → ordered list (numbered)
- Comparisons → table
- Key facts (hours, price, address) → definition list or bold label

**FAQ Section (add for recipe, travel-guide, restaurant-review):**
- 3-5 questions, natural phrasing
- Include long-tail keywords in questions
- Answer in 2-4 sentences each
- Place after main content, before conclusion

**CTA rules by subtype:**

| Subtype | CTA type | Placement |
|---------|----------|-----------|
| `recipe` | Cooking class / related recipe | End of article |
| `travel-guide` | Book tour / visit attraction | End + mid-content |
| `restaurant-review` | Book table / view menu | End of article |
| `landing` / `service` | Book now / Contact | Above fold + end |
| `booking` | Reserve / Register | Prominent, multiple |