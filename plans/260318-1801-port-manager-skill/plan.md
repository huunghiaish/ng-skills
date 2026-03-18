---
title: "Port Manager Skill for Claude Code"
description: "Global port registry + skill + session hook to eliminate dev port conflicts across 18+ projects"
status: completed
priority: P2
effort: 3h
branch: main
tags: [skill, hook, infrastructure, port-management]
created: 2026-03-18
---

# Port Manager Skill — Implementation Plan

## Problem

18+ dev projects each needing frontend/backend/DB/cache ports. No central management causes port conflicts when running multiple projects simultaneously.

## Solution

3 components: JSON registry, SKILL.md for manual management, CJS hook for auto-detection on session start.

## Architecture

```
~/.claude/port-registry.json     ← Source of truth (global)
~/.claude/hooks/port-suggest.cjs ← SessionStart hook (global)
./port-manager/SKILL.md          ← Skill file (this repo, installs to ~/.claude/skills/)
```

Port range: 30000+, block size: 10 per project, capacity: ~100 projects.

## Phases

| # | Phase | Status | Effort | File |
|---|-------|--------|--------|------|
| 1 | Registry schema & initialization | completed | 20min | [phase-01](./phase-01-create-registry-schema.md) |
| 2 | Skill SKILL.md | completed | 1h | [phase-02](./phase-02-create-skill.md) |
| 3 | Session start hook | completed | 1h | [phase-03](./phase-03-create-hook.md) |
| 4 | Register hook in settings.json | completed | 15min | [phase-04](./phase-04-register-hook.md) |
| 5 | Update README | completed | 15min | [phase-05](./phase-05-update-readme.md) |

## Dependencies

- Phase 2 and 3 depend on Phase 1 (registry schema)
- Phase 4 depends on Phase 3 (hook must exist)
- Phase 5 depends on Phase 2 (skill must exist)

## Key Decisions

- **Block size 10**: Covers 7 common services + 3 reserved. Not configurable (YAGNI)
- **Sync file I/O in hook**: Must be fast, no async overhead for session start
- **No lock file**: Single-user tool, atomic write-rename sufficient
- **`lsof -i` for conflict check**: macOS/Linux compatible, no npm deps needed
