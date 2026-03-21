# CSR-Evaluation-Framework
# CSR Output Evaluation Framework

## Purpose

This document defines a modular scoring framework for evaluating model-generated outputs across major sections of the Clinical Study Report (CSR).

The framework is designed to support consistent evaluation across section types while preserving the specificity needed to assess outputs such as:

- Study Design
- TLF summaries
- PK/PD
- Efficacy
- Safety
- Synopsis
- Other major CSR narrative components

The core recommendation is to use a **modular rubric architecture**:

1. a **master template** with shared evaluation criteria and shared scoring logic
2. a **section-specific module** that adds criteria tailored to the content type being evaluated

This approach is preferred over either:
- a single universal rubric that is too generic to be useful, or
- completely separate rubrics that become inconsistent and difficult to compare

---

## Design Principles

The framework should:

- preserve a common evaluation logic across all sections
- allow section-specific expectations and failure modes
- prioritize factual reliability over fluency
- distinguish unsupported content from weakly supported content
- distinguish major issues from moderate and minor issues
- support both human review and structured model-based scoring
- produce outputs that are comparable, reviewable, and usable for iterative development

The framework should not:

- reward polished writing when content is inaccurate or unsupported
- use one overly generic rubric for all section types
- treat all issues as equally important
- force section-specific expectations into sections where they do not apply

---

## Recommended Architecture

## Layer 1: Master Rubric Template

The master rubric provides the shared scoring backbone used across all CSR sections.

It standardizes:

- evaluation philosophy
- support definitions
- materiality definitions
- verdict labels
- critical failure logic
- JSON output conventions
- core shared dimensions

## Layer 2: Section-Specific Modules

Each major CSR section or content family should have a section-specific module that defines:

- the purpose of that section
- what good output looks like for that section
- section-specific dimensions
- section-specific completeness expectations
- section-specific failure modes
- recommended weighting adjustments
- examples of critical errors specific to that section

---

## Shared Definitions

These definitions should apply across all section-specific rubrics.

## Support Categories

### supported
Clearly supported by the source material.

### weakly_supported
Plausibly derived from the source, but not clearly or explicitly supported.

### unsupported
Not supported by the source, materially stronger than the source supports, contradictory, or fabricated.

## Materiality Categories

### major
An issue that changes the reader's understanding, creates meaningful factual or regulatory risk, or makes the output unsafe to rely on.

### moderate
A meaningful weakness that should be revised.

### minor
A low-risk issue with limited impact on interpretation or usability.

---

## Shared Critical Failure Logic

A critical failure should be triggered when the output contains or misses an issue that materially changes interpretation or creates meaningful factual, regulatory, or scientific risk.

Examples may include:

- fabricated claim
- contradiction with source
- materially misleading interpretation
- major omission that changes meaning
- incorrect numerical characterization
- incorrect study design characterization
- incorrect treatment effect interpretation
- incorrect safety characterization

Critical failure should take precedence over otherwise acceptable performance on lower-priority dimensions.

Numeric scoring should not conceal critical safety or accuracy problems.

---

## Shared Verdict Labels

Use one verdict system consistently across all modules.

Recommended verdict labels:

- Pass
- Pass with minor revision
- Revise
- Fail

Alternative wording may be used, but it should remain standardized across the evaluation framework.

---

## Master Shared Dimensions

The following dimensions are recommended as the common backbone for most CSR section evaluations.

Not every section must weight them equally, but they should form the default template.

### 1. Source Faithfulness / Factual Accuracy
Does the output accurately reflect the source material?

### 2. Completeness Relative to Section Purpose
Does the output include the important content that should reasonably be present for that section and output type?

### 3. Internal Consistency
Is the output consistent with itself, with structured inputs, and with any referenced data or source material?

### 4. Regulatory Writing Quality
Is the output written in a manner appropriate for CSR use, including tone, precision, clarity, and structure?

### 5. Section-Purpose Fit
Does the output function appropriately for the intended section, rather than merely sounding fluent?

### 6. Detail-Level Fit
Is the level of detail appropriate for the intended section, subsection, or requested output style?

---

## Recommended Master Weighting Template

A default master weighting template could be:

- source_faithfulness: 0.30
- completeness: 0.20
- internal_consistency: 0.15
- regulatory_writing_quality: 0.15
- section_purpose_fit: 0.10
- detail_level_fit: 0.10

This should be treated as a default starting point only.

Section-specific modules should be allowed to adjust both:
- dimensions
- weighting

---

## Recommended Master JSON Template

A general scoring structure could be:

```json
{
  "dimension_scores": {
    "source_faithfulness": {"score": 0, "rationale": ""},
    "completeness": {"score": 0, "rationale": ""},
    "internal_consistency": {"score": 0, "rationale": ""},
    "regulatory_writing_quality": {"score": 0, "rationale": ""},
    "section_purpose_fit": {"score": 0, "rationale": ""},
    "detail_level_fit": {"score": 0, "rationale": ""}
  },
  "critical_failure": {
    "present": false,
    "reason": ""
  },
  "section_specific_findings": [],
  "strengths": [],
  "recommended_revisions": [],
  "overall_score": 0,
  "overall_verdict": "",
  "interpretation": "",
  "notes": ""
}
