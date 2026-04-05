# SOP Readiness Checklist

Score each item: ✅ Pass / ❌ Fail

**Target:** 13/13 before AI deployment.

---

## Clarity (4 items)

1. [ ] Mỗi bước có **WHAT cụ thể** — không dùng từ mơ hồ như "xử lý", "kiểm tra", "xem xét"
       (Ví dụ tốt: "Search CRM by email, check 'Active' status field")

2. [ ] Mỗi bước có **WHY** giải thích lý do tại sao bước đó tồn tại
       (Nếu WHY bị xóa, AI không thể thích nghi khi context thay đổi)

3. [ ] **Người mới** đọc SOP có thể thực hiện hoàn chỉnh **KHÔNG cần hỏi thêm**
       (Test: đưa cho người chưa biết quy trình đọc và thực hành thử)

4. [ ] **Không có bước nào bị bỏ qua** hoặc giả định "ai cũng biết"
       (Đặc biệt: bước chuyển đổi giữa hệ thống, bước chờ xác nhận)

---

## Completeness (4 items)

5. [ ] Tất cả **input/output được liệt kê** với định dạng và ví dụ cụ thể
       (Mỗi input cần: nguồn, định dạng, ví dụ thực tế, bắt buộc hay không)

6. [ ] **Edge cases được map đầy đủ** — ít nhất 3 ngoại lệ cho mỗi quy trình
       (Mỗi EC cần: trigger, tần suất, mức độ, cách xử lý, leo thang)

7. [ ] **Mỗi bước có phân loại automation level** (A / B / C / D)
       (Phân loại quyết định AI làm gì và con người làm gì)

8. [ ] **Tiêu chí chấp nhận (acceptance criteria) rõ ràng** cho mỗi output
       (AI phải biết "done correctly" trông như thế nào để tự verify)

---

## Security & Trust (3 items)

9. [ ] **Dữ liệu nhạy cảm được đánh dấu** (L1–L4) và có protocol xử lý tương ứng
       (L3/L4 cần: audit trail, phân quyền, AI không tự lưu trữ)

10. [ ] **Phân quyền rõ ràng**: ai được làm gì, ai được xem gì ở mỗi bước
        (Không được để mơ hồ — "team" hoặc "ai đó" không phải phân quyền)

11. [ ] **Trust threshold được thiết lập** — target ≥95% accuracy, lộ trình tăng từ 10%
        (Giai đoạn tự động hóa được ghi rõ trong bảng Trust & Tự động hóa)

---

## Operations (2 items)

12. [ ] **Lịch review được thiết lập** (weekly / monthly / quarterly) và ghi vào SOP
        (Phải có ngày review tiếp theo cụ thể, không phải "khi cần")

13. [ ] **Feedback loop được định nghĩa**: quy trình thu thập, phân loại và xử lý lỗi AI
        (Tag lỗi → categorize → update SOP → re-test → increment version)

---

## Score Interpretation

| Score | Trạng thái | Hành động |
|-------|-----------|-----------|
| 13/13 | Ready for AI deployment | Triển khai, monitor theo lịch |
| 10–12 | Minor gaps — proceed with caution | Fix gaps trước khi scale |
| 7–9 | Significant gaps — review needed | Quay lại Phase 2, bổ sung |
| <7 | Not ready | Revisit toàn bộ Phase 2 |

**Lưu ý:** Nếu bất kỳ item nào trong Security (9–11) fail → không triển khai dù tổng điểm cao.
