# ng:seo — SEO Audit Toolkit

> **Forked from:** [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) (MIT License)

Comprehensive SEO auditing toolkit for Claude Code.

## Skills

| Skill | Purpose |
|-------|---------|
| `ng:seo` | Main orchestrator / router |
| `ng:seo-audit` | Full site audit (crawl up to 500 pages) |
| `ng:seo-page` | Single page deep analysis |
| `ng:seo-content` | E-E-A-T & content quality |
| `ng:seo-technical` | Technical SEO (9 categories) |
| `ng:seo-images` | Image optimization |
| `ng:seo-human-content` | Pre-upload content audit |

## Install

```bash
git clone https://github.com/huunghiaish/ng-skills.git /tmp/ng-skills
cp -r /tmp/ng-skills/seo*/ ~/.claude/skills/
rm -rf /tmp/ng-skills
```

## Usage

```bash
/ng:seo audit https://example.com
/ng:seo page https://example.com/blog/post
/ng:seo content https://example.com/about
/ng:seo technical https://example.com
/ng:seo images https://example.com
/ng:seo human-content ./content/blog-post.md
```
