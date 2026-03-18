# Code Review: Port Manager Skill

**Score: 8.5/10** -- Solid implementation, clean separation of concerns, correct patterns. A few edge cases worth addressing.

## Scope

- Files: `port-manager/SKILL.md`, `~/.claude/hooks/port-suggest.cjs`, `~/.claude/settings.json`, `README.md`
- Focus: Correctness, security, edge cases, consistency

## Overall Assessment

Well-structured skill with clear command documentation, proper fail-open hook pattern, and atomic write strategy. The implementation follows KISS/YAGNI principles appropriately.

## Critical Issues

None.

## High Priority

### H1. `check` command regex may miss ports above 39999

SKILL.md line 72: `grep -E ':(3[0-9]{4}) '` matches ports 30000-39999. With block size 10 starting at 30000, capacity is 1000 ports (100 projects) so this stays under 31000 in practice. However, the regex is fragile if `startPort` is ever changed. Consider documenting this constraint or using a dynamic grep range.

**Impact:** Low probability but would silently miss conflicts for high port numbers.

### H2. Hook does not handle malformed JSON gracefully before `JSON.parse`

Line 23: `JSON.parse(raw)` inside try/catch -- this IS handled by the outer catch block, which logs and exits 0. Correct fail-open behavior. No action needed.

**Status:** Not an issue on closer inspection.

## Medium Priority

### M1. SKILL.md: `allocate` does not validate `nextBlock` won't exceed port range

If a user allocates 100+ projects, `nextBlock` could exceed 65535. The skill should check `nextBlock + blockSize - 1 <= 65535` before allocating.

**Fix:** Add step between 2 and 3: "If `nextBlock + blockSize - 1 > 65535`, error: 'Port range exhausted.'"

### M2. SKILL.md: `release` does not reclaim blocks but also does not warn about fragmentation

This is explicitly documented (line 65: "do NOT reclaim block number"). Good design decision for simplicity. Just noting the trade-off is acknowledged.

### M3. Hook log directory is `__dirname/.logs` (inside `~/.claude/hooks/.logs`)

Line 47: Logs go to `~/.claude/hooks/.logs/hook-log.jsonl`. This is fine but not obvious. Could mention in a README. Minor.

### M4. SKILL.md `check` command: `lsof` output format varies by OS

The `lsof` command and grep pattern work on macOS/Linux but output format can differ across distributions. The skill targets single-user dev machines so this is acceptable, but worth noting in docs.

## Low Priority

### L1. SKILL.md: No `$ARGUMENTS` parsing instructions for partial matches

Line 29 says "parse `$ARGUMENTS`" but doesn't specify behavior for partial matches like "al" (allocate?) or typos. The fallback to `AskUserQuestion` handles this implicitly.

### L2. README: Missing mention of manual hook installation steps

Line 94 says "see each skill's README for setup instructions" but `port-manager/` has no README.md, only SKILL.md. Users installing via the global method (`cp -r`) won't get the hook installed.

**Fix:** Add a `port-manager/README.md` with hook installation instructions, or add a note in the main README.

### L3. Hook: `path.basename(cwd)` used in message but not sanitized

Line 33: `path.basename(cwd)` is used in console output. No injection risk since it's stdout to Claude, not shell execution. Safe.

## Security

- **No command injection risks**: Hook uses only `fs` and `path` built-ins, no shell execution
- **No secret exposure**: Registry contains only paths and port numbers
- **Atomic write pattern**: Correct `.tmp` + `mv` prevents corruption
- **Fail-open**: Hook always exits 0, never blocks sessions

## Positive Observations

1. **Clean fail-open pattern** with crash logging -- exactly right for hooks
2. **Atomic write** via tmp+mv prevents registry corruption
3. **YAGNI applied well**: No lock files, no configurable block size, no port reclamation
4. **Version field** in registry enables future schema migration
5. **`AskUserQuestion`** used for destructive operations (release, re-allocate, corrupt reset)
6. **Hook is sync-only** as required for SessionStart performance
7. **Settings.json** properly registered, valid JSON, correct matcher pattern

## Consistency Check

- Registry path `~/.claude/port-registry.json` consistent across SKILL.md, hook, and README
- Block size 10, start port 30000 consistent between plan and SKILL.md
- 7 services documented in both block layout table and allocate step 4
- README table entry matches SKILL.md description

## Recommended Actions (Priority Order)

1. Add port range exhaustion check to `allocate` command (M1)
2. Add `port-manager/README.md` with hook install instructions (L2)
3. Consider documenting the 30000-39999 grep constraint (H1)

## Plan Status

All 5 phases appear implemented:
- [x] Phase 1: Registry schema (defined in SKILL.md allocate command)
- [x] Phase 2: SKILL.md created
- [x] Phase 3: Hook created
- [x] Phase 4: Hook registered in settings.json
- [x] Phase 5: README updated

Plan statuses in `plan.md` still show "pending" -- should be updated to "complete".

## Unresolved Questions

1. Should `port-manager/README.md` be created for hook installation docs, or is the main README sufficient?
2. Plan phase statuses need updating -- is that the lead's responsibility or should it be flagged for update?
