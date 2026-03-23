# Audit Checklist

Use this checklist when performing Step 3 — Gap analysis.

---

## A. Feature Completeness

For each feature in PRD/requirements:
- [ ] Is the feature implemented?
- [ ] Does logic match requirements?
- [ ] Are there features in code not documented in docs?

**Result format:**

| Feature | Required (docs) | Actual (code) | Gap | Severity |
|---------|----------------|---------------|-----|----------|
| ...     | ...            | ...           | ... | ...      |

---

## B. Edge Cases — check per feature

### Input validation
- [ ] Null / undefined / empty string input
- [ ] Input exceeding max length
- [ ] Special characters, SQL injection, XSS
- [ ] Wrong data type (string instead of number)
- [ ] Negative numbers, zero when invalid

### Authentication & authorization
- [ ] Accessing another user's resources
- [ ] Actions when not logged in
- [ ] Token expiration mid-operation
- [ ] Admin deleting/locking themselves
- [ ] Role escalation

### Concurrency & race conditions
- [ ] Double submit (clicking button twice)
- [ ] Ordering when stock depletes simultaneously
- [ ] Two users editing same record

### Network & system failures
- [ ] Timeout calling external API
- [ ] Database connection lost
- [ ] Partial write (crash before transaction commit)
- [ ] Does retry logic create duplicates?

### Business logic
- [ ] Currency/quantity decimal precision
- [ ] Timezone handling
- [ ] Can workflow get stuck in a state?
- [ ] Rollback / undo on mid-flow error

### Data integrity
- [ ] Cascade delete side effects
- [ ] Foreign key constraints
- [ ] Unique constraints properly enforced

---

## C. Security Checklist

- [ ] Passwords hashed (not plain text)
- [ ] JWT secret strong, not hardcoded
- [ ] SQL queries use parameterized/ORM
- [ ] File upload: validate type, size, scan malware
- [ ] Rate limiting on auth endpoints
- [ ] Sensitive data not logged to console
- [ ] CORS configured correctly

---

## D. Output format for AUDIT.md

```markdown
# Audit — [Project Name]

**Audit date:** [date]
**Auditor:** AI-assisted audit

## Summary

| Category | Count |
|----------|-------|
| Total features checked | X |
| Fully implemented | X |
| Partially implemented | X |
| Missing | X |
| Edge cases found | X |
| CRITICAL issues | X |
| HIGH issues | X |
| MEDIUM issues | X |

## Gap Analysis

[Feature completeness table]

## Edge Cases & Issues

### [Feature Name]

**Issue:** Specific description
**Trigger condition:** When does this occur
**Impact:** What happens
**Severity:** CRITICAL / HIGH / MEDIUM / LOW
**Recommendation:** How to fix

...

## Risk Matrix

[See references/risk-matrix.md for correct format]
```
