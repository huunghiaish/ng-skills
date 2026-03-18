---
phase: 1
title: Registry Schema & Initialization
status: completed
effort: 20min
---

# Phase 1 — Registry Schema & Initialization

## Overview

Define the JSON schema for `~/.claude/port-registry.json`. No code creates this file upfront — the skill's `allocate` command and the hook both create it lazily on first use.

## Schema

```json
{
  "version": 1,
  "blockSize": 10,
  "startPort": 30000,
  "nextBlock": 30000,
  "allocations": {}
}
```

### Allocation entry (keyed by absolute project path):

```json
{
  "/Users/nghia/Projects/onetake": {
    "name": "onetake",
    "block": [30000, 30009],
    "services": {
      "frontend": 30000,
      "backend": 30001,
      "database": 30002,
      "redis": 30003,
      "queue": 30004,
      "admin": 30005,
      "websocket": 30006
    },
    "allocatedAt": "2026-03-18"
  }
}
```

### Port Block Layout

| Offset | Service | Notes |
|--------|---------|-------|
| +0 | Frontend dev server | Vite, Next, etc. |
| +1 | Backend API | Express, FastAPI, etc. |
| +2 | Database | Postgres, MySQL, etc. |
| +3 | Cache (Redis) | |
| +4 | Queue worker | Celery, Bull, etc. |
| +5 | Admin panel | |
| +6 | WebSocket | |
| +7-9 | Reserved | Future services |

## Implementation Notes

- **Lazy creation**: Both skill and hook check `fs.existsSync()` and create default registry if missing
- **Atomic writes**: Write to `.tmp` file then `fs.renameSync()` to prevent corruption
- **`version` field**: Future-proofing for schema migrations (check `version === 1`)
- **Project name**: Derived from `path.basename(cwd)` at allocation time

## Helper Functions (shared between skill instructions and hook)

The skill is pure SKILL.md (Claude reads instructions + executes commands). No shared JS library needed. The hook is standalone CJS.

Registry read/write logic lives only in the hook (`port-suggest.cjs`). The skill instructs Claude to use `cat`, `node -e`, or inline JS to read/write the registry.

## Success Criteria

- [x] Schema documented and agreed upon
- [x] Lazy init produces valid default registry
- [x] Atomic write pattern defined
