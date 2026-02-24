def nested_parentheses_count(s):
    stack = []
    depth = 0
    for ch in s:
        if ch == '(':
            stack.append(ch)
            depth = max(depth, len(stack))
        elif ch == ')':
            if stack:
                stack.pop()
    return depth