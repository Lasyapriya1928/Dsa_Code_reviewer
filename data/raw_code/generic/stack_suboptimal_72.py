def check_redundant_parentheses(expr):
    stack = []
    for ch in expr:
        if ch == ')':
            count = 0
            while stack and stack[-1] != '(':
                stack.pop()
                count += 1
            stack.pop()
            if count <= 1:
                return True
        else:
            stack.append(ch)
    return False