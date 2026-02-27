---
name: code-documentation-architecture
description: Generate complete repository documentation and system architecture artifacts from source code. Use when Codex must create or refresh `project_structure.md`, `code_summary.md`, `architecture.md`, `tasks.md`, and `issues.md` for onboarding, audits, handoffs, refactors, migrations, and technical planning.
---

# Code Documentation Architecture

Use this skill to transform a repository into five aligned documentation artifacts:

1. `project_structure.md`
2. `code_summary.md`
3. `architecture.md`
4. `tasks.md`
5. `issues.md`

## Workflow

1. Confirm scope and constraints.
- Confirm repository root, excluded paths, and target audience.
- Confirm whether output should be new files or updates to existing files.
- Confirm planning horizon for `tasks.md` (stabilization, refactor, migration, feature roadmap).

2. Build repository inventory.
- Use fast discovery commands (`rg --files`, `rg`, build/tool manifests, CI files, infra config).
- Identify entrypoints, modules/packages, services, data stores, message channels, and external integrations.
- Identify schema sources (ORM models, SQL migrations, OpenAPI/GraphQL, DTOs, protobuf/avro/jsonschema).

3. Create `project_structure.md`.
- Follow [project_structure_template.md](references/project_structure_template.md).
- Keep the tree concise and responsibility-first: directory -> role -> notable files.
- Include generated-code and vendor exclusions explicitly.

4. Create `code_summary.md`.
- Follow [code_summary_template.md](references/code_summary_template.md).
- Summarize behavior and ownership boundaries, not just file counts.
- Document key runtime flows and failure handling.

5. Create `architecture.md`.
- Follow [architecture_template.md](references/architecture_template.md).
- Document context, containers, component interactions, and data flow.
- Include schema catalog section that links data entities/contracts to owning components.

6. Create `tasks.md`.
- Follow [tasks_template.md](references/tasks_template.md).
- Organize by phases, tasks, and subtasks with dependencies and acceptance criteria.
- Ensure each subtask is atomic, testable, and mapped to affected files/components.

7. Create `issues.md`.
- Follow [issues_template.md](references/issues_template.md).
- Capture confirmed bugs, gaps, and operational risks discovered while reading the code.
- Include severity, impact, evidence, reproduction conditions, and proposed remediation.

8. Run consistency checks.
- Apply [quality_checklist.md](references/quality_checklist.md).
- Ensure terminology, component names, and interfaces are consistent across all five files.
- Record unknowns and assumptions explicitly instead of guessing.

## Output Rules

- Use exact filenames unless user requests different names.
- Prefer concrete evidence from source files over inferred claims.
- Mark uncertain items with `Assumption:` and list validation steps.
- Keep sections stable across updates so diffs remain reviewable.
- When updating existing docs, preserve manually authored notes unless they conflict with code reality.

## Reference Files

- [project_structure_template.md](references/project_structure_template.md)
- [code_summary_template.md](references/code_summary_template.md)
- [architecture_template.md](references/architecture_template.md)
- [tasks_template.md](references/tasks_template.md)
- [issues_template.md](references/issues_template.md)
- [quality_checklist.md](references/quality_checklist.md)
