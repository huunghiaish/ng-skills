# Risk Matrix — Severity Scale

## Level Definitions

| Level | Icon | Condition | Required Action |
|-------|------|-----------|-----------------|
| CRITICAL | 🔴 | Data loss / security breach / full product down / financial loss | Fix before release |
| HIGH | 🟠 | Core flow broken, user stuck unable to complete task | Fix this sprint |
| MEDIUM | 🟡 | Edge case affecting <20% users, workaround exists | High-priority backlog |
| LOW | 🟢 | UX friction, cosmetic, minor inconsistency | Regular backlog |

## Assessment Rules

- **Do not mark HIGH** if workaround is clear and easy → mark MEDIUM
- **Must mark CRITICAL** if: user can lose money, other users' data exposed, or unrecoverable
- **Always state "Trigger condition"** for CRITICAL and HIGH — no vague descriptions
- **Every issue must have a specific action** — never write "needs further investigation"

## Risk Matrix Table Format

```markdown
## Risk Matrix

| # | Risk | Description | Likelihood | Impact | Severity | Action |
|---|------|-------------|-----------|--------|----------|--------|
| 1 | [Short name] | [Description + trigger condition] | High/Med/Low | High/Med/Low | 🔴 CRITICAL | [Specific action] |
| 2 | ... | ... | ... | ... | 🟠 HIGH | ... |
```

## Correct Example

✅ **Correct:**
- Risk: "Double charge on payment"
- Description: "User clicks pay button twice quickly → 2 requests sent → charged twice"
- Severity: CRITICAL
- Action: "Add idempotency key to payment endpoint, disable button after first click"

❌ **Wrong:**
- Risk: "Possible payment issue"
- Severity: HIGH
- Action: "Needs further review"
