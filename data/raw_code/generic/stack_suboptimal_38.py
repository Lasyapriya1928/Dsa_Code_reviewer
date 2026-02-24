def evaluate_simple(expr):
    stack = []
    num = 0
    for ch in expr:
        if ch.isdigit():
            num = num * 10 + int(ch)
        else:
            stack.append(num)
            stack.append(ch)
            num = 0
    stack.append(num)
    return stack