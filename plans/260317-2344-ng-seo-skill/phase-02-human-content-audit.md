# Phase 2: Build Human Content Audit

**Priority:** High | **Status:** pending | **Effort:** Medium
**Depends on:** Phase 1 (shared references needed)

## Overview

New skill `ng:seo-human-content` — audit local content files before uploading to website.

## Input Types
- **Local folder:** Markdown, HTML, DOCX files + images/videos
- **URL preview:** Staging/preview URL for pre-publish audit
- **Single file:** One markdown/HTML file

## Steps

### 2.1 Create SKILL.md structure
- `AskUserQuestion` to determine:
  - Input type (local folder / URL / single file)
  - Content type (blog post / landing page / product page / service page)
  - Primary keyword (optional, for density analysis)
- Read input files (Glob + Read for local, WebFetch for URL)

### 2.2 Implement 7-point audit checklist

**1. Heading Hierarchy**
- H1 count (exactly 1), keyword in H1
- H2-H6 logical order, no skipped levels
- Extract heading tree for structure visualization

**2. Readability Analysis**
- Word count vs page type minimums (from `seo/references/quality-gates.md`)
- Sentence length average (target 15-20 words)
- Paragraph length (target 2-4 sentences)
- Flesch Reading Ease estimation (target 60-70)

**3. Image SEO**
- Scan for images in content + folder
- Check: alt text present, file size (<200KB warn, >500KB critical)
- Recommend: WebP/AVIF format, width/height attributes
- Flag: missing lazy loading suggestion for below-fold

**4. Keyword Analysis**
- Primary keyword density (1-3% target)
- Semantic variations present
- Suggest: title tag (50-60 chars), meta description (150-160 chars)
- Check: keyword in H1, first paragraph, URL slug suggestion

**5. E-E-A-T Signals**
- Reference `seo/references/eeat-framework.md`
- Check: author bio, credentials, sources cited, date stamps
- Flag: missing experience markers, no external citations

**6. Schema Suggestion**
- Detect content type → recommend JSON-LD
- Reference `seo/references/schema-templates.md`
- Generate copy-paste snippet (Article, BlogPosting, Product, etc.)
- Include: og:title, og:description, og:image, twitter:card

**7. Content Structure**
- Table of contents recommendation (if >1500 words)
- Internal linking opportunities
- CTA placement analysis
- Content freshness signals

### 2.3 Implement scoring engine
- Score 0-100 per category, weighted average for total
- Weights:
  | Category | Weight |
  |----------|--------|
  | Heading hierarchy | 15% |
  | Readability | 15% |
  | Image SEO | 10% |
  | Keyword analysis | 20% |
  | E-E-A-T signals | 20% |
  | Schema/meta | 10% |
  | Content structure | 10% |

### 2.4 Generate output report
- Content Score Card (0-100) with visual bars
- Action Items: Critical → High → Medium → Low
- Copy-paste snippets: meta tags, schema JSON-LD, OG tags
- Save to `plans/reports/seo-human-content-YYMMDD-HHmm.md`

## Todo
- [ ] 2.1 Create SKILL.md with AskUserQuestion flow
- [ ] 2.2 Implement 7-point checklist logic
- [ ] 2.3 Implement scoring engine
- [ ] 2.4 Implement report generation with copy-paste snippets

## Files to Create
```
seo-human-content/SKILL.md
seo-human-content/references/audit-checklist.md    # detailed checklist rules
seo-human-content/references/report-template.md    # output format template
```

## Success Criteria
- SKILL.md <150 lines
- Handles: local folder, single file, URL preview
- Generates actionable report with copy-paste snippets
- Score card with 0-100 breakdown
