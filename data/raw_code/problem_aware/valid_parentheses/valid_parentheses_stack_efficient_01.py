def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)

    return not stack
#Pattern: Stack
#Time: O(n)
#Space: O(n)

"""num_loops = 1
max_loop_depth = 1
uses_list = 1      # stack
uses_dict = 1      # mapping
has_recursion = 0
lines_of_code = medium
num_functions = 1
"""