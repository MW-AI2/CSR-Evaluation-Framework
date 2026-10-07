# Scorer 8 — Data Updates from Source Tables

**Applies to:** `up.tableNum`, `up.tableNum.tc`, `up.textNum`, `up.textNum.tc`, `up.tableEvent`, `up.tableEvent.tc`, `up.content`

---

## Scorer: Data Updates from Source Tables

[PURPOSE: determine whether GENERATED_TEXT (1) accurately reflects source table values with zero numeric drift, (2) applies updates only where source data differs, (3) preserves original formatting, (4) correctly handles tracked changes and field codes per the variant's rules, (5) is internally consistent (narrative numbers vs. table numbers vs. footnote references).]

---

## INPUTS

### SOURCE_TEXT
The pre-update text or table (what the user selected).

### SOURCE_DATA_TABLES
The provided source data tables. Co-equal with SOURCE_TEXT as ground truth for numeric values — SOURCE_DATA_TABLES takes precedence for data facts.

### GENERATED_TEXT
The updated text/table with (for `.tc` variants) tracked changes.

### TARGET_DETAIL_LEVEL
Standard

### OPTIONAL_REFERENCE_TEXT
A human-updated version (if available).

---

## ELEMENTS TO CHECK

- Every updated value matches SOURCE_DATA_TABLES exactly (no calculations, no recalculated percentages)
- No value changed where source matches original
- Source data table number updated in footnote (table variants) or in parentheses (text variants)
- Original formatting (font color, % style, cell structure) preserved
- For `.tc` variants: tracked-changes markup applied ONLY to values that changed; NOT applied to numerically identical values; NOT applied to field codes
- For caption table numbers in `.tc` variants: field code format applied, NOT tracked changes
- Field code format for Table/Figure cross-references in `up.textNum` / `up.textNum.tc`: word "Table" or "Figure" inside the span, double backslashes preserved
- For `up.tableEvent` / `up.tableEvent.tc`: new entries added without overwriting existing; threshold-based removal applied; original sort order preserved
- For `up.content`: references in `#0000FF`; source document name mentioned

---

## DIMENSION 2: DATA_ACCURACY (0–5)

- **5** = every value matches source exactly; no spurious changes; no calculated or inferred values
- **4** = one minor label-level mismatch; all numbers correct
- **3** = one moderate value drift (e.g., wrong decimal, wrong row updated)
- **2** = multiple value drifts or any calculated value
- **1** = systemic data unreliability
- **0** = data wrong

## DIMENSION 4: MARKUP_AND_FIELDCODE_COMPLIANCE (0–5)

- **5** = tracked changes applied correctly only where values changed; field code format applied correctly to caption table numbers and cross-refs; double backslashes preserved
- **4** = minor markup deviation
- **3** = one moderate issue (e.g., tracked changes applied to a numerically identical value, or field code missing on one cross-ref)
- **2** = multiple issues (e.g., tracked changes applied to caption table number instead of field code)
- **1** = systemic markup failure
- **0** = unusable

---

## CRITICAL FAILURE RULES

- ANY numeric value does not match SOURCE_DATA_TABLES (single wrong number = critical failure)
- Calculated or recalculated value introduced
- For `.tc` variants: tracked changes applied to a value that did not change, OR applied to caption table number instead of field code
- Field code span missing the word "Table"/"Figure" inside it
- Original formatting destroyed
- For `up.tableEvent` variants: existing entry overwritten instead of retained

---

## OVERALL SCORE

**Weights:**

| Dimension | Weight |
|---|---|
| source_faithfulness | 0.45 |
| data_accuracy | 0.30 |
| regulatory_writing_quality | 0.05 |
| markup_and_fieldcode_compliance | 0.10 |
| internal_consistency | 0.10 |

[Rest of template unchanged.]
