# issues.md

## 1. Scope
- Repository: `sample-app`
- Analysis date: 2026-02-27
- Review focus: duplicate order creation under retries
- Excluded paths: `node_modules`, `dist`

## 2. Summary
- Total issues identified: 1
- Critical: 0
- High: 1
- Medium: 0
- Low: 0
- Notes: One confirmed correctness bug with operational impact.

## 3. Open Issues

### Issue 1: Duplicate order creation on retried requests
- Status: confirmed
- Severity: high
- Category: reliability
- Affected files/components: `api/orders`, `services/orders`, `db/orders_repo`
- Related task IDs: `Task 1.1`, `Task 1.2`
- Evidence: repeated requests create multiple rows because no idempotency key is checked before insert
- User or system impact: customers can be charged twice or see duplicate orders
- Trigger or reproduction conditions: resend the same order request after a timeout or client retry
- Suspected root cause: write path does not enforce request uniqueness
- Recommended fix: store and verify an idempotency key before persisting an order
- Validation steps: run a duplicate request test before and after the fix

## 4. Cross-Cutting Risks
| Risk | Related Issues | Impact | Mitigation |
|---|---|---|---|
| Payment duplication | `Issue 1` | customer trust and financial correction work | prioritize fix before rollout |

## 5. Priority Order
| Priority | Issue | Reason | Blocking |
|---|---|---|---|
| P0 | `Issue 1` | direct correctness and financial risk | `Task 1.2` |

## 6. Task Link Coverage
| Issue | Linked Tasks | Purpose | Needs New Task |
|---|---|---|---|
| `Issue 1` | `Task 1.1`, `Task 1.2` | fix and validate | no |

## 7. Deferred or Unverified Findings
| Finding | Reason Deferred | What Would Confirm It |
|---|---|---|
| Potential retry storm under load | not reproduced in example | load test with client retries |

## 8. Change Log
- 2026-02-27 - Example - Initial sample issue log.
