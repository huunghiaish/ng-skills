# Prompt Extractor Report Template

## Structure

```markdown
# Prompt Extraction Report: {Project Name}

**Generated:** {date}
**Project:** {path}
**Total Prompts Extracted:** {count}

## Reference Documents

### Original Requirements (Human-Written)
- `{file}` — {brief description}

### AI-Generated Artifacts Analyzed
- `{file}` — {what it implements}

---

## Project Overview

{2-3 sentences: what the project does, tech stack, scale}

## Prompt Sequence

### Phase 1: Project Setup
| # | Prompt | Purpose | Output | Depends On |
|---|--------|---------|--------|------------|
| 1 | {reconstructed prompt text} | {goal} | {files created} | — |
| 2 | {prompt} | {goal} | {files} | #1 |

### Phase 2: Core Features
| # | Prompt | Purpose | Output | Depends On |
|---|--------|---------|--------|------------|
| 3 | {prompt} | {goal} | {files} | #1, #2 |

### Phase 3: Integration & Polish
| # | Prompt | Purpose | Output | Depends On |
|---|--------|---------|--------|------------|

### Phase 4: Documentation
| # | Prompt | Purpose | Output | Depends On |
|---|--------|---------|--------|------------|

## Prompt Details

### Prompt #{n}: {Short Title}

**Phase:** {setup|scaffold|feature|integration|polish|docs}
**Purpose:** {what it achieves}
**Dependencies:** #{x}, #{y}

**Prompt:**
> {Full reconstructed prompt text, ready to copy-paste}

**Input Context Required:**
- {file or knowledge needed before running this prompt}

**Expected Output:**
- {files/changes this prompt produces}

**Notes:** {any caveats, manual steps between prompts, etc.}

---

## Reuse Guide

### How to Apply These Prompts to Your Project
1. Adapt prompt #{n} by replacing {X} with your {Y}
2. Execute in order, respecting dependencies
3. After each phase, verify output before proceeding

### Customization Points
- {what to change for different tech stacks}
- {what to change for different project requirements}

## Gaps & Caveats
- {requirements not covered by any extracted prompt}
- {manual edits detected between AI prompts}
- {uncertain reconstructions marked with caveats}
```

## Writing Guidelines

- Prompts must be **copy-paste ready** — complete, actionable text
- Include tech stack specifics in prompts (not generic "add auth")
- Note when a prompt likely included pasted context (e.g., "with this schema: ...")
- Keep Purpose column under 10 words
- Dependencies use prompt numbers only
