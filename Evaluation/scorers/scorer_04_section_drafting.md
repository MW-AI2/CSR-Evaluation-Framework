# Scorer 4 — Section Drafting from Source Data

**Applies to:** `dr.section`, `dr.section.table`, `cn.draftSection`, `jp.draftSection`

---

## Scorer: Section Drafting from Source Data

[PURPOSE: determine whether GENERATED_TEXT is (1) traceable to source documents and tables, (2) complete in covering required section elements at Standard detail, (3) written in lean regulatory medical writing style, (4) compliant with `[VERIFY: ...]` discipline for undefined abbreviations AND (for `dr.section.table`) with Bayer table formatting, (5) internally consistent across narrative and any in-text table.]

---

## INPUTS

### SOURCE_TEXT
The attached data tables and supporting documents from which the section is drafted. Primary ground truth. Every claim must be traceable here.

### SECTION_TEMPLATE_EXPECTATIONS
Expected section elements (narrative structure, required subsections, in-text table requirements per template). For `dr.section.table`, also includes the Bayer table formatting specification.

### GENERATED_TEXT
The drafted section.

### TARGET_DETAIL_LEVEL
Standard

### OPTIONAL_REFERENCE_TEXT
An approved section exemplar (if available).

---

## ELEMENTS TO CHECK

- Every data point, abbreviation, and term traceable to SOURCE_TEXT
- Undefined abbreviations retained verbatim with `[VERIFY: definition not in source]` appended (not expanded by inference)
- Required section elements per template present at Standard detail
- Lean medical writing style: concise, objective, non-promotional, interpretation only where source supports it
- For `dr.section.table`: in-text table present where template requires; Bayer table HTML structure correctly applied (`MsoNormalTable` class, caption styling, column header styling, row header styling, footnote styling, correct border colors `#000000`, source citations in `#0000FF`, `lang` attribute)
- For `cn.draftSection` / `jp.draftSection`: NMPA/PMDA register maintained while traceability preserved

---

## DIMENSION 2: SECTION_COMPLETENESS_AND_TRACEABILITY (0–5)

- **5** = all required elements present; every claim traceable; `[VERIFY: ...]` used correctly where applicable
- **4** = complete with minor traceability drift
- **3** = one moderate gap (missing subsection or one untraceable claim)
- **2** = multiple gaps or an inferred abbreviation expansion not supported by source
- **1** = major traceability failure
- **0** = unsafe to use

## DIMENSION 4: FORMAT_FIDELITY (0–5)

For `dr.section.table`: Bayer table HTML spec compliance.
For `dr.section` / `cn.draftSection` / `jp.draftSection`: narrative formatting and (for cn/jp) target-language register fidelity.

- **5** = fully compliant
- **4** = minor formatting deviation
- **3** = one moderate deviation (e.g., wrong footnote style, missing `lang` attribute)
- **2** = multiple deviations or wrong overall structure
- **1** = largely non-compliant
- **0** = unusable

---

## CRITICAL FAILURE RULES

- Numeric data point fabricated or not traceable to a source table
- Abbreviation expanded by inference without `[VERIFY: ...]` when definition not in source
- Primary endpoint result or safety conclusion misstated vs. source
- For `dr.section.table`: Bayer table structure materially broken (wrong table tag, missing caption row, missing footnote row)
- For cn/jp drafts: translation-induced factual drift from source

---

## OVERALL SCORE

**Weights:**

| Dimension | Weight |
|---|---|
| source_faithfulness | 0.40 |
| section_completeness_and_traceability | 0.25 |
| regulatory_writing_quality | 0.15 |
| format_fidelity | 0.10 |
| internal_consistency | 0.10 |

[Rest of template unchanged.]
