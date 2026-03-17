# AI-Generated File Detection Heuristics

## Classification Signals

### Strong Human-Written Signals
- File extensions: `.docx`, `.xlsx`, `.xls`, `.pptx`, `.pdf` (office docs)
- File names: `requirement*`, `spec*`, `PRD*`, `SRS*`, `proposal*`, `QA_*`, `hosochao*`, `brief*`
- Content patterns: informal language, inconsistent formatting, bullet lists without headers
- Vietnamese/native language content in business docs
- Scanned documents, handwritten notes

### Strong AI-Generated Signals
- Perfectly structured markdown with consistent header hierarchy
- Files named: `code-standards.md`, `system-architecture.md`, `codebase-summary.md`, `design-guidelines.md`, `deployment-guide.md`, `project-roadmap.md`, `development-roadmap.md`
- Contains patterns: "## Overview", "## Architecture", "### Key Features", "## Tech Stack"
- Source code files in `src/`, `app/`, `frontend/`, `backend/`, `api/`
- Config files: `docker-compose.yml`, `package.json`, `tsconfig.json` (likely scaffolded)
- Git history check: files created in bulk commits with AI-style commit messages

### Ambiguous (need user confirmation)
- README.md (could be either)
- `.env.example` (template vs hand-crafted)
- Database migration files (hand-written SQL vs auto-generated)
- Test files (could be TDD human-written or AI-generated)

## Git History Heuristics

Check git log for patterns:
```bash
git log --oneline --diff-filter=A -- <file>  # when file was first added
git log --format="%H %s" --diff-filter=A      # bulk-add commits
```

AI-generated indicators in commits:
- Large number of files added in single commit
- Commit messages like "feat: implement X", "add Y component", "scaffold Z"
- Multiple unrelated features in one commit

## Confidence Scoring

- **HIGH confidence AI**: structured md + standard naming + bulk commit = 90%+
- **HIGH confidence Human**: office format + requirement naming = 90%+
- **MEDIUM**: needs user confirmation = 50-89%
- Present MEDIUM confidence files for explicit user review
