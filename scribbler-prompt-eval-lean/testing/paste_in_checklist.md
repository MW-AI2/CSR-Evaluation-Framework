# Scribbler 2.0 Prototype — Per-Scorer Paste-In Checklist

Use this for the manual prototype evaluation loop:
**Generation** (run the standard prompt in Scribbler against a representative source) →
**Assembly** (paste the Scribbler output into the matching consolidated scorer as GENERATED_TEXT) →
**Scoring** (paste the assembled scorer into a *fresh* Scribbler session with the source selected/attached).

Rules that apply to every scorer:
- The **scoring session must be a brand-new Scribbler conversation** with no residual context from the generation session.
- In the scoring session, **select the source document in Word and attach any reference files** named below. The scorer reads these as SOURCE_TEXT / SOURCE_DATA_TABLES / FORMATTING_SPEC; they are **not** pasted into the template.
- **Only the Scribbler output is pasted** into the scorer, between the `<<<PASTE SCRIBBLER OUTPUT HERE>>>` markers.
- The scorer returns its JSON inside a single `<pre><code>` block; copy that block out as the evaluation record.
- The **generation context profile must mirror production** for the prompt, or the generated output is not representative.

Legend for "Select in Word": **Full doc** = whole open document; **Selection** = highlight the specific range/table/paragraph; **Comments** = document must contain the review comments.

---

## Scorer 1 — Summarization / Overview
Prompts: `da.summarizeDoc`, `da.summarizeContent`, `da.summarizeChat`, `da.tldr`, `rv.summarize`

| Prompt | Generation context profile | Paste as GENERATED_TEXT | Scoring session: select in Word | Attach as files |
|---|---|---|---|---|
| da.summarizeDoc | Full doc open | The summary output | Full doc (the summarized document) | — |
| da.summarizeContent | A selection highlighted | The summary output | The same selection | — |
| da.summarizeChat | A Scribbler conversation present | The summary output | The conversation text as the source | — |
| da.tldr | Full doc open (document-type matters) | The TL;DR output | Full doc | Document-type conventions (DOCUMENT_TYPE_CONVENTIONS) as an attached reference |
| rv.summarize | Doc with comments | The comment summary | Full doc **with comments visible** | — |

Note: STRUCTURAL_FIT is scored only for `da.tldr`; attach the document-type template for it.

---

## Scorer 2 — Extraction / Listing
Prompts: `da.listData`, `ab.extract`

| Prompt | Generation context profile | Paste as GENERATED_TEXT | Scoring session: select in Word | Attach as files |
|---|---|---|---|---|
| da.listData | Full doc open; data category specified in prompt | The extracted list | Full doc | The EXTRACTION_RULES (data category + scope) if held separately |
| ab.extract | Full doc open | The abbreviation list/table | Full doc | The `ab.extract` formatting rules (alphabetical, two-column, Latin italics, obsolete-exclusion) as EXTRACTION_RULES |

---

## Scorer 3 — Definition / Explanation
Prompt: `da.define`

| Prompt | Generation context profile | Paste as GENERATED_TEXT | Scoring session: select in Word | Attach as files |
|---|---|---|---|---|
| da.define | Term highlighted as selection | The definition | The term (selection) | **REGULATORY_CONTEXT_REFERENCE**: the ICH/FDA/EMA definition(s) for the term, with source + version — required so the evaluator can verify accuracy and citations |

---

## Scorer 4 — Section Drafting from Source Data
Prompts: `dr.section`, `dr.section.table`, `jp.draftSection`  (`jp.translate` is in shelved Scorer 11)

| Prompt | Generation context profile | Paste as GENERATED_TEXT | Scoring session: select in Word | Attach as files |
|---|---|---|---|---|
| dr.section | Source data tables + supporting docs attached | The drafted section | The target section location | **Source data tables + supporting documents** (SOURCE_TEXT); **SECTION_TEMPLATE_EXPECTATIONS** |
| dr.section.table | As above, section requires in-text table | The drafted section incl. table | The target section location | Source data + supporting docs; SECTION_TEMPLATE_EXPECTATIONS; **Bayer table FORMATTING_SPEC** (see condensed spec, Scorer 7) |
| jp.draftSection | As dr.section; output in Japanese (PMDA) | The Japanese drafted section | The target section location | Source data + supporting docs (English); SECTION_TEMPLATE_EXPECTATIONS; note PMDA register |

Note: evaluate traceability against the English source even when the draft is Japanese; keep `[VERIFY: ...]` tokens verbatim.

---

## Scorer 5 — Editing with Tracked Changes
Prompts: `ed.grammar`, `ed.clarity`, `ed.streamline`, `tr.pastTense`

| Prompt | Generation context profile | Paste as GENERATED_TEXT | Scoring session: select in Word | Attach as files |
|---|---|---|---|---|
| ed.grammar | A selection highlighted | The edited output (or `No corrections needed.`) | **The original pre-edit selection** (this is SOURCE_TEXT and the markup reference) | — |
| ed.clarity | A selection highlighted | The edited output | The original pre-edit selection | — |
| ed.streamline | A selection highlighted | The edited output | The original pre-edit selection | — |
| tr.pastTense | A selection highlighted | The edited output | The original pre-edit selection | — |

Note: the scorer needs the **pre-edit text** to verify meaning preservation and tracked-changes markup. Select the original text, not the edited result, as the source.

---

## Scorer 6 — Consistency Check Within Document
Prompts: `ed.consistency`, `ab.footnoteAbbr`

| Prompt | Generation context profile | Paste as GENERATED_TEXT | Scoring session: select in Word | Attach as files |
|---|---|---|---|---|
| ed.consistency | Wording selected; full doc open as search space | The consistency report | **Both**: the selected wording **and** the full document (DOCUMENT_FULL_TEXT) | — |
| ab.footnoteAbbr | In-text table selected | The discrepancy report | The in-text table **and its footnote** (search space is the table, not the whole doc) | — |

---

## Scorer 7 — Formatting Transformation
Prompts: `tr.tabulate`, `tr.mirrorFormat`

| Prompt | Generation context profile | Paste as GENERATED_TEXT | Scoring session: select in Word | Attach as files |
|---|---|---|---|---|
| tr.tabulate | Text selection to tabulate | The HTML table output | The source text selection (SOURCE_TEXT) | **Bayer table FORMATTING_SPEC** (condensed spec below) |
| tr.mirrorFormat | Table [x] selected; Table [y] attached as context | The HTML table output | **Table [y]** (the content source, SOURCE_TEXT) | **Table [x]** (the format to mirror, FORMATTING_SPEC) |

Reminder: for `tr.mirrorFormat`, Table **[y]** is the content source; Table **[x]** is the format to mirror.

---

## Scorer 8 — Data Updates from Source Tables (highest stakes)
Prompts: `up.tableNum`, `up.tableNum.tc`, `up.textNum`, `up.textNum.tc`, `up.tableEvent`, `up.tableEvent.tc`, `up.content`

| Prompt | Generation context profile | Paste as GENERATED_TEXT | Scoring session: select in Word | Attach as files |
|---|---|---|---|---|
| up.tableNum | In-text table selected; source tables attached | The updated table | The pre-update table (SOURCE_TEXT) | **SOURCE_DATA_TABLES** (required) |
| up.tableNum.tc | As above, tracked changes | The updated table w/ TC | The pre-update table | SOURCE_DATA_TABLES |
| up.textNum | Paragraph selected; source tables attached | The updated paragraph | The pre-update paragraph | SOURCE_DATA_TABLES |
| up.textNum.tc | As above, tracked changes | The updated paragraph w/ TC | The pre-update paragraph | SOURCE_DATA_TABLES |
| up.tableEvent | Event table selected; source tables attached | The updated event table | The pre-update event table | SOURCE_DATA_TABLES (+ threshold value if applicable) |
| up.tableEvent.tc | As above, tracked changes | The updated event table w/ TC | The pre-update event table | SOURCE_DATA_TABLES (+ threshold) |
| up.content | Paragraph with refs selected; source data + sections attached | The updated content | The pre-update paragraph | SOURCE_DATA_TABLES + referenced source document(s) by name |

Note: **every** prompt here needs BOTH the pre-update text (selected) AND the SOURCE_DATA_TABLES (attached). A single wrong number is a critical failure, so supplying the full source set is essential.

---

## Scorer 9 — Content QC Against Source
Prompt: `qc.contentCheck`

| Prompt | Generation context profile | Paste as GENERATED_TEXT | Scoring session: select in Word | Attach as files |
|---|---|---|---|---|
| qc.contentCheck | Paragraph selected; source tables attached | The QC findings | The paragraph under QC (SOURCE_TEXT) | **SOURCE_DATA_TABLES** (required) |

Note: output feeds the Word comment-bubble pipeline; any format break is a critical failure. Supply the same source tables used at generation.

---

## Scorer 10 — Comment Review / Triage / Reply
Prompts: `rv.triage`, `rv.triageTable`, `rv.agenda`, `rv.aiReview`, `rv.aiReply`, `rv.genericReply`

| Prompt | Generation context profile | Paste as GENERATED_TEXT | Scoring session: select in Word | Attach as files |
|---|---|---|---|---|
| rv.triage | Doc with comments | The triage table | Full doc **with comments** | — |
| rv.triageTable | Doc with unresolved comments | The triage table | Full doc with comments | — |
| rv.agenda | Triage table pasted into prompt at generation | The agenda table | The source document | **The triage table** used as input |
| rv.aiReview | Full doc open | The AI review comments | Full doc | — |
| rv.aiReply | Doc with comments (+ replies) | The AI replies | Full doc with comments | — |
| rv.genericReply | Doc with comments | The generic replies | Full doc with comments | The exact generic reply text (for the verbatim check) |

Note: apply only the rules in the scorer's applicability matrix for the prompt under evaluation. `rv.genericReply` is checked by exact verbatim match; `rv.aiReply` replies must be 25–50 words; `rv.aiReview` must state the AI role in each comment.

---

## Condensed Bayer table FORMATTING_SPEC (attach for Scorers 4-table, 7)
Attach this (or the full Bayer spec) when scoring any table-formatting output:
- `<table class="MsoNormalTable" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse">`
- Caption: first row, single cell spanning all columns, `MsoCaption`, bottom border `#000000`
- Column headers: `BayerTableColumnHeadings` / `BayerTableStyleLeftJustified`, bottom border `#000000`
- Row headers: first column `BayerTableRowHeadings`; other data cells `BayerTableStyleLeftJustified`
- Footnotes: last row, single spanning cell, `BayerTableFootnote`, top border `#000000`
- Borders declared inline on each `<th>/<td>` (not on `<tr>`); replace `windowtext` with `#000000`
- Citations in footnotes use `#0000FF`; include `lang="EN-US"` on text spans
- Headings: section numbers removed; `margin-left`/`text-indent` zero only on headings
- Preserve REF field spans (`mso-field-code` with `_Ref` bookmarks); preserve caption whitespace verbatim; no em dashes unless warranted; no markdown; allowed HTML tags only
