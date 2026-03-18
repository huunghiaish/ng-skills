---
phase: 5
title: Update README
status: completed
effort: 15min
depends_on: [2]
---

# Phase 5 — Update README

## Overview

Add `ng:port-manager` to the ng-skills README.md skills table and add a note about the global hook component.

## File Path

`/Users/nghia/Projects/ng-skills/README.md`

## Changes

### 1. Add to Available Skills table

Add row after the last skill entry:

```markdown
| [`ng:port-manager`](./port-manager/) | Manage dev server port allocations across projects. Assigns unique 10-port blocks (30000+) per project to prevent conflicts. Includes session-start hook for auto-detection. |
```

### 2. Add Global Components section

After the "Skill Structure" section, add:

```markdown
## Global Components

Some skills include components that install globally to `~/.claude/`:

| Skill | Component | Location | Purpose |
|-------|-----------|----------|---------|
| `ng:port-manager` | Hook | `~/.claude/hooks/port-suggest.cjs` | Auto-detect project ports on session start |
| `ng:port-manager` | Registry | `~/.claude/port-registry.json` | Port allocation data (created on first use) |

These require manual installation — see each skill's README for setup instructions.
```

### 3. Add usage example

In the Usage section, add:

```markdown
# Port management
/ng:port-manager allocate
/ng:port-manager list
/ng:port-manager check
```

## Implementation Steps

1. Read current README.md
2. Add table row to Available Skills
3. Add Global Components section
4. Add usage examples
5. Keep consistent formatting

## Todo

- [x] Add skill to Available Skills table
- [x] Add Global Components section
- [x] Add usage examples
- [x] Verify markdown renders correctly

## Success Criteria

- README accurately describes port-manager skill
- Global components documented with install notes
- Consistent formatting with existing content
