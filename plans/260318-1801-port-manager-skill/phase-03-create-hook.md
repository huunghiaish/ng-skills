---
phase: 3
title: Create SessionStart Hook
status: completed
effort: 1h
depends_on: [1]
---

# Phase 3 — Create SessionStart Hook

## Overview

Create `~/.claude/hooks/port-suggest.cjs` — a lightweight CJS hook that fires on session start. Reads port registry and injects context about the current project's port allocations (or suggests allocation if unregistered).

## File Path

`/Users/nghia/.claude/hooks/port-suggest.cjs`

## Hook Pattern (from existing hooks)

```javascript
#!/usr/bin/env node
/**
 * SessionStart Hook - Port allocation context injection
 * Fires: session start/resume/clear/compact
 * Purpose: Inject port info for current project or suggest allocation
 * Exit: Always 0 (fail-open)
 */

try {
  const fs = require('fs');
  const path = require('path');
  const os = require('os');

  const REGISTRY_PATH = path.join(os.homedir(), '.claude', 'port-registry.json');

  // Read stdin for payload
  let input = '';
  // ... (sync stdin read)

  const cwd = process.cwd(); // or from payload

  // Read registry
  if (!fs.existsSync(REGISTRY_PATH)) {
    // No registry yet — suggest allocation
    console.log('Port Manager: No registry found. Use /ng:port-manager allocate to set up port allocations.');
    process.exit(0);
  }

  const registry = JSON.parse(fs.readFileSync(REGISTRY_PATH, 'utf-8'));
  const allocation = registry.allocations[cwd];

  if (!allocation) {
    console.log(`Port Manager: Project "${path.basename(cwd)}" has no port allocation. Use /ng:port-manager allocate to assign ports.`);
  } else {
    // Inject port context
    const services = Object.entries(allocation.services)
      .map(([name, port]) => `  ${name}: ${port}`)
      .join('\n');
    console.log(`Port Manager: ${allocation.name} ports (${allocation.block[0]}-${allocation.block[1]}):\n${services}`);
  }

  process.exit(0);
} catch (e) {
  // Crash logging (same pattern as other hooks)
  try {
    const fs = require('fs');
    const p = require('path');
    const logDir = p.join(__dirname, '.logs');
    if (!fs.existsSync(logDir)) fs.mkdirSync(logDir, { recursive: true });
    fs.appendFileSync(p.join(logDir, 'hook-log.jsonl'),
      JSON.stringify({ ts: new Date().toISOString(), hook: 'port-suggest', status: 'crash', error: e.message }) + '\n');
  } catch (_) {}
  process.exit(0); // fail-open
}
```

## Key Design Decisions

1. **No stdin parsing needed**: Hook uses `process.cwd()` for project path (same as other session hooks)
2. **Sync only**: `fs.readFileSync`, `fs.existsSync` — no async, no promises
3. **No npm deps**: Pure Node.js builtins (fs, path, os)
4. **Fail-open**: Any error → log to `.logs/hook-log.jsonl` → `process.exit(0)`
5. **Lightweight output**: Just `console.log()` — hook output becomes `additionalContext` in session

## Output Scenarios

| Scenario | Output |
|----------|--------|
| No registry file | Suggest `/ng:port-manager allocate` |
| Project not in registry | Suggest allocation for this project |
| Project registered | Show port summary (name + all service:port pairs) |
| Registry parse error | Silent fail (log + exit 0) |

## Implementation Steps

1. Create `/Users/nghia/.claude/hooks/port-suggest.cjs`
2. Add shebang `#!/usr/bin/env node`
3. Implement try-catch wrapper with crash logging
4. Read registry, lookup CWD, output appropriate message
5. Keep under 80 lines

## Todo

- [x] Create `port-suggest.cjs` following existing hook patterns
- [x] Test with no registry file (should suggest allocation)
- [x] Test with registry but no CWD entry (should suggest allocation)
- [x] Test with registry and CWD entry (should show ports)
- [x] Test crash recovery (corrupt JSON → fail-open)

## Success Criteria

- Hook runs in <50ms (sync file read only)
- Correct output for all 4 scenarios
- Crash logging works
- Never blocks session start
