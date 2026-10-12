# Scribbler 2.0 Integration

Scribbler 2.0 is a Microsoft Word add-in. It maintains the standard prompt library, stores the
evaluation (scorer) prompts linked to each standard prompt, and executes both generation and
scoring. This affects the scorers in three concrete ways, all already applied to `dist/`.

## 1. Source is delivered by session context, not pasted

In the scoring session, the source document is **selected in Word** and reference files are
**attached to the context panel**. The scorer is instructed to treat these as SOURCE_TEXT (and
SOURCE_DATA_TABLES / FORMATTING_SPEC where relevant). Only GENERATED_TEXT is pasted into the
scorer, between the paste-in markers. If a required source is genuinely absent, the scorer asks
for it rather than fabricating.

## 2. Output contract: HTML fragment, no markdown

Every Scribbler reply must be a single valid HTML5 fragment with no markdown and no commentary,
using only an allowed tag set. So each scorer returns its JSON wrapped in a single
`<pre><code>` block (Scribbler's recommended Option A): the reply is contract-compliant HTML,
and the JSON payload stays intact and parseable. `code` and `pre` are in the allowed tag set.

## 3. Context profiles must mirror production

The generation step must reproduce the production context profile for each prompt (full
document vs. selection vs. uploaded references, and whether comments are required), or the
generated output is not representative. `testing/paste_in_checklist.md` records the profile per
prompt for both the generation and scoring halves.

## Session isolation

The scoring session must be a **fresh Scribbler conversation** with no residual context from the
generation session, so the evaluator judges only what it is explicitly given.

## Not folded in (by decision)

The full Bayer output contract (closed style-class vocabulary, formatting rules) is **not**
encoded in the scorers during the prototype. The only contract-aware instruction they carry is
the `<pre><code>` JSON wrapper. Folding the full contract into the base template remains a
candidate change for after the prototype; the build pipeline can propagate it cleanly if adopted.
