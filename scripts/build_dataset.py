# --------------------------------------------------
# DATASET BUILDER (Robust + Recursive)
# --------------------------------------------------
import os
import sys

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PROJECT_ROOT)
import ast
import pandas as pd
from backend.services.feature_extractor import extract_features


# --------------------------------------------------
# CONFIG
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RAW_CODE_DIR = os.path.join(BASE_DIR, "data", "raw_code")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "dataset.csv")

VALID_PATTERNS = {
    "brute_force",
    "dynamic_programming",
    "hashing",
    "recursion",
    "stack",
    "two_pointer"
}

VALID_EFFICIENCIES = {
    "efficient",
    "suboptimal",
    "inefficient"
}


# --------------------------------------------------
# MAIN BUILD FUNCTION
# --------------------------------------------------

def build_dataset():

    print("Building dataset from:", RAW_CODE_DIR)
    print("-" * 50)

    rows = []
    skipped = 0

    for root, _, files in os.walk(RAW_CODE_DIR):
        for file in files:

            if not file.endswith(".py"):
                continue

            file_path = os.path.join(root, file)
            name = file.replace(".py", "")

            try:
                parts = name.split("_")

                # Expected format:
                # pattern_efficiency_index
                # Example:
                # brute_force_efficient_01

                parts = name.split("_")

                if len(parts) < 3:
                    raise ValueError("Filename format invalid")

                index = parts[-1]
                efficiency = parts[-2]
                pattern = "_".join(parts[:-2])

                if pattern not in VALID_PATTERNS:
                    raise ValueError(f"Invalid pattern: {pattern}")

                if efficiency not in VALID_EFFICIENCIES:
                    raise ValueError(f"Invalid efficiency: {efficiency}")

                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()

                # Ensure valid Python
                ast.parse(code)

                # Extract features
                features = extract_features(code)

                features["pattern_label"] = pattern
                features["efficiency_label"] = efficiency

                rows.append(features)

            except Exception as e:
                skipped += 1
                print("Skipped:", file)
                print("Reason:", repr(e))
                print("-" * 30)

    df = pd.DataFrame(rows)

    df.to_csv(OUTPUT_PATH, index=False)

    print("\nDataset created successfully!")
    print("Total rows:", len(df))
    print("Total skipped:", skipped)
    print("Saved to:", OUTPUT_PATH)
    print("-" * 50)


# --------------------------------------------------

if __name__ == "__main__":
    build_dataset()