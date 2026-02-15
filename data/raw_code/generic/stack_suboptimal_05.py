def stack_evaluate_rpn(tokens):
    stack = []

    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            stack.append(eval(f"{a}{token}{b}"))
        else:
            stack.append(int(token))

    return stack[0]

#Pattern: stack
