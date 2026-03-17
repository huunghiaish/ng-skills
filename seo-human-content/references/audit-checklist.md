# Human Content Audit Checklist

Detailed rules for each audit point. Reference from SKILL.md Step 2.

## 1. Heading Hierarchy
- **H1:** Exactly 1 per page. Must contain primary keyword.
- **H2-H6:** Logical order, no skipped levels (e.g., H2→H4 is bad).
- **Descriptive:** Each heading should summarize section content.
- **Keyword placement:** Primary keyword in H1, secondary in H2s.
- **Scoring:** 100 if perfect hierarchy, -20 per issue.

## 2. Readability
- **Word count minimums:**
  | Type | Min |
  |------|-----|
  | Blog | 1,500 | Landing | 600 | Product | 400 | Service | 800 |
- **Sentence length:** Avg 15-20 words. Flag >25 words.
- **Paragraph length:** 2-4 sentences. Flag >5 sentences.
- **Flesch estimate:** Target 60-70 for general audience. Quality indicator only.
- **Scoring:** 100 if meets all, -10 per below-minimum metric.

## 3. Image SEO
- **Alt text:** Present on all images, descriptive (10-125 chars), keywords natural.
- **File size:**
  | Category | Target | Warning | Critical |
  |----------|--------|---------|----------|
  | Thumbnail | <50KB | >100KB | >200KB |
  | Content | <100KB | >200KB | >500KB |
  | Hero | <200KB | >300KB | >700KB |
- **Format:** WebP/AVIF preferred. Flag JPEG/PNG without reason.
- **Dimensions:** width/height attributes recommended.
- **File names:** Descriptive, hyphenated, lowercase.
- **Scoring:** 100 if all images pass, -10 per missing alt, -5 per oversized.

## 4. Keyword Analysis
- **Primary keyword:** Must appear in title, H1, first 100 words, URL slug suggestion.
- **Density:** 1-3% natural. Flag <0.5% (under-optimized) or >4% (stuffing).
- **Semantic variations:** At least 3-5 related terms present.
- **Title tag suggestion:** 50-60 chars, keyword near beginning.
- **Meta description suggestion:** 150-160 chars, compelling CTA, keyword included.
- **Scoring:** 100 if keyword well-placed + natural density + variations.

## 5. E-E-A-T Signals
Reference `seo/references/eeat-framework.md` for full criteria.
- **Author bio:** Present with name, credentials, relevant experience.
- **Sources:** External citations to authoritative sources.
- **Experience markers:** Original data, case studies, personal anecdotes.
- **Date stamps:** Publication date, last updated date.
- **Scoring:** Use E-E-A-T framework scoring (0-100).

## 6. Schema Suggestion
Reference `seo/references/schema-templates.md`.
- **Auto-detect content type:**
  | Content | Schema Type |
  |---------|------------|
  | Blog post | Article or BlogPosting |
  | Product page | Product |
  | Service page | Service |
  | Landing page | WebPage |
  | About page | Organization + Person |
- **Generate:** Complete JSON-LD snippet ready to copy-paste.
- **Meta tags:** og:title, og:description, og:image, og:url, twitter:card.
- **Scoring:** 100 if schema provided, 0 if none suggested (always suggest).

## 7. Content Structure
- **ToC:** Recommend if >1,500 words.
- **Internal links:** Suggest 3-5 per 1,000 words with descriptive anchors.
- **CTA:** At least 1 clear call-to-action present.
- **Lists/tables:** Use for scannable data where appropriate.
- **Scoring:** 100 if good structure, -15 per missing element.

## Grade Scale
| Grade | Score | Meaning |
|-------|-------|---------|
| A | 90-100 | Excellent, publish-ready |
| B | 70-89 | Good, minor tweaks |
| C | 50-69 | Moderate, needs work |
| D | 30-49 | Poor, significant issues |
| F | 0-29 | Not ready, major rewrite |
