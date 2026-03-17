# ng-skills

Custom [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skills collection for product auditing and development workflows.

All skills use the `ng:` namespace prefix to avoid conflicts with other skill collections.

## Skills

### ng:feature-audit

Audit vibe-coded projects by scanning requirement docs (PRD/Spec/SRS), generating feature maps & user flows, verifying completeness, and detecting risks.

**Commands:**

```
/ng:feature-audit               # Full audit (all 5 phases)
/ng:feature-audit scan           # Scan & understand project
/ng:feature-audit map            # Generate feature map & flows
/ng:feature-audit verify         # Verify docs completeness
/ng:feature-audit risk           # Detect edge cases & risks
/ng:feature-audit report         # Generate final scored report
```

**What it does:**

| Phase | Output |
|-------|--------|
| Scan | Project overview, tech stack, doc structure |
| Map | Feature matrix, user flow diagrams (Mermaid) |
| Verify | Cross-reference requirements vs code, gap detection |
| Risk | 7-category risk analysis (security, UX, scalability...) |
| Report | Scored report with traffic-light ratings & recommendations |

**Scoring areas:** Feature completeness (30%) · Doc accuracy (20%) · Edge case coverage (20%) · Security posture (15%) · UX completeness (15%)

## Installation

### Option 1: Claude Code CLI (recommended)

```bash
claude install-skill https://github.com/huunghiaish/ng-skills
```

This installs all skills under `~/.claude/skills/`.

### Option 2: Manual

```bash
# Clone the repo
git clone https://github.com/huunghiaish/ng-skills.git /tmp/ng-skills

# Copy desired skill(s) to your skills directory
cp -r /tmp/ng-skills/feature-audit ~/.claude/skills/

# Clean up
rm -rf /tmp/ng-skills
```

### Verify installation

```bash
ls ~/.claude/skills/feature-audit/SKILL.md
```

Then start Claude Code and type `/ng:feature-audit` to confirm it appears in the skill list.

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI installed
- Claude Pro/Team/Enterprise subscription

## Usage

1. `cd` into the project you want to audit
2. Run `/ng:feature-audit` for a full audit, or pick a specific phase
3. Reports are saved to `plans/reports/` in your project directory

## Repo Structure

```
ng-skills/
├── README.md
└── feature-audit/                        # Folder name (copy to ~/.claude/skills/)
    ├── SKILL.md                          # Core skill (name: ng:feature-audit)
    └── references/
        ├── risk-categories.md            # 7 risk categories + severity matrix
        ├── report-templates.md           # Report format templates
        ├── mermaid-flow-examples.md      # Flow diagram examples
        └── verification-checklist.md     # Completeness check items
```

## License

MIT
