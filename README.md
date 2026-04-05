# ng-skills

A collection of Claude Code skills by [@huunghiaish](https://github.com/huunghiaish).

## Available Skills

| Skill | Description |
|-------|-------------|
| [`ng:audit-product-feature`](./ng-audit-product-feature/) | Audit software projects for feature completeness, edge cases, and business logic risks. Compares PRD/SRS against actual code, detects missing edge cases, generates scored reports. |
| [`ng:prompt-extractor`](./ng-prompt-extractor/) | Reverse-engineer prompts from vibe-coded projects. Analyze original requirements vs AI-generated docs/code to extract reusable prompt sequences with purpose and execution order. |
| [`ng:enhance-prompt`](./ng-enhance-prompt/) | Transforms vague UI ideas into polished, optimized prompts. Forked from [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills/tree/main/skills/enhance-prompt). |
| [`ng:seo`](./ng-seo/) | SEO audit toolkit — full site, single page, content quality, technical, images, pre-upload audit, SEO content rewrite, tracking plan (Umami+Clarity), tracking report. Forked from [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo). |
| [`ng:port-manager`](./ng-port-manager/) | Manage dev server port allocations across projects. Assigns unique 10-port blocks (20000+) per project to prevent conflicts. Includes session-start hook for auto-detection. |
| [`ng:frontend-slides`](./ng-frontend-slides/) | Create stunning HTML presentations from scratch or PPT conversion. Vietnamese-optimized fork of [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) with proper diacritics, Vietnamese fonts, and bilingual UI. |
| [`ng:biz-research`](./ng-biz-research/) | Research business domain from company documents and stakeholder interviews. 5 business personas, 3 interview modes. Builds knowledge base for process mapping. |
| [`ng:biz-process-mapping`](./ng-biz-process-mapping/) | Map all business processes into structured catalog with BPMN diagrams. Process tree, department mapping, Mermaid flowcharts, gap analysis. |
| [`ng:biz-assessment`](./ng-biz-assessment/) | Assess processes for automation readiness. Score x/10 on 6 criteria, classify: AI Agent / AI Automation / n8n / Manual. |
| [`ng:biz-roadmap`](./ng-biz-roadmap/) | Create prioritized automation implementation roadmap. Quick wins → medium → long-term. ROI-based timeline, budget estimation. |
| [`ng:biz-deep-dive`](./ng-biz-deep-dive/) | Deep dive into a specific business process with RRI-style interview. Detailed implementation spec for dev team handoff. |
| [`ng:biz-sop`](./ng-biz-sop/) | Build AI-readable SOPs using SOP Framework v2.0. 3 phases: Preparation (ROI), Development (WHAT+WHY+edge cases), Operations (package+review). |

## Installation

### Global (Recommended)

Available across all projects:

```bash
git clone https://github.com/huunghiaish/ng-skills.git /tmp/ng-skills
cp -r /tmp/ng-skills/ng-*/ ~/.claude/skills/
rm -rf /tmp/ng-skills
```

### Per Project

Available only in a specific project:

```bash
git clone https://github.com/huunghiaish/ng-skills.git /tmp/ng-skills
cp -r /tmp/ng-skills/ng-*/ /your/project/.claude/skills/
rm -rf /tmp/ng-skills
```

> **Note:** Only `ng-*/` folders are skills. Other directories (`plans/`, `docs/`) are internal project files.

## Usage

Once installed, invoke skills via slash command in Claude Code:

```bash
# Audit a project
/ng:audit-product-feature

# With specific instructions
/ng:audit-product-feature audit this project against the PRD

# Vietnamese output
/ng:audit-product-feature audit project này, viết báo cáo tiếng Việt

# Extract prompts from a vibe-coded project
/ng:prompt-extractor

# SEO audit
/ng:seo audit https://example.com
/ng:seo page https://example.com/blog/post
/ng:seo human-content ./content/blog-post.md

# SEO content rewrite (after audit)
/ng:seo rewrite ./content.docx ./plans/reports/seo-audit.md

# === Business Process Automation (BPA) Chain ===

# Step 1: Research business domain from docs
/ng:biz-research ./company-docs/
/ng:biz-research interview --vi

# Step 2: Map all processes
/ng:biz-process-mapping @knowledge-base.md
/ng:biz-process-mapping --department "Kinh doanh"

# Step 3: Assess automation readiness
/ng:biz-assessment @process-catalog.md
/ng:biz-assessment --quick @process-catalog.md

# Step 4: Create prioritized roadmap
/ng:biz-roadmap @assessment-matrix.md
/ng:biz-roadmap quickwins @assessment-matrix.md

# Step 5: Deep dive into 1 process
/ng:biz-deep-dive "customer onboarding"
/ng:biz-deep-dive PROC-001 --from process-catalog.md

# Step 6: Build SOP for dev handoff
/ng:biz-sop @process-spec.md
/ng:biz-sop @process-spec.md --phase 2

# Port management
/ng:port-manager allocate
/ng:port-manager list
/ng:port-manager check

# Create presentations
/ng:frontend-slides
/ng:frontend-slides convert presentation.pptx sang web
```

Skills also activate automatically based on natural language:

```
"audit this project against the PRD"
"check for missing edge cases"
"create an overview of this codebase"
```

## Skill Structure

Each skill follows the [Claude Code skills standard](https://docs.claude.com/en/docs/claude-code/skills):

```
skill-name/
├── SKILL.md              # Entry point — Claude reads this on activation
├── README.md             # Human documentation
├── scripts/              # Executable tools (Python/Node.js)
└── references/           # Detailed docs loaded as-needed
```

## Global Components

Some skills include components that install globally to `~/.claude/`:

| Skill | Component | Location | Purpose |
|-------|-----------|----------|---------|
| `ng:port-manager` | Hook | `~/.claude/hooks/port-suggest.cjs` | Auto-detect project ports on session start |
| `ng:port-manager` | Registry | `~/.claude/port-registry.json` | Port allocation data (created on first use) |

These require manual installation — see each skill's README for setup instructions.

## Contributing

PRs welcome. Each skill must pass validation:

```bash
# Requires skill-creator toolchain
python scripts/package_skill.py <skill-folder>/
```

## License

MIT
