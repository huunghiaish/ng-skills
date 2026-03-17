# Phase 1: Fork Core Skills

**Priority:** High | **Status:** done | **Effort:** Medium

## Overview

Fork 5 sub-skills from claude-seo, create main orchestrator, adapt to ng-skills conventions.

## Source

Clone at `/tmp/claude-seo` (already cloned). MIT license.

## Steps

### 1.1 Create main orchestrator `seo/SKILL.md`
- Router skill: parse `/ng:seo <command>` and delegate to sub-skills
- Commands: `audit <url>`, `page <url>`, `content <url>`, `technical <url>`, `images <url>`, `human-content <path|url>`
- Include language mode (English default, Vietnamese switchable)
- Scope & security section
- **Target:** <100 lines

### 1.2 Fork shared references to `seo/references/`
Copy + trim from `/tmp/claude-seo/seo/references/`:
| Source | Target | Action |
|--------|--------|--------|
| `eeat-framework.md` (215 lines) | `eeat-framework.md` | Trim to <150 lines, remove verbose examples |
| `quality-gates.md` (156 lines) | `quality-gates.md` | Trim to <150 lines, condense tables |
| `cwv-thresholds.md` (109 lines) | `scoring-weights.md` | Merge CWV thresholds + scoring weights into one file |
| `schema-types.md` (119 lines) | `schema-templates.md` | Merge with templates.json data, <150 lines |

### 1.3 Fork fetch-page script
- Copy `/tmp/claude-seo/scripts/fetch_page.py` (187 lines) → `seo/scripts/fetch-page.py`
- Keep SSRF prevention, Googlebot UA, redirect tracking
- Remove unused features if any
- Ensure works with `~/.claude/skills/.venv/bin/python3`

### 1.4 Fork seo-audit (112 lines — fits)
- Copy `/tmp/claude-seo/skills/seo-audit/SKILL.md`
- Rename `name: ng:seo-audit`
- Replace agent delegation with inline sequential execution (no agents)
- Update reference paths to `seo/references/*`
- Update script path to `seo/scripts/fetch-page.py`

### 1.5 Fork seo-page (78 lines — fits)
- Copy `/tmp/claude-seo/skills/seo-page/SKILL.md`
- Rename `name: ng:seo-page`
- Update reference paths

### 1.6 Fork seo-content (161 → <150 lines)
- Copy `/tmp/claude-seo/skills/seo-content/SKILL.md`
- Rename `name: ng:seo-content`
- **Trim:** Condense GEO/AI Overviews section (~8 lines saved)
- **Trim:** Merge AI content markers into compact list (~3 lines saved)
- Update explicit reference to `seo/references/eeat-framework.md`

### 1.7 Fork seo-technical (153 → <150 lines)
- Copy `/tmp/claude-seo/skills/seo-technical/SKILL.md`
- Rename `name: ng:seo-technical`
- **Trim:** Condense JS SEO canonical guidance (~5 lines saved)
- Move detailed guidance to quality-gates.md reference

### 1.8 Fork seo-images (168 → <150 lines)
- Copy `/tmp/claude-seo/skills/seo-images/SKILL.md`
- Rename `name: ng:seo-images`
- **Trim:** Remove JPEG XL future note (3 lines)
- **Trim:** Condense responsive images code example (6 lines)
- **Trim:** Condense fetchpriority/decoding sections (9 lines)

### 1.9 Create README with attribution
- `seo/README.md` — fork attribution to AgriciDaniel/claude-seo
- Installation instructions
- Command reference table

## Todo
- [x] 1.1 Create orchestrator SKILL.md (71 lines)
- [x] 1.2 Fork + trim shared references (4 files, all <100 lines)
- [x] 1.3 Fork fetch-page.py script (187 lines)
- [x] 1.4 Fork seo-audit (65 lines)
- [x] 1.5 Fork seo-page (71 lines)
- [x] 1.6 Fork + trim seo-content (92 lines, trimmed from 161)
- [x] 1.7 Fork + trim seo-technical (80 lines, trimmed from 153)
- [x] 1.8 Fork + trim seo-images (84 lines, trimmed from 168)
- [x] 1.9 Create README

## Files to Create
```
seo/SKILL.md
seo/README.md
seo/references/eeat-framework.md
seo/references/quality-gates.md
seo/references/scoring-weights.md
seo/references/schema-templates.md
seo/scripts/fetch-page.py
seo-audit/SKILL.md
seo-page/SKILL.md
seo-content/SKILL.md
seo-technical/SKILL.md
seo-images/SKILL.md
```

## Success Criteria
- All 6 SKILL.md files <150 lines
- All references <150 lines
- `package_skill.py` validates each skill
- Orchestrator routes commands correctly
