# Archetype Scorer → Standard Prompt Dependency Map

This document maps each archetype benchmarking scorer to the standard prompts in the current library that it evaluates. It is the authoritative reference for which scorer to invoke when benchmarking a given prompt.

- **Library size:** 36 standard prompts
- **Archetype scorers:** 12
- **Coverage:** 36 / 36 (100%)

---

## 1. Summary Table

| Scorer # | Scorer Name | Prompt Count | Standard Prompt IDs |
|---|---|---|---|
| 1 | Summarization / Overview | 5 | `da.summarizeDoc`, `da.summarizeContent`, `da.summarizeChat`, `da.tldr`, `rv.summarize` |
| 2 | Extraction / Listing | 2 | `da.listData`, `ab.extract` |
| 3 | Definition / Explanation | 1 | `da.define` |
| 4 | Section Drafting from Source Data | 4 | `dr.section`, `dr.section.table`, `cn.draftSection`, `jp.draftSection` |
| 5 | Editing with Tracked Changes | 4 | `ed.grammar`, `ed.clarity`, `ed.streamline`, `tr.pastTense` |
| 6 | Consistency Check Within Document | 2 | `ed.consistency`, `ab.footnoteAbbr` |
| 7 | Formatting Transformation | 2 | `tr.tabulate`, `tr.mirrorFormat` |
| 8 | Data Updates from Source Tables | 7 | `up.tableNum`, `up.tableNum.tc`, `up.textNum`, `up.textNum.tc`, `up.tableEvent`, `up.tableEvent.tc`, `up.content` |
| 9 | Content QC Against Source | 1 | `qc.contentCheck` |
| 10 | Comment Review / Triage / Reply | 6 | `rv.triage`, `rv.triageTable`, `rv.agenda`, `rv.aiReview`, `rv.aiReply`, `rv.genericReply` |
| 11 | Translation | 2 | `cn.translate`, `jp.translate` |
| 12 | Multi-Step Workflow (STROBE) | 1 | `cn.strobe` |
| **Total** | | **36** | |

---

## 2. Detailed Mapping

### Scorer 1 — Summarization / Overview

**Rationale for grouping:** All five prompts generate condensed representations of source content (document, selection, conversation, or comments) with no transformation of underlying facts. Shared failure modes: fabricated facts, omitted key points, promotional tone, structural non-compliance.

| Prompt ID | Category | Prompt Title | Scope of Input |
|---|---|---|---|
| `da.summarizeDoc` | Document Analysis | Summarize document | Full document + attachments |
| `da.summarizeContent` | Document Analysis | Summarize content | Cursor selection |
| `da.summarizeChat` | Document Analysis | Summarize conversation | Conversation history |
| `da.tldr` | Document Analysis | Too long; didn't read (TL;DR) | Full document; typed template |
| `rv.summarize` | Review | Summarize comments | Document comments |

**Prompt-specific notes within archetype:**
- `da.tldr` carries an additional document-type-classification step; scorer dimension 4 (`structural_fit`) carries the weight for this.
- `rv.summarize` requires author attribution and separation of original comments vs. replies; captured in Elements to Check.

---

### Scorer 2 — Extraction / Listing

**Rationale for grouping:** Both prompts enumerate qualifying instances from source with verbatim fidelity. Shared failure modes: missed instances (recall), hallucinated instances (precision), non-verbatim definitions, format non-compliance.

| Prompt ID | Category | Prompt Title | Extracted Entity |
|---|---|---|---|
| `da.listData` | Document Analysis | List data instances | User-specified data category |
| `ab.extract` | Abbreviations | List of abbreviations | Abbreviations + definitions |

**Prompt-specific notes within archetype:**
- `ab.extract` has stricter formatting rules (alphabetical, two-column, no column headings, Latin italics, obsolete-entry exclusion). Scorer dimension 4 (`format_compliance`) encodes these.

---

### Scorer 3 — Definition / Explanation

**Rationale for grouping:** Singleton. Only prompt producing a short authoritative definition of a term. Ground truth is external regulatory/clinical consensus rather than attached source text.

| Prompt ID | Category | Prompt Title |
|---|---|---|
| `da.define` | Document Analysis | Define |

---

### Scorer 4 — Section Drafting from Source Data

**Rationale for grouping:** All four prompts generate full regulatory document sections (e.g., CSR sections) from attached source data tables and supporting documents, with strict traceability (`[VERIFY: definition not in source]` discipline).

| Prompt ID | Category | Prompt Title | Output Language | In-Text Table? |
|---|---|---|---|---|
| `dr.section` | Content Drafting | Draft [CSR] section | English | No |
| `dr.section.table` | Content Drafting | Draft [CSR] section with table | English | Yes (Bayer format) |
| `cn.draftSection` | China | Draft content in Mandarin | Mandarin (NMPA) | Possible |
| `jp.draftSection` | Japan | Draft content in Japanese | Japanese (PMDA) | Possible |

**Prompt-specific notes within archetype:**
- `dr.section.table` triggers Bayer table HTML spec enforcement in scorer dimension 4 (`format_fidelity`).
- `cn.draftSection` / `jp.draftSection` shift dimension 4 to target-language regulatory register (NMPA/PMDA) rather than Bayer table spec.

---

### Scorer 5 — Editing with Tracked Changes

**Rationale for grouping:** All four prompts perform meaning-preserving transformations on selected text with tracked-changes markup at smallest editable range. Shared failure modes: meaning drift, oversized change range, scope creep across edit types, unmarked edits.

| Prompt ID | Category | Prompt Title | Edit Type |
|---|---|---|---|
| `ed.grammar` | Content Editing & Improvement | Grammar | Grammar only (no style) |
| `ed.clarity` | Content Editing & Improvement | Make clearer | Clarity |
| `ed.streamline` | Content Editing & Improvement | Streamline complex sentence | Simplification / splitting |
| `tr.pastTense` | Content Transformation | Convert to past tense | Verb tense only |

**Prompt-specific notes within archetype:**
- `ed.grammar` requires `"No corrections needed."` output when nothing to fix; this is a critical failure if violated.
- `tr.pastTense` is more mechanical than the others; verb-tense correctness is the primary dimension 2 driver.

---

### Scorer 6 — Consistency Check Within Document

**Rationale for grouping:** Both prompts detect occurrences or discrepancies across a document and classify each (verbatim vs. non-verbatim; present vs. missing). Shared failure modes: missed occurrences, hallucinated occurrences, misclassification.

| Prompt ID | Category | Prompt Title | Target of Check |
|---|---|---|---|
| `ed.consistency` | Content Editing & Improvement | Phrasing consistency | Selected wording across document |
| `ab.footnoteAbbr` | Abbreviations | Table footnote abbreviations check | Abbreviations in in-text table footnote |

---

### Scorer 7 — Formatting Transformation

**Rationale for grouping:** Both prompts preserve source content verbatim while applying a target formatting specification. Shared failure modes: content alteration, format spec violation, commentary leakage.

| Prompt ID | Category | Prompt Title | Target Format Source |
|---|---|---|---|
| `tr.tabulate` | Content Transformation | Tabulate | Bayer table HTML spec |
| `tr.mirrorFormat` | Content Transformation | Mirror table format | Format of selected Table [x] |

---

### Scorer 8 — Data Updates from Source Tables

**Rationale for grouping:** All seven prompts update values or references in a text/table from provided source data tables. Shared failure modes: numeric drift, calculated/recalculated values, formatting destruction, tracked-changes mis-application, field-code format errors. **Highest-stakes archetype in the library** — a single wrong number is a regulatory risk and is treated as a critical failure.

| Prompt ID | Category | Prompt Title | Target | Tracked Changes? | Field Codes? |
|---|---|---|---|---|---|
| `up.tableNum` | Data & Content Updates | Update numbers in table | In-text table | No | Caption field codes |
| `up.tableNum.tc` | Data & Content Updates | Update numbers in table – TC | In-text table | Yes | Caption field codes (NOT tracked) |
| `up.textNum` | Data & Content Updates | Update numbers in text | Paragraph | No | Table/Figure cross-ref field codes |
| `up.textNum.tc` | Data & Content Updates | Update numbers in text – TC | Paragraph | Yes | Table/Figure cross-ref field codes (NOT tracked) |
| `up.tableEvent` | Data & Content Updates | Update event data in table | In-text table (events) | No | Caption field codes |
| `up.tableEvent.tc` | Data & Content Updates | Update event data in table – TC | In-text table (events) | Yes | Caption field codes (NOT tracked) |
| `up.content` | Data & Content Updates | Update content in text with references | Paragraph with refs | No | Reference styling (`#0000FF`) |

**Prompt-specific notes within archetype:**
- `.tc` variants add tracked-changes markup rules AND the critical exception that caption table numbers must use field-code format, never tracked changes. Scorer dimension 4 (`markup_and_fieldcode_compliance`) carries this.
- `up.tableEvent` / `up.tableEvent.tc` add entry-addition, threshold-based removal, and original-sort-order preservation rules.
- `up.content` is the only variant with reference color coding (`#0000FF`) and source document naming requirement.

---

### Scorer 9 — Content QC Against Source

**Rationale for grouping:** Singleton. Unique in the library because its output feeds directly into a downstream Word comment-bubble pipeline, making output format violations a critical failure (not just a dimension 4 penalty). Hybrid of verification (detection) and strict formatting (output).

| Prompt ID | Category | Prompt Title |
|---|---|---|
| `qc.contentCheck` | Quality Control | AI content QC |

---

### Scorer 10 — Comment Review / Triage / Reply

**Rationale for grouping:** All six prompts operate on document comments as primary input and produce either a classification (triage), a derived artifact (agenda), AI-authored comments, or AI replies. Shared failure modes: misclassification (MAJOR vs. MINOR; comment type), author misattribution, ungrounded replies, structural non-compliance in output tables.

| Prompt ID | Category | Prompt Title | Operation |
|---|---|---|---|
| `rv.triage` | Review | Triage comments by priority | Classification + table |
| `rv.triageTable` | Review | Comment triage table | Classification + proposed responses |
| `rv.agenda` | Review | Meeting agenda from triage | Filtered table from triage output |
| `rv.aiReview` | Review | AI document review | AI-authored comments |
| `rv.aiReply` | Review | AI comment replies | AI-authored replies (25–50 words) |
| `rv.genericReply` | Review | Kind reminder to implement | Verbatim boilerplate reply |

**Prompt-specific notes within archetype:**
- `rv.genericReply` requires verbatim use of the generic text; any deviation = critical failure.
- `rv.triage` and `rv.triageTable` have distinct column specs; scorer dimension 4 (`output_structure_compliance`) applies the correct spec per prompt.
- `rv.agenda` critical failure includes any row with status other than "Needs Discussion" or "Needs Clarification".
- `rv.aiReview` must state the AI role in each comment.

---

### Scorer 11 — Translation

**Rationale for grouping:** Both prompts perform content-preserving translation into a target language with the appropriate target-market regulatory register. Shared failure modes: semantic drift, numeric/dose/drug-name alteration, inappropriate register, formatting loss.

| Prompt ID | Category | Prompt Title | Target Language | Target Register |
|---|---|---|---|---|
| `cn.translate` | China | Translate to Mandarin | Mandarin (Simplified) | NMPA |
| `jp.translate` | Japan | Translate to Japanese | Japanese | PMDA |

**Note:** This scorer reframes dimension 3 as `target_language_regulatory_register` in place of the generic `regulatory_writing_quality`.

---

### Scorer 12 — Multi-Step Workflow (STROBE)

**Rationale for grouping:** Singleton. The only prompt in the library implementing a sequential, variable-gated workflow (variable intake → confirmation → Steps 1–4 execution). Dimension 4 is omitted and weights redistributed.

| Prompt ID | Category | Prompt Title |
|---|---|---|
| `cn.strobe` | China | MA STROBE |

---

## 3. Reverse Index — Prompt → Scorer

For quick lookup when benchmarking a specific prompt.

| Prompt ID | Scorer |
|---|---|
| `ab.extract` | Scorer 2 — Extraction / Listing |
| `ab.footnoteAbbr` | Scorer 6 — Consistency Check |
| `cn.draftSection` | Scorer 4 — Section Drafting |
| `cn.strobe` | Scorer 12 — Multi-Step Workflow |
| `cn.translate` | Scorer 11 — Translation |
| `da.define` | Scorer 3 — Definition / Explanation |
| `da.listData` | Scorer 2 — Extraction / Listing |
| `da.summarizeChat` | Scorer 1 — Summarization |
| `da.summarizeContent` | Scorer 1 — Summarization |
| `da.summarizeDoc` | Scorer 1 — Summarization |
| `da.tldr` | Scorer 1 — Summarization |
| `dr.section` | Scorer 4 — Section Drafting |
| `dr.section.table` | Scorer 4 — Section Drafting |
| `ed.clarity` | Scorer 5 — Editing with Tracked Changes |
| `ed.consistency` | Scorer 6 — Consistency Check |
| `ed.grammar` | Scorer 5 — Editing with Tracked Changes |
| `ed.streamline` | Scorer 5 — Editing with Tracked Changes |
| `jp.draftSection` | Scorer 4 — Section Drafting |
| `jp.translate` | Scorer 11 — Translation |
| `qc.contentCheck` | Scorer 9 — Content QC |
| `rv.agenda` | Scorer 10 — Comment Review |
| `rv.aiReply` | Scorer 10 — Comment Review |
| `rv.aiReview` | Scorer 10 — Comment Review |
| `rv.genericReply` | Scorer 10 — Comment Review |
| `rv.summarize` | Scorer 1 — Summarization |
| `rv.triage` | Scorer 10 — Comment Review |
| `rv.triageTable` | Scorer 10 — Comment Review |
| `tr.mirrorFormat` | Scorer 7 — Formatting Transformation |
| `tr.pastTense` | Scorer 5 — Editing with Tracked Changes |
| `tr.tabulate` | Scorer 7 — Formatting Transformation |
| `up.content` | Scorer 8 — Data Updates |
| `up.tableEvent` | Scorer 8 — Data Updates |
| `up.tableEvent.tc` | Scorer 8 — Data Updates |
| `up.tableNum` | Scorer 8 — Data Updates |
| `up.tableNum.tc` | Scorer 8 — Data Updates |
| `up.textNum` | Scorer 8 — Data Updates |
| `up.textNum.tc` | Scorer 8 — Data Updates |

---

## 4. Prompts with In-Scorer Overrides

The following prompts carry explicit prompt-specific overrides inside their archetype scorer (rather than being split into a dedicated scorer). This is the "hybrid, archetype-primary" model recommended in the preceding analysis.

| Prompt ID | Scorer | Override Location |
|---|---|---|
| `da.tldr` | Scorer 1 | Dimension 4 (`structural_fit`) + document-type-classification critical failure |
| `ab.extract` | Scorer 2 | Dimension 4 (`format_compliance`) — alphabetical sort, two-column, no headings, Latin italics, obsolete exclusion |
| `dr.section.table` | Scorer 4 | Dimension 4 (`format_fidelity`) — Bayer table HTML spec |
| `cn.draftSection` / `jp.draftSection` | Scorer 4 | Dimension 4 (`format_fidelity`) reframed as NMPA/PMDA register |
| `ed.grammar` | Scorer 5 | Critical failure if `"No corrections needed."` not returned when applicable |
| `up.tableNum.tc` / `up.textNum.tc` / `up.tableEvent.tc` | Scorer 8 | Dimension 4 (`markup_and_fieldcode_compliance`) — tracked-changes + field-code rules |
| `up.tableEvent` / `up.tableEvent.tc` | Scorer 8 | Entry-addition, threshold removal, sort-order preservation rules |
| `up.content` | Scorer 8 | Reference color coding (`#0000FF`) + source document naming |
| `rv.genericReply` | Scorer 10 | Critical failure if generic text not used verbatim |
| `rv.agenda` | Scorer 10 | Critical failure if status filter not applied |
