# Scorer 3 — Definition / Explanation

**Applies to:** `da.define`

---

## Scorer: Definition / Explanation Outputs

[PURPOSE: determine whether GENERATED_TEXT is (1) factually correct, (2) contextually appropriate for pharmaceutical/regulatory medical writing, (3) appropriately scoped (2–4 sentences per the system prompt), (4) consistent with ICH/FDA/EMA framing where applicable, (5) safe to use.]

---

## INPUTS

### SOURCE_TEXT
The term or concept to be defined (the user's selection). Primary input, but the "ground truth" is established regulatory/clinical consensus knowledge for the term.

### REGULATORY_CONTEXT_REFERENCE
ICH / FDA / EMA definitions or guidance where the term has a formal regulatory meaning. Use to verify accuracy and detect oversimplification.

### GENERATED_TEXT
The definition or explanation.

### TARGET_DETAIL_LEVEL
Standard

### OPTIONAL_REFERENCE_TEXT
A reference definition from an authoritative glossary (if available).

---

## ELEMENTS TO CHECK

- Definition is accurate per regulatory/clinical consensus
- Regulatory context (ICH/FDA/EMA) mentioned when the term carries formal regulatory meaning
- Length is 2–4 sentences unless concept warrants more
- No oversimplification that changes meaning
- No introduction of unrelated concepts

---

## DIMENSION 2: DEFINITIONAL_ACCURACY (0–5)

- **5** = accurate and appropriately scoped; regulatory context noted where relevant
- **4** = accurate; minor missing context
- **3** = one moderate inaccuracy or missing regulatory context on a term where it is material
- **2** = multiple inaccuracies or materially misleading simplification
- **1** = largely incorrect
- **0** = wrong definition

## DIMENSION 4: SCOPE_FIT (0–5)

**Question:** Does the length and specificity match the "2–4 sentences unless required otherwise" scoping rule?

- **5** = well-scoped
- **4** = slightly long or short
- **3** = noticeably off-scope
- **2** = substantially off-scope
- **1** = far off-scope
- **0** = unusable

---

## CRITICAL FAILURE RULES

- Wrong definition (e.g., defining AE as SAE)
- Regulatory context stated incorrectly (e.g., misattributing an ICH definition)
- Fabricated regulatory citation

---

## OVERALL SCORE

**Weights:**

| Dimension | Weight |
|---|---|
| source_faithfulness (reinterpreted as "accuracy against established regulatory/clinical knowledge") | 0.40 |
| definitional_accuracy | 0.25 |
| regulatory_writing_quality | 0.15 |
| scope_fit | 0.10 |
| internal_consistency | 0.10 |

[Rest of template unchanged.]
