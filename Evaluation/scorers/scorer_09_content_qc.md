# Scorer 9 — Content QC Against Source

**Applies to:** `qc.contentCheck`

---

## Scorer: Content QC Against Source

[PURPOSE: determine whether GENERATED_TEXT (1) correctly identifies all real discrepancies between paragraph and source tables (recall), (2) does NOT flag non-discrepancies (precision), (3) uses the required output format exactly, (4) correctly uses `"Unable to verify - no source found"` where appropriate, (5) is internally consistent.]

---

## INPUTS

### SOURCE_TEXT
The paragraph under QC.

### SOURCE_DATA_TABLES
The provided source data tables. Ground truth for all numeric values.

### GENERATED_TEXT
The QC findings output.

### TARGET_DETAIL_LEVEL
Standard

### OPTIONAL_REFERENCE_TEXT
A manual QC pass (if available).

---

## ELEMENTS TO CHECK

- Every real discrepancy identified
- No non-discrepancy flagged
- No "correct" confirmations included
- Each finding on its own line, separated by exactly three line breaks
- Each finding in exact format: `*Qualifier and incorrect value -> correct value (Table number)*`
- Shortest qualifier that uniquely identifies the metric
- No output thinking, commentary, headers, or justification outside the format
- If no discrepancies: `*AI QC performed, no findings*` (and nothing else)
- `"Unable to verify - no source found"` used when semantic match absent
- No calculations performed to derive values
- No style/spelling/capitalization/grammar flagged
- In-text references to Sections, Listings, and 2-numeral Tables/Figures NOT checked; references to 3+ numeral tables ARE checked

---

## DIMENSION 2: DISCREPANCY_DETECTION_ACCURACY (0–5)

- **5** = all real discrepancies found, no false positives, no missed "Unable to verify" cases
- **4** = one minor false positive or minor miss
- **3** = one moderate miss OR one moderate false positive
- **2** = multiple misses or false positives
- **1** = detection unreliable
- **0** = detection fundamentally wrong

## DIMENSION 4: OUTPUT_FORMAT_DISCIPLINE (0–5)

- **5** = every finding in exact format; exactly three line breaks between findings; no commentary; no confirmations
- **4** = minor spacing deviation
- **3** = one finding mis-formatted or one commentary line present
- **2** = multiple format deviations
- **1** = output format largely wrong
- **0** = format breaks downstream commenting

---

## CRITICAL FAILURE RULES

- False negative on a real numeric discrepancy
- Hallucinated discrepancy (value flagged that actually matches source)
- Calculated value used to derive a "finding"
- Format deviation that would break the downstream comment-bubble pipeline (e.g., multi-finding single line, commentary interspersed, wrong separator) — critical because this prompt feeds directly into Word comment bubbles
- Style/spelling/grammar flagged as a discrepancy

---

## OVERALL SCORE

**Weights:**

| Dimension | Weight |
|---|---|
| source_faithfulness | 0.40 |
| discrepancy_detection_accuracy | 0.30 |
| regulatory_writing_quality | 0.05 |
| output_format_discipline | 0.15 |
| internal_consistency | 0.10 |

[Rest of template unchanged.]
