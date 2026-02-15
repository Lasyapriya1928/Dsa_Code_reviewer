def is_valid(s):
    def helper(i, stack):
        if i == len(s):
            return not stack

        if s[i] in "([{":
            return helper(i + 1, stack + [s[i]])

        if not stack:
            return False

        top = stack[-1]
        if (top, s[i]) not in [("(", ")"), ("{", "}"), ("[", "]")]:
            return False

        return helper(i + 1, stack[:-1])

    return helper(0, [])
"""has_recursion = 1
uses_list = 1
num_loops = 0
"""