# Schema.org Types & Templates
## Schema.org v29.4 (Dec 2025) — JSON-LD preferred

Content with proper schema has ~2.5x higher chance of AI citation (Google/Microsoft, March 2025).

## Active — Recommend freely
| Type | Use Case |
|------|----------|
| Organization | Company info (name, url, logo, contactPoint) |
| LocalBusiness | Physical businesses (address, phone, hours, geo) |
| Product | Physical/digital products (name, sku, brand, offers) |
| ProductGroup | Variant products (variesBy, hasVariant) |
| Service | Service businesses (provider, areaServed, offers) |
| Article | Blog posts, news (headline, author, dates, image) |
| BlogPosting | Blog content (same as Article + blog context) |
| Person | Author/team (name, jobTitle, sameAs, worksFor) |
| ProfilePage | Author profiles (mainEntity Person — E-E-A-T) |
| VideoObject | Video content (thumbnail, duration, contentUrl) |
| BreadcrumbList | Navigation (itemListElement with position) |
| WebSite | Site-level (name, url, SearchAction for sitelinks) |
| Event | Events (startDate, location, organizer, offers) |
| Review / AggregateRating | Ratings (ratingValue, reviewCount) |

## Restricted
| Type | Restriction |
|------|------------|
| FAQPage | Gov/health authority sites ONLY (since Aug 2023). Still benefits AI citation on other sites. |

## Deprecated — NEVER recommend
HowTo (Sept 2023), SpecialAnnouncement (July 2025), ClaimReview (June 2025),
VehicleListing (June 2025), Dataset (late 2025), Practice Problem (late 2025).

## Recent Additions (2024-2026)
- Product Certification (April 2025) — energy ratings, safety certs
- LoyaltyProgram (June 2025) — member pricing
- ConferenceEvent, PerformingArtsEvent (Dec 2025)

---

## JSON-LD Templates

### Article / BlogPosting
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Title",
  "author": {"@type": "Person", "name": "Author", "url": "https://..."},
  "publisher": {"@type": "Organization", "name": "Org", "logo": {"@type": "ImageObject", "url": "https://..."}},
  "datePublished": "2026-01-01",
  "dateModified": "2026-01-15",
  "image": "https://...",
  "description": "Summary"
}
```

### Product
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "image": "https://...",
  "description": "Description",
  "brand": {"@type": "Brand", "name": "Brand"},
  "offers": {"@type": "Offer", "price": "99.99", "priceCurrency": "USD", "availability": "https://schema.org/InStock"}
}
```

### LocalBusiness
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "address": {"@type": "PostalAddress", "streetAddress": "123 St", "addressLocality": "City", "addressRegion": "State", "postalCode": "12345"},
  "telephone": "+1-xxx-xxx-xxxx",
  "openingHours": "Mo-Fr 09:00-17:00"
}
```

### Organization
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Org Name",
  "url": "https://...",
  "logo": "https://...",
  "contactPoint": {"@type": "ContactPoint", "telephone": "+1-xxx", "contactType": "customer service"}
}
```

## Validation Checklist
1. `@context` is `"https://schema.org"` (not http)
2. `@type` is valid, non-deprecated
3. All required properties present
4. URLs absolute, dates ISO 8601, no placeholder text
