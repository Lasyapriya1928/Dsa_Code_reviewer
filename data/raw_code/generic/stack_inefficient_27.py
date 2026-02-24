def min_brackets_to_add(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ch)
    return len(stack)