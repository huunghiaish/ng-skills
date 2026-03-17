# Codebase Exploration Guide

## If repomix context file exists

Look for: `repomix-output.xml`, `context.xml`, `repomix-output.md`

If found → read it. Contains entire codebase packed together.
No need to browse individual files.

## If no repomix file

Use these commands to explore:

```bash
# Overview structure
find . -type f -name "*.md" | head -50
find . -type d | grep -v node_modules | grep -v .git | head -30

# Find docs
find . -type f \( -name "*.md" -o -name "*.txt" \) \
  | grep -iE "prd|srs|spec|requirement|readme" | head -20

# Find entry points
find . -name "package.json" -not -path "*/node_modules/*" | head -5
find . -name "*.py" -name "main*" | head -5
```

## Reading order

1. README.md — product overview
2. Requirements/PRD — WHAT to build
3. SRS/Spec — HOW to build
4. Source code — WHAT was actually built

## When docs are missing

If no PRD/SRS, reconstruct from code:
- Route/endpoint names → feature list
- Database schema/models → data model
- UI components → user flows

Mark "(inferred from code)" when using this approach.
