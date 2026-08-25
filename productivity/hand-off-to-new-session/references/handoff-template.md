# HANDOFF.md Template

Use this template when assembling the hand-off document. Fill every section — use "(none)" for empty sections, never leave blanks.

---

```markdown
# Session Handoff

> Generated: `YYYY-MM-DDTHH:MM:SSZ` | Session: `<session_id>` | Project: `<project_name>`

---

## §1 Quick-start

_One-paragraph summary a new agent reads first._

**User's goal**: <verbatim quote from checkpoint §1>

**TL;DR**: <2-3 sentences: what happened, where things stand, what to do next>

---

## §2 Project context

**Project**: <name and one-line description from MEMORY.md>

**Workspace**: `<absolute path>`

**Branch**: `<current branch>` | **Remote**: `<origin url>`

**Rules** (hard constraints):
- <rule from MEMORY.md>
- ...

**Session directives** (this session only):
- <directive from checkpoint §3>
- (none)

---

## §3 Session summary

_What was done this session, in chronological order._

| # | Action | Outcome |
|---|--------|---------|
| 1 | <what was done> | <result> |
| 2 | ... | ... |

**Commits made this session**:
- `<short hash>` <message>
- (none)

---

## §4 Changes made

_Files created, modified, or deleted. One line per file + why._

| File | Action | Rationale |
|------|--------|-----------|
| `<absolute path>` | created/modified/deleted | <why> |
| ... | ... | ... |

---

## §5 Current state

**Task status**:
- <completed task>
- <in-progress task> — <what remains>
- <blocked task> — <blocker>

**Uncommitted changes**:
```
<git status output, or "(none — working tree clean)">
```

**Running processes / live resources**:
- <from checkpoint §9>
- (none)

**Files in flight**:
- `<path>` — <purpose>

---

## §6 Next steps

_Concrete, actionable steps. Each must be executable without additional context._

1. <next step — from checkpoint §2>
2. <second priority>
3. ...

**Unresolved questions**:
- <from checkpoint §11>
- (none)

---

## §7 Key decisions

| Decision | Rationale | Alternatives rejected |
|----------|-----------|----------------------|
| <what was decided> | <why> | <what was considered> |
| ... | ... | ... |

**Promoted to MEMORY.md**: <list or "(none yet)">

---

## §8 Errors and fixes

| Error | Fix | Recurrence risk |
|-------|-----|-----------------|
| <error description> | <how fixed> | <high/low + mitigation> |
| (none) | | |

---

## §9 Discoveries

_Facts learned this session that a new agent should know._

- <discovery from checkpoint §7>
- <discovery from MEMORY.md>
- ...

**Candidates for promotion to MEMORY.md**:
- <item that should persist>
- (none)

---

_End of handoff. A new session should read this file first, then load checkpoint.md for full detail on any section._
```
