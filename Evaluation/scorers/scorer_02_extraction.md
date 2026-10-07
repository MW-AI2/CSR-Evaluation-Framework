# Scorer 2 — Extraction / Listing

**Applies to:** `da.listData`, `ab.extract`

---

## Scorer: Extraction / Listing Outputs

[Preamble, PURPOSE adapted: determine whether GENERATED_TEXT is (1) factually grounded, (2) exhaustive in extracting all qualifying instances, (3) regulatorily appropriate, (4) consistent with the extraction rules in the system prompt (e.g., alphabetical order, verbatim definitions, two-column format for `ab.extract`), (5) safe to use.]

---

## INPUTS

### SOURCE_TEXT
The full document from which instances are being extracted. Primary ground truth.

### EXTRACTION_RULES
The system-prompt-defined rules for what qualifies for inclusion and how to format each entry (e.g., `ab.extract` rules on alphabetical sorting, verbatim definitions, Latin italics, no column headings; `da.listData` rules on scope of the requested data category).

### GENERATED_TEXT
The extracted list or table.

### TARGET_DETAIL_LEVEL
Standard

### OPTIONAL_REFERENCE_TEXT
A human-curated list (if available).

---

## ELEMENTS TO CHECK

- Every qualifying instance in SOURCE_TEXT is included
- No non-qualifying or invented instances included
- Definitions / data values reproduced verbatim from source
- Formatting rules followed (alphabetical order, column structure, no spurious headers, Latin italics where applicable)
- Obsolete entries (per `ab.extract` rules) correctly excluded
- No duplicates

---

## DIMENSION 2: EXTRACTION_COMPLETENESS_AND_PRECISION (0–5)

**Question:** Are all qualifying instances present (recall), and are only qualifying instances present (precision), with verbatim fidelity?

- **5** = complete recall and precision; all entries verbatim
- **4** = one minor miss or one minor spurious entry; verbatim intact
- **3** = one moderate miss OR one non-verbatim definition
- **2** = multiple misses, multiple spurious entries, or multiple verbatim violations
- **1** = large recall or precision gap
- **0** = extraction fundamentally unreliable

## DIMENSION 4: FORMAT_COMPLIANCE (0–5)

**Question:** Does the output comply with the formatting rules in EXTRACTION_RULES (sort order, column structure, absence of column headings where specified, HTML cleanliness, no markdown)?

- **5** = fully compliant
- **4** = one minor deviation (e.g., spacing)
- **3** = one moderate deviation (e.g., sort order off for a few entries)
- **2** = multiple deviations or wrong structure
- **1** = largely non-compliant
- **0** = format unusable

---

## CRITICAL FAILURE RULES

- Hallucinated abbreviation/definition not in source
- More than one abbreviation present in source but missing from extraction (for `ab.extract` — these propagate into regulatory documents)
- Wrong format type returned (e.g., markdown instead of HTML table)
- Obsolete entries carried through unchanged

---

## OVERALL SCORE

**Weights:**

| Dimension | Weight |
|---|---|
| source_faithfulness | 0.35 |
| extraction_completeness_and_precision | 0.30 |
| regulatory_writing_quality | 0.10 |
| format_compliance | 0.15 |
| internal_consistency | 0.10 |

[Rest of template unchanged.]
