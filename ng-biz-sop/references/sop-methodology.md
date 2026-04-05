# SOP Methodology — SOP Framework v2.0

Reference: https://sop-framework.vercel.app/ by Minh Đỗ

---

## Phase 1: Preparation

Goal: Determine if the process is worth documenting before investing effort.

### Step 1 — ROI Screening

**Formula:**
```
ROI = (time_saved_per_month × 12 × labor_cost) / (documentation_hours × labor_cost)
    = (time_per_execution_min × frequency_per_month × error_reduction%) / documentation_hours
```

**Inputs to gather:**
| Input | Description | Example |
|-------|-------------|---------|
| `time_per_execution` | Minutes per single run | 45 min |
| `frequency` | Times per week or month | 20×/month |
| `error_rate` | % of runs that go wrong | 15% |
| `error_cost` | Time/money to fix one error | 2 hours |
| `documentation_hours` | Estimated hours to document | 8 hours |

**Decision thresholds:**
- ROI < 1.5x → Warn user. High documentation cost relative to benefit. Suggest skipping or lightweight version.
- ROI 1.5–3x → Proceed. Standard priority.
- ROI > 3x → High priority. Mark as critical automation candidate.

### Step 2 — Pain Point Documentation

**Categories to probe:**
- **Time waste**: Steps that take longer than they should
- **Error-prone**: Steps where mistakes happen frequently
- **Bottleneck**: Steps that block other work
- **Knowledge-dependent**: Steps only one person knows how to do
- **Compliance risk**: Steps with regulatory or audit implications

Gather specific examples with numbers. "It sometimes fails" is not useful. "It fails ~3×/week, costs 2h to fix each time" is.

### Step 3 — Input/Output Mapping

**I/O Matrix template:**
```
INPUT
  Source      | Format        | Example           | Required?
  ------------|---------------|-------------------|----------
  CRM system  | CSV export    | customer_data.csv | Yes
  Email       | Plain text    | Support ticket    | Yes

OUTPUT
  Product     | Format        | Acceptance Criteria
  ------------|---------------|--------------------
  Report PDF  | PDF           | All fields filled, no nulls
  CRM update  | System record | Status = "Processed"
```

Quality gates define "done correctly" — without them, AI cannot self-verify.

---

## Phase 2: Development

Goal: Document every action with enough detail that AI can execute without asking questions.

### Step 4 — WHAT + WHY Documentation Format

Each step must have three components:

```
Step [N]: [Step Name]
WHAT:   [Specific action — verb + object + location]
        Good: "Search CRM by email address, check 'Active' status field"
        Bad:  "Verify customer" (too vague)
WHY:    [Reasoning — why this action matters]
        Good: "Prevents sending to churned customers; reduces bounce rate; maintains sender reputation"
        Bad:  "To make sure it's correct" (not actionable)
RESULT: [Expected outcome — what to see if done correctly]
        Good: "Customer record found with Active status, OR error triggered → Edge Case EC-03"
        Bad:  "Customer is verified" (not verifiable)
```

**Rule:** If WHY is missing, AI cannot adapt when context changes or exceptions occur. WHY is what separates a checklist from a procedure.

### Step 5 — Edge Case Mapping

For every step, challenge: "What if this goes wrong?"

**Edge case record format:**
```
EC-[ID]: [Short name]
  Trigger:    [Condition that activates this edge case]
  Frequency:  rare | occasional | common
  Severity:   minor | major | critical
  Handling:   [Specific steps to resolve]
  Escalate:   [Who to notify and when]
```

**Classification:**
| Frequency | Severity | Handling |
|-----------|----------|----------|
| common + minor | auto | AI handles silently, logs |
| occasional + major | review | AI flags, human reviews |
| rare + critical | escalate | AI stops, human takes over |

Rule: Every question AI asks during execution = an unpackaged edge case. Zero questions = complete SOP.

### Step 6 — Task Classification Decision Tree

```
Is the step fully rule-based (input → deterministic output)?
  YES → Can errors be auto-detected?
          YES → Level A (Full AI)
          NO  → Level B (AI + Review)
  NO  → Does it require context, judgment, or relationships?
          JUDGMENT → Level C (Human-led, AI assists)
          CREATIVITY/RELATIONSHIP → Level D (Human-only)

Modifier: Are consequences of error severe or irreversible?
  YES → Upgrade one level (A→B, B→C, C→D)
```

### Step 7 — Trust & Security Protocol

**Trust building progression:**
```
Week 1–2:  10% automation (spot-check every run)
Week 3–4:  30% automation (check failed runs only)
Month 2:   50% automation (random 20% sample)
Month 3+:  80–100% automation (exception-based review)
```

Advance only when accuracy holds ≥95% at current level for 2 consecutive weeks.

**Data sensitivity levels:**
- L1 — Public: No restrictions
- L2 — Internal: Logged access
- L3 — Confidential: Role-based access, audit trail
- L4 — Restricted: Human-only handling, no AI storage

---

## Phase 3: Operations

Goal: Make the SOP maintainable, versioned, and self-improving.

### Step 8 — SOP Packaging

Use `sop-template.md` as the master structure. Consolidate all Phase 1 + Phase 2 outputs.

Versioning format: `MAJOR.MINOR`
- MAJOR: process fundamentally changes (new system, new owner, rewritten steps)
- MINOR: clarification, edge case added, wording improved

### Step 9 — Review Cycle

**Trigger-based reviews (immediate):**
- Any AI execution failure or unexpected output
- Process change (new system, new team, new regulation)
- System update affecting tools used in SOP
- Error rate spikes above baseline

**Scheduled reviews:**
| Process Type | Frequency |
|-------------|-----------|
| High-volume, customer-facing | Weekly |
| Internal operational | Monthly |
| Compliance / regulatory | Quarterly |
| Low-frequency, stable | Bi-annual |

**Feedback loop:**
1. Tag AI execution failures with EC-ID (existing) or NEW (new edge case)
2. Categorize: wrong action, missing context, ambiguous instruction, system change
3. Update SOP: add/update edge case or step
4. Re-run readiness checklist
5. Increment MINOR version, log change
