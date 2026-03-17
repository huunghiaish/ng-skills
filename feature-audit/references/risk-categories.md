# Risk Categories for Product Audit

## 1. Functional Gaps (Impact: High)
Missing or incomplete features relative to requirements.

**Check for:**
- Requirements listed in PRD but no corresponding code
- Partial implementations (started but not completed)
- Features mentioned in UI but non-functional
- Missing CRUD operations (e.g., can create but not delete)
- Workflows that dead-end without resolution

**Evidence format:** `[REQ-ID] → [Expected] → [Actual] → [Gap]`

## 2. Edge Cases (Impact: High)
Unhandled boundary conditions and unusual inputs.

**Check for:**
- Empty/null inputs not validated
- Max length/size limits not enforced
- Concurrent modifications (race conditions)
- Timezone/locale handling
- Unicode/special character handling
- Negative numbers, zero, overflow values
- First-time user vs returning user paths
- Network failure during multi-step operations

## 3. Security Risks (Impact: Critical)
Auth, authorization, and data protection issues.

**Check for:**
- Missing authentication on protected routes
- Broken authorization (horizontal/vertical privilege escalation)
- Input not sanitized (XSS, SQL injection, command injection)
- Sensitive data in logs, URLs, or error messages
- Missing CORS configuration
- Hardcoded secrets or API keys
- Missing rate limiting on auth endpoints
- Insecure direct object references (IDOR)
- Missing CSRF protection

## 4. Data Integrity (Impact: High)
Inconsistent states and missing validations.

**Check for:**
- Missing database constraints (unique, not null, foreign key)
- No transaction wrapping for multi-table operations
- Orphaned records possible on deletion
- Enum values not validated at API boundary
- Date/time stored without timezone info
- Missing cascade delete/update rules
- Inconsistent data formats between services

## 5. UX Gaps (Impact: Medium)
Missing user-facing states and feedback.

**Check for:**
- No loading indicators for async operations
- Missing error messages (silent failures)
- No empty state design (first use, no data)
- Missing confirmation for destructive actions
- No success feedback after form submissions
- Pagination missing on long lists
- No offline/connectivity handling
- Missing accessibility (a11y) considerations

## 6. Scalability (Impact: Medium-High)
Performance issues under load.

**Check for:**
- N+1 query patterns
- Unbounded SELECT queries (no LIMIT)
- Missing database indexes on filtered/sorted columns
- Large file uploads without streaming
- No caching strategy for frequently accessed data
- Missing pagination on API endpoints
- Synchronous operations that should be async/queued
- Missing connection pooling

## 7. Integration Risks (Impact: Medium)
Third-party and inter-service communication issues.

**Check for:**
- No retry logic for external API calls
- Missing timeout configuration
- No circuit breaker pattern for failing services
- API version not pinned (breaking changes risk)
- Webhook delivery not idempotent
- Missing error handling for third-party failures
- No fallback when external service is down
- Inconsistent error response formats

## Severity Matrix

| Severity | Impact | Likelihood | Action |
|----------|--------|------------|--------|
| Critical | System down / data loss / security breach | High | Fix immediately |
| High | Feature broken / data integrity risk | Medium-High | Fix before release |
| Medium | Degraded UX / performance concern | Medium | Plan fix in next sprint |
| Low | Minor inconvenience / cosmetic | Low | Backlog |
