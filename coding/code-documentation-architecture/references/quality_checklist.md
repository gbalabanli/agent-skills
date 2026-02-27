# Documentation Quality Checklist

Use this checklist before finalizing documentation outputs.

## File Set Completeness
- `project_structure.md` exists.
- `code_summary.md` exists.
- `architecture.md` exists.
- `tasks.md` exists.
- `issues.md` exists when bugs, risks, or validation gaps were identified.

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
- Each task has an explicit status.
- Blockers are called out with `Blocked by` when applicable.
- Each task has explicit acceptance criteria.
- Subtasks are atomic and verifiable.
- Dependencies and critical path are identified.
- Issue-to-task mapping is present for work driven by known bugs or findings.

## Issue Tracking Integrity (`issues.md`)
- Each issue includes severity and affected scope.
- Each issue links to related task IDs when remediation or validation work exists.
- Findings are tied to concrete code evidence or clearly marked as assumptions.
- Recommended fixes and validation steps are actionable.
- Priority ordering reflects actual impact and blockers.

## Maintainability
- Section headings remain stable for future diffs.
- Open questions are listed explicitly.
- Document date/context is updated.
