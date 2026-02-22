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

    # Efficiency is always second last
    efficiency_label = parts[-2]

    # Join all words except last two (efficiency + index)
    pattern_raw = "_".join(parts[:-2]).lower()

    # 🔥 Normalize pattern labels
    if "bruteforce" in pattern_raw or "nested" in pattern_raw:
        pattern_label = "brute_force"

    elif "dp" in pattern_raw or "table" in pattern_raw:
        pattern_label = "dynamic_programming"

    elif "hash" in pattern_raw or "dict" in pattern_raw or "counter" in pattern_raw:
        pattern_label = "hashing"

    elif "stack" in pattern_raw:
        pattern_label = "stack"

    elif "two" in pattern_raw or "pointer" in pattern_raw:
        pattern_label = "two_pointer"

    elif "recurs" in pattern_raw or "helper" in pattern_raw:
        pattern_label = "recursion"

    else:
        pattern_label = "other"

    return pattern_label, efficiency_label

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
