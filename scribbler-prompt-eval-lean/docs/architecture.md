# Architecture

## Two layers, merged at build time

The framework separates a single shared scaffold from task-specific content, then merges them
into standalone prompts at build time (not at runtime).

- **Layer 1 — base template** (`templates/base_evaluator_scorer_template.md`): the universal
  content, identical in every scorer. Role framing and conservative-scoring directive;
  evaluation principles; the three universal dimensions (Source Faithfulness, Regulatory
  Writing Quality, Internal Consistency); critical-failure structure; diagnostic bands; JSON
  output format; verdict rules; field expectations; evaluation method; input block.
- **Layer 2 — archetype blocks** (defined in `scripts/build_scorers.py` `ARCHETYPES`, mirrored
  in `archetypes/`): purpose, inputs, elements to check, Dimensions 2 and 4, critical-failure
  examples, and the weights vector.

## Why merge at build time instead of a runtime composer

The original design used a runtime composer to combine base + archetype on every evaluation.
The team chose to pre-merge into 10 standalone prompts so Scribbler can run each one directly.
The trade-off: the common base content is now duplicated across 10 files, so it can drift.

The build pipeline removes that risk:
- `build_scorers.py` injects the **same** extracted common blocks into every merged file.
- `verify_common.py` asserts those blocks are byte-identical across all 10 files.
- CI runs both on every PR, and fails if `dist/` is stale or the blocks drift.

The one intentional exception is Scorer 3's Dimension 1, which appends a documented note that
Source Faithfulness is assessed against a regulatory reference for that archetype.

## Scoring model

Five dimensions scored 0–5, each with a rationale. Dimensions 1, 3, 5 are universal; 2 and 4
are task-specific. Weights sum to 1.0 per scorer (enforced in the build) and vary by archetype.
A critical failure caps the overall score at 2.5. Output is JSON (wrapped in `<pre><code>` for
the Scribbler contract) with a quick-read block, dimension scores, critical-failure flag,
likely error source, issue lists, overall score, verdict, interpretation, and an audit block.

Comparability is within-archetype: because weights and the task-specific dimensions differ by
archetype, composite scores are comparable only within one archetype; library-wide trends hold
for the three universal dimensions.
