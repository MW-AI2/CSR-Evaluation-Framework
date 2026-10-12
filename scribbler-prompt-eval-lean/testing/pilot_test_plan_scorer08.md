# Pilot Test Plan — Scorer 8 (Data Updates from Source Tables)

**Goal:** Prove the evaluation loop works end to end in Scribbler 2.0, and confirm Scorer 8 scores correctly, before scaling to the other nine archetypes. Scorer 8 is chosen because it is the highest-stakes archetype: a single wrong number is a critical failure, so it exercises the critical-failure logic and the audit trail hardest.

**Scope:** 2-3 of the seven Scorer 8 prompts. Suggested: `up.tableNum` (table, no tracked changes), `up.textNum.tc` (text, tracked changes), `up.content` (references + source-document naming). This covers a non-tracked variant, a tracked variant, and the reference variant.

**Effort:** About half a day. Owner: TBD.

---

## Step 1 — Prepare test cases (per prompt, 3 cases each)

For each of the 2-3 prompts, build three cases with a known answer key:
1. **Correct case** — output matches the source tables exactly. Expected: Pass, no critical failure.
2. **Known-bad numeric case** — introduce one wrong number. Expected: critical failure fires, overall score capped at 2.5, verdict Fail.
3. **Markup/format case** (for `.tc` and `up.content`) — e.g. tracked changes applied to an unchanged value, or a missing source-document name. Expected: the relevant critical or Dimension 4 rule fires.

Keep the source data tables and the pre-update text for each case; you will need them in both the generation and scoring sessions.

## Step 2 — Generate (Scribbler session A)

For each case: open the source document in Word, select the pre-update table/paragraph, attach the source data tables, and run the standard prompt. Save the Scribbler output. (See the per-scorer checklist, Scorer 8 row, for the exact context profile per prompt.)

## Step 3 — Assemble

Paste each Scribbler output into `scorer_08_data_consolidated.md` as GENERATED_TEXT, between the `<<<PASTE SCRIBBLER OUTPUT HERE>>>` markers. Do not paste the source — it is supplied by context in the next step.

## Step 4 — Score (Scribbler session B — a FRESH conversation)

Start a brand-new Scribbler session (no residual context from Step 2). Select the pre-update text in Word and attach the source data tables. Paste the assembled scorer. Run it. Copy the JSON from the returned `<pre><code>` block into the results spreadsheet.

## Step 5 — Check each result against expectations

Record PASS/FAIL for the loop on each of these:

| Check | What to confirm |
|---|---|
| JSON returned clean | Reply is a single `<pre><code>` block containing parseable JSON; `json_valid = TRUE` |
| Source read from context | Scorer did NOT report the source missing; it compared against the attached tables |
| Correct case | No critical failure; overall score high; verdict Pass |
| Known-bad numeric case | `critical_failure_present = TRUE`; overall_score capped at 2.5; verdict Fail |
| Markup/format case | Correct rule fired (critical vs. Dimension 4) per the revised scorer |
| N/A handling | For non-tracked `up.tableNum`, Dimension 4 scored as N/A and weights renormalized, not penalized |
| Rationales specific | Each dimension rationale cites the specific value/location, not generic text |

## Step 6 — Human calibration

Have one reviewer independently score the same outputs (overall score + verdict). Enter their scores in the spreadsheet's human columns and set `agreement_flag`. For any DISAGREE, note whether the scorer or the human was right and whether a template wording change is needed.

## Step 7 — Decide go / fix

- **Go:** if the loop mechanics hold and the scorer fires correctly on the known-bad cases with human agreement, proceed to the other archetypes (Scorer 9, then 2, 4, then the rest).
- **Fix:** if a template issue appears (e.g. scorer misreads context, or a rule mis-fires), adjust the archetype definition in the build script and regenerate. The fix propagates to all 10 files, and the consistency check reconfirms the common base is intact.

---

## Success criteria for the pilot

1. All loop-mechanics checks pass for every case.
2. Every known-bad case is caught (no false negatives on wrong numbers).
3. No correct case is failed (no false positives at the top).
4. Human and scorer agree on verdict for at least the clear cases; divergences are understood.
5. The results spreadsheet is populated and readable, with audit fields captured for every run.

## What to record (every run)

Use `evaluation_results_template.csv`. Minimum per run: run_id, prompt_id/version, generator_model, scorer_version, base_template_version, the five dimension scores + rationales, critical-failure flag and reason, overall score and verdict, and (for calibration runs) the human score, verdict, and agreement flag.
