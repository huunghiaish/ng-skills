---
name: ng:biz-research
description: "Research business domain from company documents and stakeholder interviews. 5 business personas, 3 interview modes. Builds knowledge base for process mapping. Use for business analysis, domain research, process discovery."
argument-hint: "[document-path|folder] [--vi] [--quick]"
allowed-tools: Read, Glob, Grep, Bash, Write, AskUserQuestion, WebFetch
---

# Business Domain Research

Adapted from RRI (Reverse Requirements Interview) methodology. Instead of asking "Tell me about your business", proposes "I understand your business like this — correct?"

**Output:** Business Knowledge Base → feeds into `/ng:biz-process-mapping`

## Language Mode

Default: Vietnamese (primary audience is Vietnamese businesses). Switch to English if user requests.

## Default (No Arguments)

Use AskUserQuestion to present modes:

| Mode | Description |
|------|-------------|
| `research <path>` | Full research from documents (PDF, Word, images) |
| `interview` | Interactive stakeholder interview (no docs) |
| `quick <path>` | Quick scan, auto-propose, minimal questions |

## Input Types

- PDF → use `~/.claude/skills/.venv/bin/python3` with pypdf if needed, or Read for .md/.txt
- Word (.docx) → use python-docx or describe requirement to user
- Images → use Read tool (multimodal)
- Folders → scan all supported files
- URLs → use WebFetch
- No input → pure interview mode

## The 5 Business Personas

| # | Persona | Perspective | Focus |
|---|---------|------------|-------|
| 1 | **Khách hàng (Customer)** | "Nếu tôi là khách hàng..." | Customer journey, pain points, expectations, touchpoints |
| 2 | **Chủ doanh nghiệp (Owner/CEO)** | "Từ góc nhìn kinh doanh..." | Vision, strategy, revenue model, competitive advantage |
| 3 | **Quản lý vận hành (Operations)** | "Khi vận hành hàng ngày..." | Daily workflows, bottlenecks, team structure, tools used |
| 4 | **Tài chính & Tuân thủ (Finance)** | "Về mặt tài chính..." | Costs, margins, compliance, reporting, audit |
| 5 | **IT & Hệ thống (Technology)** | "Về mặt hệ thống..." | Current tech, integrations, data flow, limitations |

## 3 Interview Modes

| Mode | Speed | When | Example |
|------|-------|------|---------|
| **CHALLENGE** | Fast | Known patterns | "Tôi thấy quy trình bán hàng gồm: tiếp nhận → báo giá → chốt đơn. Đúng không?" |
| **GUIDED** | Medium | Multiple options | "Kênh bán hàng chính: (a) Online (b) Showroom (c) Đại lý (d) Tất cả?" |
| **EXPLORE** | Deep | Unknowns | "Mô tả quy trình xử lý khi khách hàng khiếu nại?" |

## 3 Question Layers

| Layer | Source | Effect |
|-------|--------|--------|
| **AUTO-ANSWERED** | From documents | Skip — already know |
| **SMART-ASKED** | Contextualized from docs | Ask with context |
| **CHALLENGE-PROPOSED** | AI proposes from patterns | Propose → confirm/reject |

## Workflow

### Step 0: Document Analysis

- Scan provided documents/folder
- Extract: company name, industry, products/services, org structure, existing processes
- Build initial context; estimate % of questions auto-answered

### Step 1: Interactive Interview

- Use AskUserQuestion for structured UI
- Group 2-4 related questions per round
- Show round header: "Round N — [Persona] Persona"
- Order: Owner/CEO → Operations → Customer → Finance → IT
- Priority: P0 (core business model) → P1 (key processes) → P2 (supporting) → P3 (details)

CHALLENGE mode format:
```json
{
  "question": "[CHALLENGE] Tôi thấy quy trình bán hàng gồm 5 bước: Tiếp nhận lead → Tư vấn → Báo giá → Chốt đơn → Giao hàng. Đúng không?",
  "header": "Chủ doanh nghiệp (Owner)",
  "options": [
    { "label": "Đúng rồi", "description": "Chấp nhận như mô tả" },
    { "label": "Chưa đúng", "description": "Tôi muốn sửa lại" },
    { "label": "Đúng nhưng cần bổ sung", "description": "Cơ bản đúng nhưng thiếu một số bước" }
  ]
}
```

GUIDED mode format:
```json
{
  "question": "[GUIDED] Mô hình kinh doanh chính?",
  "header": "Chủ doanh nghiệp (Owner)",
  "options": [
    { "label": "B2B", "description": "Bán cho doanh nghiệp" },
    { "label": "B2C", "description": "Bán cho người tiêu dùng" },
    { "label": "B2B2C", "description": "Cả hai" },
    { "label": "Khác", "description": "Mô hình khác" }
  ]
}
```

EXPLORE mode format:
```json
{
  "question": "[EXPLORE] Mô tả quy trình từ khi nhận đơn hàng đến khi giao hàng xong?",
  "header": "Quản lý vận hành (Operations)",
  "options": [
    { "label": "Đơn giản: nhận → xác nhận → giao", "description": "Ít bước, ít phê duyệt" },
    { "label": "Nhiều bước + phê duyệt", "description": "Cần qua nhiều khâu kiểm tra" },
    { "label": "Tùy loại đơn hàng", "description": "Khác nhau cho từng loại" },
    { "label": "Để tôi mô tả", "description": "Quy trình phức tạp hơn" }
  ]
}
```

### Step 2: Business Architecture Summary (6 Dimensions)

| Dimension | Question | Examples |
|-----------|----------|----------|
| **Ngành nghề** | Lĩnh vực kinh doanh? | Sản xuất, Dịch vụ, Thương mại, Công nghệ |
| **Mô hình** | Mô hình kinh doanh? | B2B, B2C, B2B2C, Marketplace |
| **Quy mô** | Quy mô hiện tại? | Startup, SME, Enterprise |
| **Kênh** | Kênh vận hành chính? | Online, Offline, Hybrid, Multi-channel |
| **Hệ thống** | Mức độ số hóa? | Manual, Partial digital, Fully digital |
| **Giai đoạn** | Giai đoạn phát triển? | Khởi nghiệp, Tăng trưởng, Ổn định, Mở rộng |

### Step 3: Generate Knowledge Base

Read `references/biz-research-output-format.md` for format.
Save to `plans/reports/biz-research-{company-slug}-YYMMDD-HHmm.md`

## After Research

```
/ng:biz-research → knowledge-base.md
  ↓
/ng:biz-process-mapping @knowledge-base.md → process-catalog.md
```

## Quick Mode (--quick)

- Skip interview, auto-propose everything from documents
- Use CHALLENGE mode only — "I found X, correct?"
- 10-15 questions max
- Good for initial scan before deep research
