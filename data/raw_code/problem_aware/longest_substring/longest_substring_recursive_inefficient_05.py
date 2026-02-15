def helper(s, i, seen):
    if i == len(s) or s[i] in seen:
        return len(seen)

    return max(
        helper(s, i + 1, seen | {s[i]}),
        helper(s, i + 1, set())
    )

def length_of_longest_substring(s):
    return helper(s, 0, set())
"""has_recursion = 1
uses_set = 1
num_loops = 0
"""