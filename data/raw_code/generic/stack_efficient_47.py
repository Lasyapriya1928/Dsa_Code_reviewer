def evaluate_parentheses_score(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(0)
        else:
            val = stack.pop()
            score = 1 if val == 0 else 2 * val
            if stack:
                stack[-1] += score
            else:
                stack.append(score)
    return stack[0]