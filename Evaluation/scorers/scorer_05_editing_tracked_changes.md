# Scorer 5 — Editing with Tracked Changes

**Applies to:** `ed.grammar`, `ed.clarity`, `ed.streamline`, `tr.pastTense`

---

## Scorer: Editing with Tracked Changes

[PURPOSE: determine whether GENERATED_TEXT (1) preserves source meaning exactly, (2) applies the correct and minimal edits for the requested edit type, (3) is written in appropriate regulatory register, (4) marks every change with correct tracked-changes markup at the smallest editable range, (5) is internally consistent.]

---

## INPUTS

### SOURCE_TEXT
The original selected text pre-edit. Primary ground truth for meaning preservation.

### ORIGINAL_SELECTION
Same as SOURCE_TEXT for this scorer; used as the pre-edit reference to verify tracked-changes markup.

### GENERATED_TEXT
The edited output with tracked-changes markup.

### TARGET_DETAIL_LEVEL
Standard

### OPTIONAL_REFERENCE_TEXT
A human-edited version (if available).

---

## ELEMENTS TO CHECK

- Meaning fully preserved
- Only edits of the requested type applied (grammar-only for `ed.grammar`; clarity-only for `ed.clarity`; sentence-splitting/simplification for `ed.streamline`; verb tense only for `tr.pastTense`)
- Edits are minimal — smallest editable range (letter/word/phrase), not whole sentences marked as changed
- Every change wrapped in correct `<ins>` and `<del>` tracked-changes markup
- If no edit needed (`ed.grammar`): output states `"No corrections needed."`
- No stylistic edits introduced in `ed.grammar`

---

## DIMENSION 2: EDIT_CORRECTNESS_AND_MINIMALITY (0–5)

- **5** = correct edits of the requested type only, applied at minimal range, meaning preserved
- **4** = correct edits with slightly broader range than needed
- **3** = one scope creep (e.g., a style edit inside `ed.grammar`) OR one oversized change range
- **2** = multiple scope creeps or meaning subtly altered
- **1** = meaning altered or wrong edit type dominates
- **0** = destructive edit

## DIMENSION 4: TRACKED_CHANGES_MARKUP_CORRECTNESS (0–5)

- **5** = every change correctly wrapped in `<ins>`/`<del>` at smallest range; no unmarked edits
- **4** = minor markup inconsistency
- **3** = one moderate markup issue (e.g., unmarked edit, or whole sentence marked instead of word)
- **2** = multiple markup issues
- **1** = markup largely absent or wrong
- **0** = tracked changes not applied

---

## CRITICAL FAILURE RULES

- Meaning altered
- Unmarked edit (silent change)
- Stylistic edit introduced in `ed.grammar`
- Verb changed to incorrect tense form in `tr.pastTense`
- Whole-paragraph markup instead of word/phrase-level

---

## OVERALL SCORE

**Weights:**

| Dimension | Weight |
|---|---|
| source_faithfulness | 0.25 |
| edit_correctness_and_minimality | 0.30 |
| regulatory_writing_quality | 0.20 |
| tracked_changes_markup_correctness | 0.15 |
| internal_consistency | 0.10 |

[Rest of template unchanged.]
