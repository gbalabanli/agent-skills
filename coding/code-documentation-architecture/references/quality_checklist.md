# Documentation Quality Checklist

Use this checklist before finalizing documentation outputs.

## File Set Completeness
- `project_structure.md` exists.
- `code_summary.md` exists.
- `architecture.md` exists.
- `tasks.md` exists.

## Naming Consistency
- Component names match across all files.
- Service/module names match repository naming.
- Schema/entity names are consistent with source definitions.

## Evidence Quality
- Claims are backed by specific files or interfaces.
- Unknowns are marked as assumptions.
- Generated or vendored code is clearly excluded where applicable.

## Architecture Integrity
- System context includes all major external actors and systems.
- Container/component relationships are internally consistent.
- Data flows align with documented interfaces and schemas.

## Planning Integrity (`tasks.md`)
- Work is organized into phases with clear objectives.
- Each task has explicit acceptance criteria.
- Subtasks are atomic and verifiable.
- Dependencies and critical path are identified.

## Maintainability
- Section headings remain stable for future diffs.
- Open questions are listed explicitly.
- Document date/context is updated.
