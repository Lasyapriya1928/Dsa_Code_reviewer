def parentheses_depth(s):
    stack = []
    max_depth = 0
    for ch in s:
        if ch == '(':
            stack.append(ch)
            max_depth = max(max_depth, len(stack))
        elif ch == ')':
            stack.pop()
    return max_depth