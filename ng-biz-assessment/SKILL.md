---
name: ng:biz-assessment
description: "Assess business processes for automation readiness. Score x/10 on 6 criteria, classify: AI Agent / AI Automation / n8n / Manual. Use for automation assessment, process evaluation, automation scoring."
argument-hint: "[process-catalog-path] [--vi] [--quick]"
allowed-tools: Read, Glob, Grep, Bash, Write, AskUserQuestion
---

# Automation Assessment

Evaluate each business process for automation readiness and recommend automation type.

**Input:** Process Catalog from `/ng:biz-process-mapping`
**Output:** Assessment Matrix → feeds into `/ng:biz-roadmap`

## Language Mode

Default: Vietnamese. Switch to English if requested.

## Default (No Arguments)

Use `AskUserQuestion`:

| Operation | Description |
|-----------|-------------|
| `assess <path>` | Full assessment of all processes in catalog |
| `score <PROC-ID>` | Score a single process |
| `compare <PROC-ID> <PROC-ID>` | Side-by-side comparison |
| `quick <path>` | Quick scan — auto-score from catalog data only |

## The 6 Assessment Criteria

Read `references/assessment-criteria.md` for scoring details.

| # | Criterion | Question | Weight |
|---|-----------|----------|--------|
| 1 | **Frequency** | Quy trình thực hiện bao lâu 1 lần? | 15% |
| 2 | **Rule-based** | Quy trình dựa trên quy tắc rõ ràng hay cần phán đoán? | 25% |
| 3 | **Error Rate** | Tỷ lệ lỗi/sai sót hiện tại? | 15% |
| 4 | **Data Availability** | Dữ liệu đã số hóa chưa? | 20% |
| 5 | **Volume** | Khối lượng giao dịch/tháng? | 10% |
| 6 | **Integration** | Cần kết nối bao nhiêu hệ thống? | 15% |

**Automation Score** = Weighted average of 6 criteria (0-10).

## 4 Automation Levels

| Score Range | Level | Label | Description | Examples |
|-------------|-------|-------|-------------|----------|
| 8-10 | A | **Full AI Agent** | Tự động hoàn toàn, AI tự quyết định | Phân loại email, chatbot CSKH |
| 6-7.9 | B | **AI Automation** | AI xử lý + human review | Xử lý hóa đơn, tạo báo cáo |
| 4-5.9 | C | **Simple Automation** | Rule-based, no-code (n8n/Zapier) | Gửi email theo trigger, sync data |
| 0-3.9 | D | **Manual** | Cần phán đoán, sáng tạo, quan hệ | Đàm phán, coaching, chiến lược |

## Workflow

### Step 1: Load Process Catalog

Read catalog → extract all PROC-IDs with available data.

For each process, auto-score what's known from catalog:
- Frequency → directly from detail card
- Status (Manual/Digital) → informs Data Availability
- Pain points → informs Error Rate
- Tools → informs Integration complexity

### Step 2: Score Each Process

For criteria that cannot be auto-scored, use `AskUserQuestion`.

Group 2-3 processes per round. Use GUIDED mode:

```json
{
  "question": "Quy trình [Name]: Mức độ dựa trên quy tắc vs phán đoán?",
  "header": "📊 Assessment — Rule-based (PROC-XXX)",
  "options": [
    { "label": "9-10: 100% quy tắc", "description": "IF-THEN rõ ràng, không cần suy nghĩ" },
    { "label": "7-8: Chủ yếu quy tắc", "description": "80%+ theo rule, ít ngoại lệ" },
    { "label": "5-6: Mix", "description": "Nửa rule, nửa phán đoán" },
    { "label": "3-4: Chủ yếu phán đoán", "description": "Cần kinh nghiệm, context" },
    { "label": "1-2: Hoàn toàn phán đoán", "description": "Sáng tạo, quan hệ, chiến lược" }
  ]
}
```

### Step 3: Classification

Based on weighted score, classify each process.

For borderline cases (±0.5 of boundary), use `AskUserQuestion` CHALLENGE:
```json
{
  "question": "PROC-XXX score 5.8 — gần ranh giới AI Automation (6.0). Bạn nghĩ nên phân loại thế nào?",
  "header": "⚖️ Borderline Classification",
  "options": [
    { "label": "Simple Automation (n8n)", "description": "An toàn, dễ implement" },
    { "label": "AI Automation", "description": "Đầu tư thêm, hiệu quả hơn" }
  ]
}
```

### Step 4: Recommendations

For each process, recommend:
- **Tool suggestion:** specific tools (n8n, Zapier, Claude API, custom agent...)
- **Quick description:** what the automation would do
- **Prerequisites:** what needs to happen before automating
- **Risk level:** Low / Medium / High

### Step 5: Generate Assessment Matrix

Read `references/assessment-output-format.md`.
Save to `plans/reports/automation-assessment-{company-slug}-YYMMDD-HHmm.md`

## Quick Mode (--quick)

- Auto-score everything from catalog data
- No interview, no AskUserQuestion
- Best-guess classification
- Mark uncertain scores with "~" prefix
- Good for initial overview before detailed assessment

## After Assessment

```
/ng:biz-assessment → assessment-matrix.md
  ↓
/ng:biz-roadmap @assessment-matrix.md → roadmap.md
```
