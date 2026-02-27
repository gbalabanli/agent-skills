# tasks.md

## 1. Planning Scope
- Goal: stabilize order creation
- Planning horizon: stabilization
- In-scope systems/components: `api/orders`, `services/orders`, `db/orders_repo`
- Out-of-scope items: UI changes

## 2. Assumptions and Constraints
- Assumption 1: database schema is unchanged
- Constraint 1: fix must ship without API contract changes

## 3. Phase Plan

## Phase 1: Stabilize writes
**Objective:** Prevent duplicate order creation under retry conditions.  
**Exit criteria:** Duplicate submissions are idempotent and covered by tests.  

### Task 1.1: Add idempotency guard
- Status: in_progress
- Goal: reject duplicate writes safely
- Scope: add request key handling in service layer
- Affected files/components: `services/orders`, `db/orders_repo`
- Blocked by:
- Dependencies:
- Risks: incorrect deduplication could reject valid writes
- Acceptance criteria: repeated requests with the same key create one record only

#### Subtask 1.1.1: Persist request keys
- Action: add lookup and insert flow in persistence layer
- Deliverable: repository update and tests
- Done when: duplicate key checks pass in automated tests

### Task 1.2: Validate duplicate request handling
- Status: blocked
- Goal: confirm the fix works under retry conditions
- Scope: integration test coverage for repeated requests
- Affected files/components: `tests/orders`, `api/orders`
- Blocked by: `Issue 1`, `Task 1.1`
- Dependencies: `Task 1.1`
- Risks: flaky retry simulation may hide regressions
- Acceptance criteria: regression test fails before the fix and passes after it

#### Subtask 1.2.1: Add retry scenario test
- Action: create an integration test that sends the same request twice
- Deliverable: repeat-request coverage
- Done when: the test reliably reproduces and validates the bug fix

## 4. Critical Path and Dependencies
| Item | Status | Depends On | Blocked By | Blocks | Notes |
|---|---|---|---|---|---|
| `Task 1.1` | `in_progress` |  |  | `Task 1.2` | Core remediation work |
| `Task 1.2` | `blocked` | `Task 1.1` | `Issue 1`, `Task 1.1` |  | Waiting for remediation work |

## 5. Validation and Rollout Gates
| Gate | Criteria | Evidence Required |
|---|---|---|
| Phase 1 complete | duplicate writes prevented | passing regression tests |

## 6. Risk Register
| Risk | Trigger | Mitigation | Owner |
|---|---|---|---|
| False deduplication | key generation mismatch | validate key rules in tests | backend |

## 7. Issue-to-Task Mapping
| Task ID | Related Issues | Relationship | Notes |
|---|---|---|---|
| `Task 1.1` | `Issue 1` | fixes | primary remediation |
| `Task 1.2` | `Issue 1` | validates | regression coverage |

## 8. Change Log
- 2026-02-27 - Example - Initial sample plan.
