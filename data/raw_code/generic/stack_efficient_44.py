def calculate_min_add(s):
    stack = []
    balance = 0
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                balance += 1
    return balance + len(stack)