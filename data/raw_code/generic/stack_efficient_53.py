def evaluate_infix_simple(expr):
    stack = []
    num = 0
    sign = '+'
    for ch in expr + '+':
        if ch.isdigit():
            num = num * 10 + int(ch)
        else:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            sign = ch
            num = 0
    return sum(stack)