# Prompt Analysis Methodology

## Phase 1 — Requirement Mapping

For each original requirement document:
1. Extract discrete requirements/features (numbered list)
2. Map each requirement → which AI-generated files implement it
3. Identify unmapped requirements (gaps) and unmapped code (extras)

## Phase 2 — Artifact Dependency Graph

Build dependency order by analyzing:
- **Import/require chains**: which files import from which
- **Database models → API → Frontend**: natural build order
- **Config/env → infrastructure → application**: setup order
- **Package.json/requirements.txt**: project scaffold came first

Common vibe-coding order:
1. Project scaffold (create-next-app, vite, etc.)
2. Database schema/models
3. Backend API endpoints
4. Frontend components
5. Integration/wiring
6. Styling/polish
7. Documentation generation

## Phase 3 — Prompt Reconstruction

For each logical group of AI-generated artifacts:

### Determine Prompt Type
| Type | Indicators | Example |
|------|-----------|---------|
| **Scaffold** | Project init files, configs, boilerplate | "Create a Next.js app with TypeScript, Tailwind, Prisma" |
| **Feature** | New component/endpoint/model cluster | "Add user authentication with JWT and bcrypt" |
| **Fix** | Small targeted changes, error handling | "Fix the login form validation to handle empty fields" |
| **Refactor** | Restructured existing code, renamed files | "Refactor API routes to use middleware pattern" |
| **Docs** | Generated documentation files | "Generate system architecture documentation" |
| **Integration** | Wiring between existing components | "Connect frontend auth form to backend /api/auth endpoint" |

### Reconstruct Prompt Content
Analyze the output artifact to infer the input prompt:
- What tech stack was specified? (from package.json, configs)
- What feature was requested? (from component/endpoint names)
- What constraints were given? (from error handling patterns, validation rules)
- What style was requested? (from UI patterns, naming conventions)

### Assess Context Requirements
For each prompt, determine what context the AI likely needed:
- Previous files that must exist before this prompt works
- Documentation or specs that were likely pasted as context
- Error messages that may have triggered fix prompts

## Phase 4 — Sequence Validation

Verify the reconstructed sequence makes sense:
- Can each prompt execute given only the outputs of prior prompts?
- Are there circular dependencies? (indicates parallel prompts)
- Are there gaps? (manual human edits between AI prompts)

Mark any prompt with "(inferred — may have been manual edit)" if uncertain.
