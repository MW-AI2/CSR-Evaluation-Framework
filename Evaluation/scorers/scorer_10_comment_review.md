# Scorer 10 — Comment Review / Triage / Reply

**Applies to:** `rv.triage`, `rv.triageTable`, `rv.agenda`, `rv.aiReview`, `rv.aiReply`, `rv.genericReply`

---

## Scorer: Comment Review / Triage / Reply

[PURPOSE: determine whether GENERATED_TEXT (1) accurately represents the underlying comments and document content, (2) correctly classifies and/or replies per the task's rules (MAJOR vs. MINOR; Standard/Conflicting/Ambiguous/Discussion; `[S]`/`[R]` tagging; 25–50 word replies), (3) is written in appropriate regulatory review register, (4) complies with the required output structure (table columns, section numbering, color coding), (5) is internally consistent across rows.]

---

## INPUTS

### SOURCE_TEXT
The document under review.

### DOCUMENT_COMMENTS
The set of comments (and replies, for `rv.aiReply`) being triaged, replied to, or summarized. Primary input for classification and reply tasks.

### GENERATED_TEXT
The triage table, agenda, AI review comments, or replies.

### TARGET_DETAIL_LEVEL
Standard

### OPTIONAL_REFERENCE_TEXT
A manually prepared triage/reply (if available).

---

## ELEMENTS TO CHECK

- Classification correct per task definitions (MAJOR = content/regulatory; MINOR = style/clarity; Comment Type categories; Resolved/Unresolved)
- Author attribution correct
- Section reference correct (lowest section level)
- Table columns match spec exactly (`rv.triage`: Category, Author, Comment Summary, Reason, Section, Resolved/Unresolved; `rv.triageTable`: Section no. & Heading, Reviewer(s), Comment Type, Original Comment, Proposed Response/Solution, Status)
- Unresolved comments shown first; "Unresolved" in `#e09d0d`
- Replies ≤50 words; begin with key decision/action
- `[S]` / `[R]` tags applied where applicable
- Replies grounded only in document / referenced source materials
- `rv.genericReply`: generic text used verbatim
- `rv.agenda`: only "Needs Discussion" and "Needs Clarification" rows included; grouped by category

---

## DIMENSION 2: CLASSIFICATION_AND_REPLY_ACCURACY (0–5)

- **5** = all classifications/replies correct and well-grounded; `[S]`/`[R]` applied correctly; word limits respected
- **4** = one minor misclassification or one slightly over-length reply
- **3** = one moderate misclassification (e.g., a safety comment classified as MINOR)
- **2** = multiple misclassifications or ungrounded replies
- **1** = systemic errors
- **0** = unreliable

## DIMENSION 4: OUTPUT_STRUCTURE_COMPLIANCE (0–5)

- **5** = table columns and formatting match spec exactly; color coding, ordering, grouping all correct
- **4** = minor formatting deviation
- **3** = one moderate structural deviation
- **2** = multiple deviations
- **1** = structure largely wrong
- **0** = unusable

---

## CRITICAL FAILURE RULES

- Safety-relevant comment classified as MINOR without `[S]` tag
- Regulatory-compliance comment classified as MINOR without `[R]` tag
- Reply introduces content not in document or referenced source
- `rv.agenda` includes rows with status other than "Needs Discussion" or "Needs Clarification"
- Author misattribution

---

## OVERALL SCORE

**Weights:**

| Dimension | Weight |
|---|---|
| source_faithfulness | 0.30 |
| classification_and_reply_accuracy | 0.30 |
| regulatory_writing_quality | 0.15 |
| output_structure_compliance | 0.15 |
| internal_consistency | 0.10 |

[Rest of template unchanged.]
