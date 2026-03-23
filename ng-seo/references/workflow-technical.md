# Technical SEO Audit (9 Categories)

### 1. Crawlability
- robots.txt valid, XML sitemap exists, noindex intentional, crawl depth <3 clicks
- AI crawlers: GPTBot, ClaudeBot, Google-Extended, PerplexityBot management

### 2. Indexability
- Canonical tags, duplicate content, thin content, pagination, hreflang, index bloat

### 3. Security
- HTTPS, valid SSL, no mixed content
- Headers: CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy

### 4. URL Structure
- Clean, descriptive, hyphenated, no chains, flag >100 chars

### 5. Mobile
- Responsive, viewport meta, touch targets 48x48px, font 16px+, no horizontal scroll
- Mobile-first indexing 100% complete (July 2024)

### 6. Core Web Vitals (see `scoring-weights.md`)
- LCP ≤2.5s | INP ≤200ms | CLS ≤0.1

### 7. Structured Data
- JSON-LD preferred, validate types (see `schema-templates.md`)

### 8. JavaScript SEO
- Content in initial HTML vs JS-rendered? CSR vs SSR?
- Serve canonical, robots, structured data in initial HTML

### 9. IndexNow
- Support for Bing, Yandex, Naver

## Output
Technical Score: XX/100
9-category breakdown table with ✅/⚠️/❌ status
Issues by priority: Critical → High → Medium → Low
