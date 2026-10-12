# Open Decisions

Two decisions need owner sign-off. Both can be answered empirically during the Scorer 8 pilot
and the first calibration runs.

## 1. Should `rv.genericReply` be split out of Scorer 10?

- **Context:** Scorer 10 covers six operations (triage, triage table, agenda, AI review, AI
  reply, generic reply). `rv.genericReply` is pure verbatim boilerplate — mechanically unlike the
  others.
- **Current state:** kept in Scorer 10 with a per-prompt applicability matrix and a deterministic
  verbatim check (exact match = 5; any deviation = critical failure).
- **Options:** (a) keep as-is with the override; (b) split into its own scorer or a deterministic
  non-LLM check.
- **How to decide:** during the pilot, see whether the single scorer handles it cleanly or
  whether the mixed rules cause confusion.

## 2. Should Regulatory Writing Quality use one fixed library-wide weight?

- **Context:** this universal dimension currently ranges from 0.05 to 0.20 across archetypes,
  which means composite scores are comparable only within an archetype.
- **Current state:** per-archetype weights, documented.
- **Options:** (a) keep per-archetype and document the comparability limit; (b) fix one weight
  library-wide to strengthen cross-archetype comparability.
- **How to decide:** confirm during the pilot whether cross-archetype comparison is actually
  needed in practice; if not, keep per-archetype.

## Related non-blocking items

- Update `docs/dependency_map.md` to show active scope as 34 prompts across 10 archetypes, with
  Scorers 11 and 12 marked shelved.
- Validate the evaluator model against human reviewers before relying on scores (starts with the
  Scorer 8 pilot).
