# Pre-Upload Content SEO Audit

Audit content files BEFORE publishing. Local files or staging URL.

## Step 1 — Gather Input
Use `AskUserQuestion`:
- Input type: local folder / single file / staging URL
- Page type: blog (1,500 min) / landing (600) / product (400) / service (800)
- Primary keyword (optional free text)

For local: `Glob` + `Read`. For URL: `WebFetch`.

## Step 2 — 7-Point Audit

### 1. Heading Hierarchy (15%)
H1 exactly 1 with keyword. H2-H6 logical order, no skipped levels.

### 2. Readability (15%)
Word count vs type minimum. Sentence avg 15-20 words. Paragraph 2-4 sentences.

### 3. Image SEO (10%)
Alt text present/quality. Size thresholds. Format (WebP/AVIF). Dimensions set.

### 4. Keyword Analysis (20%)
Density 1-3%. In title/H1/first paragraph. Semantic variations (3-5 terms).
Generate: title tag (50-60 chars), meta description (150-160 chars).

### 5. E-E-A-T Signals (20%)
Author bio, credentials, sources cited, date stamps. See `eeat-framework.md`.

### 6. Schema Suggestion (10%)
Auto-detect type → JSON-LD snippet. See `schema-templates.md`.
Also generate: OG tags, Twitter Card tags.

### 7. Content Structure (10%)
ToC if >1,500 words. Internal link opportunities. CTA placement.

## Step 3 — Score & Report
```
Content SEO Score: XX/100  [Grade]

Heading:     XX/100  ████████░░
Readability: XX/100  ██████████
Images:      XX/100  ███████░░░
Keywords:    XX/100  █████░░░░░
E-E-A-T:     XX/100  ████████░░
Schema:      XX/100  ██████░░░░
Structure:   XX/100  ███████░░░
```

### Copy-Paste Snippets
- Title tag + meta description
- OG tags (og:title, og:description, og:image, og:url)
- Twitter Card tags
- JSON-LD schema

### Grade Scale
A (90-100) publish-ready | B (70-89) minor tweaks | C (50-69) needs work
D (30-49) significant issues | F (0-29) major rewrite
