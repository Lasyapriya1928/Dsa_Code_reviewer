def stack_valid_parentheses(s):
    stack = []

    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

#Pattern: stack
