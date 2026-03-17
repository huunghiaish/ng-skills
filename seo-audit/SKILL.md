---
name: ng:seo-audit
description: "Full website SEO audit: crawl up to 500 pages, detect business type, analyze technical SEO, content quality, images, generate health score 0-100. Use for 'audit site', 'full SEO check', 'website health'."
---

# Full Website SEO Audit

## Process

1. **Fetch homepage** — use `seo/scripts/fetch-page.py` or `WebFetch` to retrieve HTML
2. **Detect business type** — analyze homepage signals (e-commerce, SaaS, local, blog)
3. **Crawl site** — follow internal links up to 500 pages, respect robots.txt
4. **Run analysis sequentially:**
   - Technical SEO — robots.txt, sitemaps, canonicals, CWV, security headers
   - Content Quality — E-E-A-T, readability, thin content, AI citation readiness
   - Images — alt text, file size, format, lazy loading
   - On-Page SEO — titles, meta descriptions, headings, internal links
5. **Score** — aggregate into SEO Health Score (0-100)
6. **Report** — generate prioritized action plan

## Crawl Configuration

```
Max pages: 500
Respect robots.txt: Yes
Follow redirects: Yes (max 3 hops)
Timeout per page: 30 seconds
Delay between requests: 1 second
```

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
- Overall SEO Health Score (0-100)
- Business type detected
- Top 5 critical issues
- Top 5 quick wins

### Category Breakdowns
For each category: score, issues found, recommendations.
Reference `seo/references/eeat-framework.md` for E-E-A-T criteria.
Reference `seo/references/quality-gates.md` for content thresholds.
Reference `seo/references/scoring-weights.md` for CWV thresholds.

### Priority Definitions
- **Critical**: Blocks indexing or causes penalties (fix immediately)
- **High**: Significantly impacts rankings (fix within 1 week)
- **Medium**: Optimization opportunity (fix within 1 month)
- **Low**: Nice to have (backlog)

## Output Files

Save to `plans/reports/`:
- `seo-audit-YYMMDD-HHmm-report.md` — Comprehensive findings + action plan
