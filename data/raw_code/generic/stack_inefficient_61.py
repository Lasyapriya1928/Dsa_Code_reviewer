def reverse_parentheses(s):
    stack = []
    for ch in s:
        if ch == ')':
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            if stack:
                stack.pop()
            stack.extend(temp)
        else:
            stack.append(ch)
    return "".join(stack)