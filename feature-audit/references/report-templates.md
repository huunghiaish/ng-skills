# Audit Report Templates

## Feature Map Report (`audit-{date}-feature-map.md`)

```markdown
# Feature Map - {Project Name}

**Date:** {date} | **Auditor:** Claude Code | **Version:** {version}

## Project Overview
- **Purpose:** {one-line description}
- **Target users:** {user types}
- **Tech stack:** {stack summary}

## Feature Matrix

| # | Feature | PRD | Spec | SRS | Code | Tests | Status |
|---|---------|-----|------|-----|------|-------|--------|
| 1 | {name}  | Y/N | Y/N  | Y/N | Y/N  | Y/N   | {status} |

Status: complete | partial | missing | undocumented

## Core Features
### F1: {Feature Name}
- **Description:** {what it does}
- **User flow:**
  1. {step 1}
  2. {step 2}
- **Alt paths:** {alternative flows}
- **Mermaid flow:** (embedded diagram)

## Secondary Features
{same structure}

## Integrations
{third-party services, APIs}

## Undocumented Features
{features found in code but not in docs}
```

## Verification Report (`audit-{date}-verification.md`)

```markdown
# Verification Report - {Project Name}

**Date:** {date} | **Docs scanned:** {count} | **Requirements found:** {count}

## Cross-Reference Matrix

| Requirement | PRD Ref | Spec Ref | SRS Ref | Code Location | Match |
|-------------|---------|----------|---------|---------------|-------|
| {req}       | {ref}   | {ref}    | {ref}   | {file:line}   | Y/N/P |

Match: Y=yes, N=no, P=partial

## Gaps Found

### Documented but Not Implemented
| # | Requirement | Source Doc | Severity |
|---|------------|------------|----------|
| 1 | {req}      | {doc}      | {level}  |

### Implemented but Not Documented
| # | Feature | Code Location | Risk |
|---|---------|---------------|------|
| 1 | {feat}  | {file:line}   | {risk} |

### Inconsistencies
| # | Item | Doc Says | Code Does | Impact |
|---|------|----------|-----------|--------|
| 1 | {item} | {doc}  | {actual}  | {impact} |

## API Contract Verification
{endpoint-by-endpoint comparison}

## Data Model Verification
{schema vs doc comparison}
```

## Risk Report (`audit-{date}-risks.md`)

```markdown
# Risk Report - {Project Name}

**Date:** {date} | **Total risks:** {count} | **Critical:** {n} | **High:** {n}

## Risk Summary
| Severity | Count | Top Concern |
|----------|-------|-------------|
| Critical | {n}   | {concern}   |
| High     | {n}   | {concern}   |
| Medium   | {n}   | {concern}   |
| Low      | {n}   | {concern}   |

## Critical Risks
### R1: {Risk Title}
- **Category:** {functional/security/data/ux/scale/integration}
- **Location:** {file:line or doc reference}
- **Description:** {what's wrong}
- **Impact:** {what could happen}
- **Evidence:** {code snippet or doc quote}
- **Recommendation:** {how to fix}

## High Risks
{same structure}

## Medium Risks
{same structure}

## Low Risks
{brief list format}
```

## Final Report (`audit-{date}-final-report.md`)

```markdown
# Audit Final Report - {Project Name}

**Date:** {date} | **Overall Score:** {score}/100 | **Risk Level:** {level}

## Executive Summary
{2-3 sentences: overall health, top concerns, recommendation}

## Scorecard

| Area | Score | Weight | Weighted | Status |
|------|-------|--------|----------|--------|
| Feature completeness | {%} | 30% | {pts} | {color} |
| Doc accuracy | {%} | 20% | {pts} | {color} |
| Edge case coverage | {%} | 20% | {pts} | {color} |
| Security posture | {%} | 15% | {pts} | {color} |
| UX completeness | {%} | 15% | {pts} | {color} |
| **Total** | | **100%** | **{total}** | |

Color: green (>80) | yellow (50-80) | red (<50)

## Top Findings
1. {most critical finding}
2. {second}
3. {third}

## Recommendations (Priority Order)
1. **[Critical]** {action item}
2. **[High]** {action item}
3. **[Medium]** {action item}

## Detailed Reports
- [Feature Map](./audit-{date}-feature-map.md)
- [Verification](./audit-{date}-verification.md)
- [Risks](./audit-{date}-risks.md)

## Unresolved Questions
- {any questions that need CTO/team clarification}
```

## Console Output Format

```
=== AUDIT COMPLETE: {Project Name} ===

Score: {score}/100 ({level})

  Feature completeness  [{bar}] {%}%  {color}
  Doc accuracy          [{bar}] {%}%  {color}
  Edge case coverage    [{bar}] {%}%  {color}
  Security posture      [{bar}] {%}%  {color}
  UX completeness       [{bar}] {%}%  {color}

Top 3 Issues:
  1. [CRITICAL] {issue}
  2. [HIGH] {issue}
  3. [HIGH] {issue}

Reports saved to: {reports_path}/
```
