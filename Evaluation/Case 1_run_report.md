# Dummy Test Run — Scorer 1 / da.summarizeDoc / GOLD-01-CLEAN

**Purpose:** Worked example of the full "How to Run Case 1 (Clean)" walkthrough with plausible dummy JSON outputs from an evaluator (Claude Opus, temp 0, 3 runs). Use this as a template for how a real completed Case 1 record should look before you proceed to Case 2.

**All numbers below are dummy.** The three JSON files in this folder are hand-crafted to illustrate realistic variance; they are not from an actual Scribbler run.

---

## Section 1 — Metadata (as filled in the input template)

| Field | Value |
|---|---|
| Test case ID | `GOLD-01-CLEAN` |
| Date run (UTC) | 2026-10-12 |
| Scorer being tested | Scorer 1 — Summarization / Overview |
| Scorer prompt version / hash | `v1.0-merged-2026-10-12` |
| Standard prompt being evaluated | `da.summarizeDoc` |
| Generator model | `GOLD-FIXTURE` |
| Generator temperature | `N/A — fixture` |
| Generator prompt version | `N/A — fixture` |
| Evaluator model | `claude-opus-4.7` |
| Evaluator temperature | `0` |
| Runs | 1, 2, 3 of 3 |
| Test case type | `gold-clean` |
| Expected verdict | `Pass or Pass with minor revision` |
| Blinding confirmed | ☑ Yes |

---

## Section 6 — Envelope check (per run)

### Run 1

| Envelope field | Expected | Actual | Pass? |
|---|---|---|---|
| `overall_verdict` | Pass or Pass-w-minor | `Pass` | ✅ |
| `quick_read.status` | 🟢 Pass | 🟢 Pass | ✅ |
| `overall_score` | ≥ 4.3 | **5.0** | ✅ |
| `critical_failure.present` | false | false | ✅ |
| `source_faithfulness` | 5 | 5 | ✅ |
| `coverage_completeness` | ≥ 4 | 5 | ✅ |
| `structural_fit` | 5 | 5 | ✅ |
| `internal_consistency` | 5 | 5 | ✅ |
| `likely_error_source` | "none" | "none" | ✅ |
| `unsupported_claims` | empty | [] | ✅ |

### Run 2

| Envelope field | Expected | Actual | Pass? |
|---|---|---|---|
| `overall_verdict` | Pass or Pass-w-minor | `Pass` | ✅ |
| `quick_read.status` | 🟢 Pass | 🟢 Pass | ✅ |
| `overall_score` | ≥ 4.3 | **4.6** | ✅ |
| `critical_failure.present` | false | false | ✅ |
| `source_faithfulness` | 5 | 5 | ✅ |
| `coverage_completeness` | ≥ 4 | 4 | ✅ |
| `structural_fit` | 5 | 5 | ✅ |
| `internal_consistency` | 5 | 5 | ✅ |
| `likely_error_source` | "none" | "none" | ✅ |
| `unsupported_claims` | empty | [] | ✅ |

### Run 3

| Envelope field | Expected | Actual | Pass? |
|---|---|---|---|
| `overall_verdict` | Pass or Pass-w-minor | `Pass with minor revision` | ✅ |
| `quick_read.status` | 🟢 Pass | 🟢 Pass | ✅ |
| `overall_score` | ≥ 4.3 | **4.4** | ✅ |
| `critical_failure.present` | false | false | ✅ |
| `source_faithfulness` | 5 | 5 | ✅ |
| `coverage_completeness` | ≥ 4 | 4 | ✅ |
| `structural_fit` | 5 | 5 | ✅ |
| `internal_consistency` | 5 | 5 | ✅ |
| `likely_error_source` | "none" | "none" | ✅ |
| `unsupported_claims` | empty | [] | ✅ |

### Post-run checklist (applies to all three runs)

| Check | Result |
|---|---|
| Valid JSON | ☑ 3/3 |
| Five dimension scores present | ☑ 3/3 |
| overall_score on 0–5 with 1 decimal | ☑ 3/3 |
| quick_read.status matches verdict | ☑ 3/3 |
| Critical-failure cap enforced where applicable | ☑ N/A (no criticals) |
| likely_error_source is allowed value | ☑ 3/3 |
| Severity prefixes on claims lists | ☑ (only Run 3 flagged a minor weakly-supported claim; correctly prefixed `minor:`) |
| source_reference tied to specific locations | ☑ (only Run 3 populated; cites Results Secondary paragraph + Conclusion) |
| Falls within envelope | ☑ 3/3 |

---

## Section 8 — Aggregate verdict for Case 1

| Measurement | Value |
|---|---|
| Median `overall_score` | **4.6** |
| Mean `overall_score` | **4.67** |
| Spread (max − min) | **0.6** |
| Verdict distribution | Pass × 2, Pass with minor revision × 1 |
| Modal verdict | **Pass** |
| Envelope violations across all 3 runs | **0** |
| Critical-failure firings | **0** |

### Dimension-level stability

| Dimension | Run 1 | Run 2 | Run 3 | Spread |
|---|---|---|---|---|
| source_faithfulness | 5 | 5 | 5 | 0 |
| coverage_completeness | 5 | 4 | 4 | 1 |
| regulatory_writing_quality | 5 | 5 | 4 | 1 |
| structural_fit | 5 | 5 | 5 | 0 |
| internal_consistency | 5 | 5 | 5 | 0 |

### What this result tells you

Per the Step 8 decision table:

> **All 3 runs inside envelope, spread 0.6–1.0 → Proceed to Case 2, but note the spread.**

**Amber band.** The evaluator is calibrated (no envelope violations, no spurious critical failures, no over-penalization) but shows mild variance on two dimensions — `coverage_completeness` and `regulatory_writing_quality`. Reading the rationales across the three runs:

- `coverage_completeness` oscillates between 5 (Run 1) and 4 (Runs 2–3) based on how strictly the judge interprets "Standard granularity" — specifically whether minor demographic/comorbidity detail counts as a required inclusion. The rubric wording for this dimension (4 vs. 5) could be sharpened.
- `regulatory_writing_quality` drops to 4 in Run 3 only, driven entirely by one phrase ("acceptable safety profile"). Even though that phrase is lifted verbatim from the source, Run 3's judge treated it as marginally interpretive. The rubric could add a clarifying note that verbatim source-conclusion phrases are not interpretive.

Neither issue requires blocking progress to Case 2, but both are worth logging as rubric-refinement candidates when you next revisit the scorer prompt.

---

## Section 9 — CSV log row (append to running comparison log)

```csv
test_case_id,prompt_id,generator_model,evaluator_model,run_number,overall_score,overall_verdict,critical_failure_present,source_faithfulness,coverage_completeness,regulatory_writing_quality,structural_fit,internal_consistency,likely_error_source
GOLD-01-CLEAN,da.summarizeDoc,GOLD-FIXTURE,claude-opus-4.7,1,5.0,Pass,false,5,5,5,5,5,none
GOLD-01-CLEAN,da.summarizeDoc,GOLD-FIXTURE,claude-opus-4.7,2,4.6,Pass,false,5,4,5,5,5,none
GOLD-01-CLEAN,da.summarizeDoc,GOLD-FIXTURE,claude-opus-4.7,3,4.4,Pass with minor revision,false,5,4,4,5,5,none
```

---

## Section 10 — Decision: proceed or stop?

Decision gate from the walkthrough:

- ☑ All 3 Case 1 runs fall inside the envelope
- ☑ Spread on `overall_score` is ≤ 1.0 (actual: 0.6)
- ☑ Post-run checklist passes for all 3 runs

**Decision: PROCEED TO CASE 2.** Note the amber-band variance in the comparison log so you can monitor whether it persists across future gold-set reruns and across other prompts in the Summarization archetype.

---

## What this first-case run bought you (filled against the walkthrough's four questions)

1. **Valid JSON reliability.** 3/3 parseable, all required fields present. The evaluator model produces stable schema compliance.
2. **No over-penalization.** Lowest score across all runs was 4.4 (comfortably above 4.0). No signs of systemic downward bias.
3. **No spurious critical failures.** 0/3. The scorer's critical-failure trigger is not firing on clean content.
4. **Run-to-run stability.** Spread of 0.6 on `overall_score` means 3 runs per cell will be adequate for future benchmarking; you don't need to escalate to N=5. Keep N=3 as the standard going forward.

---

## Files in this run bundle

- `testcase_da.summarizeDoc_GOLD_case01_clean_run1.json` — dummy evaluator output, run 1 (overall_score 5.0)
- `testcase_da.summarizeDoc_GOLD_case01_clean_run2.json` — dummy evaluator output, run 2 (overall_score 4.6)
- `testcase_da.summarizeDoc_GOLD_case01_clean_run3.json` — dummy evaluator output, run 3 (overall_score 4.4)
- `dummy_run_report.md` — this file (envelope checks + aggregate + CSV + decision)
- `GOLD-01-CLEAN_comparison_log.csv` — standalone CSV ready to append to the master benchmarking log
