---
name: ng:seo-technical
description: "Technical SEO audit: crawlability, indexability, security, URL structure, mobile, Core Web Vitals, structured data, JS rendering, IndexNow. Use for 'technical SEO', 'crawl issues', 'robots.txt', 'Core Web Vitals'."
---

# Technical SEO Audit

## Categories

### 1. Crawlability
- robots.txt: exists, valid, not blocking important resources
- XML sitemap: exists, referenced in robots.txt, valid format
- Noindex tags: intentional vs accidental
- Crawl depth: important pages within 3 clicks of homepage
- JS rendering: critical content requires JS execution?

#### AI Crawler Management
| Crawler | Company | Token | Purpose |
|---------|---------|-------|---------|
| GPTBot | OpenAI | `GPTBot` | Model training |
| ChatGPT-User | OpenAI | `ChatGPT-User` | Real-time browsing |
| ClaudeBot | Anthropic | `ClaudeBot` | Model training |
| PerplexityBot | Perplexity | `PerplexityBot` | Search + training |
| Google-Extended | Google | `Google-Extended` | Gemini training (NOT search) |

Blocking `Google-Extended` does NOT affect Search/AI Overviews (those use `Googlebot`).

### 2. Indexability
- Canonical tags: self-referencing, no conflicts with noindex
- Duplicate content: near-duplicates, www vs non-www
- Thin content: pages below minimum word counts
- Pagination, hreflang, index bloat

### 3. Security
- HTTPS enforced, valid SSL, no mixed content
- Headers: CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy

### 4. URL Structure
- Clean, descriptive, hyphenated, no query params for content
- Redirects: no chains (max 1 hop), 301 for permanent
- Flag URL >100 chars, inconsistent trailing slashes

### 5. Mobile
- Responsive design, viewport meta tag
- Touch targets: min 48x48px, font min 16px, no horizontal scroll
- Mobile-first indexing 100% complete (July 2024)

### 6. Core Web Vitals
Reference `seo/references/scoring-weights.md` for thresholds.
- **LCP** ≤2.5s | **INP** ≤200ms (replaced FID March 2024) | **CLS** ≤0.1
- 75th percentile of real user data, tiebreaker ranking signal

### 7. Structured Data
- JSON-LD preferred. Validate against Google's supported types.
- Reference `seo/references/schema-templates.md`

### 8. JavaScript SEO
- Content visible in initial HTML vs requires JS?
- CSR vs SSR identification, SPA framework flags
- Serve critical SEO elements (canonical, robots, structured data) in initial HTML

### 9. IndexNow
- Check support for Bing, Yandex, Naver (not Google)

## Output

### Technical Score: XX/100
| Category | Status | Score |
|----------|--------|-------|
| Crawlability | ✅/⚠️/❌ | XX/100 |
| Indexability | ✅/⚠️/❌ | XX/100 |
| Security | ✅/⚠️/❌ | XX/100 |
| URL Structure | ✅/⚠️/❌ | XX/100 |
| Mobile | ✅/⚠️/❌ | XX/100 |
| Core Web Vitals | ✅/⚠️/❌ | XX/100 |
| Structured Data | ✅/⚠️/❌ | XX/100 |
| JS Rendering | ✅/⚠️/❌ | XX/100 |
| IndexNow | ✅/⚠️/❌ | XX/100 |

### Issues by Priority: Critical → High → Medium → Low
