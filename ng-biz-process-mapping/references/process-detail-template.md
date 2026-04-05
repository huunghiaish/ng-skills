# Process Detail Card Template

## Format per Level 2 Process

```markdown
### PROC-{NNN}: {Tên quy trình}

**Phòng ban:** {Department}
**Mục đích:** {1-2 câu mô tả lý do quy trình tồn tại}

| Field | Value |
|-------|-------|
| Trigger | {Sự kiện khởi đầu quy trình} |
| Input | {Dữ liệu/tài liệu đầu vào} |
| Output | {Kết quả/sản phẩm đầu ra} |
| Actors | {Ai tham gia: vai trò, phòng ban} |
| Frequency | {daily / weekly / monthly / on-demand} |
| Duration | {Thời gian trung bình: X phút/giờ/ngày} |
| Volume | {Số lượng giao dịch/lần thực hiện per period} |
| Tools | {Phần mềm/công cụ sử dụng} |
| Status | {Manual / Partial digital / Full digital} |

**Các bước chính:**
1. {Bước 1} — {Actor} — {Tool nếu có}
2. {Bước 2} — {Actor} — {Tool nếu có}
3. ...

**Pain Points:**
- {Vấn đề 1}: {Mô tả ngắn + ảnh hưởng}
- {Vấn đề 2}: ...

**Handoffs:**
- Nhận từ: PROC-{XXX} ({tên quy trình trước})
- Chuyển cho: PROC-{YYY} ({tên quy trình sau})
```

## PROC-ID Convention

Format: `PROC-{NNN}` — sequential per department.

| Range | Department |
|-------|-----------|
| PROC-001 → PROC-099 | Kinh doanh (Sales) |
| PROC-100 → PROC-199 | Vận hành (Operations) |
| PROC-200 → PROC-299 | Tài chính (Finance) |
| PROC-300 → PROC-399 | Nhân sự (HR) |
| PROC-400 → PROC-499 | IT & Hệ thống |
| PROC-500 → PROC-599 | Marketing |
| PROC-600 → PROC-699 | CSKH (Customer Service) |
| PROC-700+ | Khác |

## Process Status Classification

| Status | Description | Icon |
|--------|-------------|------|
| Manual | 100% thủ công, giấy tờ/Excel | 📝 |
| Partial digital | Có dùng phần mềm nhưng nhiều bước thủ công | ⚡ |
| Full digital | Hoàn toàn trên hệ thống, ít can thiệp thủ công | 🟢 |

## Frequency Guide

| Label | Meaning |
|-------|---------|
| Realtime | Liên tục, không có schedule |
| Daily | 1+ lần/ngày |
| Weekly | 1-5 lần/tuần |
| Monthly | 1-4 lần/tháng |
| Quarterly | Mỗi quý |
| On-demand | Khi có yêu cầu |
| Event-driven | Khi có sự kiện trigger |
