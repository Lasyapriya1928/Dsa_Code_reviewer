def calculate_score(s):
    stack = []
    for ch in s:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == '+':
                stack.append(a + b)
            elif ch == '*':
                stack.append(a * b)
    return stack[-1]