---
name: init-workspace
description: Scaffold and initialize standard AI agent development workspace files (.ai/AGENTS.md, .ai/LESSONS_LEARNED.md, .ai/FEATURE_HISTORY.md, .ai/TASKS.md, .ai/ARCHITECTURE.md) tailored to a project's codebase, tech stack, and git history. Use when initializing a new or existing codebase for optimal AI-agent collaboration based on Andrej Karpathy's agent principles.
---

# Init Workspace

Use this skill to bootstrap or repair the `.ai/` agent development directory in any workspace.

## Workflow

1. **Inspect Target Workspace**:
   - Detect project type, primary languages, build system (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, etc.).
   - Check if `.ai/` directory or root documentation (`AGENTS.md`, `CLAUDE.md`, `README.md`) already exists.
   - Inspect git history to retrieve recent commits if available.

2. **Run Initialization CLI**:
   - Execute the workspace initialization script:
     ```bash
     python coding/init-workspace/scripts/init_workspace.py --path <project_root> --output-dir .ai
     ```
   - If overwriting existing files is required, pass `--overwrite`.

3. **Customize Workspace Files**:
   - Update `.ai/AGENTS.md` with explicit build/test commands, tools, and safety boundaries.
   - Update `.ai/ARCHITECTURE.md` with system entry points and core module descriptions.
   - Seed `.ai/TASKS.md` with initial task backlog items and verification criteria.
   - Initialize `.ai/FEATURE_HISTORY.md` with active features and initial session dev summaries.
   - Ensure `.ai/LESSONS_LEARNED.md` is clean and ready for recording pitfalls and corrections.

4. **Validate Workspace Setup**:
   - Confirm all 5 files exist inside `.ai/`: `AGENTS.md`, `LESSONS_LEARNED.md`, `FEATURE_HISTORY.md`, `TASKS.md`, `ARCHITECTURE.md`.
   - Verify formatting and clickable file links.

## Workspace Structure

All workspace memory and agent instruction files reside in `<project_root>/.ai/`:

```
<project_root>/
└── .ai/
    ├── AGENTS.md            # Agent rules, setup commands, build/test scripts, safety rules
    ├── LESSONS_LEARNED.md    # Memory log for failures, gotchas, framework pitfalls, user rules
    ├── FEATURE_HISTORY.md    # Feature-centric development history & session summaries
    ├── TASKS.md              # Active task backlog, feature milestones, verification status
    └── ARCHITECTURE.md       # High-level architecture map, entry points, module descriptions
```

## Maintenance Rules for AI Agents

- **Failure Logging**: Record non-trivial build errors, framework traps, and user feedback in `.ai/LESSONS_LEARNED.md`.
- **Feature Session Logging**: Group session development summaries under their respective feature headers in `.ai/FEATURE_HISTORY.md`.
- **Task Tracking**: Update checkboxes in `.ai/TASKS.md` immediately upon completing items.

## Resource Usage

- Script: `scripts/init_workspace.py`
- Templates: `assets/*.template`
- Guide: `references/karpathy_agent_workspace_guide.md`

## Validation

1. Run `python coding/init-workspace/scripts/init_workspace.py --help` to confirm script readiness.
2. Confirm `.ai/` directory and all 5 markdown files exist and contain non-empty project details.
