# Kế hoạch Đo lường Website Booking — langnghenhatrangxua.com

**Ngày:** 2026-03-25
**Mục tiêu:** Đo baseline → cải tiến website → đo lại sau 1 tuần → đánh giá hiệu quả
**Công cụ hiện có:** GTM (GTM-T97JMFT7), Microsoft Clarity (vzamc2sjqv)
**Công cụ mới:** Umami (thay thế GA4 + GTM) + giữ Clarity

### Stack Analytics

| Trước | Sau | Lý do |
|-------|-----|-------|
| GTM + GA4 + Clarity | **Umami + Clarity** | Umami cover traffic + events + funnels. Clarity cover heatmap + recordings. Bỏ GTM vì Umami track events native bằng `data-umami-event`. Privacy-friendly, self-host, ad-blocker không chặn. |

> **Lưu ý:** Giữ GTM container hiện tại nhưng **không thêm tags mới**. Nếu sau này cần Facebook Pixel / Google Ads conversion thì bật lại GTM cho mục đích đó.

---

## 1. Hiện trạng Booking Flow

### 1.1 Sơ đồ toàn bộ điểm Booking trên site

```
                          ┌─────────────────────────────────────────┐
                          │            HOMEPAGE (/)                  │
                          │  CTA: "Schedule a FREE consultation"     │
                          │  → link /booking (404!)                  │
                          └────┬──────────────┬──────────────┬──────┘
                               │              │              │
                    ┌──────────▼──┐   ┌───────▼───────┐  ┌──▼──────────────┐
                    │  About Us    │   │  Workshop/*   │  │ General Intro/* │
                    │ CTA: Explore │   │  (8 pages)    │  │  Tet Holiday    │
                    │ → /booking-  │   │               │  │  Light Show     │
                    │   request    │   │               │  │  Food Stories   │
                    └──────────────┘   └───────┬───────┘  └──┬──────────────┘
                                               │             │
                    ┌──────────────────────────▼─────────────▼──────────────┐
                    │              3 LOẠI ĐIỂM BOOKING                      │
                    ├──────────────────────────────────────────────────────┤
                    │                                                      │
                    │  ① /booking-request (Tổng hợp)                       │
                    │     Form: chọn dịch vụ → điền info → submit          │
                    │     Hotline: 0935 810 808                            │
                    │     Email: info@langnghenhatrangxua.com              │
                    │                                                      │
                    │  ② /workshop/* (8 workshop riêng lẻ)                 │
                    │     Mỗi trang có inline form "Book the workshop"     │
                    │     Hotline: 0922 451 451                            │
                    │     Email: salesnhatrangxua@gmail.com                │
                    │     → Cooking class dùng email riêng:                │
                    │       hello.cookingclassntx@gmail.com                │
                    │                                                      │
                    │  ③ Hotline / Email (không qua form)                  │
                    │     → Không track được nếu gọi trực tiếp             │
                    └──────────────────────────────────────────────────────┘
```

### 1.2 Chi tiết 8 Workshop Pages (mỗi trang có booking riêng)

| Workshop | URL | Có giá? | Có lịch? | Form? | Đặc biệt |
|----------|-----|---------|----------|-------|-----------|
| Lacquer Painting | /workshop/lacquer-painting | ❌ | ❌ | ✅ Inline | Trẻ <6 miễn phí, 6-11 giảm 50% |
| Bamboo Dragonfly | /workshop/bamboo-dragonfly | ❌ | ❌ | ✅ Inline | |
| Seashell Decoration | /workshop/seashell-decoration | ❌ | ❌ | ✅ Inline | |
| Canvas Painting | /workshop/canvas-painting | ❌ | ❌ | ✅ Inline | |
| Conical Hat | /workshop/conical-hat-decoration | ❌ | ❌ | ✅ Inline | |
| Incense Making | /workshop/incense-making | ❌ | ❌ | ✅ Inline | |
| Clay Pottery | /workshop/clay-pottery | ❌ | ❌ | ✅ Inline | ~60 phút |
| Cooking Class | /workshop/cooking-class | ❌ | ❌ | ✅ Inline | Email riêng, VAT chưa bao gồm |

**Nhận xét chung:** Tất cả 8 workshop đều KHÔNG hiển thị giá và lịch — rào cản lớn nhất để booking.

### 1.3 Vấn đề phát hiện

**Critical:**
- CTA homepage "Schedule a FREE consultation" — text từ template tài chính, không phải du lịch
- Link `/booking` trên homepage → **404!** Link đúng là `/booking-request`
- **Không trang nào hiện giá** — user phải submit form mới biết giá → conversion rất thấp
- Không có thank-you/confirmation page sau submit → không track được conversion

**High:**
- 3 email khác nhau cho booking (info@, sales@, hello.cooking@) — thiếu nhất quán
- 2 hotline khác nhau (0935 810 808 vs 0922 451 451) — gây hoang mang
- Không có Zalo (kênh #1 tại VN) — mất conversion kênh quan trọng nhất
- Meta description booking page chỉ là "Booking" — zero SEO value
- Không có floating CTA hoặc sticky booking bar

**Medium:**
- Workshop form không có date/time picker — phải liên hệ qua lại nhiều lần
- Không có review/testimonial trên booking pages
- Tet Holiday page chỉ có liên hệ partnership, không có booking cho khách tham quan

---

## 2. Những gì cần đo (Metrics Framework)

### A. TRAFFIC METRICS (Nguồn truy cập)

| Metric | Mô tả | Công cụ | Cách đo |
|--------|--------|---------|---------|
| **Sessions** | Tổng lượt truy cập/tuần | Umami | Tự động |
| **Users** | Số người dùng unique | Umami | Tự động |
| **Traffic source** | Organic / Direct / Social / Referral / Paid | Umami | Tự động |
| **Landing page** | Trang vào đầu tiên | Umami | Tự động |
| **Geo / City** | Vị trí người dùng (VN vs quốc tế, TP nào) | Umami | Tự động |
| **Language** | Ngôn ngữ trình duyệt (vi, en, ko, zh, ja...) | Umami | Tự động |
| **Device** | Mobile / Desktop / Tablet | Umami | Tự động |
| **New vs Returning** | Khách mới vs quay lại | Umami | Tự động |

### B. BEHAVIOR METRICS (Hành vi trên trang)

| Metric | Mô tả | Công cụ | Cách đo |
|--------|--------|---------|---------|
| **Bounce Rate** | % rời trang không tương tác | Umami | Tự động |
| **Avg. Engagement Time** | Thời gian tương tác TB | Umami | Tự động |
| **Pages/Session** | Số trang xem/phiên | Umami | Tự động |
| **Scroll Depth** | % cuộn trang (25/50/75/90/100%) | Clarity | Scroll heatmap (tự động) |
| **Click Heatmap** | Vùng click nhiều nhất | Clarity | Tự động |
| **Scroll Heatmap** | Xem user cuộn đến đâu | Clarity | Tự động |
| **Session Recording** | Video replay hành vi user | Clarity | Tự động |
| **Dead Clicks** | Click vào nơi không có link | Clarity | Tự động |
| **Rage Clicks** | Click liên tục (frustration) | Clarity | Tự động |
| **Quick Backs** | Vào trang rồi back ngay | Clarity | Tự động |

### C. CONVERSION METRICS (Chuyển đổi — QUAN TRỌNG NHẤT)

Có **3 nhóm conversion** cần track riêng:

#### C1. General Booking (`/booking-request`)

| Metric | Mô tả | Công cụ | Cách đo |
|--------|--------|---------|---------|
| **Booking Page Views** | Lượt xem /booking-request | Umami | Page view filter |
| **General Form Start** | Bắt đầu điền form | Umami | **Custom event** ⚡ |
| **General Form Submit** | Nhấn "Submit registration" | Umami | **Custom event** ⚡ |
| **CTA Click from Homepage** | % click CTA booking từ homepage | Umami | **Custom event** ⚡ |

#### C2. Workshop Booking (`/workshop/*` — 8 trang)

| Metric | Mô tả | Công cụ | Cách đo |
|--------|--------|---------|---------|
| **Workshop Page Views** | Lượt xem mỗi workshop (tách theo slug) | Umami | Page view filter |
| **Workshop Form Start** | Focus vào form "Book the workshop" | Umami | **Custom event** ⚡ |
| **Workshop Form Submit** | Nhấn "Submit registration" trên workshop | Umami | **Custom event** ⚡ |
| **Workshop → General Booking** | User rời workshop đến /booking-request | Umami | Page flow analysis |

#### C3. Contact Conversions (tất cả trang)

| Metric | Mô tả | Công cụ | Cách đo |
|--------|--------|---------|---------|
| **Phone Click** | Click hotline (cả 0935 và 0922) | Umami | **Custom event** ⚡ |
| **Email Click** | Click mailto: links | Umami | **Custom event** ⚡ |
| **Zalo/Social Click** | Click Zalo/Facebook/Messenger | Umami | **Custom event** ⚡ |

#### C4. Tổng hợp

| Metric | Công thức |
|--------|-----------|
| **Total Form Submissions** | General Submit + Workshop Submit |
| **Total Contact Actions** | Phone + Email + Zalo clicks |
| **Overall Conversion Rate** | (Total Submissions + Contact Actions) / Sessions × 100 |
| **Form Abandonment Rate** | (Form Start − Form Submit) / Form Start × 100 |
| **Workshop Conversion Rate** | Workshop Submit / Workshop Page Views × 100 (tách theo workshop) |

### D. FUNNEL METRICS (2 phễu chính)

**Phễu 1: General Booking (qua homepage)**
```
[Any Page Visit] → [CTA Click] → [/booking-request View] → [Form Start] → [Form Submit]
     100%             ??%              ??%                     ??%            ??%
```

**Phễu 2: Workshop Booking (trực tiếp)**
```
[Workshop Page View] → [Scroll to Form] → [Form Start] → [Form Submit]
       100%                 ??%               ??%            ??%
```

**Phễu 3: Workshop → General (cross-funnel)**
```
[Workshop View] → [Click "Explore now"/CTA] → [/booking-request] → [Form Submit]
     100%                ??%                        ??%                ??%
```

Đo drop-off tại mỗi bước để biết chỗ nào mất khách nhiều nhất.
**Quan trọng:** So sánh conversion rate giữa workshop booking vs general booking để biết flow nào hiệu quả hơn.

---

## 3. Setup cần làm NGAY (Tuần 0 — Baseline)

### 3.1 Umami Setup (thay GA4 + GTM)

#### Bước 1: Cài đặt Umami

**Option A: Self-host** (khuyến nghị — ad-blocker không chặn)
- Deploy trên VPS hoặc Vercel/Railway/Docker
- Database: PostgreSQL hoặc MySQL
- Trỏ subdomain: `analytics.langnghenhatrangxua.com`

**Option B: Umami Cloud** (nhanh, $9/tháng)
- Đăng ký tại `https://cloud.umami.is`

#### Bước 2: Thêm tracking script

```html
<!-- Thêm vào <head> của layout chính (Next.js _app hoặc layout.tsx) -->
<script defer src="https://analytics.langnghenhatrangxua.com/script.js"
        data-website-id="YOUR_WEBSITE_ID"></script>
```

> Nếu self-host trên cùng domain → ad-blocker **không chặn được** → data accuracy ~100%

#### Bước 3: Kiểm tra hoạt động
- Vào Umami dashboard → Realtime → mở website trên trình duyệt → thấy 1 active visitor = OK

### 3.2 Umami Custom Events (9 events — thay GTM)

#### Event 1–3: CTA & General Booking (HTML attributes)

```html
<!-- CTA booking (trên homepage, about, bất kỳ trang nào) -->
<a href="/booking-request"
   data-umami-event="cta-booking-click"
   data-umami-event-location="homepage-hero">
   Đặt chỗ ngay
</a>

<!-- General form submit (/booking-request) -->
<button type="submit"
   data-umami-event="general-form-submit">
   Submit registration
</button>
```

#### Event 4–5: Workshop Booking (HTML attributes)

```html
<!-- Workshop form submit (trên mỗi workshop page) -->
<button type="submit"
   data-umami-event="workshop-form-submit"
   data-umami-event-workshop="lacquer-painting">
   Submit registration
</button>

<!-- Áp dụng tương tự cho 8 workshops, thay workshop name: -->
<!-- lacquer-painting, bamboo-dragonfly, seashell-decoration,
     canvas-painting, conical-hat, incense-making,
     clay-pottery, cooking-class -->
```

#### Event 6–8: Contact Actions (HTML attributes)

```html
<!-- Phone click -->
<a href="tel:0935810808"
   data-umami-event="phone-click"
   data-umami-event-number="0935810808">
   0935 810 808
</a>

<!-- Email click -->
<a href="mailto:info@langnghenhatrangxua.com"
   data-umami-event="email-click"
   data-umami-event-address="info">
   info@langnghenhatrangxua.com
</a>

<!-- Social click -->
<a href="https://www.facebook.com/NhahangNhaTrangXua"
   data-umami-event="social-click"
   data-umami-event-platform="facebook">
   Facebook
</a>
```

#### Event 2 & 4: Form Start (JavaScript — thêm vào booking pages)

```javascript
// File: tracking-events.js (hoặc inline trong component)
// General booking form start
if (window.location.pathname === '/booking-request') {
  document.querySelector('form input')?.addEventListener('focus', () => {
    umami.track('general-form-start');
  }, { once: true });
}

// Workshop booking form start
if (window.location.pathname.startsWith('/workshop/')) {
  const workshop = window.location.pathname.split('/').pop();
  document.querySelector('form input')?.addEventListener('focus', () => {
    umami.track('workshop-form-start', { workshop });
  }, { once: true });
}
```

#### Event 9: Scroll Depth → KHÔNG CẦN (Clarity có scroll heatmap)

Clarity tự động track scroll depth bằng scroll heatmap — chi tiết hơn Umami.
Không cần duplicate tracking.

### Tổng hợp 9 events

| # | Event Name | Loại | Cách implement |
|---|-----------|------|----------------|
| 1 | `cta-booking-click` | Micro conversion | HTML `data-umami-event` |
| 2 | `general-form-start` | Funnel step | JS `addEventListener` |
| 3 | `general-form-submit` | 🔴 Primary conversion | HTML `data-umami-event` |
| 4 | `workshop-form-start` | Funnel step | JS `addEventListener` |
| 5 | `workshop-form-submit` | 🔴 Primary conversion | HTML `data-umami-event` + workshop name |
| 6 | `phone-click` | 🟠 Secondary conversion | HTML `data-umami-event` |
| 7 | `email-click` | 🟠 Secondary conversion | HTML `data-umami-event` |
| 8 | `social-click` | Engagement | HTML `data-umami-event` |
| 9 | scroll depth | Behavior | ~~Umami~~ → **Clarity scroll heatmap** |

### 3.3 Umami Funnel Setup (thay GA4 Funnel Exploration)

Trong Umami v2+ dashboard, vào **Funnels** → tạo 2 funnels:

**Funnel A: General Booking**

| Step | URL / Event |
|------|-------------|
| 1 | Page visit: `/` (hoặc any page) |
| 2 | Event: `cta-booking-click` |
| 3 | Page visit: `/booking-request` |
| 4 | Event: `general-form-start` |
| 5 | Event: `general-form-submit` |

**Funnel B: Workshop Booking**

| Step | URL / Event |
|------|-------------|
| 1 | Page visit: `/workshop/*` |
| 2 | Event: `workshop-form-start` |
| 3 | Event: `workshop-form-submit` |

> Filter theo `workshop` event property để so sánh 8 workshop.

### 3.4 Umami API — Automated Report (thay GA4 reports)

Umami cung cấp REST API để pull data tự động, không cần vào dashboard:

```bash
# Auth
TOKEN=$(curl -s -X POST https://analytics.langnghenhatrangxua.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"***"}' | jq -r '.token')

# Traffic stats tuần qua
curl -H "Authorization: Bearer $TOKEN" \
  "https://analytics.langnghenhatrangxua.com/api/websites/{id}/stats?startAt=$(date -d '7 days ago' +%s000)&endAt=$(date +%s000)"

# Custom events (booking conversions)
curl -H "Authorization: Bearer $TOKEN" \
  "https://analytics.langnghenhatrangxua.com/api/websites/{id}/events?startAt=...&endAt=...&unit=day"

# Metrics theo device / language / country
curl -H "Authorization: Bearer $TOKEN" \
  "https://analytics.langnghenhatrangxua.com/api/websites/{id}/metrics?type=device&startAt=...&endAt=..."
```

**Có thể tự động hóa:** Cron job chạy mỗi tuần → pull data → generate markdown report → so sánh với baseline.

### 3.5 Microsoft Clarity Setup (giữ nguyên)

Clarity đã cài. Cần bổ sung:

**Custom Tags:**
- `booking_general` — user vào /booking-request
- `booking_workshop` — user vào /workshop/*
- `booking_converter` — user submit form bất kỳ

**Saved Filters (tạo 4 filters):**
- "General Booking Sessions" = sessions có page /booking-request
- "Workshop Sessions" = sessions có page contains /workshop/
- "All Booking Sessions" = general OR workshop
- "Converter Sessions" = sessions có smart event "Submit registration"

**Smart Events:**
- "Submit registration" button click (tất cả trang)
- "Book the workshop" button click
- Phone number click

**Clarity đảm nhận những gì Umami KHÔNG có:**
- Heatmaps (click + scroll) trên booking pages
- Session recordings — xem user hành xử thực tế
- Rage clicks / Dead clicks — phát hiện UX frustration
- Quick backs — user vào rồi back ngay

---

## 4. Bảng so sánh Before/After (1 tuần)

### 4.1 Template đo Baseline (Tuần 0) vs After (Tuần 1)

| Metric | Tuần 0 (Baseline) | Tuần 1 (After) | Thay đổi | Đánh giá |
|--------|-------------------|----------------|----------|----------|
| **TRAFFIC** | | | | |
| Total Sessions | ___ | ___ | ___% | |
| Unique Users | ___ | ___ | ___% | |
| Mobile % | ___% | ___% | ±___% | |
| Vietnamese users % | ___% | ___% | ±___% | |
| Top 3 Traffic Sources | ___ | ___ | — | |
| **BEHAVIOR** | | | | |
| Bounce Rate (toàn site) | ___% | ___% | ±___% | ↓ tốt |
| Bounce Rate (/booking-request) | ___% | ___% | ±___% | ↓ tốt |
| Bounce Rate (/workshop/*) | ___% | ___% | ±___% | ↓ tốt |
| Avg. Engagement Time | ___s | ___s | ±___s | ↑ tốt |
| Pages/Session | ___ | ___ | ±___ | ↑ tốt |
| **GENERAL BOOKING FUNNEL** | | | | |
| /booking-request Page Views | ___ | ___ | ___% | ↑ tốt |
| CTA Click → Booking Page % | ___% | ___% | ±___% | ↑ tốt |
| Form Start Rate | ___% | ___% | ±___% | ↑ tốt |
| Form Submit Rate | ___% | ___% | ±___% | ↑ tốt |
| General Submissions | ___ | ___ | ___% | ↑ tốt |
| **WORKSHOP BOOKING FUNNEL** | | | | |
| Workshop Page Views (tổng 8) | ___ | ___ | ___% | ↑ tốt |
| Top 3 Workshop xem nhiều nhất | ___ | ___ | — | |
| Workshop Form Start Rate | ___% | ___% | ±___% | ↑ tốt |
| Workshop Form Submit Rate | ___% | ___% | ±___% | ↑ tốt |
| Workshop Submissions | ___ | ___ | ___% | ↑ tốt |
| Workshop có CR cao nhất | ___ | ___ | — | |
| Workshop có CR thấp nhất | ___ | ___ | — | |
| **CONTACT ACTIONS** | | | | |
| Phone Clicks (0935) | ___ | ___ | ___% | ↑ tốt |
| Phone Clicks (0922) | ___ | ___ | ___% | ↑ tốt |
| Email Clicks | ___ | ___ | ___% | ↑ tốt |
| Social/Zalo Clicks | ___ | ___ | ___% | ↑ tốt |
| **TỔNG CONVERSION** | | | | |
| Total Form Submissions | ___ | ___ | ___% | ↑ tốt |
| Total Contact Actions | ___ | ___ | ___% | ↑ tốt |
| Overall Conversion Rate | ___% | ___% | ±___% | ↑ tốt |
| **CLARITY INSIGHTS** | | | | |
| Dead Clicks count | ___ | ___ | ___% | ↓ tốt |
| Rage Clicks count | ___ | ___ | ___% | ↓ tốt |
| Quick Backs from booking | ___ | ___ | ___% | ↓ tốt |

### 4.1.1 So sánh Workshop vs General Booking

| Workshop | Views T0 | Submit T0 | CR T0 | Views T1 | Submit T1 | CR T1 | Δ CR |
|----------|----------|-----------|-------|----------|-----------|-------|------|
| Lacquer Painting | | | | | | | |
| Cooking Class | | | | | | | |
| Clay Pottery | | | | | | | |
| Bamboo Dragonfly | | | | | | | |
| Seashell Decoration | | | | | | | |
| Canvas Painting | | | | | | | |
| Conical Hat | | | | | | | |
| Incense Making | | | | | | | |
| **General /booking-request** | | | | | | | |

### 4.2 Cách đánh giá hiệu quả

| Thay đổi | Ý nghĩa |
|----------|---------|
| Conversion Rate tăng ≥ 20% | ✅ Cải tiến **có hiệu quả rõ rệt** |
| Conversion Rate tăng 5-20% | ⚠️ Có cải thiện, cần tiếp tục optimize |
| Conversion Rate không đổi (±5%) | ❌ Cải tiến chưa đúng chỗ, cần phân tích lại |
| Bounce Rate giảm ≥ 10% | ✅ Content/UX cải thiện tốt |
| Engagement Time tăng ≥ 15% | ✅ User quan tâm hơn |
| Funnel drop-off giảm ở bước nào | ✅ Chỗ đó đã fix đúng |

### 4.3 Lưu ý thống kê

- **1 tuần là minimum** để có data ý nghĩa. Nếu traffic thấp (<500 sessions/tuần), cần 2 tuần.
- **So sánh cùng ngày trong tuần** (T2-CN vs T2-CN) vì hành vi du lịch thay đổi theo ngày.
- **Loại bỏ traffic bất thường** (bot, internal testing) bằng filter trong Umami.
- Không thay đổi quá nhiều thứ cùng lúc — khó biết yếu tố nào tạo hiệu quả.

---

## 5. Gợi ý Cải tiến Website (dựa trên Audit)

### Ưu tiên cao — Ảnh hưởng trực tiếp đến Booking Conversion

| # | Cải tiến | Lý do | Metric bị ảnh hưởng |
|---|----------|-------|---------------------|
| 1 | **Fix link /booking → /booking-request** | CTA trên homepage dẫn đến 404! | Funnel drop-off, conversion rate |
| 2 | **Đổi CTA text** "Schedule a FREE consultation" → "Đặt chỗ ngay" hoặc "Book Now" | Text hiện tại giống template tài chính, không liên quan du lịch | CTA click rate |
| 3 | **Thêm giá / package** trên homepage và booking page | User không biết giá → không đặt | Form start rate, conversion |
| 4 | **Thêm floating CTA** "Đặt chỗ" sticky ở bottom mobile | Hiện không có CTA cố định khi cuộn | CTA visibility, click rate |
| 5 | **Thêm trust signals** vào booking page: reviews, photos, "500+ khách/tháng" | Booking page hiện rất trơ, không thuyết phục | Form submit rate |
| 6 | **Thêm Zalo button** (phổ biến VN hơn Messenger) | Kênh liên hệ chính của người Việt | Total conversions (phone + chat) |
| 7 | **Tạo Thank-you page** sau submit form | Hiện không rõ submit thành công chưa + track conversion | Conversion tracking accuracy |
| 8 | **Fix ngôn ngữ** — CTA, form labels nên là tiếng Việt cho audience VN | Site mix EN/VI lung tung | Engagement, trust |

### Ưu tiên trung bình

| # | Cải tiến | Metric |
|---|----------|--------|
| 9 | Thêm lịch chọn ngày vào booking form | Form completion rate |
| 10 | Hiện số lượng chỗ còn (urgency) | Conversion rate |
| 11 | Thêm FAQ về booking process | Bounce rate on booking page |
| 12 | Tối ưu mobile speed (giảm font files) | Mobile bounce rate, engagement |

---

## 6. Timeline thực hiện

```
Tuần 0 (NGAY BÂY GIỜ):
├── Ngày 1-2: Deploy Umami + thêm tracking script + events + Clarity filters
├── Ngày 3-7: Thu thập data baseline (KHÔNG thay đổi website)
└── Cuối tuần 0: Ghi nhận tất cả metrics vào bảng Baseline

Tuần 1 (SAU KHI CÓ BASELINE):
├── Ngày 1-2: Triển khai cải tiến ưu tiên cao (#1-#8)
├── Ngày 3-7: Thu thập data sau cải tiến
└── Cuối tuần 1: So sánh với Baseline

Tuần 2+:
├── Phân tích kết quả
├── Tiếp tục A/B test các yếu tố cụ thể
└── Lặp lại chu kỳ đo → cải tiến → đo
```

---

## 7. Checklist Setup Nhanh

### Phase 1: Setup Tracking (Ngày 1-2)
- [ ] Deploy Umami (self-host hoặc cloud)
- [ ] Thêm Umami tracking script vào website `<head>`
- [ ] Xác nhận Umami hoạt động (Dashboard > Realtime > thấy visitor)
- [ ] Thêm `data-umami-event` attributes vào 7 loại elements (mục 3.2)
- [ ] Thêm JS tracking cho form-start events (mục 3.2)
- [ ] Test tất cả events bằng cách click thử → xem Umami Events tab
- [ ] Tạo 2 Funnels trong Umami (mục 3.3)
- [ ] Tạo 4 Clarity saved filters (mục 3.5)
- [ ] Tạo 3 Clarity smart events (mục 3.5)

### Phase 2: Baseline Collection (Ngày 3-7)
- [ ] KHÔNG thay đổi website trong 5 ngày
- [ ] Kiểm tra data đang chảy vào Umami hàng ngày
- [ ] Xem Clarity recordings hàng ngày (ít nhất 10 sessions/ngày)
- [ ] Cuối tuần: điền tất cả metrics vào bảng 4.1

### Phase 3: Improvements (Tuần 1, Ngày 1-2)
- [ ] Fix link /booking → /booking-request
- [ ] Đổi CTA text phù hợp du lịch
- [ ] Xóa nội dung template (bank logos, residential loans link)
- [ ] Thống nhất hotline + email trên tất cả trang
- [ ] Thêm Zalo button

### Phase 4: Measurement (Tuần 1, Ngày 3-7)
- [ ] Thu thập data 5 ngày sau cải tiến
- [ ] Cuối tuần 1: điền bảng 4.1 cột "Tuần 1"
- [ ] So sánh và đánh giá

---

## Unresolved Questions

1. **Umami deploy ở đâu?** — Self-host (VPS/Docker) hay Umami Cloud? Nếu self-host, cần VPS có PostgreSQL. Nếu dùng Vercel thì cần database bên ngoài (Neon/Supabase).
2. **Form submit đi đâu?** — Không rõ form gửi data đến API nào, có thank-you page/confirmation message không. Cần kiểm tra code để tracking chính xác.
3. **Traffic hiện tại bao nhiêu?** — Nếu <100 sessions/tuần, cần đo 2-3 tuần mới so sánh được.
4. **Có chạy quảng cáo không?** — Nếu có paid traffic, cần tách riêng organic vs paid khi so sánh.
5. **Booking qua điện thoại có track được không?** — Nếu phần lớn booking qua hotline, web form chỉ là 1 phần. Cân nhắc dùng call tracking number riêng hoặc hỏi sales team ghi nhận nguồn.
6. **Tại sao có 2 hotline + 3 email khác nhau?** — 0935 810 808 (general) vs 0922 451 451 (workshop) vs 3 email. Cần xác nhận flow xử lý nội bộ để biết data nào cần track.
7. **Workshop nào phổ biến nhất hiện tại?** — Cần data từ team sales/operations để cross-check với web analytics.
8. **Có kế hoạch thêm tính năng booking online (chọn ngày, thanh toán)?** — Nếu có, measurement plan cần mở rộng thêm e-commerce tracking.
