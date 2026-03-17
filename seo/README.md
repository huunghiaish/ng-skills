# ng:seo — SEO Audit Toolkit

> **Forked from:** [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) (MIT License)

Single skill with 6 subcommands for comprehensive SEO auditing.

## Commands

| Command | Purpose |
|---------|---------|
| `ng:seo audit <url>` | Full site audit (crawl up to 500 pages) |
| `ng:seo page <url>` | Single page deep analysis |
| `ng:seo content <url>` | E-E-A-T & content quality |
| `ng:seo technical <url>` | Technical SEO (9 categories) |
| `ng:seo images <url>` | Image optimization |
| `ng:seo human-content <path\|url>` | Pre-upload content audit |

## Install

```bash
git clone https://github.com/huunghiaish/ng-skills.git /tmp/ng-skills
cp -r /tmp/ng-skills/seo/ ~/.claude/skills/
rm -rf /tmp/ng-skills
```

## Usage

```bash
/ng:seo audit https://example.com
/ng:seo page https://example.com/blog/post
/ng:seo human-content ./content/blog-post.md
```
