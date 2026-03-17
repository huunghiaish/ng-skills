# Image Optimization Audit

## Checks

### Alt Text
- Present on all `<img>` (except decorative), descriptive 10-125 chars, keywords natural

### File Size
| Category | Target | Warning | Critical |
|----------|--------|---------|----------|
| Thumbnails | <50KB | >100KB | >200KB |
| Content | <100KB | >200KB | >500KB |
| Hero/banner | <200KB | >300KB | >700KB |

### Format
WebP (97%+) default, AVIF (92%+) best compression, JPEG/PNG fallback, SVG for icons.
Recommend `<picture>` with format fallbacks.

### Responsive
- `srcset` + `sizes` for multiple resolutions

### Loading
- `loading="lazy"` on below-fold
- `fetchpriority="high"` on LCP/hero image
- `decoding="async"` on non-LCP images
- Do NOT lazy-load above-fold images

### CLS Prevention
- `width`/`height` attributes or `aspect-ratio` CSS on all images

### File Names
- Descriptive, hyphenated, lowercase (not IMG_1234.jpg)

## Output
| Metric | Status | Count |
|--------|--------|-------|
| Total Images | - | XX |
| Missing Alt | ❌ | XX |
| Oversized | ⚠️ | XX |
| Wrong Format | ⚠️ | XX |
| No Dimensions | ⚠️ | XX |

Prioritized list sorted by file size savings.
Recommendations: convert to WebP, add alt text, add dimensions, enable lazy loading.
