def postfix_to_infix(tokens):
    stack = []
    for token in tokens:
        if token in "+-":
            b = stack.pop()
            a = stack.pop()
            stack.append("(" + a + token + b + ")")
        else:
            stack.append(token)
    return stack.pop()