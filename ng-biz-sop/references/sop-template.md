# SOP: [Tên Quy Trình]

**Phiên bản:** [X.Y] | **Ngày tạo:** [YYYY-MM-DD] | **Người tạo:** [Tên]
**Review tiếp theo:** [YYYY-MM-DD] | **Người phê duyệt:** [Tên]

---

## 1. Tổng quan

- **Mục đích:** [Mô tả ngắn gọn — quy trình này làm gì và tại sao tồn tại]
- **Phạm vi:** [Áp dụng cho ai, trong tình huống nào, khi nào kích hoạt]
- **Kết quả mong đợi:** [Output cụ thể và có thể đo lường được]
- **Người sở hữu:** [Vai trò chịu trách nhiệm cuối cùng]

---

## 2. ROI & Đánh giá ưu tiên

| Metric | Giá trị |
|--------|---------|
| Thời gian/lần thực hiện | [X phút] |
| Tần suất | [X lần/tuần hoặc tháng] |
| Tỷ lệ lỗi hiện tại | [X%] |
| Chi phí sửa lỗi | [X giờ hoặc VND/lần] |
| Giờ tài liệu hóa | [X giờ] |
| **ROI ước tính** | **[X.Xx]** |
| **Mức ưu tiên** | **[Cao / Trung bình / Thấp]** |

---

## 3. Input / Output

### Input

| # | Nguồn | Định dạng | Ví dụ | Bắt buộc? |
|---|-------|-----------|-------|-----------|
| 1 | [Hệ thống/người cung cấp] | [CSV, email, form, ...] | [file_name.csv] | [Có/Không] |

### Output

| # | Sản phẩm | Định dạng | Tiêu chí chấp nhận |
|---|----------|-----------|---------------------|
| 1 | [Tên output] | [PDF, bản ghi CRM, ...] | [Điều kiện để coi là đúng] |

---

## 4. Quy trình chi tiết

### Bước 1: [Tên bước]

- **WHAT:** [Hành động cụ thể — động từ + đối tượng + vị trí]
- **WHY:** [Lý do thực hiện bước này — hậu quả nếu bỏ qua]
- **RESULT:** [Kết quả mong đợi sau bước này — hoặc kích hoạt EC-XX nếu sai]
- **Phân loại:** [A — Full AI / B — AI + Review / C — Human-led / D — Human-only]
- **Thời gian:** [X phút]
- **Người thực hiện:** [Vai trò]

### Bước 2: [Tên bước]

- **WHAT:** [Hành động cụ thể]
- **WHY:** [Lý do]
- **RESULT:** [Kết quả mong đợi]
- **Phân loại:** [A/B/C/D]
- **Thời gian:** [X phút]
- **Người thực hiện:** [Vai trò]

<!-- Thêm bước theo cùng cấu trúc -->

---

## 5. Xử lý ngoại lệ (Edge Cases)

| EC-ID | Tên tình huống | Điều kiện kích hoạt | Tần suất | Mức độ | Cách xử lý | Leo thang |
|-------|---------------|---------------------|----------|--------|-------------|-----------|
| EC-01 | [Tên ngắn] | [Khi nào xảy ra] | rare/occasional/common | minor/major/critical | [Các bước xử lý] | [Báo ai, khi nào] |
| EC-02 | | | | | | |
| EC-03 | | | | | | |

---

## 6. Bảo mật & Phân quyền

| Bước | Dữ liệu nhạy cảm | Mức độ (L1–L4) | Quyền truy cập | Người chịu trách nhiệm |
|------|-------------------|----------------|----------------|------------------------|
| Bước 1 | [Tên dữ liệu] | [L1/L2/L3/L4] | [Vai trò được phép] | [Tên/vai trò] |

**Ghi chú phân cấp:**
- L1 — Công khai: Không hạn chế
- L2 — Nội bộ: Ghi log truy cập
- L3 — Bảo mật: Phân quyền theo vai trò, audit trail
- L4 — Hạn chế: Chỉ con người xử lý, AI không lưu trữ

---

## 7. Trust & Tự động hóa

| Giai đoạn | Mức tự động hóa | Điều kiện tiến lên |
|-----------|-----------------|-------------------|
| Tuần 1–2 | 10% | Accuracy ≥95% trong 2 tuần |
| Tuần 3–4 | 30% | Accuracy ≥95% trong 2 tuần |
| Tháng 2 | 50% | Accuracy ≥95% trong 2 tuần |
| Tháng 3+ | 80–100% | Ổn định, review theo exception |

---

## 8. Lịch Review & Versioning

- **Tần suất review:** [weekly / monthly / quarterly]
- **Trigger review ngay:** Lỗi AI, thay đổi quy trình, cập nhật hệ thống
- **Quy tắc version:** MAJOR.MINOR — MAJOR khi quy trình thay đổi căn bản

| Version | Ngày | Thay đổi | Tác giả |
|---------|------|---------|---------|
| 1.0 | [YYYY-MM-DD] | Tạo mới | [Tên] |

---

## 9. Readiness Score

**[X/13]** — [Ready for AI deployment / Minor gaps / Review Needed / Not Ready]

Xem chi tiết: `references/sop-readiness-checklist.md`
