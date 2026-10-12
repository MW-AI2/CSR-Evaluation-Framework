# System-Prompt Gap Analysis and Revision Log (Scorers 1–10)

Active library: 34 prompts across 10 archetypes. Scorers 11 (Translation) and 12 (STROBE) are shelved.
Base template version: base-template-v1.0 (bc2b58dd7b37)

Each scorer's critical-failure rules and dimensions were checked against the backend system prompts of the standard prompts it covers. Gaps found and the revision applied:

## Scorer 1 — Summarization
- Gap: wrong-document-type critical rule applied to all 5 prompts; only `da.tldr` classifies a document type. Fix: made it `da.tldr`-only.
- Gap: Structural Fit undefined for prompts without a template. Fix: marked N/A with weight renormalization; template required only for `da.tldr`.
- Fix: added `rv.summarize` author-misattribution critical rule (system prompt requires author attribution and original-vs-reply separation).

## Scorer 2 — Extraction
- Gap: critical rule assumed HTML output. System prompts (`da.listData`, `ab.extract`) do not mandate HTML. Fix: output-format critical fires only when EXTRACTION_RULES mandates a format.
- Fix: made the "one+ missing abbreviation" rule consistent between Dimension 2 and the critical list.
- Fix: italics not penalized when the output format cannot carry them.

## Scorer 3 — Definition
- Fix: restored universal SOURCE_FAITHFULNESS; added a documented archetype note that it is assessed against REGULATORY_CONTEXT_REFERENCE. Removed double-counting; rebalanced weights (0.35/0.30/0.15/0.10/0.10).
- Fix: fabricated-citation critical rule now checks against the reference input, not model knowledge.

## Scorer 4 — Section Drafting
- Scope: `jp.draftSection` stays active (section drafting); `jp.translate` is in shelved Scorer 11.
- Fix: added explicit Japanese-output handling (read target language; traceability against English source; `[VERIFY:]` tokens kept verbatim).
- Fix: Dimension 4 split by prompt (Bayer spec for `dr.section.table`; narrative for `dr.section`; PMDA register for `jp.draftSection`). Bayer critical rule limited to `dr.section.table`.

## Scorer 5 — Editing with Tracked Changes
- Gap: missing critical failure for `ed.grammar` "No corrections needed." (required by system prompt). Fix: added.
- Fix: aligned markup severity — whole sentence = moderate; whole paragraph = critical. Unmarked edit = critical only.
- Fix: incorrect-tense critical rule limited to `tr.pastTense`. Merged duplicate SOURCE_TEXT/ORIGINAL_SELECTION input.

## Scorer 6 — Consistency Check
- Fix: missing-from-footnote critical rule limited to `ab.footnoteAbbr`.
- Fix: defined DOCUMENT_FULL_TEXT search space per prompt; non-alphabetical-order now scored in Dimension 2.
- Fix: removed stray tool-definition text (not part of the scorer).

## Scorer 7 — Formatting Transformation
- Fix: corrected Table [x]/[y] labels (source = Table [y]; mirror target format = Table [x]).
- Fix: "Bayer classes absent" critical rule limited to `tr.tabulate`; added mirror-not-applied critical rule for `tr.mirrorFormat`.
- Fix: removed content double-counting (Content Preservation is the scored dimension; Source Faithfulness covers altered claims only).

## Scorer 8 — Data Updates (highest stakes)
- Fix: added N/A rule and weight renormalization for non-`.tc` variants and prompts without captions/cross-refs.
- Fix: resolved critical-vs-scored conflict (critical rule governs and caps; Dimension 4 scores only non-critical aspects).
- Fix: clarified that source-table percentages are source values, not "calculated" values.
- Fix: added `up.content` source-document-name critical rule.

## Scorer 9 — Content QC
- Fix: commentary/pipeline-break is critical only (removed from Dimension 4 scored band).
- Fix: discrepancy scope stated as numeric-only; "Unable to verify" handling folded into Dimension 2.
- Fix: in-text reference exclusions (Sections, Listings, <=2-numeral tables) made explicit scoring rules; 3+ numeral tables checked.

## Scorer 10 — Comment Review
- Gap: missing `rv.genericReply` verbatim critical rule. Fix: added, with a deterministic verbatim check.
- Gap: missing `rv.aiReview` "state AI role" requirement. Fix: added as element + critical rule.
- Gap: `rv.aiReply` lower bound (25 words) missing. Fix: 25–50 word range added.
- Fix: added a per-prompt applicability matrix; defined `[S]`/`[R]` tags and the Comment Type categories.

## Cross-cutting
- Each merged prompt carries the full common base content, byte-identical across all 10 (verified; scorer 3's dim1 note is the one documented exception).
- Added an `audit` block to the JSON output (scorer_id, scorer_version, prompt_id, prompt_version, base_template_version).
- All weight vectors sum to 1.0 (enforced in the build).

## Open decisions (not auto-resolved; need owner sign-off)
1. Whether `rv.genericReply` is split out of Scorer 10 or kept with the override (deterministic check added either way).
2. Whether Regulatory Writing Quality uses one fixed library-wide weight or stays per archetype (currently per archetype, documented).
