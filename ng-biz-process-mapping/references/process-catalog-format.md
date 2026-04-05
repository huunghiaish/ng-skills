# Process Catalog Output Format

## Full Catalog Structure

```markdown
# Process Catalog: [Company Name]

**Ngày:** YYYY-MM-DD | **Nguồn:** [knowledge-base ref] | **Tổng quy trình:** N

## Business Architecture Summary

| Dimension | Value |
|-----------|-------|
| Ngành nghề | [Industry] |
| Quy mô | [Size] |
| Số phòng ban | [N] |
| Tổng quy trình L2 | [N] |
| Manual : Digital ratio | [X : Y] |

## Process Tree

[Hierarchical view — all departments, all levels]

## Process Landscape Diagram

[Mermaid flowchart LR — high-level cross-department]

---

## [Department Name]

### Process List

| PROC-ID | Tên | Trigger | Frequency | Status | Pain Points |
|---------|-----|---------|-----------|--------|-------------|

### PROC-XXX: [Name]
[Full detail card from process-detail-template.md]

#### Diagram
[Mermaid flowchart]

---
[Repeat per department]
---

## Cross-Process Analysis

### Handoff Map
| From | To | Data Exchanged | Method |
|------|----|---------------|--------|
| PROC-XXX | PROC-YYY | [data] | [manual/API/file] |

### Shared Resources
| Resource | Used by | Type |
|----------|---------|------|
| [Tool/system] | PROC-XXX, PROC-YYY | Software |
| [Data source] | PROC-XXX, PROC-ZZZ | Database |

### Dependencies
| Process | Depends on | Blocking? |
|---------|-----------|-----------|
| PROC-YYY | PROC-XXX | Yes — cannot start until X complete |

### Gaps Identified
| # | Gap Description | Impact | Suggested Process |
|---|----------------|--------|-------------------|

## Statistics

| Metric | Value |
|--------|-------|
| Total departments | N |
| Total L2 processes | N |
| Total L3 sub-processes | N |
| Manual processes | N (X%) |
| Partial digital | N (X%) |
| Full digital | N (X%) |
| Processes with pain points | N |
| Cross-department handoffs | N |
| Gaps identified | N |
```

## How Automation Assessment Consumes This

When `/ng:biz-assessment` reads this catalog:

1. Read Process List tables → get all PROC-IDs
2. Read Detail Cards → extract frequency, duration, status, pain points, tools
3. Read Cross-Process Analysis → understand dependencies
4. Score each PROC-ID on 6 assessment criteria
5. Generate Assessment Matrix with automation recommendations
