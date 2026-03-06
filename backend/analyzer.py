# --------------------------------------------------
# ANALYZER: Hybrid ML Inference + Explainability
# --------------------------------------------------

import os
import joblib
import pandas as pd

from services.feature_extractor import extract_features


# --------------------------------------------------
# Load Models
# --------------------------------------------------

BASE_DIR = os.path.dirname(__file__)
MODEL_DIR = os.path.join(BASE_DIR, "models")

eff_model = joblib.load(os.path.join(MODEL_DIR, "efficiency_model.pkl"))
eff_encoder = joblib.load(os.path.join(MODEL_DIR, "efficiency_label_encoder.pkl"))

pattern_model = joblib.load(os.path.join(MODEL_DIR, "pattern_model.pkl"))
pattern_encoder = joblib.load(os.path.join(MODEL_DIR, "pattern_label_encoder.pkl"))

# Load saved feature order
feature_order = joblib.load(os.path.join(MODEL_DIR, "feature_columns.pkl"))


# --------------------------------------------------
# Human Explanation Logic
# --------------------------------------------------

def generate_human_explanation(features, predicted_efficiency):

    explanation = []

    explanation.append(
        f"This implementation is classified as {predicted_efficiency} based on structural characteristics."
    )

    if features.get("max_loop_depth", 0) >= 2:
        explanation.append(
            "Nested loops indicate potential quadratic time complexity (approximately O(n²))."
        )

    elif features.get("num_loops", 0) == 1:
        explanation.append(
            "A single loop suggests linear time complexity (approximately O(n))."
        )

    if features.get("has_recursion", 0) == 1:
        explanation.append(
            "Recursive calls are present, which may add stack overhead depending on input size."
        )

    if features.get("uses_dict", 0) == 1:
        explanation.append("Dictionary usage suggests hash-based optimization.")

    if features.get("uses_set", 0) == 1:
        explanation.append("Set operations indicate constant-time membership checks.")

    if features.get("uses_append", 0) == 1 and features.get("uses_pop", 0) == 1:
        explanation.append("Append and pop operations indicate stack-like (LIFO) behavior.")

    if features.get("uses_subscript_assignment", 0) == 1:
        explanation.append(
            "Indexed state updates suggest dynamic programming style transitions."
        )

    if features.get("lines_of_code", 0) > 25:
        explanation.append(
            "The implementation includes multiple logical steps, contributing to structural complexity."
        )

    if len(explanation) == 1:
        explanation.append(
            "The structure reflects a straightforward and optimized solution."
        )

    return explanation


# --------------------------------------------------
# Hybrid Pattern Override (Rule Engine)
# --------------------------------------------------

def hybrid_pattern_override(features, model_prediction):

    # recursion
    if features.get("has_recursion", 0) == 1 and features.get("num_loops", 0) == 0:
        return "recursion"

    # stack
    if features.get("uses_append", 0) == 1 and features.get("uses_pop", 0) == 1:
        return "stack"

    # hashing
    if features.get("uses_dict", 0) == 1:
        return "hashing"

    # brute force
    if features.get("max_loop_depth", 0) >= 2:
        return "brute_force"

    # two pointer
    if (
        features.get("num_loops", 0) == 1
        and features.get("max_loop_depth", 0) == 1
        and features.get("uses_dict", 0) == 0
        and features.get("uses_set", 0) == 0
        and features.get("uses_2d_list", 0) == 0
        and (
            features.get("uses_list", 0) == 1
            or features.get("nested_subscript_usage", 0) > 0
        )
    ):
        return "two_pointer"

    # dynamic programming
    if (
        features.get("uses_2d_list", 0) == 1
        or features.get("nested_subscript_usage", 0) > 0
        or features.get("uses_subscript_assignment", 0) == 1
    ):
        return "dynamic_programming"

    return model_prediction
# --------------------------------------------------
# Main Analyze Function
# --------------------------------------------------

def analyze_code(code: str, problem_name: str = "Generic"):

    if not code.strip():
        return {"error": "No valid Python code provided."}

    try:
        features = extract_features(code)
    except:
        return {"error": "Invalid Python syntax."}

    # Ensure all required features exist
    for feature in feature_order:
        if feature not in features:
            features[feature] = 0

    # Create DataFrame in correct order
    X_input = pd.DataFrame(
        [[features[f] for f in feature_order]],
        columns=feature_order
    )

    # -----------------------------
    # Efficiency Prediction
    # -----------------------------
    eff_pred = eff_model.predict(X_input)[0]
    predicted_efficiency = eff_encoder.inverse_transform([eff_pred])[0]

    # Override efficiency with loop rules
    if features.get("max_loop_depth", 0) >= 2:
        predicted_efficiency = "inefficient"

    elif features.get("max_loop_depth", 0) == 1:
        predicted_efficiency = "suboptimal"

    # -----------------------------
    # Pattern Prediction (ML)
    # -----------------------------
    pattern_pred = pattern_model.predict(X_input)[0]
    ml_pattern = pattern_encoder.inverse_transform([pattern_pred])[0]

    # -----------------------------
    # Hybrid Override
    # -----------------------------
    predicted_pattern = hybrid_pattern_override(features, ml_pattern)

    # -----------------------------
    # Explanation
    # -----------------------------
    explanation = generate_human_explanation(features, predicted_efficiency)

    return {
        "problem_name": problem_name,
        "predicted_efficiency": predicted_efficiency,
        "predicted_pattern": predicted_pattern,
        "explanation": explanation
    }