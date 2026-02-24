def remove_outer_parentheses(s):
    stack = []
    result = []
    for ch in s:
        if ch == '(':
            if stack:
                result.append(ch)
            stack.append(ch)
        else:
            stack.pop()
            if stack:
                result.append(ch)
    return "".join(result)