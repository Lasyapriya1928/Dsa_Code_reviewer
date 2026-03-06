def generate_explanation(features: dict, predicted_pattern: str) -> list:
    reasons = []

    # ---------- BRUTE FORCE ----------
    if predicted_pattern == "brute_force":

        if features.get("num_loops", 0) >= 2:
            reasons.append(
                f"{features['num_loops']} loops detected in the code"
            )

        if features.get("max_loop_depth", 0) >= 2:
            reasons.append(
                f"Nested loops detected (depth = {features['max_loop_depth']}) suggesting quadratic complexity"
            )

        if not features.get("has_recursion", False):
            reasons.append("No recursion detected")

        if not features.get("uses_dict", False):
            reasons.append("No hashing structures used")

    # ---------- DYNAMIC PROGRAMMING ----------
    elif predicted_pattern == "dynamic_programming":

        # Strong DP signals
        if features.get("uses_2d_list", False):
            reasons.append("2D DP table detected")

        if features.get("nested_subscript_usage", 0) > 0:
            reasons.append("Nested index access like dp[i][j] detected")

        if (
            features.get("uses_subscript_assignment", False)
            and features.get("max_loop_depth", 0) >= 1
            and (
                features.get("uses_2d_list", False)
                or features.get("nested_subscript_usage", 0) > 0
            )
        ):
            reasons.append("State transition updates inside loops detected")

        if features.get("num_if_statements", 0) > 0:
            reasons.append("Conditional transitions found (common in DP)")

    # ---------- HASHING ----------
    elif predicted_pattern == "hashing":
        if features.get("uses_dict", False):
            reasons.append("Dictionary usage detected for fast lookup")

        if features.get("uses_set", False):
            reasons.append("Set usage detected for membership checking")

    # ---------- RECURSION ----------
    elif predicted_pattern == "recursion":
        if features.get("has_recursion", False):
            reasons.append("Recursive function call detected")

        if features.get("num_functions", 0) >= 1:
            reasons.append("Function definition structure found")

    # ---------- STACK ----------
    elif predicted_pattern == "stack":
        if features.get("uses_append", False) and features.get("uses_pop", False):
            reasons.append("LIFO behavior detected using append/pop operations")

    # ---------- TWO POINTER ----------
    elif predicted_pattern == "two_pointer":
        if features.get("num_loops", 0) >= 1:
            reasons.append("Loop-based traversal detected")

        reasons.append("Two index variables likely moving through the array")

    # ---------- FALLBACK ----------
    if not reasons:
        reasons.append(
            "Structural characteristics matched trained model patterns"
        )

    return reasons