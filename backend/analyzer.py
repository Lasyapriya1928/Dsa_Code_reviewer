# --------------------------------------------------
# ANALYZER: ML Inference + Explainability
# --------------------------------------------------

import os
import joblib
import pandas as pd

from backend.services.feature_extractor import extract_features
from backend.database import save_submission


# Load Models
BASE_DIR = os.path.dirname(__file__)
MODEL_DIR = os.path.join(BASE_DIR, "models")

eff_model = joblib.load(os.path.join(MODEL_DIR, "efficiency_model.pkl"))
eff_encoder = joblib.load(os.path.join(MODEL_DIR, "efficiency_label_encoder.pkl"))

pattern_model = joblib.load(os.path.join(MODEL_DIR, "pattern_model.pkl"))
pattern_encoder = joblib.load(os.path.join(MODEL_DIR, "pattern_label_encoder.pkl"))


def generate_human_explanation(features):
    explanation = []

    if features["max_loop_depth"] >= 2:
        explanation.append("Nested loops were detected.")

    if features["has_recursion"] == 1:
        explanation.append("Recursive calls were detected.")

    if features["num_loops"] > 1:
        explanation.append("Multiple loops increase computational cost.")

    if not explanation:
        explanation.append("The structure appears efficient.")

    return explanation


def analyze_code(code: str, problem_name: str = "Generic"):

    if not code.strip():
        return {"error": "No valid Python code provided."}

    try:
        features = extract_features(code)
    except:
        return {"error": "Invalid Python syntax."}

    features["loop_density"] = (
        features["num_loops"] / max(features["lines_of_code"], 1)
    )

    feature_order = [
        "num_loops",
        "max_loop_depth",
        "has_recursion",
        "uses_list",
        "uses_dict",
        "uses_set",
        "lines_of_code",
        "num_functions",
        "uses_append",
        "uses_pop",
        "loop_density"
    ]

    X_input = pd.DataFrame(
        [[features[f] for f in feature_order]],
        columns=feature_order
    )

    eff_pred = eff_model.predict(X_input)[0]
    predicted_efficiency = eff_encoder.inverse_transform([eff_pred])[0]

    pattern_pred = pattern_model.predict(X_input)[0]
    predicted_pattern = pattern_encoder.inverse_transform([pattern_pred])[0]

    explanation = generate_human_explanation(features)

    save_submission(
        problem_name,
        predicted_efficiency,
        predicted_pattern,
        explanation,
        code
    )

    return {
        "problem_name": problem_name,
        "predicted_efficiency": predicted_efficiency,
        "predicted_pattern": predicted_pattern,
        "explanation": explanation
    }