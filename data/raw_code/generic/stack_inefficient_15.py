def validate_stack_sequences(pushed, popped):
    stack = []
    j = 0
    for val in pushed:
        stack.append(val)
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return not stack