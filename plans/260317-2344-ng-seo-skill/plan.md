---
title: "ng:seo Skill Collection"
status: done
created: 2026-03-17
brainstorm: plans/reports/brainstorm-260317-2344-ng-seo-skill.md
source: https://github.com/AgriciDaniel/claude-seo (MIT)
---

# ng:seo Skill Collection — Implementation Plan

Fork claude-seo core 5 sub-skills + build new human-content-audit skill.

## Phases

| Phase | File | Status | Effort |
|-------|------|--------|--------|
| 1. Fork Core Skills | `phase-01-fork-core-skills.md` | done | medium |
| 2. Human Content Audit | `phase-02-human-content-audit.md` | done | medium |
| 3. Polish & Test | `phase-03-polish-and-test.md` | done | low |

## Architecture

```
ng-skills/
├── seo/                        # Main orchestrator
│   ├── SKILL.md                # Router: /ng:seo <command>
│   ├── README.md               # Attribution
│   ├── references/
│   │   ├── eeat-framework.md   # E-E-A-T criteria
│   │   ├── quality-gates.md    # Thresholds, word counts
│   │   ├── schema-templates.md # JSON-LD templates
│   │   └── scoring-weights.md  # Category weights
│   └── scripts/
│       └── fetch-page.py       # HTML fetcher
├── seo-audit/SKILL.md          # Full site (112 lines, fits)
├── seo-page/SKILL.md           # Single page (78 lines, fits)
├── seo-content/SKILL.md        # E-E-A-T (161→<150, trim GEO)
├── seo-technical/SKILL.md      # Technical (153→<150, trim JS SEO)
├── seo-images/SKILL.md         # Images (168→<150, trim JPEG XL)
└── seo-human-content/SKILL.md  # NEW: pre-upload audit
```

## Key Decisions
- **Free tools only** — WebFetch, curl, no API keys
- **No agents** — skill-only architecture (simpler than claude-seo's 7 agents)
- **Shared references** — centralized in `seo/references/`, sub-skills reference them
- **English primary** — Vietnamese switchable on request
