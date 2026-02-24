def calculate_bracket_value(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            val = 0
            while stack and stack[-1] != '(':
                val += stack.pop()
            stack.pop()
            stack.append(max(2 * val, 1))
    return sum(stack)