# Scorer 7 — Formatting Transformation

**Applies to:** `tr.tabulate`, `tr.mirrorFormat`

---

## Scorer: Formatting Transformation

[PURPOSE: determine whether GENERATED_TEXT (1) preserves source content verbatim, (2) applies the target formatting (Bayer spec for `tr.tabulate`; Table [x]'s format for `tr.mirrorFormat`), (3) uses appropriate regulatory presentation, (4) complies with HTML structure requirements, (5) is internally consistent.]

---

## INPUTS

### SOURCE_TEXT
The content to be reformatted (text selection for `tr.tabulate`; Table [y] for `tr.mirrorFormat`). Content ground truth — must be preserved verbatim.

### FORMATTING_SPEC
Bayer table formatting rules (`tr.tabulate`) OR the formatting of Table [x] (`tr.mirrorFormat`). The reference standard.

### GENERATED_TEXT
The reformatted HTML table.

### TARGET_DETAIL_LEVEL
Standard

### OPTIONAL_REFERENCE_TEXT
A manually formatted exemplar (if available).

---

## ELEMENTS TO CHECK

- All source content preserved verbatim (no additions, deletions, corrections)
- Bayer table structure (`tr.tabulate`): `MsoNormalTable` class; caption row with `colspan` + `MsoCaption`; column headers with correct styling and classes (`BayerTableColumnHeadings` / `BayerTableStyleLeftJustified`); data cells with `BayerTableRowHeadings` / `BayerTableStyleLeftJustified`; footnote row with `BayerTableFootnote`; borders replaced from `"windowtext"` to `#000000`; citations in `#0000FF`; `lang="EN-US"`
- Mirrored format (`tr.mirrorFormat`): column widths, header styling, shading, borders, cell padding, alignment, number formatting all mirrored from Table [x]
- No commentary in output
- Output is a single HTML table

---

## DIMENSION 2: FORMAT_FIDELITY (0–5)

- **5** = fully compliant with FORMATTING_SPEC
- **4** = minor deviation (e.g., missing `lang` attribute on one span)
- **3** = one moderate deviation (e.g., incorrect footnote class, wrong border color)
- **2** = multiple deviations or wrong overall structure
- **1** = largely non-compliant
- **0** = unusable

## DIMENSION 4: CONTENT_PRESERVATION (0–5)

- **5** = all content verbatim, nothing added or removed
- **4** = cosmetic whitespace drift only
- **3** = one moderate content change (e.g., corrected a number or label)
- **2** = multiple content changes
- **1** = substantive content loss or addition
- **0** = content unreliable

---

## CRITICAL FAILURE RULES

- Any content from source modified, corrected, or omitted
- Commentary included in output
- Wrong overall table structure (not a single HTML table)
- Bayer-required classes absent on all cells

---

## OVERALL SCORE

**Weights:**

| Dimension | Weight |
|---|---|
| source_faithfulness | 0.30 |
| format_fidelity | 0.30 |
| regulatory_writing_quality | 0.05 |
| content_preservation | 0.25 |
| internal_consistency | 0.10 |

[Rest of template unchanged.]
