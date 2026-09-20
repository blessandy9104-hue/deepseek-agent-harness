# Maya review workflow and neutral world model

## Neutral world model

The neutral world model is a provenance-first evidence layer. Each record stores a claim, source name, optional source URL, retrieval timestamp, publication timestamp when known, confidence (`low`, `medium`, or `high`), evidence type, perspective, uncertainty, and visibility. Public world evidence is stored as `public_world_context`; explicitly approved user context is stored separately as `approved_world_context`. The layer rejects likely secrets and sensitive credential fields, refuses unapproved `user_approved_context`, and never writes trusted memory or performs external actions.

Maya can access this layer locally through `:world summary`, `:world list`, and the controlled input form:

```text
:world add | claim | source | confidence | evidence_type | optional source_url
```

`:world compare [topic]` is a read-only comparison view. It shows each matching
record's source, confidence, stated uncertainty, conflict flag, and freshness.
Evidence becomes `stale` after 30 days and is flagged for review rather than
silently downgraded, deleted, or treated as false. The comparison never chooses
a winner or turns evidence into a forecast.

The layer records provenance; it does not declare absolute truth, generate automatic forecasts, or replace source comparison and human review.

## Pending-suggestion workflow

The Notebook UI now includes **Seed Demo**, **Review Suggestions**, and **World Model** controls. `Seed Demo` generates a review-only hypothesis and registers it in the pending queue. `Review Suggestions` shows the queue and current state. `World Model` shows evidence-layer status.

The review flow is deliberately staged:

1. Maya generates a conditional suggestion with alternatives, benefits, harms, barriers, reversibility, assumptions, and uncertainty.
2. The suggestion enters `pending_review` and is inspectable before any decision.
3. The user inspects it with `:suggestion inspect <id>`.
4. The user must type an explicit confirmation command: `:suggestion approve <id> confirm` or `:suggestion reject <id> confirm`.
5. Approval moves the item only to `approved_pending_sandbox_and_regression`; it does not activate code, update trusted memory, or perform external actions.
6. Rejection moves the item to `rejected_by_user` and records the review note without changing memory or taking action.
7. Every registration and review action is appended to `maya_suggestion_review_audit.jsonl`.

The workflow preserves human control, auditability, rollback requirements, privacy boundaries, uncertainty, and alternative paths.
