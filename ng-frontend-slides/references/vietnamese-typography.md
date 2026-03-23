# Vietnamese Typography Guide

Comprehensive guide for selecting and configuring fonts that properly render Vietnamese diacritics (dau) in HTML presentations.

## Vietnamese Diacritics Overview

Vietnamese uses Latin script with 12 additional characters and 5 tone marks:

**Extra characters:** a/a, a/a, d/d, e/e, o/o, o/o, u/u
**Tone marks:** sac ('), huyen (`), hoi (?), nga (~), nang (.)

These combine, e.g., "o" can appear as: o, o, o, o, o, o, o — requiring full Unicode support in the font.

**Test string** (use to verify font rendering):
```
Xin chao the gioi — Viet Nam xinh dep — Doi moi sang tao
Toi yeu Viet Nam — Ho Chi Minh — Da Nang — Hue — Ha Noi
ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz
```

---

## Tier 1: Vietnamese-First Fonts (Best Support)

These fonts were designed with Vietnamese as a primary target.

### Be Vietnam Pro
- **Type:** Sans-serif
- **Weights:** 100-900 + italics
- **Best for:** Universal — headings, body, UI
- **Source:** Google Fonts (Vietnamese subset built-in)
- **Why:** Designed specifically for Vietnamese by Vietnamese designers. Perfect diacritics spacing.
```html
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400&display=swap" rel="stylesheet">
```

### Montserrat
- **Type:** Sans-serif (geometric)
- **Weights:** 100-900 + italics
- **Best for:** Headings, display text
- **Source:** Google Fonts
- **Why:** Very popular, excellent Vietnamese support, geometric feel
```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400&display=swap" rel="stylesheet">
```

---

## Tier 2: Google Fonts with Vietnamese Subset

These fonts have explicit Vietnamese subset support on Google Fonts.

### Display / Heading Fonts

| Font | Style | Weights | Vibe | Google Fonts URL param |
|------|-------|---------|------|----------------------|
| **Lexend** | Sans-serif, modern | 100-900 | Clean, readable | `&subset=vietnamese` |
| **Plus Jakarta Sans** | Sans-serif, friendly | 200-800 | Modern, approachable | Built-in |
| **Outfit** | Sans-serif, geometric | 100-900 | Playful, modern | Built-in |
| **Nunito** | Sans-serif, rounded | 200-900 | Friendly, warm | Built-in |
| **Manrope** | Sans-serif | 200-800 | Professional | Built-in |
| **Playfair Display** | Serif, elegant | 400-900 | Premium, editorial | Built-in |
| **Lora** | Serif, contemporary | 400-700 | Literary, warm | Built-in |

### Body / Text Fonts

| Font | Style | Weights | Vibe | Notes |
|------|-------|---------|------|-------|
| **Be Vietnam Pro** | Sans-serif | 100-900 | Universal | Best Vietnamese body font |
| **Nunito** | Sans-serif, rounded | 200-900 | Friendly | Great readability |
| **Merriweather** | Serif | 300-900 | Elegant body | Long text reading |
| **Archivo** | Sans-serif | 100-900 | Technical | Good for data-heavy slides |
| **Source Sans 3** | Sans-serif | 200-900 | Neutral | Professional body text |

### Monospace Fonts

| Font | Weights | Vietnamese | Notes |
|------|---------|-----------|-------|
| **JetBrains Mono** | 100-800 | Full support | Best mono for Vietnamese |
| **Fira Code** | 300-700 | Good | Ligatures + Vietnamese |
| **Source Code Pro** | 200-900 | Good | Adobe, clean |

---

## Tier 3: Fonts That Need Testing

These fonts claim Vietnamese support but may have rendering issues with certain diacritic combinations.

| Font | Status | Issue |
|------|--------|-------|
| Space Grotesk | Partial | Some weight/diacritics combos misaligned |
| DM Sans | Mostly OK | Light weights may clip diacritics |
| Work Sans | Mostly OK | Heavy weights need line-height adjustment |
| Fraunces | Limited | Variable font, some diacritics missing in extreme weights |

---

## Fonts to AVOID for Vietnamese

These fonts have broken or missing Vietnamese diacritics:

| Font | Problem |
|------|---------|
| Archivo Black | Missing many combined diacritics |
| Bodoni Moda | Incomplete Vietnamese charset |
| Syne | No Vietnamese support |
| Cormorant | Partial — missing several diacritics |
| Cormorant Garamond | Same as Cormorant |
| Clash Display (Fontshare) | No Vietnamese subset |
| Satoshi (Fontshare) | No Vietnamese subset |

**Rule:** If a font is on this avoid list and the content is Vietnamese, use the "Vi Font" alternative from STYLE_PRESETS.md.

---

## CSS Configuration for Vietnamese

### Essential Rules

```css
/* 1. Line height — Vietnamese diacritics need breathing room */
body {
    line-height: 1.6;        /* Body text minimum */
}
h1, h2, h3, h4, h5, h6 {
    line-height: 1.3;        /* Headings */
    padding-top: 0.1em;      /* Prevent top diacritics clipping */
}

/* 2. Word breaking — Vietnamese uses spaces between syllables */
body {
    word-break: keep-all;
    overflow-wrap: break-word;
    hyphens: none;            /* Vietnamese does not hyphenate */
}

/* 3. Font loading — prevent FOIT */
@font-face {
    font-display: swap;       /* Show fallback immediately */
}

/* 4. Letter spacing — avoid tight tracking with diacritics */
h1, .display-text {
    letter-spacing: -0.01em; /* Max tightening for Vietnamese */
    /* Never go below -0.02em — diacritics will overlap */
}

/* 5. Text rendering */
body {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
}
```

### Google Fonts with Vietnamese Subset

Always include `&subset=vietnamese` or verify the font has built-in Vietnamese support:

```html
<!-- Explicit Vietnamese subset -->
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700;800&subset=vietnamese&display=swap" rel="stylesheet">

<!-- Fonts with built-in Vietnamese (no subset param needed) -->
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

---

## Font Pairing Recommendations for Vietnamese

### Modern & Clean
- Display: `Lexend` (700) + Body: `Be Vietnam Pro` (400)
- Display: `Montserrat` (700) + Body: `Nunito` (400)

### Editorial & Elegant
- Display: `Playfair Display` (700) + Body: `Be Vietnam Pro` (400)
- Display: `Lora` (700) + Body: `Merriweather` (400)

### Tech & Minimal
- Display: `Archivo` (800) + Body: `Source Sans 3` (400)
- Display: `Manrope` (700) + Body: `Manrope` (400)

### Friendly & Approachable
- Display: `Plus Jakarta Sans` (700) + Body: `Plus Jakarta Sans` (400)
- Display: `Outfit` (700) + Body: `Nunito` (400)

### Developer / Code-Heavy
- Display: `JetBrains Mono` (700) + Body: `Be Vietnam Pro` (400)
- All mono: `JetBrains Mono` (400/700)

---

## Quick Decision Tree

```
Is content Vietnamese?
├── No  → Use any font from STYLE_PRESETS.md
└── Yes → Is the preset font in the "AVOID" list?
    ├── No  → Use the preset font (add &subset=vietnamese if Google Fonts)
    └── Yes → Use the "Vi Font" alternative from STYLE_PRESETS.md
              Default fallback: Be Vietnam Pro (safe for any context)
```
