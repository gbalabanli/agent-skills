---
name: goal-criteria-create
description: "Create structured acceptance criteria from a task, plan, feature spec, or codebase context, with assigned verification methods and a ready-to-paste /goal stop condition. Use when the user says 'create acceptance criteria', 'define criteria for this', 'write acceptance criteria', 'goal criteria', 'what does done look like', 'define done', 'set criteria', 'create a /goal condition', or asks to formalize what 'complete' means for any piece of work. Also use when the user wants to combine multiple verification types (tests, lint, manual checks, subagent delegation) into a single structured criteria document."
metadata:
  short-description: Create acceptance criteria with /goal integration
  category: productivity
  tags: [acceptance-criteria, goal, verification, planning]
---

# Goal Criteria Create

Generate structured acceptance criteria with verification methods and a `/goal` stop condition.

## When to Use

- Before starting multi-step work: define what "done" means
- After a plan exists: convert plan items into verifiable criteria
- When setting a `/goal`: produce a well-formed condition from structured criteria
- When onboarding to unfamiliar work: force-explicit the success conditions

## Workflow

### Step 1 — Gather Context

Read enough to understand the work. Sources, in priority order:

1. **Explicit input**: user-provided task description, plan file, spec, or feature document
2. **Project structure**: `README.md`, `AGENTS.md`, `docs/`, architecture files
3. **Existing plans**: `docs/compose/spec/*.md`, `docs/phases/*.md`, `docs/master_plan.md`
4. **Codebase signals**: test framework (`package.json`, `pyproject.toml`, `Makefile`), linter config, CI config, type checker config
5. **Git state**: recent commits, branch name, open PR description

If the user provided a specific file or task reference, read it. If they said "this project" or "current work", scan the workspace.

Do not ask the user for information the environment already answers. Ask at most 1-2 clarifying questions only if the scope is materially ambiguous.

### Step 2 — Identify Work Items

Extract discrete work items from the context. Each work item becomes one or more criteria.

Work item sources:
- Tasks in a plan or spec (e.g., `T1: Add auth middleware`)
- Requirements in a feature document (e.g., `[S2] Design` sections)
- User-stated goals (e.g., "make the API faster")
- Implicit requirements from the codebase (e.g., "project uses TypeScript, so type checking must pass")

Group work items into categories:

| Category | What it covers | Examples |
|----------|---------------|----------|
| **Functional** | Behavior the user explicitly requested | "Login returns JWT", "Search filters by date" |
| **Integration** | How components interact | "API returns correct status codes", "Frontend renders error states" |
| **Non-functional** | Quality attributes | "Response < 200ms", "No TypeScript errors" |
| **Edge cases** | Boundary and error conditions | "Empty input handled", "Concurrent writes don't corrupt" |
| **Regression** | Existing behavior preserved | "Existing tests still pass", "No new lint warnings" |

### Step 3 — Write Acceptance Criteria

For each work item, write one criterion using this format:

```
- [ ] C<N>: <observable outcome> — verify: <method> (priority: P<N>, covers: <source>)
```

Fields:
- **C<N>**: stable criterion ID (C1, C2, ...)
- **Observable outcome**: what a reviewer can check. Must be falsifiable. Avoid "should work" — write "endpoint returns 200 with valid JSON body".
- **verify**: the verification method (see Step 4)
- **priority**: P0 (blocks everything), P1 (must ship), P2 (should ship), P3 (nice to have)
- **covers**: traceability back to the source requirement or task ID

Rules:
- Every criterion must be independently verifiable
- No criterion should depend on subjective judgment alone ("looks good")
- Combine near-identical criteria; split compound criteria ("X and Y" → two criteria)
- At least one criterion per work item; at least one criterion per category that applies

### Step 4 — Assign Verification Methods

For each criterion, assign exactly one primary verification method. Read [verification-methods.md](references/verification-methods.md) for the full catalog.

Decision flow:

```
Is there a test command that directly validates this?
  → YES: use "test:<command>"
  → NO: Is there a static check (lint, typecheck, build)?
    → YES: use "check:<command>"
    → NO: Can a human observe the result in the UI/terminal?
      → YES: use "manual:<steps>"
      → NO: Can an explore/general subagent verify by reading code or running commands?
        → YES: use "subagent:<instructions>"
        → NO: use "manual:review <file> and confirm <condition>"
```

A single criterion may have a primary method and an optional secondary method. Example:
```
C3: Auth middleware rejects expired tokens — verify: test:npm test auth.test.js, manual:curl expired-token to /api/me returns 401 (priority: P0, covers: T1)
```

### Step 5 — Synthesize the `/goal` Condition

Distill all criteria into a single natural-language condition string suitable for `/goal <condition>`.

Synthesis rules:

1. **Start with the outcome**: "All acceptance criteria in acceptance-criteria.md are satisfied"
2. **Add verification evidence**: "and the following commands pass: <list of test/check commands>"
3. **Add manual/subagent gates if present**: "and <manual/subagent criteria> are confirmed"
4. **Keep it under 300 words**: the judge model evaluates this after each turn; overly long conditions reduce reliability
5. **Make it self-contained**: the condition must be evaluable without reading other files, but may reference the criteria file by name

Template:

```
All acceptance criteria in acceptance-criteria.md are checked off. Specifically:
- Tests pass: <commands>
- Static checks pass: <commands>
- <N> manual verification items confirmed: <brief summary of each>
- <N> subagent verification items confirmed: <brief summary of each>
No P0 or P1 criteria remain unchecked.
```

If there are no manual or subagent criteria, omit those lines. If all verification is code-based, the condition simplifies to:

```
All tests and checks in acceptance-criteria.md pass: <commands>. No P0 or P1 criteria remain unchecked.
```

### Step 6 — Write the Output File

Write `acceptance-criteria.md` to the project root (or user-specified path) using the template in [criteria-template.md](references/criteria-template.md).

After writing:

1. Display the `/goal` condition string to the user, formatted as a ready-to-paste command:
   ```
   /goal <condition>
   ```
2. Display a summary table: criterion ID, priority, verification method, status
3. Remind the user: "Paste the `/goal` command to activate judge-verified stop condition"

### Step 7 — Update When Work Changes

If the user adds, removes, or changes work items after criteria exist:

1. Re-read the current `acceptance-criteria.md`
2. Add/remove/update affected criteria, preserving stable IDs
3. Re-synthesize the `/goal` condition
4. Display the updated `/goal` command

Do not regenerate the entire file. Update only affected sections.

## Output Rules

- Write only `acceptance-criteria.md`. Do not create additional files unless the user asks.
- Use imperative form for criterion outcomes: "Endpoint returns...", not "The endpoint should return..."
- Every criterion must have a verification method — no unverifiable criteria
- Priority distribution guideline: 0-1 P0, 2-4 P1, rest P2/P3. If everything is P0, nothing is.
- Preserve existing human-authored criteria when updating; only modify what the change affects
- The `/goal` condition must be a single string, no newlines inside the condition text

## Reference Files

- [criteria-template.md](references/criteria-template.md) — template for the acceptance criteria document
- [verification-methods.md](references/verification-methods.md) — catalog of verification method types with examples
