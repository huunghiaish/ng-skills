# Template: REPORT.md

Use this structure when creating `output/REPORT.md`.
Keep concise — max 1 A4 page when printed.

---

```markdown
# Audit Report — [Project Name]

**Date:** [date] | **Version:** [version if available]

---

## Overall Verdict

🟢 Ready to release
🟡 Can release but must fix HIGH issues first
🔴 Not ready — has CRITICAL issues

> [1-2 sentences explaining verdict]

---

## Top Issues to Fix Now

### 🔴 CRITICAL

1. **[Issue name]** — [1-sentence description] → Fix: [Brief fix]

### 🟠 HIGH

1. **[Issue name]** — [1-sentence description] → Fix: [Brief fix]
2. ...

---

## Recommended Actions

**This sprint (before release):**
- [ ] ...

**Next sprint:**
- [ ] ...

**Backlog:**
- [ ] ...

---

## Confidence Scores

| Category | Score | Notes |
|----------|-------|-------|
| Feature coverage | X/10 | X/Y features fully implemented |
| Edge case handling | X/10 | Based on checklist |
| Documentation quality | X/10 | PRD/SRS completeness |
| **Overall** | **X/10** | |

---

*Full details: see AUDIT.md and OVERVIEW.md*
```
