# project_structure.md

## Repository Tree

```text
sample-app/
|-- src/
|   |-- api/
|   |-- services/
|   `-- db/
|-- tests/
`-- package.json
```

## Notes

- `src/api` exposes HTTP handlers.
- `src/services` contains business logic.
- `src/db` owns persistence access.
