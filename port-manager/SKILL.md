---
name: ng:port-manager
description: "Manage dev server port allocations across projects. Assigns unique 10-port blocks (30000+) per project to prevent conflicts."
argument-hint: "list|allocate|release|check|info"
allowed-tools: Read, Bash, Write, AskUserQuestion
---

# Port Manager

Manage dev server port allocations. Each project gets a unique 10-port block starting at 30000.

**Registry:** `~/.claude/port-registry.json`

## Port Block Layout

| Offset | Service |
|--------|---------|
| +0 | Frontend dev server |
| +1 | Backend API |
| +2 | Database |
| +3 | Cache (Redis) |
| +4 | Queue worker |
| +5 | Admin panel |
| +6 | WebSocket |
| +7-9 | Reserved |

## Commands

Parse `$ARGUMENTS` to determine which command to run. If empty or unrecognized, use `AskUserQuestion` to present: list, allocate, release, check, info.

### `list`

1. Read `~/.claude/port-registry.json` with the `Read` tool
2. If file missing or `allocations` empty → print "No port allocations yet. Use `/ng:port-manager allocate`."
3. Render markdown table:

```
| Project | Path | Ports | Frontend | Backend | DB |
|---------|------|-------|----------|---------|----|
```

### `allocate`

1. Read registry. If missing, create default:
   ```json
   {"version":1,"blockSize":10,"startPort":30000,"nextBlock":30000,"allocations":{}}
   ```
2. Check if CWD already allocated → show existing, ask to confirm re-allocate via `AskUserQuestion`
3. Guard: if `nextBlock + blockSize - 1 > 65535` → error "Port range exhausted (max 65535). Release unused projects first."
4. Compute block: `[nextBlock, nextBlock + 9]`
5. Create entry:
   - `name`: basename of CWD
   - `block`: `[start, end]`
   - `services`: map all 7 offsets (frontend +0, backend +1, database +2, redis +3, queue +4, admin +5, websocket +6)
   - `allocatedAt`: today's ISO date
6. Increment `nextBlock` by `blockSize`
7. Write full JSON to `~/.claude/port-registry.json.tmp` via `Write` tool, then `mv` to final path via `Bash`
8. Print allocated ports summary

### `release`

1. Read registry
2. Find CWD in `allocations`
3. If not found → "No allocation for this project"
4. Confirm with `AskUserQuestion` before deleting
5. Remove entry (do NOT reclaim block number — gaps are fine)
6. Atomic write (`.tmp` + `mv`)

### `check`

1. Read registry
2. Collect all allocated ports from registry. Run: `lsof -iTCP -sTCP:LISTEN -nP 2>/dev/null` and filter for allocated ports only
3. For each allocated port, check if a process is listening:
   - **OK**: Expected project port in use
   - **CONFLICT**: Port in use by unexpected process
   - **Available**: Port not in use
4. Render table with PID and process name for conflicts

### `info`

1. Read registry
2. Find CWD project
3. If not found → "No allocation. Run `/ng:port-manager allocate`"
4. Show: project name, path, block range, all service→port mappings, allocation date

## Atomic Write Pattern

Always write registry changes via:
1. `Write` tool → `~/.claude/port-registry.json.tmp`
2. `Bash` → `mv ~/.claude/port-registry.json.tmp ~/.claude/port-registry.json`

## Error Handling

If registry JSON is corrupt, offer to reset via `AskUserQuestion` with confirmation.
