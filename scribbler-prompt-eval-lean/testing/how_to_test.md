# How to Test the Evaluation Framework

Three tests, in order of effort. Each builds confidence before you invest in the next.
Run Test 1 first; it is free and catches problems immediately.

---

## Test 1 — Does the repo build? (5 minutes, no Scribbler needed)

This checks the build mechanics before you test any scoring.

In the VS Code integrated terminal, from the repo root:

```bash
python scripts/build_scorers.py
python scripts/verify_common.py
```

**Expected result:** `verify_common.py` prints `Common-base consistency: PASS`.

Two notes it may also print, both expected and NOT problems:
- **"2 variants for dim1"** — Scorer 3 (Definition) intentionally adds a note to its first
  dimension because it judges against a regulatory reference, not a pasted source. By design.
- **"10 variants for output_format"** — each scorer's JSON names its own two task-specific
  dimensions, so this block legitimately differs per scorer. By design.

If you see PASS, the plumbing works. Your GitHub Action runs these same two commands on every
push, so a green check in the **Actions** tab confirms the same thing.

---

## Test 2 — Does one scorer work end-to-end in Scribbler? (half a day)

This tests the real question: does a consolidated scorer produce a sensible evaluation when run
in Scribbler? Follow `testing/pilot_test_plan_scorer08.md`. Start with `up.tableNum` (Scorer 8).

1. **Generate** — run the standard prompt in Scribbler against a source document (select the
   pre-update table, attach the source data tables). Save the output.
2. **Assemble** — paste that output into `dist/consolidated_scorers/scorer_08_data_consolidated.md`
   as GENERATED_TEXT (between the paste-in markers).
3. **Score** — paste the assembled scorer into a FRESH Scribbler session, with the source
   document selected and the source data tables attached. Let it return the JSON evaluation.

Use `testing/paste_in_checklist.md` for exactly what to select and attach per prompt.

Run three cases: one correct, one with a deliberately wrong number, one with a format issue.

---

## Test 3 — Does the scorer judge correctly? (the one that matters)

For the three cases, confirm the scorer did the right thing:

- The **correct** case passes without inventing problems.
- The **wrong-number** case fires the critical failure and caps the overall score at 2.5.
- The **format** case flags the right issue.
- Have one reviewer independently rate the same three outputs and compare. Agreement builds
  confidence; disagreement tells you whether a rule needs adjusting.

Record every run in `testing/templates/evaluation_results_template.csv` (one row per run). That
gives you readable pilot results and the audit trail.

---

## If something is wrong

Fix the SOURCE, never the generated file:
- Universal issue (affects all scorers) -> edit `templates/base_evaluator_scorer_template.md`.
- Task-specific issue (one scorer) -> edit that scorer's archetype content.

Then rerun Test 1 (`build_scorers.py` + `verify_common.py`). The fix propagates to all 10
consolidated scorers, and the consistency check reconfirms they match. Never edit anything in
`dist/` directly — Test 1 and CI will catch it if you do.

---

## When Scorer 8 passes all three

Repeat Tests 2–3 for the next scorer, in rough order of stakes: Scorer 9 (Content QC), then
Scorer 2 (Extraction), Scorer 4 (Section Drafting), then the rest. The checklist covers every
prompt.
