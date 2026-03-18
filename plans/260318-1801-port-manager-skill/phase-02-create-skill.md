---
phase: 2
title: Create Skill SKILL.md
status: completed
effort: 1h
depends_on: [1]
---

# Phase 2 — Create Skill SKILL.md

## Overview

Create `./port-manager/SKILL.md` in the ng-skills repo. This is a pure markdown skill — Claude reads instructions and executes Bash/Read/Write tools to manage the registry.

## File Path

`/Users/nghia/Projects/ng-skills/port-manager/SKILL.md`

## Frontmatter

```yaml
---
name: ng:port-manager
description: "Manage dev server port allocations across projects. Prevents port conflicts by assigning unique 10-port blocks (30000+) per project with named service slots."
argument-hint: "list|allocate|release|check|info"
allowed-tools: Read, Bash, Write, AskUserQuestion
---
```

## Commands

### Default (no args)

Use `AskUserQuestion` to present available operations:

| Command | Description |
|---------|-------------|
| `list` | Show all project port allocations |
| `allocate` | Allocate port block for current project |
| `release` | Release current project's port block |
| `check` | Scan for port conflicts with running processes |
| `info` | Show current project's port details |

### `list`

1. Read `~/.claude/port-registry.json`
2. If file missing or empty allocations: print "No port allocations yet."
3. Otherwise render table:

```
| Project | Path | Ports | Frontend | Backend | DB |
|---------|------|-------|----------|---------|----|
| onetake | /Users/.../onetake | 30000-30009 | 30000 | 30001 | 30002 |
```

### `allocate`

1. Read registry (or create default if missing)
2. Check if CWD already has allocation → if yes, show existing and ask to confirm re-allocate
3. Compute next block: `nextBlock` value, range `[nextBlock, nextBlock + blockSize - 1]`
4. Create allocation entry with:
   - `name`: `path.basename(cwd)`
   - `block`: `[start, end]`
   - `services`: all 7 named services mapped to offsets
   - `allocatedAt`: today's date
5. Update `nextBlock += blockSize`
6. Write registry atomically (write to `.tmp`, rename)
7. Print summary table of allocated ports

### `release`

1. Read registry
2. Find CWD in allocations
3. If not found: print "No allocation for this project"
4. Confirm with user via `AskUserQuestion` before deleting
5. Remove entry from allocations
6. Write registry (do NOT reclaim the block — gaps are fine, avoids reuse conflicts)

### `check`

1. Read registry
2. Run `lsof -iTCP -sTCP:LISTEN -nP 2>/dev/null` to get all listening ports
3. For each allocated port across all projects, check if something is listening
4. Report:
   - Ports in use by expected project (OK)
   - Ports in use by unexpected process (CONFLICT)
   - Ports not in use (available)
5. Format as table with PID and process name for conflicts

### `info`

1. Read registry
2. Find CWD project
3. If not found: suggest running `allocate`
4. Show project details:
   - Project name, path
   - Block range
   - All service→port mappings
   - Allocation date

## Skill Instructions — Key Patterns

The SKILL.md should instruct Claude to:

- **Registry path**: Always use `~/.claude/port-registry.json`
- **Read**: Use `Read` tool or `cat` to read registry
- **Write**: Use `Write` tool. Write full JSON (not Edit/patch)
- **Atomic write**: Write to `~/.claude/port-registry.json.tmp` then `mv` to final path
- **JSON parsing**: Parse with `JSON.parse()` in node -e, or let Claude parse directly
- **Error handling**: If registry corrupt, offer to reset with confirmation

## Implementation Steps

1. Create `/Users/nghia/Projects/ng-skills/port-manager/` directory
2. Write `SKILL.md` with frontmatter + all command instructions
3. Keep under 200 lines (should be ~120-150 lines)

## Todo

- [x] Create `port-manager/` directory
- [x] Write SKILL.md with frontmatter
- [x] Document all 5 commands with clear instructions
- [x] Include registry path, schema, and atomic write pattern
- [x] Test skill activation via `/ng:port-manager`

## Success Criteria

- Skill activates on `/ng:port-manager` or `/ng:port-manager <command>`
- All 5 commands produce correct output
- Atomic writes prevent registry corruption
- `check` command correctly detects port conflicts via `lsof`
