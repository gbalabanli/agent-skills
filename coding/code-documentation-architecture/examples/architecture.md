# architecture.md

## Architecture Style

- Primary style: modular monolith

## Component Interaction

| Component | Depends On | Interaction Type | Failure Behavior |
|---|---|---|---|
| `api/orders` | `services/orders` | sync | returns `500` on unhandled errors |
| `services/orders` | `db/orders_repo` | sync | surfaces write failure to API |

## Open Questions

- Should writes be retried on transient database errors?
