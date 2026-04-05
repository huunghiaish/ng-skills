# Business Knowledge Base Output Format

Standard output format for `/ng:biz-research`. Save to:
`plans/reports/biz-research-{company-slug}-YYMMDD-HHmm.md`

---

## Template

```markdown
# Business Knowledge Base: [Company Name]

**Ngày:** YYYY-MM-DD | **Nguồn:** [documents/interview/both] | **Câu hỏi:** N asked / M auto-answered

---

## Business Architecture (6 Dimensions)

| Dimension | Value | Implication |
|-----------|-------|-------------|
| Ngành nghề | [Industry] | [Context for processes] |
| Mô hình | [B2B/B2C/B2B2C/Marketplace] | [Customer interaction patterns] |
| Quy mô | [Startup/SME/Enterprise] | [Complexity level] |
| Kênh | [Online/Offline/Hybrid/Multi-channel] | [Channel management needs] |
| Hệ thống | [Manual/Partial digital/Fully digital] | [Automation readiness] |
| Giai đoạn | [Khởi nghiệp/Tăng trưởng/Ổn định/Mở rộng] | [Priority focus] |

---

## Company Overview

- **Tên:** [Company name]
- **Ngành:** [Industry + sub-industry]
- **Sản phẩm/Dịch vụ:** [Bulleted list]
- **Quy mô:** [Employee count, revenue range if known]
- **Thị trường:** [Geography, customer segments]
- **Website/Tài liệu nguồn:** [URLs or file paths]

---

## Organizational Structure

| Phòng ban | Chức năng chính | Số người | Người đứng đầu |
|-----------|----------------|----------|-----------------|
| [Dept 1] | [Function] | [N] | [Role/Name] |
| [Dept 2] | [Function] | [N] | [Role/Name] |

---

## Key Actors

| Actor | Vai trò trong hệ thống | Tương tác chính |
|-------|------------------------|-----------------|
| [e.g. Sales Rep] | [Initiates orders] | [CRM, Customer, Warehouse] |
| [e.g. Kế toán] | [Processes invoices] | [Finance system, Operations] |

---

## Process Inventory (Sơ bộ)

| # | Quy trình | Phòng ban | Tần suất | Hiện trạng |
|---|-----------|-----------|----------|------------|
| 1 | [Process name] | [Dept] | [Daily/Weekly/Monthly/Ad-hoc] | [Manual/Partial/Digital] |
| 2 | | | | |

> Note: This is a preliminary inventory. Use `/ng:biz-process-mapping` for detailed BPMN/flow mapping.

---

## Pain Points

| # | Vấn đề | Phòng ban | Mức độ | Ảnh hưởng |
|---|--------|-----------|--------|-----------|
| 1 | [Pain point description] | [Dept] | [Cao/Trung bình/Thấp] | [Impact description] |
| 2 | | | | |

---

## Current Systems & Tools

| Tool/Phần mềm | Mục đích | Phòng ban dùng | Mức độ tích hợp |
|---------------|---------|----------------|-----------------|
| [e.g. Excel] | [Quản lý đơn hàng] | [Kinh doanh] | [Standalone — manual export] |
| [e.g. Misa] | [Kế toán] | [Tài chính] | [No integration] |

---

## Revenue Model

- **Nguồn thu chính:** [List with % if known]
- **Mô hình định giá:** [Project-based/Recurring/Per-unit/Mixed]
- **Chu kỳ doanh thu:** [Monthly/Quarterly/Irregular]

---

## Compliance & Constraints

- [Compliance requirement 1]
- [Industry regulation, tax obligation, etc.]

---

## Decisions Log

| # | Decision | Rationale | Persona |
|---|----------|-----------|---------|
| 1 | [What was confirmed/decided] | [Why or how confirmed] | [Owner/Ops/etc.] |
| 2 | | | |

---

## Open Questions

- [ ] [Unresolved item — needs follow-up]
- [ ] [Item deferred to next session]

---

## Research Statistics

| Metric | Value |
|--------|-------|
| Personas consulted | [N/5] |
| Questions asked | [N] |
| Questions auto-answered | [M] |
| Processes identified | [N] |
| Pain points logged | [N] |
| Research mode | [Full/Quick/Interview-only] |
| Duration | [~N minutes] |
```

---

## Filling Guidelines

- **Ngành nghề:** Be specific — not just "Dịch vụ" but "Dịch vụ logistics B2B"
- **Mức độ pain point:** Cao = blocks daily operations, Trung bình = slows work, Thấp = annoyance
- **Hiện trạng process:** Manual = paper/verbal, Partial = some tool but not end-to-end, Digital = system-managed
- **Mức độ tích hợp:** Standalone, Manual export/import, File exchange (CSV/Excel), API/automated
- **Open Questions:** Always list even if short — honesty about gaps is valuable

## Slug Naming

`{company-slug}` = lowercase, hyphen-separated, no accents.
Examples: `cong-ty-abc` → `abc`, `nguyen-trading` → `nguyen-trading`
