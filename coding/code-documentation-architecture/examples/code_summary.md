# code_summary.md

## Summary

The sample app accepts requests through an API layer, validates input, delegates domain operations to services, and persists state through a database module.

## Key Runtime Flow

1. Request enters `src/api`.
2. Validation and orchestration happen in `src/services`.
3. Writes are executed by `src/db`.
4. Errors propagate back to the API with normalized responses.
