# audit-product

Comprehensive software audit: feature completeness, edge cases, risk matrix.

## Installation

```bash
# Global — available in all projects
cp -r audit-product ~/.claude/skills/

# Local — single project only
cp -r audit-product /your/project/.claude/skills/
```

## Usage

### Option 1 — Auto-trigger (recommended)

```bash
cd /your/project
claude
```

Then say naturally:
```
"audit this project against the PRD"
"check for missing edge cases"
"I need to understand this project, create an overview"
```

For Vietnamese output:
```
"audit project này, viết báo cáo tiếng Việt"
```

### Option 2 — Audit external project

```bash
cd ~/audit-product

# Step 1: pack context
python scripts/pack.py ~/projects/my-project

# Step 2: run Claude Code with add-dir
claude --add-dir ~/projects/my-project
```

## Output

The skill generates 3 files in `output/`:

| File | Content |
|------|---------|
| `OVERVIEW.md` | Feature list, user flows, data models — for newcomers |
| `AUDIT.md` | Gap analysis, edge cases, detailed risk matrix |
| `REPORT.md` | Executive summary, verdict, top issues to fix |

Default language: **English**. Add "tiếng Việt" or "Vietnamese" to request Vietnamese output.

## Structure

```
audit-product/
├── SKILL.md                         ← entry point, Claude reads on trigger
├── README.md                        ← this file
├── scripts/
│   ├── pack.py                      ← pack codebase with repomix (cross-platform)
│   └── pack.sh                      ← legacy bash version
└── references/
    ├── explore.md                   ← codebase exploration strategy
    ├── overview-template.md         ← template for OVERVIEW.md
    ├── audit-checklist.md           ← 40+ audit checkpoints
    ├── risk-matrix.md               ← CRITICAL/HIGH/MED/LOW severity scale
    └── report-template.md           ← template for REPORT.md
```
