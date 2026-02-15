# Implementation — Complexity Estimator
def estimate_time_complexity(features: dict) -> dict:
    num_loops = features.get("num_loops", 0)
    max_depth = features.get("max_loop_depth", 0)
    has_recursion = features.get("has_recursion", 0)

    # Case 1: No loops, no recursion
    if num_loops == 0 and not has_recursion:
        return {
            "time_complexity": "O(1)",
            "explanation": "No loops or recursion detected, indicating constant time complexity."
        }

    # Case 2: Recursion only
    if num_loops == 0 and has_recursion:
        return {
            "time_complexity": "O(n)",
            "explanation": "Recursive calls detected without loops, suggesting linear time complexity."
        }

    # Case 3: Single loop
    if num_loops == 1 and max_depth == 1 and not has_recursion:
        return {
            "time_complexity": "O(n)",
            "explanation": "A single loop was detected with no nesting, resulting in linear time complexity."
        }

    # Case 4: Nested loops
    if max_depth >= 2 and not has_recursion:
        return {
            "time_complexity": f"O(n^{max_depth})",
            "explanation": f"{max_depth} levels of nested loops detected, indicating polynomial time complexity."
        }

    # Case 5: Loop + recursion
    if num_loops >= 1 and has_recursion:
        return {
            "time_complexity": "O(n log n)",
            "explanation": "Both loops and recursion were detected, often seen in divide-and-conquer algorithms."
        }

    # Fallback
    return {
        "time_complexity": "Unknown",
        "explanation": "The time complexity could not be determined confidently using static rules."
    }
# test
if __name__ == "__main__":
    features = {
        'num_loops': 1,
        'max_loop_depth': 1,
        'has_recursion': 0,
        'uses_dict': 1
    }

    print(estimate_time_complexity(features))

