# Andrej Karpathy's Principles for AI Agent Workspaces

> [!NOTE]
> Synthetic Software Engineers (LLM Agents) perform best when project state, instructions, error logs, and session history are externalized into clear, structured markdown files.

## Core Architectural Pillars

### 1. Dedicated Instruction Boundary (`.ai/AGENTS.md`)
- **Purpose**: Establishes project setup rules, build/test commands, tech stack specs, and agent constraints.
- **Why**: LLM agents need unambiguous instructions on how to install, build, and test the project without guessing or running arbitrary destructive shell commands.
- **Rule**: Keep instructions concise, imperative, and verifiable.

### 2. Failure Memory & Lessons Learned (`.ai/LESSONS_LEARNED.md`)
- **Purpose**: Persistent log of bugs, build/compilation gotchas, framework edge cases, and past user corrections.
- **Why**: LLMs are stateless across independent chat sessions. Without explicit external memory, agents tend to repeat the same missteps, try broken package versions, or make forbidden edits.
- **Rule**: When an agent encounters a non-trivial failure or receives explicit feedback from the user, record the symptom, root cause, and fix in `.ai/LESSONS_LEARNED.md`.

### 3. Feature-Centric Session History (`.ai/FEATURE_HISTORY.md`)
- **Purpose**: Tracks feature evolution over time, linking individual development sessions, commit hashes, and design decisions to specific features.
- **Why**: Feature development is non-linear. Agents need to understand *why* code was structured a certain way during previous sessions to avoid breaking subtle feature requirements.
- **Rule**: Group sessions under feature headings (`## Feature: [Name]`). After completing a dev session or feature milestone, summarize the key changes and list associated commits.

### 4. Granular Task Backlog (`.ai/TASKS.md`)
- **Purpose**: Live task state tracking with explicit checkboxes (`[ ]`, `[/]`, `[x]`).
- **Why**: Keeps long-running goals focused and prevents agents from losing track of subtasks during multi-step implementations.
- **Rule**: Update task checkboxes immediately as work progresses.

### 5. High-Level Architecture Map (`.ai/ARCHITECTURE.md`)
- **Purpose**: Structural layout, entry points, module descriptions, and data flow diagrams.
- **Why**: Allows agents to quickly navigate the codebase without having to recursively list every single directory on every prompt.

---

## Maintenance Lifecycle for AI Agents

1. **Session Start**: Read `.ai/AGENTS.md` and check `.ai/TASKS.md` for active goals.
2. **Before Code Edits**: Check `.ai/ARCHITECTURE.md` for entry points and `.ai/LESSONS_LEARNED.md` for known pitfalls.
3. **During Execution**: Update `.ai/TASKS.md` checkboxes as steps complete.
4. **On Errors / Feedback**: Log new learnings to `.ai/LESSONS_LEARNED.md`.
5. **Session Wrap-Up**: Add session dev summary under the target feature in `.ai/FEATURE_HISTORY.md`.
