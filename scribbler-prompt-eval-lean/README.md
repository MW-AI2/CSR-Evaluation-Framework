# Scribbler 2.0 — Standard Prompt Evaluation (Lean / Prototype)

The 10 ready-to-use evaluation scorers for benchmarking Scribbler 2.0 standard prompts,
plus the testing materials. This is the lean version for running the manual prototype.

> There is also a full build-pipeline version of this project (with a base template +
> archetype blocks + a build script that regenerates the scorers). You only need that if you
> want to change a rule shared across all 10 scorers. For running the prototype, this lean
> version is all you need.

## What's here

| Folder | What it is |
|---|---|
| `scorers/` | The 10 finished, ready-to-run scorers (one per archetype). Paste these into Scribbler. |
| `testing/` | How to test, the per-scorer paste-in checklist, the Scorer 8 pilot plan, and the results template. |
| `scripts/json_to_results_row.py` | Turns a scorer's JSON output into a results-CSV row automatically. |
| `docs/` | Reference: dependency map (which scorer for which prompt), plus design/governance/Scribbler notes. |
| `library/` | Snapshot of the Scribbler standard prompt library. |

Active scope: 34 prompts across 10 archetypes. Translation and STROBE are out of scope for now.

## How to run an evaluation (the loop)

1. **Generate** — run a standard prompt in Scribbler against a source document.
2. **Assemble** — paste that output into the matching file in `scorers/` as GENERATED_TEXT.
3. **Score** — paste the assembled scorer into a FRESH Scribbler session, with the source
   document selected and any reference files attached. The scorer returns JSON in a
   `<pre><code>` block.

See `testing/how_to_test.md` for the full walkthrough and `testing/paste_in_checklist.md`
for exactly what to select/attach per prompt.

## Recording a result (no manual typing)

Save the JSON the scorer returned to a file, then:

```bash
python scripts/json_to_results_row.py run.json \
  --cycle-id pilot-scorer08 --generator-model claude-4.7-opus --test-case-id TC1-correct
```

It appends a fully-filled row to `testing/results/pilot_results.csv` (auto-numbered R001,
R002, ...). You only supply the few things the JSON can't know (model, test-case id, notes).

## Which scorer for which prompt?

See `docs/dependency_map.md`. Quick reference: Scorer 1 Summarization, 2 Extraction,
3 Definition, 4 Section Drafting, 5 Editing, 6 Consistency, 7 Formatting, 8 Data Updates,
9 Content QC, 10 Comment Review.
