def length_of_longest_substring(s):
    n = len(s)
    max_len = 0

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)

    return max_len
"""num_loops = 2
max_loop_depth = 2
uses_set = 1
"""
