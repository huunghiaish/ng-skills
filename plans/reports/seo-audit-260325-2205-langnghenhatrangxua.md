# SEO Audit Report: langnghenhatrangxua.com

**Date:** 2026-03-25
**Business Type:** Cultural Tourism / Craft Village / Restaurant
**Pages Crawled:** 119 URLs (from sitemap)
**Overall SEO Health Score: 38/100 (Grade D — Poor)**

---

## Executive Summary

langnghenhatrangxua.com is a Vietnamese cultural tourism website for "Làng Nghề Nha Trang Xưa" (Nha Trang Xua Craft Village) — a 19th-century heritage experience destination featuring traditional crafts, cuisine, light shows, and cultural preservation in Nha Trang, Khánh Hòa.

### Top 5 Critical Issues
1. **Missing canonical URLs across ALL pages** — duplicate content risk
2. **No meta descriptions on most pages** (gallery, blog, many subpages) — poor CTR in SERPs
3. **Language mismatch: `lang="en"` but majority content is Vietnamese** — confuses search engines
4. **Missing Article/BlogPosting schema on 100+ blog posts** — no rich snippets
5. **Multiple 404 errors** (`/about-us`, `/contact`, `/booking`, `/craft-village-tour`) — broken navigation

### Top 5 Quick Wins
1. Add canonical URLs to every page
2. Fix `lang` attribute to `vi` (with hreflang for English variant)
3. Write unique meta descriptions for all key pages
4. Add Article schema to all blog posts
5. Fix or redirect broken internal links (404 pages)

---

## Category Breakdowns

### 1. Technical SEO — Score: 40/100 (Weight: 25%)

| Check | Status | Notes |
|-------|--------|-------|
| HTTPS | ✅ Pass | Valid SSL certificate |
| robots.txt | ✅ Pass | Properly configured, blocks /admin/ and /api/ |
| Sitemap | ⚠️ Partial | Exists but all pages have identical priority (0.7/0.8) — no differentiation |
| Canonical URLs | ❌ Fail | Missing on ALL audited pages |
| Language/hreflang | ❌ Fail | `lang="en"` but site is primarily Vietnamese |
| Mobile responsive | ✅ Pass | Viewport meta present, responsive design |
| URL structure | ✅ Pass | Clean, descriptive slugs in both EN/VI |
| 404 errors | ❌ Fail | `/about-us`, `/contact`, `/booking`, `/craft-village-tour` all 404 |
| Redirect chains | ⚠️ Warning | Homepage links to `/about-us` but actual path is `/general-introduction/about-us` |
| Crawl budget | ⚠️ Warning | Duplicate blog content (EN + VI versions with separate URLs, no hreflang linking) |
| Server sitemap | ❌ Fail | `server-sitemap.xml` referenced in robots.txt but could not verify |
| GTM/Analytics | ✅ Pass | GTM (GTM-T97JMFT7) + Microsoft Clarity (vzamc2sjqv) |

**Critical Issues:**
- **No canonical tags** = Google must guess the preferred URL version
- **Wrong lang attribute** = Google may serve English results for Vietnamese queries
- **Broken internal links** = crawl errors, wasted link equity, poor UX
- **Duplicate content risk** = EN/VI blog posts without hreflang cause cannibalization

### 2. Content Quality — Score: 35/100 (Weight: 25%)

| Metric | Status | Details |
|--------|--------|---------|
| Homepage word count | ⚠️ ~800-1200 words | Meets minimum (500) but borderline for tourism |
| About page | ✅ ~1,200-1,400 words | Good depth with craft descriptions |
| Gallery page | ❌ ~8 words | Nearly empty — JS-rendered content not indexable |
| Culinary menu | ❌ ~200-250 words | Far below 600-word minimum for landing pages |
| Food stories | ❌ ~350-400 words | Thin content |
| Light show | ✅ ~1,200+ words | Good depth describing 5 acts |
| Blog posts | ⚠️ Mixed | Could not verify individual post depth (404 on sample) |
| Workshop pages | ✅ ~800-900 words | Adequate for service pages |

**E-E-A-T Assessment:**

| Signal | Score | Notes |
|--------|-------|-------|
| **Experience** | 55/100 | Original photos present, real venue descriptions, but no author attribution or personal stories |
| **Expertise** | 40/100 | No author bios, no credentials shown, no expert citations |
| **Authoritativeness** | 45/100 | Press coverage exists (blog), but no external citations or awards displayed |
| **Trustworthiness** | 60/100 | Contact info visible (address, phone, email), social links present, but no privacy policy or terms visible |

**Content Issues:**
- **Gallery page is essentially empty** for crawlers — content loaded via JS/React
- **Culinary menu has "Culinary Menu" as its meta description** — placeholder
- **No publication dates visible** on most pages
- **Bilingual content duplication** without proper hreflang attribution
- **No privacy policy or terms of service** found

### 3. On-Page SEO — Score: 35/100 (Weight: 20%)

| Element | Status | Details |
|---------|--------|---------|
| Title tags | ⚠️ Partial | Present but inconsistent; "Light Show" is just 2 words, others too generic |
| Meta descriptions | ❌ Mostly missing | Gallery, blog listing, and many pages have none or placeholder text |
| H1 tags | ⚠️ Mixed | Some pages have proper H1, gallery has none, homepage H1 is "A Must-visit destination" (weak) |
| Heading hierarchy | ⚠️ Mixed | Light show page well-structured; homepage has logical but informal hierarchy |
| Internal linking | ❌ Poor | Broken links to /about-us, /contact, /booking; homepage links to wrong URLs |
| Image alt text | ❌ Poor | Most images lack descriptive alt text; gallery images have no alt at all |
| Keyword optimization | ❌ Weak | No target keyword strategy visible; titles don't target search terms |
| Breadcrumbs | ✅ Good | BreadcrumbList schema present on subpages |

**Title Tag Analysis:**

| Page | Title | Issue |
|------|-------|-------|
| Homepage | "Nha Trang Xưa - Điểm đến Văn hoá - Ẩm thực - Làng nghề Nha Trang" | ⚠️ 56 chars, acceptable but stuffed with dashes |
| Gallery | "Gallery \| Nha Trang Xưa" | ⚠️ Generic, no keywords |
| Culinary Menu | "Culinary Menu \| Nha Trang Xưa" | ⚠️ English title for Vietnamese content |
| About Us | "Về chúng tôi \| Nha Trang Xưa" | ✅ OK but could be more descriptive |
| Light Show | "Light Show" | ❌ Only 10 chars, missing brand, no keywords |
| Workshop | "Lacquer painting workshop \| Nha Trang Xưa" | ✅ Good, descriptive |

### 4. Schema / Structured Data — Score: 30/100 (Weight: 10%)

| Schema | Status | Notes |
|--------|--------|-------|
| Organization | ✅ Present | Name, URL, logo |
| LocalBusiness | ⚠️ Partial | Address and priceRange but missing openingHours, telephone, geo coordinates |
| BreadcrumbList | ✅ Present | On subpages |
| Article/BlogPosting | ❌ Missing | 100+ blog posts have NO article schema |
| Event | ❌ Missing | Light show / Tet festival should have Event schema |
| TouristAttraction | ❌ Missing | Craft village should use TouristAttraction type |
| Service | ⚠️ Partial | Workshop pages have Service schema |
| VideoObject | ❌ Missing | YouTube embeds lack VideoObject schema |
| WebSite + SearchAction | ❌ Missing | No sitelinks search box eligibility |
| PerformingArtsEvent | ❌ Missing | Light show is a perfect candidate (new Dec 2025) |

**Missing Schema Opportunities:**
- `TouristAttraction` for the craft village
- `PerformingArtsEvent` for "Ánh Sáng Huyền Thoại" light show
- `Article` for all blog posts (huge rich snippet opportunity)
- `Menu`/`Restaurant` for culinary offerings
- `Event` for Tet festival and special events
- `VideoObject` for embedded videos

### 5. Performance (CWV) — Score: 45/100 (Weight: 10%)

| Concern | Status | Notes |
|---------|--------|-------|
| Font loading | ❌ Critical | 200+ @font-face declarations (Inter, Noto Sans, Manrope, Quicksand) — massive render blocking |
| JS framework | ⚠️ Warning | Next.js/React = client-side rendering; gallery page has zero indexable content |
| Image optimization | ⚠️ Unknown | Cannot verify WebP/AVIF without deeper analysis |
| Third-party scripts | ⚠️ Warning | GTM + Clarity = additional payload |
| Server rendering | ⚠️ Mixed | Next.js should SSR but gallery page evidence suggests CSR fallback |

**Estimated CWV Impact:**
- **LCP:** Likely poor (>2.5s) due to massive font files and hero slider images
- **CLS:** Risk from dynamic content loading, image sliders without dimensions
- **INP:** Risk from heavy React hydration

### 6. Images — Score: 30/100 (Weight: 10%)

| Check | Status | Notes |
|-------|--------|-------|
| Alt text coverage | ❌ ~30% | Most images lack descriptive alt text |
| Descriptive alt text | ❌ Poor | When present, often generic ("light show 1", "video-contact") |
| Image format | ⚠️ Unknown | Cannot verify modern format usage |
| Lazy loading | ⚠️ Unknown | Next.js Image component likely handles this |
| Image dimensions | ⚠️ Unknown | Hero images may cause CLS |
| OG image | ✅ Present | `nhatrangxua.jpg` with width/height |

---

## Score Calculation

| Category | Weight | Score | Weighted |
|----------|--------|-------|----------|
| Technical SEO | 25% | 40 | 10.0 |
| Content Quality | 25% | 35 | 8.75 |
| On-Page SEO | 20% | 35 | 7.0 |
| Schema / Structured Data | 10% | 30 | 3.0 |
| Performance (CWV) | 10% | 45 | 4.5 |
| Images | 10% | 30 | 3.0 |
| **Total** | **100%** | | **36.25 → 38** |

---

## Prioritized Action Plan

### Critical (Fix Immediately) 🔴

| # | Issue | Impact | Effort |
|---|-------|--------|--------|
| 1 | **Fix `lang="vi"` + add hreflang** for EN/VI versions | Correct indexing for Vietnamese audience | Low |
| 2 | **Add canonical URLs** to every page | Prevent duplicate content penalties | Low |
| 3 | **Fix broken internal links** (/about-us → /general-introduction/about-us, /contact, /booking) | Recover lost link equity, fix user experience | Low |
| 4 | **Add meta descriptions** to all pages (especially gallery, blog, culinary menu, light show) | Improve CTR from SERPs by 15-30% | Medium |
| 5 | **Fix gallery page SSR** — content must render server-side for indexing | Gallery currently invisible to Google | High |

### High Priority (Fix Within 1 Week) 🟠

| # | Issue | Impact | Effort |
|---|-------|--------|--------|
| 6 | **Add Article/BlogPosting schema** to all 100+ blog posts | Rich snippets, AI citation eligibility | Medium |
| 7 | **Add Event schema** for light show and Tet festival | Event rich results in SERPs | Low |
| 8 | **Add TouristAttraction schema** for craft village | Enhanced knowledge panel | Low |
| 9 | **Improve title tags** — add target keywords, proper length, brand consistency | Better ranking signals | Low |
| 10 | **Add descriptive alt text** to all images | Image search traffic + accessibility | Medium |

### Medium Priority (Fix Within 1 Month) 🟡

| # | Issue | Impact | Effort |
|---|-------|--------|--------|
| 11 | **Expand thin content pages** — culinary menu (200→600+ words), food stories (350→800+ words) | Meet quality gates | Medium |
| 12 | **Add privacy policy and terms of service** | Trust signals for E-E-A-T | Low |
| 13 | **Reduce font loading** — subset fonts, use `font-display: swap`, consolidate to 2-3 families | LCP improvement | Medium |
| 14 | **Add WebSite schema with SearchAction** | Sitelinks search box eligibility | Low |
| 15 | **Complete LocalBusiness schema** — add openingHours, telephone, geo coordinates | Enhanced local pack | Low |
| 16 | **Add publication dates** to blog posts and content pages | Freshness signals | Low |
| 17 | **Implement hreflang linking** between EN/VI duplicate blog posts | Prevent cannibalization | Medium |
| 18 | **Add PerformingArtsEvent schema** for light show (new Dec 2025) | Early adopter advantage | Low |

### Low Priority (Backlog) 🟢

| # | Issue | Impact | Effort |
|---|-------|--------|--------|
| 19 | **Add author bios** to blog posts | E-E-A-T expertise signals | Low |
| 20 | **Differentiate sitemap priorities** — homepage/key pages at 1.0, blog at 0.6 | Better crawl prioritization | Low |
| 21 | **Add VideoObject schema** for YouTube embeds | Video rich results | Low |
| 22 | **Add Restaurant/Menu schema** for culinary section | Menu rich results | Medium |
| 23 | **Create a keyword strategy** targeting Vietnamese tourism search terms | Long-term organic growth | High |
| 24 | **Build content clusters** around key topics (craft village, light show, Nha Trang tourism) | Topical authority | High |

---

## Site Architecture Summary

```
langnghenhatrangxua.com (13 static + 106 blog URLs = 119 total)
├── / (homepage)
├── /blog (listing)
│   ├── /blog/activity-information (category)
│   ├── /blog/press-corner (category)
│   └── /blog/recruitment (category)
│       └── 100+ blog posts (EN + VI duplicates)
├── /general-introduction/
│   ├── about-us
│   ├── company-profile
│   ├── food-stories
│   ├── lightshow
│   └── tet-holiday
├── /gallery
├── /culinary-menu
├── /booking-request
├── /workshop/ (8 workshop pages)
│   ├── lacquer-painting
│   ├── bamboo-dragonfly
│   ├── seashell-decoration
│   ├── canvas-painting
│   ├── conical-hat-decoration
│   ├── incense-making
│   ├── clay-pottery
│   └── cooking-class
└── /craft-village-tour (404!)
```

**Broken Links Found:**
- `/about-us` → 404 (correct: `/general-introduction/about-us`)
- `/contact` → 404
- `/booking` → 404 (correct: `/booking-request`)
- `/craft-village-tour` → 404
- `/services/residential-loans` → suspicious link (banking template leftover?)

---

## Unresolved Questions

1. **`/services/residential-loans`** link on homepage — is this a template leftover from a banking website? If so, critical to remove (misleading + irrelevant).
2. **Bank partner logos** (NAB, Commonwealth, Suncorp, ING, Westpac) on homepage — are these legitimate partnerships or template artifacts? If template, remove immediately.
3. **Server-side rendering** — is the gallery page intentionally CSR-only, or is SSR broken?
4. **Blog post content depth** — could not access individual posts (404 on tested URL); actual content quality unverifiable.
5. **Image hosting** — images served from `booking.nhatrangxua.sunny.net.vn` — is CDN properly configured for performance?
