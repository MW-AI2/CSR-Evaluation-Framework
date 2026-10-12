#!/usr/bin/env python3
"""
Append a results row from a scorer JSON output.

Usage:
    python scripts/json_to_results_row.py <scorer_output.json> [options]

It reads the JSON a scorer returned (the object inside the <pre><code> block),
maps each field into the correct column of the results CSV, and APPENDS one row.
No manual column-by-column typing.

Fields the JSON cannot know (which model generated the output, the test-case id,
the human calibration columns) can be supplied with flags, or left blank and
filled in later in Excel.

Examples:
    python scripts/json_to_results_row.py run.json \
        --generator-model claude-4.7-opus \
        --test-case-id TC1-correct \
        --prompt-version lib-2026-10 \
        --source-artifacts "pre-update table selected; source table 8.1/8 uploaded"
"""
import argparse
import csv
import datetime
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_TEMPLATE = REPO / "testing" / "templates" / "evaluation_results_template.csv"
DEFAULT_RESULTS = REPO / "testing" / "results"

# Column order must match the template header exactly.
COLUMNS = [
    "run_id", "run_date", "cycle_id", "scorer_id", "scorer_version", "archetype_name",
    "prompt_id", "prompt_version", "test_case_id", "generator_model",
    "base_template_version", "source_artifacts_used",
    "source_faithfulness_score", "source_faithfulness_rationale",
    "dim2_name", "dim2_score", "dim2_rationale",
    "regulatory_writing_quality_score", "regulatory_writing_quality_rationale",
    "dim4_name", "dim4_score", "dim4_rationale",
    "internal_consistency_score", "internal_consistency_rationale",
    "critical_failure_present", "critical_failure_reason",
    "overall_score", "overall_verdict", "likely_error_source", "diagnostic_interpretation",
    "human_reviewer", "human_overall_score", "human_verdict", "agreement_flag",
    "divergence_notes", "json_valid", "notes",
]

# Scorer-id -> readable archetype name, so archetype_name fills itself.
ARCHETYPE_NAMES = {
    "scorer_01": "Summarization / Overview",
    "scorer_02": "Extraction / Listing",
    "scorer_03": "Definition / Explanation",
    "scorer_04": "Section Drafting from Source Data",
    "scorer_05": "Editing with Tracked Changes",
    "scorer_06": "Consistency Check Within Document",
    "scorer_07": "Formatting Transformation",
    "scorer_08": "Data Updates from Source Tables",
    "scorer_09": "Content QC Against Source",
    "scorer_10": "Comment Review / Triage / Reply",
}

# The two universal task-specific dimension slots sit between the fixed dimensions.
# We detect them as the keys in dimension_scores that are not the three universal ones.
UNIVERSAL_DIMS = {"source_faithfulness", "regulatory_writing_quality", "internal_consistency"}


def load_json(path):
    text = pathlib.Path(path).read_text(encoding="utf-8").strip()
    # Tolerate a pasted <pre><code>...</code></pre> wrapper.
    for tag in ("<pre><code>", "</code></pre>", "<pre>", "</pre>", "<code>", "</code>"):
        text = text.replace(tag, "")
    text = text.strip()
    return json.loads(text)


def extract_row(data, args, run_id):
    ds = data.get("dimension_scores", {})
    # identify the two task-specific dimension keys, in order of appearance
    task_dims = [k for k in ds.keys() if k not in UNIVERSAL_DIMS]
    dim2_key = task_dims[0] if len(task_dims) > 0 else ""
    dim4_key = task_dims[1] if len(task_dims) > 1 else ""

    def score(key):
        return ds.get(key, {}).get("score", "")

    def rationale(key):
        return ds.get(key, {}).get("rationale", "")

    cf = data.get("critical_failure", {})
    audit = data.get("audit", {})
    scorer_id = audit.get("scorer_id", "")

    row = {
        "run_id": run_id,
        "run_date": args.run_date or datetime.date.today().isoformat(),
        "cycle_id": args.cycle_id,
        "scorer_id": scorer_id,
        "scorer_version": audit.get("scorer_version", ""),
        "archetype_name": ARCHETYPE_NAMES.get(scorer_id, ""),
        "prompt_id": audit.get("prompt_id", "") or args.prompt_id,
        "prompt_version": audit.get("prompt_version", "") or args.prompt_version,
        "test_case_id": args.test_case_id,
        "generator_model": args.generator_model,
        "base_template_version": audit.get("base_template_version", ""),
        "source_artifacts_used": args.source_artifacts,
        "source_faithfulness_score": score("source_faithfulness"),
        "source_faithfulness_rationale": rationale("source_faithfulness"),
        "dim2_name": dim2_key,
        "dim2_score": score(dim2_key),
        "dim2_rationale": rationale(dim2_key),
        "regulatory_writing_quality_score": score("regulatory_writing_quality"),
        "regulatory_writing_quality_rationale": rationale("regulatory_writing_quality"),
        "dim4_name": dim4_key,
        "dim4_score": score(dim4_key),
        "dim4_rationale": rationale(dim4_key),
        "internal_consistency_score": score("internal_consistency"),
        "internal_consistency_rationale": rationale("internal_consistency"),
        "critical_failure_present": str(cf.get("present", "")).upper(),
        "critical_failure_reason": cf.get("reason", ""),
        "overall_score": data.get("overall_score", ""),
        "overall_verdict": data.get("overall_verdict", ""),
        "likely_error_source": data.get("likely_error_source", ""),
        "diagnostic_interpretation": data.get("interpretation", ""),
        "human_reviewer": "",
        "human_overall_score": "",
        "human_verdict": "",
        "agreement_flag": "",
        "divergence_notes": "",
        "json_valid": "TRUE",
        "notes": args.notes,
    }
    return row


def next_run_id(results_path):
    if not results_path.exists():
        return "R001"
    with results_path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    n = len(rows) + 1
    return f"R{n:03d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json_file", help="File containing the scorer JSON output")
    ap.add_argument("--results", default=str(DEFAULT_RESULTS / "pilot_results.csv"),
                    help="Results CSV to append to (created from the template if missing)")
    ap.add_argument("--cycle-id", default="pilot")
    ap.add_argument("--generator-model", default="")
    ap.add_argument("--test-case-id", default="")
    ap.add_argument("--prompt-id", default="")
    ap.add_argument("--prompt-version", default="")
    ap.add_argument("--source-artifacts", dest="source_artifacts", default="")
    ap.add_argument("--run-date", default="")
    ap.add_argument("--notes", default="")
    args = ap.parse_args()

    data = load_json(args.json_file)
    results_path = pathlib.Path(args.results)
    results_path.parent.mkdir(parents=True, exist_ok=True)

    # create the results file with a header if it does not exist
    if not results_path.exists():
        with results_path.open("w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=COLUMNS).writeheader()

    run_id = next_run_id(results_path)
    row = extract_row(data, args, run_id)

    with results_path.open("a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=COLUMNS).writerow(row)

    print(f"Appended {run_id} to {results_path}")
    print(f"  {row['prompt_id']} | overall {row['overall_score']} | {row['overall_verdict']} "
          f"| critical_failure={row['critical_failure_present']}")


if __name__ == "__main__":
    main()
