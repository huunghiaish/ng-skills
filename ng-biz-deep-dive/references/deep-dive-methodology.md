# Deep Dive Methodology

## Philosophy

Go from "I know what this process does" to "I can build a system that does this process."

Target detail level: a developer who knows NOTHING about this business can read the spec and build automation without asking follow-up questions.

## 4 Lenses Framework

### Lens 1: Happy Path

- Start from trigger event, end at completion state
- Each step = one atomic action (cannot be split further without losing meaning)
- Include wait times and handoff points between steps
- Map every decision point as explicit IF/THEN/ELSE with criteria
- Note parallel steps (things that happen simultaneously)

### Lens 2: Exceptions

- For EVERY step, ask "what if this fails?"
- Classify recovery: auto-recoverable / needs human / fatal (process stops)
- Document frequency: rare (<1%) / occasional (1–10%) / common (>10%)
- Map escalation chain: who gets called, in what order
- Document rollback: can the process be undone? Up to which step?

### Lens 3: Data & Integration

- Entity Relationship: what data objects exist, what fields matter
- System map: which tools/systems participate in this process
- Integration method: manual copy / file import / API / email / webhook
- Data lineage: where each field originates, how it transforms, where it lands
- Validation rules: what makes data "correct" from a business perspective

### Lens 4: Business Rules

- Decision tables for complex branching logic
- Threshold values with concrete numbers (approval limits, SLA times)
- Formulas written out with worked examples using real numbers
- Seasonal/contextual variations (peak periods, special cases)
- Regulatory/compliance constraints (legal deadlines, required formats)

## Interview Techniques

| Mode | When to use | How |
|------|-------------|-----|
| CHALLENGE | AI has enough context to propose | "Bước 1 là [X]?" → user confirms or corrects |
| EXPLORE | AI has no basis to propose | Open question → user describes |
| GUIDED | Options are finite and known | Offer labeled choices, user selects |

**Rule:** Always show what you already know before asking. Saves 40–60% of interview time.

**Group questions:** Ask 2–3 related questions per round. Never one question at a time.

**Confirm per lens:** Before moving from Lens 1 to Lens 2, confirm the full happy path is correct.

## Completeness Criteria

A spec is "dev-ready" when a developer can answer YES to all of these:

1. Can I trace every path from trigger to completion?
2. Does every decision point have explicit criteria (not "depends on context")?
3. Does every exception have a concrete handling procedure?
4. Does the data model support all described operations?
5. Are all integration points defined with method and data format?
6. Do all business rules have concrete worked examples with real numbers?
7. Are SLA targets specified in measurable units (hours, minutes, %)
