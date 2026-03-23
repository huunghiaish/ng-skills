---
name: ng:frontend-slides
description: Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Supports Vietnamese content with proper diacritics rendering and Vietnamese-friendly fonts. Use when the user wants to build a presentation, convert a PPT/PPTX to web, or create slides for a talk/pitch. Forked from zarazhangrui/frontend-slides.
---

# Frontend Slides

Create zero-dependency, animation-rich HTML presentations that run entirely in the browser.

## Language Detection

**Detect the user's language from their message.** If the user writes in Vietnamese (or requests Vietnamese), follow these rules throughout:

- Set `<html lang="vi">` in generated HTML
- All UI text (navigation hints, edit button labels, export labels) in Vietnamese
- Use Vietnamese-compatible fonts — see [references/vietnamese-typography.md](references/vietnamese-typography.md)
- Ensure all diacritics (ă, â, đ, ê, ô, ơ, ư, sắc, huyền, hỏi, ngã, nặng) render correctly
- Use `font-display: swap` to prevent FOIT with Vietnamese characters
- Add `<meta charset="UTF-8">` (already required, but critical for Vietnamese)

**If user writes in English**, proceed normally without Vietnamese-specific adaptations.

## Core Principles

1. **Zero Dependencies** — Single HTML files with inline CSS/JS. No npm, no build tools.
2. **Show, Don't Tell** — Generate visual previews, not abstract choices. People discover what they want by seeing it.
3. **Distinctive Design** — No generic "AI slop." Every presentation must feel custom-crafted.
4. **Viewport Fitting (NON-NEGOTIABLE)** — Every slide MUST fit exactly within 100vh. No scrolling within slides, ever. Content overflows? Split into multiple slides.
5. **Vietnamese Typography First** — When content is Vietnamese, font selection MUST support full Vietnamese Unicode. See [references/vietnamese-typography.md](references/vietnamese-typography.md).

## Design Aesthetics

You tend to converge toward generic, "on distribution" outputs. In frontend design, this creates what users call the "AI slop" aesthetic. Avoid this: make creative, distinctive frontends that surprise and delight.

Focus on:
- Typography: Choose fonts that are beautiful, unique, and interesting. For Vietnamese content, choose from the Vietnamese-compatible font list in [references/vietnamese-typography.md](references/vietnamese-typography.md). Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics.
- Color & Theme: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes. Draw from IDE themes and cultural aesthetics for inspiration.
- Motion: Use animations for effects and micro-interactions. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions.
- Backgrounds: Create atmosphere and depth rather than defaulting to solid colors. Layer CSS gradients, use geometric patterns, or add contextual effects that match the overall aesthetic.

Avoid generic AI-generated aesthetics:
- Overused font families (Inter, Roboto, Arial, system fonts)
- Cliched color schemes (particularly purple gradients on white backgrounds)
- Predictable layouts and component patterns
- Cookie-cutter design that lacks context-specific character

Interpret creatively and make unexpected choices that feel genuinely designed for the context. Vary between light and dark themes, different fonts, different aesthetics.

## Vietnamese Typography Rules

When generating Vietnamese content:

1. **MUST use Vietnamese-compatible fonts** — Many decorative fonts break Vietnamese diacritics. See [references/vietnamese-typography.md](references/vietnamese-typography.md) for curated list.
2. **Line height** — Vietnamese diacritics need more vertical space. Use `line-height: 1.6` minimum for body, `1.3` for headings.
3. **Font size** — Vietnamese text with diacritics is visually denser. Increase `--body-size` by ~5-10% compared to English presets.
4. **Word breaking** — Vietnamese uses spaces between syllables. Set `word-break: keep-all; overflow-wrap: break-word;` to prevent mid-word breaks.
5. **Testing** — Always verify diacritics render: "Xin chào thế giới — Việt Nam xinh đẹp — Đổi mới sáng tạo"

## Viewport Fitting Rules

These invariants apply to EVERY slide in EVERY presentation:

- Every `.slide` must have `height: 100vh; height: 100dvh; overflow: hidden;`
- ALL font sizes and spacing must use `clamp(min, preferred, max)` — never fixed px/rem
- Content containers need `max-height` constraints
- Images: `max-height: min(50vh, 400px)`
- Breakpoints required for heights: 700px, 600px, 500px
- Include `prefers-reduced-motion` support
- Never negate CSS functions directly (`-clamp()`, `-min()`, `-max()` are silently ignored) — use `calc(-1 * clamp(...))` instead

**When generating, read `viewport-base.css` and include its full contents in every presentation.**

### Content Density Limits Per Slide

| Slide Type | Maximum Content |
|------------|-----------------|
| Title slide | 1 heading + 1 subtitle + optional tagline |
| Content slide | 1 heading + 4-6 bullet points OR 1 heading + 2 paragraphs |
| Feature grid | 1 heading + 6 cards maximum (2x3 or 3x2) |
| Code slide | 1 heading + 8-10 lines of code |
| Quote slide | 1 quote (max 3 lines) + attribution |
| Image slide | 1 heading + 1 image (max 60vh height) |

**For Vietnamese content:** Reduce limits by ~15% — Vietnamese text with diacritics takes more vertical space. E.g., 4-5 bullets instead of 4-6.

**Content exceeds limits? Split into multiple slides. Never cram, never scroll.**

---

## Phase 0: Detect Mode

Determine what the user wants:

- **Mode A: New Presentation** — Create from scratch. Go to Phase 1.
- **Mode B: PPT Conversion** — Convert a .pptx file. Go to Phase 4.
- **Mode C: Enhancement** — Improve an existing HTML presentation. Read it, understand it, enhance. **Follow Mode C modification rules below.**

### Mode C: Modification Rules

When enhancing existing presentations, viewport fitting is the biggest risk:

1. **Before adding content:** Count existing elements, check against density limits
2. **Adding images:** Must have `max-height: min(50vh, 400px)`. If slide already has max content, split into two slides
3. **Adding text:** Max 4-6 bullets per slide. Exceeds limits? Split into continuation slides
4. **After ANY modification, verify:** `.slide` has `overflow: hidden`, new elements use `clamp()`, images have viewport-relative max-height, content fits at 1280x720
5. **Proactively reorganize:** If modifications will cause overflow, automatically split content and inform the user. Don't wait to be asked

**When adding images to existing slides:** Move image to new slide or reduce other content first. Never add images without checking if existing content already fills the viewport.

---

## Phase 1: Content Discovery (New Presentations)

**Ask ALL questions in a single AskUserQuestion call** so the user fills everything out at once.

**Adapt question text to user's detected language (Vietnamese or English).**

### Vietnamese Questions:

**Question 1 — Muc dich** (header: "Muc dich"):
Bai trinh bay nay dung cho muc dich gi? Options: Pitch deck / Day hoc-Huong dan / Hoi nghi-Thuyet trinh / Noi bo cong ty

**Question 2 — Do dai** (header: "Do dai"):
Khoang bao nhieu slide? Options: Ngan 5-10 / Vua 10-20 / Dai 20+

**Question 3 — Noi dung** (header: "Noi dung"):
Ban da co noi dung chua? Options: Da co day du / Co ghi chu so / Chi co chu de

**Question 4 — Chinh sua truc tiep** (header: "Chinh sua"):
Ban co can chinh sua text truc tiep tren trinh duyet? Options:
- "Co (Khuyen dung)" — Chinh sua text ngay tren trinh duyet, tu dong luu, xuat file
- "Khong" — Chi xem, file nhe hon

### English Questions (same as original):

**Question 1 — Purpose** (header: "Purpose"):
What is this presentation for? Options: Pitch deck / Teaching-Tutorial / Conference talk / Internal presentation

**Question 2 — Length** (header: "Length"):
Approximately how many slides? Options: Short 5-10 / Medium 10-20 / Long 20+

**Question 3 — Content** (header: "Content"):
Do you have content ready? Options: All content ready / Rough notes / Topic only

**Question 4 — Inline Editing** (header: "Editing"):
Do you need to edit text directly in the browser after generation? Options:
- "Yes (Recommended)" — Can edit text in-browser, auto-save to localStorage, export file
- "No" — Presentation only, keeps file smaller

**Remember the user's editing choice — it determines whether edit-related code is included in Phase 3.**

If user has content, ask them to share it.

### Step 1.2: Image Evaluation (if images provided)

If user selected "No images" -> skip to Phase 2.

If user provides an image folder:
1. **Scan** — List all image files (.png, .jpg, .svg, .webp, etc.)
2. **View each image** — Use the Read tool (Claude is multimodal)
3. **Evaluate** — For each: what it shows, USABLE or NOT USABLE (with reason), what concept it represents, dominant colors
4. **Co-design the outline** — Curated images inform slide structure alongside text. This is NOT "plan slides then add images" — design around both from the start
5. **Confirm via AskUserQuestion** (header: "Outline"/"Dan y"): "Does this slide outline and image selection look right?" Options: Looks good / Adjust images / Adjust outline

**Logo in previews:** If a usable logo was identified, embed it (base64) into each style preview in Phase 2.

---

## Phase 2: Style Discovery

**This is the "show, don't tell" phase.** Most people can't articulate design preferences in words.

### Step 2.0: Style Path

Ask how they want to choose (header: "Style"/"Phong cach"):
- "Cho toi xem mau" / "Show me options" (recommended) — Generate 3 previews based on mood
- "Toi biet minh muon gi" / "I know what I want" — Pick from preset list directly

**If direct selection:** Show preset picker and skip to Phase 3. Available presets are defined in [STYLE_PRESETS.md](STYLE_PRESETS.md).

### Step 2.1: Mood Selection (Guided Discovery)

Ask (header: "Cam xuc"/"Vibe", multiSelect: true, max 2):

**Vietnamese:** Khan gia nen cam thay the nao?
- An tuong / Tu tin — Chuyen nghiep, dang tin cay
- Hung phan / Nang dong — Doi moi, manh me
- Binh tinh / Tap trung — Ro rang, sau sac
- Truyen cam hung — Xuc dong, dang nho

**English:** What feeling should the audience have?
- Impressed/Confident — Professional, trustworthy
- Excited/Energized — Innovative, bold
- Calm/Focused — Clear, thoughtful
- Inspired/Moved — Emotional, memorable

### Step 2.2: Generate 3 Style Previews

Based on mood, generate 3 distinct single-slide HTML previews showing typography, colors, animation, and overall aesthetic. Read [STYLE_PRESETS.md](STYLE_PRESETS.md) for available presets and their specifications.

**For Vietnamese content:** Use Vietnamese sample text in previews: "Xin chao" as title, "Bai trinh bay duoc tao boi..." as subtitle. This lets user see how Vietnamese diacritics look in each style.

| Mood | Suggested Presets |
|------|-------------------|
| Impressed/Confident | Bold Signal, Electric Studio, Dark Botanical |
| Excited/Energized | Creative Voltage, Neon Cyber, Split Pastel |
| Calm/Focused | Notebook Tabs, Paper & Ink, Swiss Modern |
| Inspired/Moved | Dark Botanical, Vintage Editorial, Pastel Geometry |

Save previews to `.claude-design/slide-previews/` (style-a.html, style-b.html, style-c.html). Each should be self-contained, ~50-100 lines, showing one animated title slide.

Open each preview automatically for the user.

### Step 2.3: User Picks

Ask (header: "Style"/"Chon phong cach"):
Which style preview do you prefer? Options: Style A: [Name] / Style B: [Name] / Style C: [Name] / Mix elements / Pha tron cac yeu to

If "Mix elements", ask for specifics.

---

## Phase 3: Generate Presentation

Generate the full presentation using content from Phase 1 (text, or text + curated images) and style from Phase 2.

If images were provided, the slide outline already incorporates them from Step 1.2. If not, CSS-generated visuals (gradients, shapes, patterns) provide visual interest.

**Before generating, read these supporting files:**
- [html-template.md](html-template.md) — HTML architecture and JS features
- [viewport-base.css](viewport-base.css) — Mandatory CSS (include in full)
- [animation-patterns.md](animation-patterns.md) — Animation reference for the chosen feeling
- [references/vietnamese-typography.md](references/vietnamese-typography.md) — **Read if Vietnamese content** for font selection

**Key requirements:**
- Single self-contained HTML file, all CSS/JS inline
- `<html lang="vi">` for Vietnamese content, `<html lang="en">` for English
- Include the FULL contents of viewport-base.css in the `<style>` block
- Use Vietnamese-compatible fonts from [references/vietnamese-typography.md](references/vietnamese-typography.md) when content is Vietnamese
- Use fonts from Fontshare or Google Fonts — never system fonts
- Add detailed comments explaining each section
- Every section needs a clear `/* === SECTION NAME === */` comment block
- For Vietnamese: add `font-display: swap` in @font-face or Google Fonts URL parameter

### Vietnamese-Specific HTML Additions

```html
<!-- Add to <head> for Vietnamese content -->
<html lang="vi">
<meta charset="UTF-8">
<!-- Google Fonts with Vietnamese subset -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
```

```css
/* Vietnamese typography adjustments */
body {
    line-height: 1.6; /* Extra space for diacritics */
    word-break: keep-all;
    overflow-wrap: break-word;
}

/* Ensure diacritics don't clip */
h1, h2, h3, h4, h5, h6 {
    line-height: 1.3;
    padding-top: 0.1em; /* Prevent top diacritics clipping */
}
```

---

## Phase 4: PPT Conversion

When converting PowerPoint files:

1. **Extract content** — Run `python scripts/extract-pptx.py <input.pptx> <output_dir>` (install python-pptx if needed: `pip install python-pptx`)
2. **Confirm with user** — Present extracted slide titles, content summaries, and image counts
3. **Detect language** — If extracted text is Vietnamese, activate Vietnamese font/typography rules
4. **Style selection** — Proceed to Phase 2 for style discovery
5. **Generate HTML** — Convert to chosen style, preserving all text, images (from assets/), slide order, and speaker notes (as HTML comments)

---

## Phase 5: Delivery

1. **Clean up** — Delete `.claude-design/slide-previews/` if it exists
2. **Open** — Use `open [filename].html` to launch in browser
3. **Summarize** — Tell the user (in their language):

**Vietnamese summary:**
- Vi tri file, ten phong cach, so slide
- Dieu huong: Phim mui ten, Space, cuon/vuot, nhan nav dots
- Tuy chinh: Bien CSS `:root` cho mau sac, link font cho kieu chu, class `.reveal` cho animations
- Neu co chinh sua truc tiep: Di chuot goc tren trai hoac nhan E de vao che do chinh sua, nhan vao text de sua, Ctrl+S de luu

**English summary:**
- File location, style name, slide count
- Navigation: Arrow keys, Space, scroll/swipe, click nav dots
- How to customize: `:root` CSS variables for colors, font link for typography, `.reveal` class for animations
- If inline editing was enabled: Hover top-left corner or press E to enter edit mode, click any text to edit, Ctrl+S to save

---

## Supporting Files

| File | Purpose | When to Read |
|------|---------|-------------|
| [STYLE_PRESETS.md](STYLE_PRESETS.md) | 12 curated visual presets with colors, fonts, and signature elements | Phase 2 (style selection) |
| [viewport-base.css](viewport-base.css) | Mandatory responsive CSS — copy into every presentation | Phase 3 (generation) |
| [html-template.md](html-template.md) | HTML structure, JS features, code quality standards | Phase 3 (generation) |
| [animation-patterns.md](animation-patterns.md) | CSS/JS animation snippets and effect-to-feeling guide | Phase 3 (generation) |
| [scripts/extract-pptx.py](scripts/extract-pptx.py) | Python script for PPT content extraction | Phase 4 (conversion) |
| [references/vietnamese-typography.md](references/vietnamese-typography.md) | Vietnamese-compatible fonts and typography rules | Phase 3 (Vietnamese content) |

---

## Attribution

Forked from [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) (MIT License).
Vietnamese optimization by [@huunghiaish](https://github.com/huunghiaish).
