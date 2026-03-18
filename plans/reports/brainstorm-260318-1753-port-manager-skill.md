# Brainstorm: Port Manager Skill

## Problem
Multiple dev projects (18+) each need frontend, backend, DB, cache ports. No central management → port conflicts when running multiple projects simultaneously. Need Claude Code to auto-suggest and track port allocations.

## Requirements
- Global registry at `~/.claude/port-registry.json`
- Range: 30000+, block size: 10 per project
- Auto-trigger on session start (hook) + manual invoke (skill)
- Support 4-6 services per project
- Avoid cross-project port conflicts

## Agreed Solution

### Architecture: 3 Components

| Component | Location | Purpose |
|-----------|----------|---------|
| Registry | `~/.claude/port-registry.json` | Source of truth for all allocations |
| Skill | `~/.claude/skills/port-manager/SKILL.md` | Manual management: list, allocate, release, check |
| Hook | Session start hook (CJS) | Auto-detect unregistered projects, suggest allocation |

### Registry Schema
```json
{
  "nextBlock": 30020,
  "blockSize": 10,
  "startPort": 30000,
  "allocations": {
    "/path/to/project": {
      "name": "project-name",
      "block": [30000, 30009],
      "services": {
        "frontend": 30000,
        "backend": 30001,
        "database": 30002,
        "redis": 30003
      },
      "allocatedAt": "2026-03-18"
    }
  }
}
```

### Port Block Layout (within each 10-port block)
- +0: Frontend dev server
- +1: Backend API
- +2: Database
- +3: Cache (Redis)
- +4: Queue worker
- +5: Admin panel
- +6: WebSocket
- +7-9: Reserved

### Hook Behavior (session start)
1. Read CWD → check registry
2. If unregistered → inject suggestion message to allocate
3. If registered → inject port info into context

### Skill Commands
- `/port-manager list` — all allocations table
- `/port-manager allocate` — allocate block for current project
- `/port-manager release` — release current project's block
- `/port-manager check` — scan running processes for port conflicts
- `/port-manager info` — current project's port details

### Implementation Considerations
- Hook must be lightweight (CJS, sync file reads) to not slow session start
- Registry file should be human-readable JSON with comments via field names
- Skill should validate no duplicate allocations
- `check` command uses `lsof -i` to detect actual port usage conflicts

### Risk Assessment
- **Low risk**: Registry corruption → mitigate with atomic writes + backup
- **Low risk**: Port conflicts with non-managed apps → `check` command scans all ports
- **Negligible**: Block exhaustion → 30000-30999 = 100 projects capacity

## Next Steps
Create implementation plan with phases for registry, hook, and skill.
