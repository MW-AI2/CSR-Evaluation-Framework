# Scorer 6 — Consistency Check Within Document

**Applies to:** `ed.consistency`, `ab.footnoteAbbr`

---

## Scorer: Consistency Check Within Document

[PURPOSE: determine whether GENERATED_TEXT (1) correctly identifies all occurrences / discrepancies, (2) correctly classifies each (verbatim vs. non-verbatim; missing vs. extra; in-order vs. out-of-order), (3) presents findings in the specified output structure, (4) uses tracked changes to highlight non-verbatim differences, (5) is internally consistent.]

---

## INPUTS

### SOURCE_TEXT
The selected wording (`ed.consistency`) or the in-text table (`ab.footnoteAbbr`).

### DOCUMENT_FULL_TEXT
The full document used as the reference search space.

### GENERATED_TEXT
The consistency-check report (table of occurrences, or list of abbreviation discrepancies).

### TARGET_DETAIL_LEVEL
Standard

### OPTIONAL_REFERENCE_TEXT
A manually produced consistency check (if available).

---

## ELEMENTS TO CHECK

- All occurrences identified (recall)
- No non-occurrences flagged (precision)
- Verbatim vs. non-verbatim classification correct
- Non-verbatim differences highlighted with tracked changes
- Location pinpointed (section/paragraph)
- For `ab.footnoteAbbr`: correct detection of missing-from-footnote, extra-in-footnote, and non-alphabetical order
- Only inconsistencies listed (not confirmations)

---

## DIMENSION 2: DETECTION_RECALL_AND_PRECISION (0–5)

- **5** = all true occurrences/discrepancies found, no false positives
- **4** = one minor miss or one minor false positive
- **3** = one moderate miss or one moderate false positive
- **2** = multiple misses or false positives
- **1** = largely unreliable detection
- **0** = detection fundamentally wrong

## DIMENSION 4: OUTPUT_STRUCTURE_COMPLIANCE (0–5)

- **5** = output matches the required structure exactly (table columns, tracked-changes markup for non-verbatim, correct exclusion of confirmations)
- **4** = minor deviation
- **3** = one moderate deviation (missing column, missing tracked changes on non-verbatim rows)
- **2** = multiple deviations
- **1** = structure largely wrong
- **0** = unusable

---

## CRITICAL FAILURE RULES

- A real non-verbatim occurrence misclassified as verbatim (meaning drift risk)
- Missing-from-footnote abbreviation not detected (`ab.footnoteAbbr`)
- Hallucinated occurrence that does not exist in the document

---

## OVERALL SCORE

**Weights:**

| Dimension | Weight |
|---|---|
| source_faithfulness | 0.30 |
| detection_recall_and_precision | 0.35 |
| regulatory_writing_quality | 0.10 |
| output_structure_compliance | 0.15 |
| internal_consistency | 0.10 |

[Rest of template unchanged.]
