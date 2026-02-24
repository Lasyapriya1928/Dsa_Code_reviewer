def clean_brackets(s):
    stack = []
    result = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
            result.append(ch)
        elif ch == ')':
            if stack:
                stack.pop()
                result.append(ch)
        else:
            result.append(ch)
    return "".join(result)