# Single Page SEO Analysis

## What to Analyze

### On-Page SEO
- Title tag: 50-60 chars, primary keyword, unique
- Meta description: 150-160 chars, compelling, keyword
- H1: exactly one, matches intent, keyword
- H2-H6: logical hierarchy, no skipped levels
- URL: short, descriptive, hyphenated
- Internal/external links: sufficient, relevant anchors

### Content Quality
- Word count vs page type minimums (see `quality-gates.md`)
- Readability: Flesch score, grade level
- Keyword density: natural (1-3%), semantic variations
- E-E-A-T signals: author bio, credentials, experience markers
- Content freshness: dates visible

### Technical Elements
- Canonical tag, meta robots, Open Graph, Twitter Card, hreflang

### Schema Markup
- Detect types (JSON-LD preferred), validate, identify opportunities
- NEVER recommend HowTo (deprecated) or FAQ (restricted to gov/health)

### Images
- Alt text, file size (<200KB warn, >500KB critical), format, dimensions, lazy loading

### Core Web Vitals (flags only)
- Potential LCP/INP/CLS issues from HTML analysis

## Output
```
Overall Score: XX/100

On-Page SEO:     XX/100  ████████░░
Content Quality: XX/100  ██████████
Technical:       XX/100  ███████░░░
Schema:          XX/100  █████░░░░░
Images:          XX/100  ████████░░
```

Issues by priority: Critical → High → Medium → Low
Schema suggestions: ready-to-use JSON-LD (see `schema-templates.md`)
