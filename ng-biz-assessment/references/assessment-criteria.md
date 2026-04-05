# Assessment Criteria — Scoring Guide

## 6 Criteria Detail

### 1. Frequency (Tần suất) — Weight: 15%

| Score | Frequency | Rationale |
|-------|-----------|-----------|
| 9-10 | Realtime / nhiều lần/ngày | ROI cao nhất khi tự động hóa |
| 7-8 | Daily (1-3 lần/ngày) | Tiết kiệm đáng kể mỗi ngày |
| 5-6 | Weekly (vài lần/tuần) | Đáng tự động hóa |
| 3-4 | Monthly (vài lần/tháng) | Cân nhắc nếu mất nhiều thời gian |
| 1-2 | Quarterly / yearly | ROI thấp trừ khi rất phức tạp |

### 2. Rule-based (Dựa trên quy tắc) — Weight: 25%

Tiêu chí quan trọng nhất — AI/automation chỉ hiệu quả với quy tắc rõ ràng.

| Score | Level | Description |
|-------|-------|-------------|
| 9-10 | 100% rule | IF-THEN logic, lookup tables, formulas |
| 7-8 | 80%+ rule | Phần lớn theo rule, ít ngoại lệ cần xử lý |
| 5-6 | 50/50 | Nửa rule nửa judgment — AI có thể hỗ trợ |
| 3-4 | 20% rule | Chủ yếu cần context, kinh nghiệm |
| 1-2 | Pure judgment | Sáng tạo, đàm phán, quan hệ con người |

### 3. Error Rate (Tỷ lệ lỗi) — Weight: 15%

Quy trình lỗi nhiều → automation giúp giảm lỗi.

| Score | Error Rate | Impact |
|-------|-----------|--------|
| 9-10 | >20% lỗi | Automation sẽ cải thiện lớn |
| 7-8 | 10-20% lỗi | Đáng kể |
| 5-6 | 5-10% lỗi | Trung bình |
| 3-4 | 2-5% lỗi | Ít lỗi |
| 1-2 | <2% lỗi | Đã tốt, automation ít cải thiện |

### 4. Data Availability (Sẵn sàng dữ liệu) — Weight: 20%

Dữ liệu phải digital + structured để automation hoạt động.

| Score | Status | Description |
|-------|--------|-------------|
| 9-10 | Full digital + API | Dữ liệu trong DB/cloud, có API sẵn |
| 7-8 | Digital + structured | Excel/spreadsheet có cấu trúc, có thể export |
| 5-6 | Partial digital | Mix: một phần digital, một phần giấy/chat |
| 3-4 | Mostly manual | Chủ yếu giấy tờ, email, chat |
| 1-2 | Paper-only | 100% thủ công, không có dữ liệu số |

### 5. Volume (Khối lượng) — Weight: 10%

| Score | Volume | Impact |
|-------|--------|--------|
| 9-10 | >500 transactions/tháng | Scale lớn, automation cần thiết |
| 7-8 | 100-500/tháng | Đáng kể |
| 5-6 | 30-100/tháng | Trung bình |
| 3-4 | 10-30/tháng | Ít |
| 1-2 | <10/tháng | Quá ít, manual OK |

### 6. Integration Complexity (Độ phức tạp tích hợp) — Weight: 15%

Score NGƯỢC: ít hệ thống = dễ tự động = score CAO.

| Score | Systems | Description |
|-------|---------|-------------|
| 9-10 | 1 system | Single app, self-contained |
| 7-8 | 2 systems | Một integration, API available |
| 5-6 | 3-4 systems | Nhiều integration, cần middleware |
| 3-4 | 5+ systems | Phức tạp, nhiều điểm failure |
| 1-2 | Legacy/no API | Hệ thống cũ, không có API, cần RPA |

## Weighted Score Calculation

```
Score = (Frequency × 0.15) + (Rule-based × 0.25) + (Error Rate × 0.15) 
      + (Data Availability × 0.20) + (Volume × 0.10) + (Integration × 0.15)
```

## Classification Thresholds

| Range | Level | Recommendation |
|-------|-------|----------------|
| 8.0 - 10.0 | A: Full AI Agent | Build custom AI agent with autonomous decision-making |
| 6.0 - 7.9 | B: AI Automation | AI processes + human reviews critical outputs |
| 4.0 - 5.9 | C: Simple Automation | n8n, Zapier, Make — no-code/low-code tools |
| 0.0 - 3.9 | D: Manual | Keep human, optimize process instead of automating |

## Edge Cases

- Score 8+ but Data Availability < 4 → Downgrade to B (need data first)
- Score 6+ but Rule-based < 3 → Cap at C (judgment needed, AI not reliable)
- Score < 4 but Error Rate > 8 → Flag for process improvement before automation
- Score < 4 but Volume > 8 → Consider C for volume handling only
