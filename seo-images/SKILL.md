---
name: ng:seo-images
description: "Image optimization for SEO and performance: alt text, file sizes, formats, responsive images, lazy loading, CLS prevention. Use for 'image optimization', 'alt text', 'image SEO', 'image audit'."
---

# Image Optimization Analysis

## Checks

### Alt Text
- Present on all `<img>` (except decorative: `role="presentation"`)
- Descriptive (not "image.jpg"), 10-125 chars
- Keywords included naturally, not stuffed

### File Size
| Category | Target | Warning | Critical |
|----------|--------|---------|----------|
| Thumbnails | <50KB | >100KB | >200KB |
| Content images | <100KB | >200KB | >500KB |
| Hero/banner | <200KB | >300KB | >700KB |

### Format
| Format | Support | Use Case |
|--------|---------|----------|
| WebP | 97%+ | Default recommendation |
| AVIF | 92%+ | Best compression |
| JPEG | 100% | Fallback for photos |
| PNG | 100% | Graphics with transparency |
| SVG | 100% | Icons, logos |

Recommend `<picture>` with format fallbacks:
```html
<picture>
  <source srcset="img.avif" type="image/avif">
  <source srcset="img.webp" type="image/webp">
  <img src="img.jpg" alt="Description" width="800" height="600" loading="lazy">
</picture>
```

### Responsive Images
- `srcset` for multiple sizes, `sizes` matching breakpoints
- Appropriate resolution for device pixel ratios

### Lazy Loading
- `loading="lazy"` on below-fold images
- Do NOT lazy-load above-fold/hero images (hurts LCP)
- Add `fetchpriority="high"` to LCP/hero image
- Add `decoding="async"` to non-LCP images

### CLS Prevention
- `width` and `height` attributes on all `<img>`
- Or `aspect-ratio` CSS as alternative
- Flag images without dimensions

### File Names
- Descriptive: `blue-running-shoes.webp` not `IMG_1234.jpg`
- Hyphenated, lowercase

### CDN Usage
- Check if images served from CDN
- Recommend CDN for image-heavy sites

## Output

### Image Audit Summary
| Metric | Status | Count |
|--------|--------|-------|
| Total Images | - | XX |
| Missing Alt Text | ❌ | XX |
| Oversized | ⚠️ | XX |
| Wrong Format | ⚠️ | XX |
| No Dimensions | ⚠️ | XX |
| Not Lazy Loaded | ⚠️ | XX |

### Prioritized Optimization List
Sorted by file size impact (largest savings first):
| Image | Size | Format | Issues | Est. Savings |
|-------|------|--------|--------|--------------|

### Recommendations
1. Convert X images to WebP (est. XX KB savings)
2. Add alt text to X images
3. Add dimensions to X images
4. Enable lazy loading on X below-fold images
