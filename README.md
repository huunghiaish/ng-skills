# ng-skills

A collection of Claude Code skills by [@huunghiaish](https://github.com/huunghiaish).

## Available Skills

| Skill | Description |
|-------|-------------|
| [`ng:audit-product-feature`](./audit-product-feature/) | Audit software projects for feature completeness, edge cases, and business logic risks. Compares PRD/SRS against actual code, detects missing edge cases, generates scored reports. |
| [`ng:prompt-extractor`](./prompt-extractor/) | Reverse-engineer prompts from vibe-coded projects. Analyze original requirements vs AI-generated docs/code to extract reusable prompt sequences with purpose and execution order. |
| [`ng:enhance-prompt`](./enhance-prompt/) | Transforms vague UI ideas into polished, optimized prompts. Forked from [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills/tree/main/skills/enhance-prompt). |
| [`ng:seo`](./ng-seo/) | SEO audit toolkit — full site, single page, content quality, technical, images, pre-upload audit, SEO content rewrite. Forked from [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo). |
| [`ng:port-manager`](./port-manager/) | Manage dev server port allocations across projects. Assigns unique 10-port blocks (20000+) per project to prevent conflicts. Includes session-start hook for auto-detection. |
| [`ng:frontend-slides`](./frontend-slides/) | Create stunning HTML presentations from scratch or PPT conversion. Vietnamese-optimized fork of [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) with proper diacritics, Vietnamese fonts, and bilingual UI. |

## Installation

### Global (Recommended)

Available across all projects:

```bash
git clone https://github.com/huunghiaish/ng-skills.git /tmp/ng-skills
cp -r /tmp/ng-skills/*/ ~/.claude/skills/
rm -rf /tmp/ng-skills
```

### Per Project

Available only in a specific project:

```bash
git clone https://github.com/huunghiaish/ng-skills.git /tmp/ng-skills
cp -r /tmp/ng-skills/*/ /your/project/.claude/skills/
rm -rf /tmp/ng-skills
```

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
