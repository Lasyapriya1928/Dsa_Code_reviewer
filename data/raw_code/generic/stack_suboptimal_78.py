def stack_difference(a, b):
    stack = list(a)
    for val in b:
        if stack and stack[-1] == val:
            stack.pop()
    return stack