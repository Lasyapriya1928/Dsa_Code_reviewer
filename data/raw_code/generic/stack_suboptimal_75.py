def simulate_stack_sequence(seq):
    stack = []
    output = []
    for val in seq:
        stack.append(val)
        if len(stack) > 2:
            output.append(stack.pop())
    return output