# Business Research Methodology

Adapted from RRI (Reverse Requirements Interview) for business domain discovery.

## Core Principle

**Original RRI:** Propose software requirements → confirm/reject instead of open-ended elicitation.
**Adapted:** Propose business domain understanding → confirm/correct instead of "tell me about your business."

Same cognitive shift: interviewer arrives with structured hypotheses, stakeholder acts as validator — not lecturer.

---

## Why This Works

Open-ended: "Mô tả quy trình kinh doanh của bạn?" → 30-minute monologue, 20% signal.

Propose-confirm: "Tôi hiểu quy trình bán hàng gồm 4 bước. Đúng không?" → 30-second confirmation, 80% signal.

---

## The 5 Business Personas

### 1. Khách hàng (Customer) — maps to End User in RRI
- Journey stages: Awareness → Consideration → Purchase → Use → Support → Loyalty
- Captures: pain points at each stage, expectations vs reality, touchpoints, retention drivers
- Interview focus: what frustrates customers, why they choose/leave, support experience

### 2. Chủ doanh nghiệp (Owner/CEO) — maps to Business Analyst in RRI
- Captures: vision & strategy, revenue streams, cost structure, competitive landscape, growth plans
- Interview focus: what metrics matter, where bottlenecks block growth, strategic priorities
- Highest priority persona — sets context for all others

### 3. Quản lý vận hành (Operations) — maps to Operator in RRI
- Captures: department structure, daily workflows, tools & systems, bottlenecks, SLAs
- Interview focus: what breaks, what's manual, where time is wasted
- Most process-rich persona — feeds directly into process mapping

### 4. Tài chính & Tuân thủ (Finance) — maps to QA/Tester in RRI
- Captures: revenue model & pricing, cost centers, compliance requirements, reporting cadence
- Interview focus: approval workflows, reporting burden, financial risk areas
- Validates feasibility of proposed process improvements

### 5. IT & Hệ thống (Technology) — maps to Developer in RRI
- Captures: current tech stack, integration landscape, data flow, technical debt, limitations
- Interview focus: what systems don't talk to each other, where data is duplicated, manual workarounds
- Determines automation readiness level

---

## Interview Flow

**Optimal persona order:** Owner → Operations → Customer → Finance → IT

**Rationale:**
1. Owner sets business context and priorities (big picture first)
2. Operations reveals how strategy translates to daily work
3. Customer provides external validation of internal processes
4. Finance adds financial constraints and compliance overlay
5. IT reveals technical reality and feasibility boundaries

---

## 3 Interview Modes Selection Logic

| Mode | Use when | Signal | Speed |
|------|----------|--------|-------|
| **CHALLENGE** | Documents provided OR industry pattern is clear | "I already know X — confirm?" | Fast |
| **GUIDED** | Multiple valid options exist, need to narrow | "Which of A/B/C/D?" | Medium |
| **EXPLORE** | Unique/complex area, no prior context | "Describe this in your own words" | Deep |

**Rule:** Default to CHALLENGE when documents available. Fall back to GUIDED when CHALLENGE rejected. Use EXPLORE sparingly for complex or ambiguous areas.

---

## 3 Question Layers

| Layer | When | Action |
|-------|------|--------|
| **AUTO-ANSWERED** | Fact found in documents (company name, org chart, product list) | Record silently, skip question |
| **SMART-ASKED** | Partial info in documents, need confirmation | Ask with context: "The brochure mentions X — does this mean Y?" |
| **CHALLENGE-PROPOSED** | No docs but industry pattern applies | Propose confidently: "Most [industry] companies do X. Is that true here?" |

---

## Interview Cadence

- **Full research:** 30-50 questions, 20-30 minutes, all 5 personas
- **Quick mode:** 10-15 questions, 10 minutes, Owner + Operations only
- **Group size per round:** 2-4 related questions
- **Round labeling:** "Round N — [Persona] Persona"

---

## Auto-Answer Sources

| Document Type | Auto-answers |
|---------------|-------------|
| Company brochure / website | Name, industry, products/services, tagline |
| Org chart | Department structure, headcount, reporting lines |
| Process manual / SOP | Existing workflows, approval steps |
| Financial report | Revenue model, cost structure (high level) |
| Job descriptions | Roles, responsibilities, required tools |
| Marketing materials | Customer segments, value proposition |
