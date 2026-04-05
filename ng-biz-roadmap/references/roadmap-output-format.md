# Roadmap Output Format

Save to: `plans/reports/automation-roadmap-{company-slug}-YYMMDD-HHmm.md`

---

```markdown
# Automation Roadmap: [Company Name]

**Ngày:** YYYY-MM-DD | **Nguồn:** [assessment file path] | **Tổng processes:** N

## Executive Summary

- **Quick Wins:** N processes, ước tính tiết kiệm X giờ/tháng (~X VND)
- **Phase 2:** N processes, ước tính tiết kiệm X giờ/tháng (~X VND)
- **Phase 3:** N processes, ước tính tiết kiệm X giờ/tháng (~X VND)
- **Total ROI Year 1:** ~X VND tiết kiệm vs ~Y VND đầu tư (payback: Z tháng)
- **Khuyến nghị bắt đầu:** [Tên Quick Win đầu tiên — lý do ngắn gọn]

---

## Priority Matrix

| PROC-ID | Quy trình | Auto Score | ROI | Pain | Ease | Priority | Phase | Effort | Tiết kiệm/tháng |
|---------|-----------|-----------|-----|------|------|----------|-------|--------|----------------|
| PROC-001 | [Tên] | 8/10 | 8 | 7 | 9 | 8.0 | Quick Win | 3 ngày | 20 giờ |
| PROC-002 | [Tên] | 6/10 | 6 | 5 | 6 | 5.9 | Phase 2 | 2 tuần | 12 giờ |

---

## Process Entry Template

_Use this structure for each item under Phase 1 / Phase 2 / Phase 3:_

### [QW/P2/P3]-N: [Tên Quy Trình] (PROC-XXX)

- **Loại automation:** [n8n / Zapier / Script / AI API / AI Agent]
- **Mô tả:** [Cụ thể cần tự động hóa gì]
- **Effort:** [X person-days]
- **Chi phí setup:** [~X VND]
- **Chi phí hàng tháng:** [~X VND]
- **Tiết kiệm hàng tháng:** [X giờ = ~Y VND]
- **Phụ thuộc:** [Không / PROC-YYY phải xong trước]
- **Rủi ro:** Thấp / Trung bình / Cao
- **Metric đo lường:** [Cách xác nhận thành công]

---

## Phase 1: Quick Wins (Tháng 1-2)

[List entries using Process Entry Template above]

## Phase 2: Medium Impact (Tháng 2-4)

[List entries using Process Entry Template above]

## Phase 3: Strategic (Tháng 4-8)

[List entries using Process Entry Template above]

---

## Backlog

| PROC-ID | Quy trình | Lý do hoãn | Xem lại |
|---------|-----------|-----------|---------|
| PROC-XXX | [Tên] | [ROI thấp / quá phức tạp / chờ tool] | Q3/Q4 2026 |

---

## Dependency Map

```mermaid
flowchart TD
    A[PROC-001: Tên] --> B[PROC-003: Tên]
    A --> C[PROC-004: Tên]
    D[PROC-002: Tên] --> B
    E[Data Cleanup] --> D
    style A fill:#4ade80
    style D fill:#4ade80
    style B fill:#60a5fa
    style C fill:#60a5fa
    style E fill:#f87171
```

Legend: xanh lá = Quick Win, xanh dương = Phase 2, đỏ = prerequisite

---

## Budget Summary

| Phase | Chi phí setup | Chi phí/tháng | Tiết kiệm/tháng | Payback |
|-------|--------------|--------------|-----------------|---------|
| Quick Wins | ~X VND | ~X VND | ~X VND | X tháng |
| Phase 2 | ~X VND | ~X VND | ~X VND | X tháng |
| Phase 3 | ~X VND | ~X VND | ~X VND | X tháng |
| **Tổng** | **~X VND** | **~X VND** | **~X VND** | **X tháng** |

---

## Full Gantt Timeline

```mermaid
gantt
    title Automation Roadmap — Full Timeline
    dateFormat  YYYY-MM-DD
    section Quick Wins (T1-2)
    QW-1 [Tên]:    2026-05-01, 5d
    QW-2 [Tên]:    2026-05-06, 7d
    section Phase 2 (T2-4)
    P2-1 [Tên]:    2026-06-01, 14d
    P2-2 [Tên]:    2026-06-15, 21d
    section Phase 3 (T4-8)
    P3-1 [Tên]:    2026-09-01, 30d
```

---

## Next Steps

1. Phê duyệt roadmap này
2. Chọn Quick Win đầu tiên → `/ng:biz-deep-dive "[tên quy trình]"`
3. Xây SOP → `/ng:biz-sop @detailed-spec.md`
4. Triển khai và đo lường theo metric đã định
5. Review hàng tháng, điều chỉnh priority nếu cần
```
