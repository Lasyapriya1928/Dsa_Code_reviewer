import os
import sys
import csv

# -------------------------------------------------
# FORCE PROJECT ROOT INTO PYTHON PATH (CRITICAL)
# -------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

# -------------------------------------------------
# NOW IMPORT BACKEND MODULES
# -------------------------------------------------
from backend.services.feature_extractor import extract_features

RAW_CODE_DIR = os.path.join("data", "raw_code")
OUTPUT_CSV = os.path.join("data", "dataset.csv")


def parse_labels_from_filename(filename: str):
    name = filename.replace(".py", "")
    parts = name.split("_")

    # Problem-aware format
    if len(parts) >= 4:
        pattern_label = parts[-3]
        efficiency_label = parts[-2]
        return pattern_label, efficiency_label

    # Generic format
    elif len(parts) == 3:
        pattern_label = parts[0]
        efficiency_label = parts[1]
        return pattern_label, efficiency_label

    else:
        raise ValueError(f"Invalid filename format: {filename}")


def build_dataset():
    rows = []

    for root, _, files in os.walk(RAW_CODE_DIR):
        for file in files:
            if not file.endswith(".py"):
                continue

            file_path = os.path.join(root, file)

            # Determine source type
            source = "problem_aware" if "problem_aware" in root else "generic"

            # Read code
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()

            # Extract AST features
            features = extract_features(code)

            # Parse labels from filename
            try:
                pattern_label, efficiency_label = parse_labels_from_filename(file)
            except ValueError as e:
                print(f"Skipping {file}: {e}")
                continue

            row = {
                **features,
                "pattern_label": pattern_label,
                "efficiency_label": efficiency_label,
                "source": source
            }

            rows.append(row)

    if not rows:
        raise RuntimeError("No data collected. Check raw_code directory.")

    # Write CSV
    fieldnames = rows[0].keys()
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Dataset created with {len(rows)} rows → {OUTPUT_CSV}")


if __name__ == "__main__":
    build_dataset()
