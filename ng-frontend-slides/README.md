# ng:frontend-slides

Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Vietnamese-optimized fork with proper diacritics rendering and Vietnamese-friendly font selection.

Forked from [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) (10k+ stars).

## What's Different from Upstream

| Feature | Upstream | This Fork |
|---------|----------|-----------|
| Language detection | English only | Auto-detect Vietnamese/English |
| Vietnamese fonts | Not supported | Curated list of Vietnamese-compatible fonts per preset |
| UI text | English | Vietnamese when user writes in Vietnamese |
| Typography rules | Standard | Vietnamese diacritics-aware (line-height, clipping, density) |
| Font reference | N/A | `references/vietnamese-typography.md` with 20+ tested fonts |
| Content density | Standard | -15% for Vietnamese (diacritics need more space) |
| PPT extraction | ASCII-safe | `ensure_ascii=False` for Vietnamese text preservation |

## Key Features

- **Zero Dependencies** — Single HTML files with inline CSS/JS
- **12 Style Presets** — Each with Vietnamese font alternatives
- **PPT Conversion** — Extract and convert .pptx files, preserving Vietnamese text
- **Visual Style Discovery** — Generate 3 previews with Vietnamese sample text
- **Vietnamese Typography** — Proper diacritics rendering, line-height, word-breaking

## Usage

```bash
# In Claude Code
/ng:frontend-slides

> "Tao bai trinh bay pitch deck cho startup AI cua toi"
> "Convert presentation.pptx sang web"
> "Create a conference talk about microservices"
```

## File Structure

```
frontend-slides/
├── SKILL.md                              # Main skill entry point
├── STYLE_PRESETS.md                      # 12 visual presets with Vi font alternatives
├── viewport-base.css                     # Mandatory responsive CSS
├── html-template.md                      # HTML architecture and JS features
├── animation-patterns.md                 # CSS/JS animation reference
├── scripts/
│   └── extract-pptx.py                  # PPT content extraction
├── references/
│   └── vietnamese-typography.md          # Vietnamese font guide (20+ fonts)
├── LICENSE                               # MIT (original + fork)
└── README.md                            # This file
```

## Requirements

- [Claude Code](https://claude.ai/code) CLI
- For PPT conversion: Python with `python-pptx` (`pip install python-pptx`)

## License

MIT — see [LICENSE](LICENSE).
