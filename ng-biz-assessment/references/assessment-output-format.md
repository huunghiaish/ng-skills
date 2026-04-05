# Assessment Output Format

```markdown
# Automation Assessment: [Company Name]

**Ngày:** YYYY-MM-DD | **Nguồn:** [catalog ref] | **Tổng processes:** N

## Summary

| Level | Count | % | Description |
|-------|-------|---|-------------|
| A: Full AI Agent | N | X% | Tự động hoàn toàn |
| B: AI Automation | N | X% | AI + human review |
| C: Simple Automation | N | X% | n8n/Zapier |
| D: Manual | N | X% | Giữ thủ công |

**Top 3 Quick Wins:** PROC-XXX, PROC-YYY, PROC-ZZZ
**Estimated total savings:** X hours/month

## Assessment Matrix

| PROC-ID | Process | Dept | Freq | Rule | Error | Data | Vol | Integ | Score | Level | Tool |
|---------|---------|------|------|------|-------|------|-----|-------|-------|-------|------|
| PROC-XXX | [Name] | [Dept] | X | X | X | X | X | X | X.X | A/B/C/D | [Tool] |

## Detail per Process

### PROC-XXX: [Name] — Level [A/B/C/D] (Score: X.X/10)

**Criteria Breakdown:**
| Criterion | Score | Weight | Weighted | Rationale |
|-----------|-------|--------|----------|-----------|
| Frequency | X | 15% | X.XX | [Why this score] |
| Rule-based | X | 25% | X.XX | [Why] |
| Error Rate | X | 15% | X.XX | [Why] |
| Data Avail | X | 20% | X.XX | [Why] |
| Volume | X | 10% | X.XX | [Why] |
| Integration | X | 15% | X.XX | [Why] |
| **Total** | | | **X.XX** | |

**Recommendation:**
- **Automation type:** [AI Agent / AI Automation / n8n / Manual]
- **Tool suggestion:** [Specific tool]
- **What to automate:** [1-2 sentence description]
- **Prerequisites:** [What needs to happen first]
- **Risk:** [Low / Medium / High]
- **Estimated effort:** [person-days]
- **Expected savings:** [hours/month]

**Edge Case Flags:**
- [Any scoring anomalies or overrides]

---
[Repeat per process]

## Heatmap View

Visual score comparison across all processes:

| Process | Freq | Rule | Err | Data | Vol | Int | Total |
|---------|------|------|-----|------|-----|-----|-------|
| [Name] | 🟢9 | 🟢8 | 🟡5 | 🟢7 | 🟡6 | 🟢8 | 🟢7.3 |
| [Name] | 🟡6 | 🔴2 | 🟢8 | 🟡5 | 🟢7 | 🟡5 | 🟡4.8 |

Legend: 🟢 7-10 | 🟡 4-6 | 🔴 0-3

## Recommendations Summary

### Nên tự động hóa ngay (Level A+B, Score ≥ 6)
1. PROC-XXX: [Name] — [Tool] — [1-line description]
2. ...

### Nên dùng automation đơn giản (Level C, Score 4-6)
1. PROC-XXX: [Name] — [Tool] — [1-line description]
2. ...

### Giữ thủ công, cải tiến quy trình (Level D, Score < 4)
1. PROC-XXX: [Name] — [Reason to keep manual]
2. ...

### Cần chuẩn bị trước khi tự động
1. PROC-XXX: [What prerequisite is missing]
2. ...

## Open Questions
- [Any processes that couldn't be fully assessed]
- [Missing data points]
```

## How Roadmap Consumes This

When `/ng:biz-roadmap` reads this assessment:
1. Read Assessment Matrix → all PROC-IDs with scores and levels
2. Read Detail → effort estimates, prerequisites, risk
3. Read Recommendations Summary → grouped by level
4. Apply priority scoring (score + ROI + pain + ease)
5. Generate phased roadmap with timeline
