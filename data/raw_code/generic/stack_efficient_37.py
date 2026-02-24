def remove_unbalanced(s):
    stack = []
    result = []
    for ch in s:
        if ch == '(':
            stack.append(len(result))
            result.append(ch)
        elif ch == ')':
            if stack:
                stack.pop()
                result.append(ch)
        else:
            result.append(ch)
    while stack:
        idx = stack.pop()
        result[idx] = ''
    return "".join(result)