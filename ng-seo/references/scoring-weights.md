# Scoring Weights & Core Web Vitals Thresholds

## Full Site Audit Weights
| Category | Weight |
|----------|--------|
| Technical SEO | 25% |
| Content Quality | 25% |
| On-Page SEO | 20% |
| Schema / Structured Data | 10% |
| Performance (CWV) | 10% |
| Images | 10% |

## Single Page Weights
| Category | Weight |
|----------|--------|
| On-Page SEO | 25% |
| Content Quality | 25% |
| Technical | 20% |
| Schema | 15% |
| Images | 15% |

## Human Content Audit Weights
| Category | Weight |
|----------|--------|
| Keyword analysis | 20% |
| E-E-A-T signals | 20% |
| Heading hierarchy | 15% |
| Readability | 15% |
| Schema/meta | 10% |
| Image SEO | 10% |
| Content structure | 10% |

---

## Core Web Vitals (Feb 2026)

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤2.5s | 2.5s–4.0s | >4.0s |
| INP (Interaction to Next Paint) | ≤200ms | 200ms–500ms | >500ms |
| CLS (Cumulative Layout Shift) | ≤0.1 | 0.1–0.25 | >0.25 |

- INP replaced FID on March 12, 2024. FID fully removed Sept 9, 2024.
- Evaluation: 75th percentile of real user data (CrUX)
- CWV is a tiebreaker signal — matters when content quality is similar
- Dec 2025 update weights mobile CWV more heavily
- Pass rates: 57.1% desktop, 49.7% mobile

### LCP Subparts
| Subpart | Target |
|---------|--------|
| TTFB | <800ms |
| Resource Load Delay | Minimize |
| Resource Load Time | Depends on size |
| Element Render Delay | Minimize |

### Common Bottlenecks
**LCP:** Unoptimized hero images, render-blocking CSS/JS, slow TTFB, third-party scripts, font loading
**INP:** Long JS tasks (>50ms), heavy event handlers, DOM >1500 elements, sync XHR, layout thrashing
**CLS:** Missing image dimensions, dynamic content injection, font shifts, ads without reserved space

### Priority
1. **LCP** — most impactful for perceived performance
2. **CLS** — most common issue
3. **INP** — matters most for interactive apps

---

## Priority Definitions
- **Critical**: Blocks indexing or causes penalties (fix immediately)
- **High**: Significantly impacts rankings (fix within 1 week)
- **Medium**: Optimization opportunity (fix within 1 month)
- **Low**: Nice to have (backlog)

## Score Grades
| Grade | Score | Meaning |
|-------|-------|---------|
| A | 90-100 | Excellent SEO health |
| B | 70-89 | Good, minor improvements needed |
| C | 50-69 | Moderate, significant opportunities |
| D | 30-49 | Poor, major issues |
| F | 0-29 | Critical, urgent fixes needed |
