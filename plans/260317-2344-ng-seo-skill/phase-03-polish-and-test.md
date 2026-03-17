# Phase 3: Polish & Test

**Priority:** Medium | **Status:** pending | **Effort:** Low
**Depends on:** Phase 1, Phase 2

## Overview

Validate all skills, test on real projects, calibrate scoring, push to repo.

## Steps

### 3.1 Validate all skills
- Run `package_skill.py` on each skill directory
- Verify: frontmatter valid, description <200 chars, SKILL.md <150 lines
- Fix any validation failures

### 3.2 Test on real project
- Test `ng:seo-audit` on a live website
- Test `ng:seo-page` on a single URL
- Test `ng:seo-human-content` on local markdown/HTML files
- Verify reports are actionable and scores reasonable

### 3.3 Install to global skills
- Copy all seo-* dirs to `~/.claude/skills/`
- Verify skills appear in catalog
- Test slash commands work

### 3.4 Update ng-skills README
- Add all ng:seo-* skills to table
- Attribution to claude-seo
- Usage examples for each command

### 3.5 Commit & push
- Commit with conventional format
- Push to origin/main

## Todo
- [ ] 3.1 Validate all skills with package_skill.py
- [ ] 3.2 Test on real projects (live site + local content)
- [ ] 3.3 Install to ~/.claude/skills/
- [ ] 3.4 Update README.md
- [ ] 3.5 Commit & push

## Success Criteria
- All skills pass validation
- Reports generated successfully on real content
- Skills visible in Claude Code catalog
- README updated with full command reference
