def evaluate_boolean(expr):
    stack = []
    for token in expr:
        if token in "01":
            stack.append(int(token))
        elif token == '&':
            b = stack.pop()
            a = stack.pop()
            stack.append(a & b)
    return stack[-1]