def estimate_space_complexity(features: dict) -> dict:
    uses_ds = (
        features.get("uses_list", 0) or
        features.get("uses_dict", 0) or
        features.get("uses_set", 0)
    )

    has_recursion = features.get("has_recursion", 0)

    if not uses_ds and not has_recursion:
        return {
            "space_complexity": "O(1)",
            "explanation": "No auxiliary data structures or recursion detected, indicating constant extra space usage."
        }

    if has_recursion and not uses_ds:
        return {
            "space_complexity": "O(n)",
            "explanation": "Recursive calls require stack space proportional to input size."
        }

    if uses_ds:
        return {
            "space_complexity": "O(n)",
            "explanation": "Auxiliary data structures such as lists, dictionaries, or sets were used, requiring linear extra space."
        }

    return {
        "space_complexity": "Unknown",
        "explanation": "Space complexity could not be determined confidently using static rules."
    }
# test
features = {
    "uses_dict": 1,
    "has_recursion": 0
}

print(estimate_space_complexity(features))
