# ng-skills

A collection of Claude Code skills by [@huunghiaish](https://github.com/huunghiaish).

## Available Skills

| Skill | Description |
|-------|-------------|
| [`ng:audit-product-feature`](./audit-product-feature/) | Audit software projects for feature completeness, edge cases, and business logic risks. Compares PRD/SRS against actual code, detects missing edge cases, generates scored reports. |

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

## Contributing

PRs welcome. Each skill must pass validation:

```bash
# Requires skill-creator toolchain
python scripts/package_skill.py <skill-folder>/
```

## License

MIT
