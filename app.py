from flask import Flask, render_template, request
import os
import json
import pandas as pd

from pipeline.parsers.csv_parser import parse_csv
from pipeline.parsers.github_parser import parse_github
from pipeline.processors.normalizer import normalize_candidate
from pipeline.processors.merge_processor import merge_candidates
from pipeline.processors.confidence import calculate_confidence
from pipeline.processors.provenance import add_provenance

app = Flask(__name__)

UPLOAD_FOLDER = "data/input"
OUTPUT_FOLDER = "data/output"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/transform", methods=["POST"])
def transform():

    csv_file = request.files["csv_file"]
    github_file = request.files["github_file"]

    csv_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        csv_file.filename
    )

    github_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        github_file.filename
    )

    csv_file.save(csv_path)
    github_file.save(github_path)

    # Parse recruiter CSV
    candidates = parse_csv(csv_path)

    # Normalize recruiter data
    normalized_candidates = []

    for candidate in candidates:
        normalized_candidates.append(
            normalize_candidate(candidate)
        )

    # Parse GitHub JSON
    github_profiles = parse_github(github_path)

    # Merge recruiter + GitHub
    merged_candidates = merge_candidates(
        normalized_candidates,
        github_profiles
    )

    # Confidence + Provenance
    for candidate in merged_candidates:

        candidate["confidence"] = calculate_confidence(candidate)

        candidate["provenance"] = add_provenance(candidate)

        # Replace NaN values with None
        for key, value in candidate.items():

            # Skip lists (like skills)
            if isinstance(value, list):
                continue

            # Replace only pandas NaN values
            if pd.isna(value):
                candidate[key] = None

    # Save final JSON
    output_path = os.path.join(
        app.config["OUTPUT_FOLDER"],
        "final_candidates.json"
    )

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            merged_candidates,
            file,
            indent=4,
            ensure_ascii=False
        )

    return render_template(
        "result.html",
        candidates=merged_candidates
    )


if __name__ == "__main__":
    app.run(debug=True)