# Deep Dive Question Bank

Use these questions as a reference during the interview. Group 2–3 related questions per `AskUserQuestion` round.

## Happy Path Questions

- Quy trình bắt đầu khi nào / từ đâu? (trigger event)
- Bước đầu tiên cụ thể là gì? Ai làm? Trên hệ thống nào?
- Sau bước [X], chuyển sang bước gì tiếp theo?
- Có điểm nào cần chờ phê duyệt không? Từ ai?
- Bước nào mất thời gian nhiều nhất? Tại sao?
- Có bước nào phải làm song song không?
- Kết quả cuối cùng là gì? Ai nhận? Ở đâu?
- Tổng thời gian từ đầu đến cuối (best case)?

## Exception Questions

- Bước [X] có thể fail không? Khi nào xảy ra?
- Nếu [input] không hợp lệ → xử lý thế nào?
- Nếu [hệ thống] offline → làm gì tạm thời?
- Nếu người phê duyệt nghỉ phép → ai thay?
- Trường hợp nào buộc phải hủy toàn bộ quy trình?
- Lỗi nào hay xảy ra nhất? Tần suất khoảng bao lâu 1 lần?
- Khi lỗi xảy ra, ai chịu trách nhiệm xử lý?
- Có thể rollback/undo không? Đến bước nào thì không undo được?

## Data Questions

- Dữ liệu nào cần nhập ở bước [X]?
- Dữ liệu này lấy từ đâu? (nhập tay / copy-paste / API / scan / email)
- Định dạng cụ thể? (Excel, PDF, form web, email, database)
- Ai có quyền xem? Ai có quyền sửa?
- Dữ liệu này liên kết với dữ liệu nào khác?
- Có validate không? Quy tắc validate cụ thể?
- Sau khi xử lý, dữ liệu lưu ở đâu? Bao lâu?
- Có báo cáo / export dữ liệu này không? Cho ai?

## Business Rule Questions

- Công thức tính [giá / chiết khấu / hoa hồng / phí]? Cho ví dụ với số thực.
- Ai được phê duyệt đến mức nào? Ngưỡng cụ thể?
- SLA: phải xử lý xong trong bao lâu? Tính từ khi nào?
- Có quy tắc đặc biệt cho [khách VIP / đơn lớn / trường hợp X]?
- Mùa cao điểm có quy tắc khác không?
- Yêu cầu pháp lý / compliance nào liên quan?
- Hãy cho 1 ví dụ thực tế với số liệu cụ thể.

## Integration Questions

- Bước [X] dùng hệ thống / công cụ nào?
- Hệ thống A và B trao đổi dữ liệu thế nào? (copy thủ công / API / file / email)
- Có API sẵn không? REST / SOAP / GraphQL? Có docs không?
- Tần suất sync dữ liệu giữa các hệ thống?
- Khi hệ thống A cập nhật, B có tự cập nhật không?
- Có webhook / event nào kích hoạt bước tiếp theo không?
