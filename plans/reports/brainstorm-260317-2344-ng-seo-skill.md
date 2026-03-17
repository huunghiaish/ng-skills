# Brainstorm: ng:seo Skill Collection

**Date:** 2026-03-17
**Status:** Agreed

## Problem Statement

Need Claude Code skills for SEO auditing:
1. **Human content audit** — audit local files (blog, landing page) before upload
2. **Full site audit** — scan all pages of a live website
3. **Single page audit** — deep analysis of one URL

Common output: scan → audit → report → strategy suggestions.

## Approach: Fork + Customize claude-seo

**Source:** [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) (MIT license)

### Why fork vs build from scratch
- claude-seo already has solid audit/page/content logic, scoring weights, E-E-A-T framework
- 12 sub-skills is overkill → keep core 5 + add 1 new
- Rewrite references/templates to fit ng-skills conventions
- Rename all to `ng:seo-*` namespace

### What to keep (Core 5)
| Sub-skill | Purpose |
|-----------|---------|
| `ng:seo-audit` | Full site audit, crawl up to 500 pages, health score 0-100 |
| `ng:seo-page` | Single page deep dive (on-page, meta, schema, images, CWV) |
| `ng:seo-content` | E-E-A-T analysis, readability, thin content detection |
| `ng:seo-technical` | robots.txt, sitemaps, canonicals, security headers, CWV |
| `ng:seo-images` | Image optimization (alt, size, format, lazy loading) |

### What to drop
- seo-schema, seo-sitemap, seo-hreflang, seo-geo, seo-competitor-pages, seo-programmatic, seo-plan
- DataForSEO extension, Banana extension
- 7 agent definitions (simplify to skill-only architecture)

### What to add (NEW)
| Sub-skill | Purpose |
|-----------|---------|
| `ng:seo-human-content` | Audit local files before upload to website |

## New Feature: ng:seo-human-content

### Input Types
- **Local files:** Markdown, HTML, DOCX, images, videos in a folder
- **URL preview:** Staging/preview URL for pre-publish audit

### Audit Checklist
1. **Heading hierarchy** — H1-H6 structure, keyword in H1, no skipped levels
2. **Readability** — Flesch score, sentence length, paragraph length, grade level
3. **Image SEO** — Alt text presence/quality, file size (<200KB warning, >500KB critical), format (WebP/AVIF recommended), dimensions set
4. **Keyword analysis** — Primary keyword density (1-3%), semantic variations, title tag suggestion (50-60 chars), meta description suggestion (150-160 chars)
5. **E-E-A-T signals** — Author bio, credentials, sources cited, experience markers, date stamps
6. **Schema suggestion** — Recommend JSON-LD based on content type (Article, BlogPosting, HowTo, Product, etc.)
7. **Content structure** — Table of contents, internal link opportunities, CTA placement, word count vs page type minimums

### Output
- **Content Score Card** (0-100) with breakdown per category
- **Action Items** prioritized: Critical → High → Medium → Low
- **Schema snippet** ready to copy-paste
- **Meta tags** ready to copy-paste (title, description, OG, Twitter Card)

## Architecture

```
ng-skills/seo/
├── SKILL.md                    # Main orchestrator (router for subcommands)
├── README.md                   # Attribution to claude-seo
├── references/
│   ├── eeat-framework.md       # E-E-A-T criteria (from claude-seo)
│   ├── quality-gates.md        # Word count, scoring thresholds
│   ├── schema-templates.md     # JSON-LD templates
│   └── scoring-weights.md      # Category weights for scores
└── scripts/
    └── fetch-page.py           # HTML fetcher (from claude-seo)
```

Sub-skills as separate dirs:
```
ng-skills/seo-audit/SKILL.md
ng-skills/seo-page/SKILL.md
ng-skills/seo-content/SKILL.md
ng-skills/seo-technical/SKILL.md
ng-skills/seo-images/SKILL.md
ng-skills/seo-human-content/SKILL.md    # NEW
```

## Integration
- **Free tools only:** WebFetch, curl, Lighthouse CLI (optional)
- **No API keys required** for base functionality
- **Language:** English primary, Vietnamese switchable

## Implementation Plan (suggested phases)

### Phase 1: Fork Core
- Fork 5 sub-skills from claude-seo, rename to ng:seo-*
- Adapt references to ng-skills conventions (<150 lines each)
- Create main orchestrator SKILL.md with `/ng:seo <command>` router

### Phase 2: Build Human Content Audit
- Create ng:seo-human-content sub-skill
- Support local files (md, html, docx) + URL preview
- Implement 7-point checklist
- Schema suggestion engine

### Phase 3: Polish & Test
- Test on real projects
- Scoring calibration
- README with attribution

## Risks
- **claude-seo is large** — need aggressive trimming to fit skill size limits
- **CWV measurement** — can't measure real CWV from HTML alone, only flag potential issues
- **Content parsing** — DOCX/image analysis needs scripts (Python)

## Success Criteria
- All 3 use cases working: human content, full site, single page
- Reports actionable with copy-paste schema/meta snippets
- Score 0-100 with clear breakdown
- Each sub-skill <150 lines SKILL.md

## Next Steps
- Create implementation plan with detailed phases
- Start Phase 1: fork + adapt core 5 sub-skills
