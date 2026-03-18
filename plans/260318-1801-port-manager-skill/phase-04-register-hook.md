---
phase: 4
title: Register Hook in settings.json
status: completed
effort: 15min
depends_on: [3]
---

# Phase 4 — Register Hook in settings.json

## Overview

Add `port-suggest.cjs` to `~/.claude/settings.json` under the existing `SessionStart` hooks array.

## File Path

`/Users/nghia/.claude/settings.json`

## Current State

```json
"SessionStart": [
  {
    "matcher": "startup|resume|clear|compact",
    "hooks": [
      {
        "type": "command",
        "command": "node \"$HOME/.claude/hooks/session-init.cjs\""
      }
    ]
  }
]
```

## Target State

Add port-suggest hook to the existing SessionStart entry's hooks array:

```json
"SessionStart": [
  {
    "matcher": "startup|resume|clear|compact",
    "hooks": [
      {
        "type": "command",
        "command": "node \"$HOME/.claude/hooks/session-init.cjs\""
      },
      {
        "type": "command",
        "command": "node \"$HOME/.claude/hooks/port-suggest.cjs\""
      }
    ]
  }
]
```

## Implementation Steps

1. Read current `~/.claude/settings.json`
2. Add new hook entry to `hooks.SessionStart[0].hooks` array
3. Write back with same formatting (2-space indent)

## Why append (not separate entry)

Same matcher pattern (`startup|resume|clear|compact`). Adding to existing entry keeps config DRY. Order: session-init first (sets up env), port-suggest second (reads project context).

## Todo

- [x] Edit settings.json to add port-suggest hook
- [x] Verify JSON is valid after edit
- [x] Test session start fires both hooks

## Success Criteria

- `settings.json` remains valid JSON
- Port suggest hook fires on every session start
- Existing session-init hook unaffected
