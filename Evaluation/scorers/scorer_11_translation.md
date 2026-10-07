# Scorer 11 — Translation (Mandarin / Japanese)

**Applies to:** `cn.translate`, `jp.translate`

---

## Scorer: Translation (Mandarin / Japanese)

[PURPOSE: determine whether GENERATED_TEXT (1) faithfully conveys all source meaning without factual drift, (2) uses accurate target-language terminology, (3) uses appropriate target-market regulatory register (NMPA for Mandarin; PMDA for Japanese), (4) preserves the original formatting and structure, (5) is internally consistent.]

---

## INPUTS

### SOURCE_TEXT
The source-language content to be translated.

### TARGET_REGULATORY_REGISTER
- **Mandarin:** NMPA regulatory submission register.
- **Japanese:** PMDA regulatory submission register.

### GENERATED_TEXT
The translated content.

### TARGET_DETAIL_LEVEL
Standard

### OPTIONAL_REFERENCE_TEXT
A human translation (if available).

---

## ELEMENTS TO CHECK

- Full semantic coverage (no omissions)
- No invented content
- Numbers, drug names, abbreviations, and units preserved exactly
- Target-language terminology matches regulatory usage (NMPA/PMDA)
- Original formatting and structure preserved (headings, bullets, paragraphs, tables)
- No source-language fragments left untranslated (unless deliberately preserved per convention, e.g., brand names)

---

## DIMENSION 2: TRANSLATION_FIDELITY (0–5)

- **5** = complete semantic coverage; no factual drift; terminology accurate
- **4** = minor terminology drift
- **3** = one moderate terminology error or minor omission
- **2** = multiple errors or one material omission
- **1** = translation unreliable
- **0** = translation wrong

## DIMENSION 3 (reframed): TARGET_LANGUAGE_REGULATORY_REGISTER (0–5)

(Replaces generic REGULATORY_WRITING_QUALITY for this scorer.)

- **5** = fully appropriate NMPA/PMDA register
- **4** = minor register deviation
- **3** = noticeable register issue (e.g., too colloquial)
- **2** = multiple register issues
- **1** = inappropriate register
- **0** = unusable for submission

## DIMENSION 4: FORMATTING_PRESERVATION (0–5)

- **5** = all formatting preserved exactly
- **4** = minor deviation
- **3** = one moderate deviation
- **2** = multiple deviations
- **1** = structure largely lost
- **0** = unusable

---

## CRITICAL FAILURE RULES

- Factual drift (number, dose, drug name, endpoint changed)
- Omission of a regulatorily material sentence
- Register inappropriate for NMPA/PMDA submission
- Formatting destroyed

---

## OVERALL SCORE

**Weights:**

| Dimension | Weight |
|---|---|
| source_faithfulness | 0.40 |
| translation_fidelity | 0.30 |
| target_language_regulatory_register | 0.15 |
| formatting_preservation | 0.10 |
| internal_consistency | 0.05 |

[Rest of template unchanged, with `"regulatory_writing_quality"` in the JSON renamed to `"target_language_regulatory_register"`.]
