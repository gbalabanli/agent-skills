# architecture.md Template

## 1. Scope and Context
- System boundary:
- In-scope components:
- Out-of-scope components:

## 2. Architecture Style
- Primary style (modular monolith, microservices, event-driven, etc.):
- Rationale:
- Key tradeoffs:

## 3. System Context (C4 Level 1)
| Actor/System | Relationship | Interface |
|---|---|---|
| User |  |  |

## 4. Container View (C4 Level 2)
| Container | Responsibility | Technology | Scaling/Availability Notes |
|---|---|---|---|
| API service |  |  |  |

## 5. Component Interaction View (C4 Level 3)
| Component | Depends On | Interaction Type | Failure Behavior |
|---|---|---|---|
| `...` |  | sync/async |  |

## 6. Data Flow
### Request Flow A
1. Entry:
2. Processing:
3. Persistence:
4. Response/event:

### Request Flow B
1. Entry:
2. Processing:
3. Persistence:
4. Response/event:

## 7. Schema and Contract Catalog
| Schema/Entity/Contract | Type (DB/API/Event) | Defined In | Owned By | Consumed By |
|---|---|---|---|---|
| `User` | DB | `...` | `...` | `...` |

## 8. API and Integration Contracts
| Contract | Provider | Consumer | Versioning | Notes |
|---|---|---|---|---|
| `...` |  |  |  |  |

## 9. Deployment and Infrastructure
- Environments:
- Build and release flow:
- Infra dependencies:
- Runtime topology:

## 10. Reliability, Performance, and Security
- SLO/SLA expectations:
- Bottlenecks and hot paths:
- Fault tolerance and retry strategy:
- Security controls:

## 11. Architectural Decisions and Tradeoffs
| Decision | Status | Reason | Consequence |
|---|---|---|---|
| `...` | proposed/accepted/deprecated |  |  |

## 12. Open Questions
- Q1:
