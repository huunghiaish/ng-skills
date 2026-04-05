# Prioritization Framework

## Priority Score Formula

```
Priority = (Automation_Score × 0.3) + (ROI_Impact × 0.3) + (Pain_Level × 0.2) + (Ease × 0.2)
```

All inputs are 0-10. Max priority score = 10.

---

## Input Scoring Guides

### Automation Score (from Assessment)
Already calculated in `/ng:biz-assessment`. Use directly. Do not recalculate.

### ROI Impact (0-10)
| Score | Meaning |
|-------|---------|
| 1-2 | Saves < 2 hours/month |
| 3-4 | Saves 2-8 hours/month |
| 5-6 | Saves 8-20 hours/month |
| 7-8 | Saves 20-60 hours/month |
| 9-10 | Saves > 60 hours/month or prevents significant revenue loss |

### Pain Level (0-10)
| Score | Meaning |
|-------|---------|
| 1-2 | Minor inconvenience |
| 3-4 | Noticeable time waste |
| 5-6 | Regular bottleneck, occasional errors |
| 7-8 | Major bottleneck, frequent errors, customer impact |
| 9-10 | Critical: losing customers/money, compliance risk |

### Ease of Implementation (0-10)
| Score | Meaning |
|-------|---------|
| 1-2 | Custom AI agent, complex multi-system integrations, months of work |
| 3-4 | Custom development needed, multiple system integrations |
| 5-6 | Mix of config + custom code, moderate complexity |
| 7-8 | Mostly configurable tools (n8n, Zapier), clear business rules |
| 9-10 | Simple automation, existing tools sufficient, < 1 week setup |

---

## Phase Classification

### Quick Wins (Priority ≥ 7)
- Implement immediately in Month 1-2
- Low risk, high visibility — builds stakeholder confidence
- Tools: n8n, Zapier, Google Apps Script, simple AI prompts
- Each item: 1-2 weeks implementation time

### Phase 2: Medium Impact (Priority 5-7)
- Plan and execute in Month 2-4
- May need custom development or API integrations
- Tools: n8n + custom code, Claude/GPT API, CRM integrations
- Each item: 2-8 weeks implementation time

### Phase 3: Strategic (Priority 3-5)
- Complex, high-value automation
- May require AI agents with multiple capabilities or orchestration
- Tools: Custom AI agents, workflow orchestration, multi-system integration
- Each item: 1-3 months implementation time

### Backlog (Priority < 3)
- Not worth automating at current maturity/cost level
- Revisit quarterly — tools and AI capabilities improve rapidly
- Document reason for deferral

---

## Budget Guidelines (VND)

| Automation Type | Setup Cost | Monthly Cost |
|----------------|-----------|--------------|
| n8n (self-hosted) | 2-5M | 0.5-1M |
| n8n (cloud) | 0 | 1-3M |
| Zapier | 0 | 1-5M |
| Google Apps Script | 0 | 0 |
| Custom script | 5-15M | 0.5-2M |
| AI automation (API) | 5-20M | 2-10M |
| AI Agent (custom) | 20-80M | 5-20M |
| Full platform | 50-200M | 10-50M |

**Note:** Setup cost = dev time + configuration + testing. Monthly cost = tool licenses + maintenance + API usage.

---

## Risk Assessment

| Risk Level | Criteria |
|-----------|---------|
| Low | No customer-facing impact, reversible, well-understood domain |
| Medium | Partial customer impact, moderate rollback complexity |
| High | Direct customer/revenue impact, hard to roll back, compliance sensitive |

High-risk items should be moved to Phase 2 or 3 regardless of priority score.
