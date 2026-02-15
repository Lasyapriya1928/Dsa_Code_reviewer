def length_of_longest_substring(s):
    max_len = 0
    n = len(s)

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)

    return max_len

#Pattern: BruteForce
#Time: O(n²)
#Space: O(n)

"""num_loops = 2
max_loop_depth = 2
uses_set = 1
uses_dict = 0
has_recursion = 0
num_functions = 1
lines_of_code = medium
"""