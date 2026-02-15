# --------------------------------------------------
# ML INFERENCE SERVICE
# --------------------------------------------------

import os
import joblib
import numpy as np
import pandas as pd

# --------------------------------------------------
# Load Models
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

EFF_MODEL_PATH = os.path.join(MODEL_DIR, "efficiency_model.pkl")
EFF_ENCODER_PATH = os.path.join(MODEL_DIR, "efficiency_label_encoder.pkl")

PATTERN_MODEL_PATH = os.path.join(MODEL_DIR, "pattern_model.pkl")
PATTERN_ENCODER_PATH = os.path.join(MODEL_DIR, "pattern_label_encoder.pkl")

eff_model = joblib.load(EFF_MODEL_PATH)
eff_encoder = joblib.load(EFF_ENCODER_PATH)

pattern_model = joblib.load(PATTERN_MODEL_PATH)
pattern_encoder = joblib.load(PATTERN_ENCODER_PATH)


# --------------------------------------------------
# Feature Order (MUST match training order)
# --------------------------------------------------

FEATURE_COLS = [
    "num_loops",
    "max_loop_depth",
    "has_recursion",
    "uses_list",
    "uses_dict",
    "uses_set",
    "lines_of_code",
    "num_functions",
    "loop_density",
    "uses_append",
    "uses_pop",
]


# --------------------------------------------------
# Efficiency Prediction
# --------------------------------------------------

def predict_efficiency(features: dict):

    X_input = pd.DataFrame(
        [[features[col] for col in FEATURE_COLS]],
        columns=FEATURE_COLS
    )

    pred_encoded = eff_model.predict(X_input)[0]
    pred_label = eff_encoder.inverse_transform([pred_encoded])[0]

    explanation = generate_explanation(features)

    return {
        "predicted_efficiency": pred_label,
        "explanation": explanation
    }


# --------------------------------------------------
# Pattern Prediction
# --------------------------------------------------

def predict_pattern(features: dict):

    X_input = pd.DataFrame(
        [[features[col] for col in FEATURE_COLS]],
        columns=FEATURE_COLS
    )

    pred_encoded = pattern_model.predict(X_input)[0]
    pred_label = pattern_encoder.inverse_transform([pred_encoded])[0]

    return pred_label


# --------------------------------------------------
# Human Explanation Logic
# --------------------------------------------------

def generate_explanation(features):

    explanation = []

    if features["max_loop_depth"] >= 2:
        explanation.append(
            "Nested loops were detected, which significantly increases time complexity."
        )

    if features["num_loops"] > 1:
        explanation.append(
            "Multiple loops contribute to higher computational cost."
        )

    if features["has_recursion"] == 1:
        explanation.append(
            "Recursive calls were detected, which may increase runtime overhead."
        )

    if features["lines_of_code"] > 20:
        explanation.append(
            "The solution is relatively long, which may indicate inefficiency."
        )

    if not explanation:
        explanation.append(
            "The structure of the code appears efficient and well-optimized."
        )

    return explanation
