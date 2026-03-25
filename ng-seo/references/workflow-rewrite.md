# SEO Content Rewrite
# Optimized for: Travel · Restaurant · Booking (Local Business / Vietnam)

Rewrite content to maximize SEO scores across all 8 audit dimensions.

## Step 1 — Gather Input

Parse arguments: `rewrite <content-file> [audit-report]`

If missing, use `AskUserQuestion`:

| Question | Options |
|----------|---------|
| Content file | .docx, .md, .txt, .html |
| Audit report | Optional: path to seo audit report |
| Content subtype | See subtype table below |
| Primary keyword | Free text |
| Language | Vietnamese (default) / English |
| Author info | Name, title, credentials (for E-E-A-T) |

### Content Subtype Reference

| Subtype | Code | Min Words | ToC |
|---------|------|-----------|-----|
| Recipe / Công thức | `recipe` | 800 | ✗ |
| Travel guide | `travel-guide` | 1,000 | ✓ if >1,200 |
| Destination review | `destination-review` | 600 | ✗ |
| Restaurant review | `restaurant-review` | 500 | ✗ |
| Activity / Trải nghiệm | `activity` | 600 | ✗ |
| Landing page | `landing` | 600 | ✗ |
| Service page | `service` | 800 | ✗ |
| Booking / Event | `booking` | 400 | ✗ |
| News / Tin tức | `news` | 400 | ✗ |

## Step 2 — Read Content

**For .docx:** Extract text:
```bash
~/.claude/skills/.venv/bin/python3 -c "
from docx import Document
doc = Document('FILE_PATH')
for p in doc.paragraphs:
    style = p.style.name if p.style else 'Normal'
    print(f'[{style}] {p.text}')
"
```

**For .md/.txt/.html:** Read directly. **Audit report:** Parse 8-dimension scores.

## Step 3 — Analyze Gaps

Score each dimension 0-100. Load `references/workflow-rewrite-strategies.md`.

Priority (fix worst first):
1. **Heading Hierarchy** (15%) — structural foundation
2. **Readability** (15%) — word count vs subtype target, flow
3. **E-E-A-T Signals** (15%) — author, dates (lower weight for non-YMYL)
4. **Keyword Analysis** (20%) — placement, density, semantic + local keywords
5. **Local SEO** (10%) — NAP, city keyword, maps link, hours/booking
6. **Content Structure** (10%) — ToC (subtype-dependent), links, CTA
7. **Image SEO** (10%) — alt text
8. **Schema** (10%) — JSON-LD, OG, Twitter

## Step 4 — Rewrite Content

Apply strategies from `references/workflow-rewrite-strategies.md` for dimensions < 70.

**Rules:**
- Preserve original voice and tone
- Expand, don't replace — add sections, don't delete existing
- Keyword density 1-3% (natural, not stuffed)
- All additions must be relevant and valuable
- Match content language (Vietnamese/English)
- Output as clean Markdown

## Step 5 — Generate SEO Metadata

1. **Title tag** (50-60 chars, keyword near start)
2. **Meta description** (150-160 chars, with CTA)
3. **JSON-LD schema** (auto-detect from subtype — see `references/schema-templates.md`)
4. **OG tags** + **Twitter Card** tags
5. **Image alt text** suggestions
6. **Local SEO block** (NAP, if service/landing/restaurant subtype)

Use `references/workflow-rewrite-output.md` for templates.

## Step 6 — Extract Images (if .docx)

For .docx input, extract embedded images:
```bash
~/.claude/skills/.venv/bin/python3 -c "
from docx import Document
import os
doc = Document('FILE_PATH')
out_dir = 'OUTPUT_DIR/{slug}-images'
os.makedirs(out_dir, exist_ok=True)
count = 0
for rel in doc.part.rels.values():
    if 'image' in rel.reltype:
        count += 1
        img = rel.target_part
        ext = os.path.splitext(img.partname)[1]
        with open(os.path.join(out_dir, f'hinh-{count}{ext}'), 'wb') as f:
            f.write(img.blob)
"
```

View each image to map correctly to content captions. Update markdown image paths to relative `{slug}-images/hinh-X.png`.

## Step 7 — Export to .docx

Export rewritten markdown to Word document with embedded images:
```bash
~/.claude/skills/.venv/bin/python3 -c "
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import re, os
# Read markdown, strip frontmatter, parse headings/lists/images/paragraphs
# Add images with Inches(5.5) width, italic gray captions
# Handle **bold**, bullet lists, numbered lists
# Save as {filename}-seo-optimized.docx
"
```

## Step 8 — Report & Output

Generate 4 output files:

| File | Content |
|------|---------|
| `{slug}-seo-optimized.md` | Rewritten content with images |
| `{slug}-seo-optimized.docx` | Word export with embedded images |
| `{slug}-seo-metadata.md` | Title, meta, JSON-LD, OG, Twitter, alt text, local SEO block |
| `seo-rewrite-{date}-{slug}.md` | Before/after score report |

### Report template (seo-rewrite-{date}-{slug}.md)

```markdown
# SEO Rewrite Report — {Title}

**Source:** {original filename}
**Subtype:** {content subtype code}
**Author:** {author}
**Date:** {date}

## SEO Score: XX/100 [Grade X] → XX/100 [Grade X]

Dimension    Before  After  Change
─────────────────────────────────────
Heading:     XX  →  XX    (+XX)
Readability: XX  →  XX    (+XX)
Images:      XX  →  XX    (+XX)
Keywords:    XX  →  XX    (+XX)
E-E-A-T:     XX  →  XX    (+XX)
Local SEO:   XX  →  XX    (+XX)
Schema:      XX  →  XX    (+XX)
Structure:   XX  →  XX    (+XX)
─────────────────────────────────────
Weighted:    XX  →  XX    (+XX)

Word count: XXX → XXX (+XXX)
Target: X,XXX (subtype: {code})
Status: ✅ Met / ❌ XXX short

## Changes Applied
- [Dimension] Description of change

## Output Files
| File | Description |
...

## Remaining Manual Actions
| Action | Priority |
...
```

Grade: A (90-100) | B (70-89) | C (50-69) | D (30-49) | F (0-29)

Never fabricate author credentials — ask user for real info.