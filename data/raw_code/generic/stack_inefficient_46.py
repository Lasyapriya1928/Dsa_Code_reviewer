def remove_invalid_closing(s):
    stack = []
    result = []
    for ch in s:
        if ch == ')':
            if stack:
                stack.pop()
                result.append(ch)
        else:
            stack.append(ch)
            result.append(ch)
    return "".join(result)