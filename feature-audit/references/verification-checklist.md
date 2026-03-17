# Verification Checklist

## Document Completeness

### Requirements Document
- [ ] All requirements have unique IDs
- [ ] Each requirement has acceptance criteria
- [ ] Priority defined (must/should/could/won't)
- [ ] Dependencies between requirements documented
- [ ] Non-functional requirements included (performance, security, a11y)

### PRD (Product Requirements Document)
- [ ] Problem statement clearly defined
- [ ] Target users/personas identified
- [ ] Success metrics defined
- [ ] Feature list with priorities
- [ ] Out-of-scope items listed
- [ ] User stories with acceptance criteria

### Technical Spec
- [ ] Architecture overview with diagrams
- [ ] API endpoints documented (method, path, request/response)
- [ ] Data models/schemas defined
- [ ] Authentication/authorization strategy
- [ ] Error handling strategy
- [ ] Third-party integrations documented
- [ ] Migration strategy (if applicable)

### SRS (Software Requirements Specification)
- [ ] Functional requirements mapped to PRD features
- [ ] System interfaces documented
- [ ] Performance requirements quantified
- [ ] Security requirements explicit
- [ ] Data retention/privacy requirements
- [ ] Compliance requirements (GDPR, etc.)

## Cross-Reference Checks

### Requirements → Code
- [ ] Every "must" requirement has code implementation
- [ ] Every "should" requirement has code or documented deferral
- [ ] No orphan code (implemented without requirement)

### Docs → Code Consistency
- [ ] API routes in spec match actual routes
- [ ] Request/response schemas match actual DTOs
- [ ] Database schema matches actual migrations
- [ ] Env vars documented match actual usage
- [ ] Error codes in docs match actual error responses

### Code → Tests
- [ ] Core business logic has unit tests
- [ ] API endpoints have integration tests
- [ ] Auth flows have security tests
- [ ] Edge cases from requirements have test cases

## Vibe-Code Specific Checks
- [ ] No TODO/FIXME/HACK comments left unresolved
- [ ] No placeholder/dummy data in production code
- [ ] No hardcoded values that should be configurable
- [ ] No console.log/print debugging left in
- [ ] No commented-out code blocks
- [ ] No duplicate implementations of same logic
- [ ] Error messages are user-friendly, not stack traces
- [ ] AI-generated code has been reviewed for correctness
