def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
#Pattern: Hashing
#Time: O(n)
#Space: O(n)

"""num_loops = 2
max_loop_depth = 2
uses_set = 1
uses_dict = 0
has_recursion = 0
num_functions = 1
lines_of_code = medium
"""