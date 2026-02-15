def is_valid(s):
    prev = None
    while s != prev:
        prev = s
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return s == ""
#Pattern: BruteForce
#Time: O(n²)
#Space: O(1)

"""num_loops = 2
max_loop_depth = 2
uses_list = 0
uses_dict = 0
has_recursion = 0
lines_of_code = small
num_functions = 1
"""