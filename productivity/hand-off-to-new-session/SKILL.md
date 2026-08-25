---
name: hand-off-to-new-session
description: "Generate a consolidated HANDOFF.md at project root that gives a new session (or different CLI tool) full context about what just happened. Reads checkpoint.md (11 sections), project MEMORY.md, task progress files, session diffs, git state, and conversation history. Use when the user says 'hand off', 'handoff', 'new session context', 'export session', 'transfer context', 'prepare for next session', 'wrap up session', 'create handoff doc', 'session summary', or wants to continue work in a fresh session or different agent CLI. Produces a single actionable document — key decisions summarized, not a full message log."
metadata:
  short-description: Export session context to HANDOFF.md for new sessions
  category: productivity
  tags: [session, handoff, context-transfer, productivity]
---

# Hand Off to New Session

Generate a single `HANDOFF.md` at the project root that gives a fresh session everything it needs to continue work without re-reading the full conversation. Output is **key decisions summarized**, not a full message log.

## When this runs

- End of a long session before starting a new one
- Before switching to a different CLI tool (Codex, OpenCode, etc.)
- When context is getting large and the user wants a clean restart
- When explicitly asked to "hand off", "export session", or "wrap up"

## Data sources

| # | Source | Tool | What it provides |
|---|--------|------|-----------------|
| 1 | `checkpoint.md` (11 sections) | `read` | Active intent, next action, directives, task tree, current work, files, discovered knowledge, errors, live resources, design decisions, open notes |
| 2 | Project `MEMORY.md` | `read` | Project context, rules, architecture decisions, durable knowledge |
| 3 | `tasks/<id>/progress.md` | `glob` + `read` | Per-task journals with granular progress |
| 4 | `notes.md` | `read` | Free-form session scratchpad |
| 5 | `storage/session_diff/<sid>.json` | `read` | File-level changes made this session |
| 6 | Git state | `bash` | `git status`, `git diff --stat`, `git log --oneline -20` |
| 7 | Conversation history | `history` | Key user messages and decisions (search, not dump) |

## Workflow

### Step 1: Locate session data

Identify the current session ID and project paths. The session ID is in the system prompt under "This session has memory at ...". Extract:
- Session ID (e.g., `ses_xxx`)
- Session memory dir: the path from the system prompt
- Project ID: from the memory path or by reading the checkpoint's execution context section

If the session ID is already known from context, skip the search.

### Step 2: Read all data sources in parallel

All of these are independent reads. Issue them all at once:

1. `read` the checkpoint.md at `<session_dir>/checkpoint.md`
2. `read` the project MEMORY.md (find project UUID from checkpoint or memory search)
3. `glob` for `tasks/*/progress.md` in the session dir, then `read` each match
4. `read` the notes.md at `<session_dir>/notes.md`
5. `read` the session diff at `<mimocode_data>/storage/session_diff/<session_id>.json`
6. `bash` git status --short
7. `bash` git diff --stat HEAD
8. `bash` git log --oneline -20
9. `history` search for "decided tradeoff reason chose" (limit 10)
10. `history` search for "error fix resolved workaround" (limit 10)

### Step 3: Assemble HANDOFF.md

Map checkpoint sections to HANDOFF sections:

| Checkpoint | HANDOFF section |
|-----------|----------------|
| §1 Active intent | §1 Quick-start (verbatim quote) |
| §2 Next concrete action | §6 Next steps |
| §3 Directives | §2 Project context |
| §4 Task tree | §5 Current state |
| §5 Current work | §3 Session summary |
| §6 Files and code sections | §4 Changes made |
| §7 Discovered knowledge | §9 Discoveries |
| §8 Errors and fixes | §8 Errors and fixes |
| §9 Live resources | §5 Current state |
| §10 Design decisions | §7 Key decisions |
| §11 Open notes | §6 Next steps |

Merge project MEMORY.md content:
- Project context + rules → §2
- Architecture decisions → §7 (merge with checkpoint §10)
- Discovered durable knowledge → §9 (merge with checkpoint §7)

Use the template from `references/handoff-template.md`. Fill every section — use "(none)" for empty sections, never leave blanks.

### Step 4: Write and confirm

Write `HANDOFF.md` to the project root (the working directory). Report to the user:
- Path where HANDOFF.md was written
- Number of sections populated vs. "(none)"
- Any data sources that were missing or empty

## Output principles

1. **Key decisions only** — summarize into 1-2 sentences with rationale. No raw message dumps.
2. **Actionable next steps** — each step concrete enough for a new agent to execute immediately.
3. **Absolute file paths** — a new session may have a different working directory.
4. **Timestamped** — include generation time and session ID for traceability.
5. **Verbatim user quotes** — preserve exact words for intent and directives.
6. **Cross-reference** — e.g., "See §4 Changes for the files involved" instead of repeating content.

## Fallbacks

| Scenario | Fallback |
|----------|----------|
| `checkpoint.md` missing | Use `history` tool to reconstruct; note "No checkpoint found" |
| `MEMORY.md` missing | Use `memory` search with `scope: "projects"`; note "No project memory" |
| `session_diff` missing | Use `git diff --stat HEAD` and `git status` |
| `tasks/` empty | Use checkpoint §4 task tree; note "(no task journals)" |
| `notes.md` empty | Skip; note "(no session notes)" |
| `history` returns nothing | Rely on checkpoint; note "Limited conversation history" |
| Not a git repo | Skip git steps; note "Not a git repository" |

## Reference Files

- [handoff-template.md](references/handoff-template.md) — full HANDOFF.md template structure
