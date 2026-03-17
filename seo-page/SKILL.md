---
name: ng:seo-page
description: "Deep single-page SEO analysis: on-page elements, content quality, technical meta tags, schema, images, CWV flags. Use for 'analyze this page', 'check page SEO', single URL review."
---

# Single Page Analysis

## What to Analyze

### On-Page SEO
- Title tag: 50-60 chars, includes primary keyword, unique
- Meta description: 150-160 chars, compelling, includes keyword
- H1: exactly one, matches page intent, includes keyword
- H2-H6: logical hierarchy (no skipped levels), descriptive
- URL: short, descriptive, hyphenated, no parameters
- Internal links: sufficient, relevant anchor text
- External links: to authoritative sources, reasonable count

### Content Quality
- Word count vs page type minimums (see `seo/references/quality-gates.md`)
- Readability: Flesch Reading Ease, grade level
- Keyword density: natural (1-3%), semantic variations
- E-E-A-T signals: author bio, credentials, experience markers
- Content freshness: publication date, last updated

### Technical Elements
- Canonical tag: present, self-referencing or correct
- Meta robots: index/follow unless intentionally blocked
- Open Graph: og:title, og:description, og:image, og:url
- Twitter Card: twitter:card, twitter:title, twitter:description
- Hreflang: if multi-language, correct implementation

### Schema Markup
- Detect all types (JSON-LD preferred)
- Validate required properties
- Identify missing opportunities
- NEVER recommend HowTo (deprecated) or FAQ (restricted to gov/health)

### Images
- Alt text: present, descriptive, includes keywords naturally
- File size: flag >200KB (warning), >500KB (critical)
- Format: recommend WebP/AVIF over JPEG/PNG
- Dimensions: width/height set for CLS prevention
- Lazy loading: loading="lazy" on below-fold images

### Core Web Vitals (flags only — not measurable from HTML)
- Potential LCP issues (huge hero images, render-blocking resources)
- Potential INP issues (heavy JS, no async/defer)
- Potential CLS issues (missing image dimensions, injected content)

## Output

### Page Score Card
```
Overall Score: XX/100

On-Page SEO:     XX/100  ████████░░
Content Quality: XX/100  ██████████
Technical:       XX/100  ███████░░░
Schema:          XX/100  █████░░░░░
Images:          XX/100  ████████░░
```

### Issues Found
Organized by priority: Critical → High → Medium → Low

### Recommendations
Specific, actionable improvements with expected impact

### Schema Suggestions
Ready-to-use JSON-LD code. Reference `seo/references/schema-templates.md`.
