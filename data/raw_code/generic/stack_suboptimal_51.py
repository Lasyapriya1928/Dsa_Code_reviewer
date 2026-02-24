def check_balanced_types(s):
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0