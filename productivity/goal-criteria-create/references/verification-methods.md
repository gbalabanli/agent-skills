# Verification Methods Catalog

Each acceptance criterion must have exactly one primary verification method and may have one optional secondary method.

## Method Types

### 1. `test:<command>` — Automated Tests

Run a test command and confirm exit code 0 with expected pass count.

**When to use**: The criterion validates behavior that has or can have an automated test.

**Examples**:
- `test:npm test -- --grep "auth"` — run auth-related tests
- `test:pytest tests/test_api.py::test_login` — run specific test
- `test:go test ./internal/auth/...` — run package tests
- `test:cargo test auth_middleware` — run Rust tests

**Evidence**: Command output showing all tests pass, exit code 0.

**Anti-patterns**:
- `test:npm test` (too broad — may pass while the specific criterion fails)
- `test:echo "looks good"` (not a real test)

### 2. `check:<command>` — Static Analysis / Build

Run a static check, linter, type checker, or build command and confirm exit code 0.

**When to use**: The criterion validates code quality, type safety, or compilability.

**Examples**:
- `check:npx tsc --noEmit` — TypeScript type checking
- `check:ruff check .` — Python linting
- `check:go vet ./...` — Go static analysis
- `check:npm run build` — build succeeds
- `check:eslint src/ --max-warnings 0` — no lint warnings
- `check:mypy src/` — Python type checking

**Evidence**: Command output showing 0 errors, exit code 0.

**Anti-patterns**:
- `check:ls` (not a real check)
- Mixing test commands into check (tests are `test:`, not `check:`)

### 3. `manual:<steps>` — Human-Observable Verification

Describe steps a human (or the agent itself) can perform to visually or interactively confirm the criterion.

**When to use**: The criterion validates UI behavior, user experience, visual output, or anything not easily automated.

**Format**: `<action> → <expected observation>`

**Examples**:
- `manual:navigate to /login, enter valid credentials → redirects to /dashboard with welcome message`
- `manual:run 'npm start', open http://localhost:3000 → page loads without console errors`
- `manual:submit form with empty email → inline error "Email is required" appears below field`
- `manual:check terminal output after 'make deploy' → shows "Deployed to staging" with no warnings`
- `manual:review src/auth.ts and confirm all error paths return structured JSON`

**Evidence**: Agent or human confirms the observation matches the expected result.

**Anti-patterns**:
- `manual:check if it works` (too vague — what action? what observation?)
- `manual:review the code` (not specific — what to look for?)

### 4. `subagent:<instructions>` — Subagent Delegation

Spawn an explore or general subagent with specific instructions to verify the criterion.

**When to use**: The criterion requires reading multiple files, tracing code paths, or running exploratory commands that are too complex for a single manual step but don't have a dedicated test.

**Format**: `<agent_type>: "<task>"`

**Examples**:
- `subagent:explore: "Read src/auth/ and confirm all middleware functions handle the error case where req.user is undefined. Report which files and line numbers handle this."`
- `subagent:general: "Run 'grep -r TODO src/ | grep -v test' and confirm no TODO comments remain in production code. Report any found."`
- `subagent:explore: "Trace the request flow from routes/api.ts through to the database layer. Confirm every path includes input validation."`
- `subagent:general: "Check that all new functions added in this change have JSDoc comments with @param and @returns tags."`

**Evidence**: Subagent report confirming the condition, with file/line references.

**Anti-patterns**:
- `subagent:check if the code is good` (too vague)
- `subagent:explore: "verify everything"` (not specific enough to verify)

## Method Selection Decision Tree

```
Criterion validates behavior that can be tested automatically?
├─ YES → Is there an existing test?
│  ├─ YES → test:<existing test command>
│  └─ NO → Can a test be written cheaply?
│     ├─ YES → test:<test command> (write the test first)
│     └─ NO → subagent:<trace the code path and confirm behavior>
├─ NO → Is it a code quality / type safety / build criterion?
│  ├─ YES → check:<linter/typecheck/build command>
│  └─ NO → Is it observable in the UI or terminal output?
│     ├─ YES → manual:<action → expected observation>
│     └─ NO → subagent:<specific exploration instructions>
```

## Combining Methods

A criterion may have a primary and secondary method separated by comma:

```
C3: Login returns JWT on valid credentials — verify: test:npm test auth.test.js, manual:curl -X POST /api/login with valid creds returns 200 with token (priority: P0, covers: T1)
```

The primary method is the authoritative check. The secondary method provides additional confidence.

## Method-to-Evidence Mapping

| Method | Evidence type | Where it appears in output |
|--------|--------------|---------------------------|
| `test:` | Command output + exit code | Verification Commands section |
| `check:` | Command output + exit code | Verification Commands section |
| `manual:` | Step-by-step observation | Manual Verification Steps section |
| `subagent:` | Subagent report with references | Subagent Verification section |
