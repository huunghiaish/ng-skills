# Full Website SEO Audit

## Process
1. **Fetch homepage** — `WebFetch` or `scripts/fetch-page.py`
2. **Detect business type** — e-commerce, SaaS, local, blog
3. **Crawl site** — follow internal links up to 500 pages, respect robots.txt
4. **Run analysis sequentially:** technical → content → images → on-page
5. **Score** — aggregate into SEO Health Score (0-100)
6. **Report** — prioritized action plan

## Crawl Config
Max pages: 500 | Respect robots.txt | Follow redirects (max 3 hops)
Timeout: 30s per page | Delay: 1s between requests

## Scoring Weights
| Category | Weight |
|----------|--------|
| Technical SEO | 25% |
| Content Quality | 25% |
| On-Page SEO | 20% |
| Schema / Structured Data | 10% |
| Performance (CWV) | 10% |
| Images | 10% |

## Report Structure
### Executive Summary
- Overall SEO Health Score (0-100), business type, top 5 critical issues, top 5 quick wins

### Category Breakdowns
For each: score, issues found, recommendations.
- Technical SEO — crawlability, indexability, security, CWV
- Content Quality — E-E-A-T, thin content, readability
- On-Page SEO — titles, meta descriptions, headings, internal links
- Schema — current implementation, validation errors, missing opportunities
- Performance — LCP, INP, CLS flags
- Images — alt text, oversized, format

Reference `eeat-framework.md`, `quality-gates.md`, `scoring-weights.md`.

## Output
Save to `plans/reports/seo-audit-YYMMDD-HHmm.md`
