# Governance

## Standard operations

- **Add a prompt:** classify it against the 10 archetypes and add it to `docs/dependency_map.md`.
  Create a **new archetype only if** Dimension 2, Dimension 4, **and** the critical-failure list
  would all need to be substantially different — not just one of them.
- **Deprecate a prompt:** remove it from the dependency map; retire the scorer if it was a
  singleton.
- **Update a shared rule:** edit `templates/` (universal) or the archetype entry (task-specific),
  rebuild, and record the change date and version in `CHANGELOG.md`.

## Multi-archetype prompts (decision order)

1. Default to a **single primary archetype with embedded overrides** (Option A).
2. **Dominance test:** if one archetype captures >=70% of failure modes, use Option A.
3. **Multiple-artifact test:** if the prompt produces distinct output artifacts, use compound
   scoring (Option C).
4. **Recurrence trigger:** three or more prompts with the same cross-archetype pattern -> propose
   a new hybrid archetype (Option D).
5. **Composite scorers** (Option B) require explicit approval; use sparingly.
6. Document the decision in the dependency map's reverse index.
7. Re-evaluate at version bumps.

## Audit trail (mandatory per run)

Every evaluation run logs: `scorer_id`, `scorer_version`, `prompt_id`, `prompt_version`,
`base_template_version`, and a hash of the rendered (consolidated) scorer. These are emitted in
the scorer's `audit` JSON block and recorded in the results sheet. This is what keeps a score
produced in one month comparable to one produced later.

## Versioning

- Base template: `base-template-vX.Y (<hash>)`; bump on scaffold changes.
- Scorer: `scorer_version` in the audit block; bump on any change to that scorer.
