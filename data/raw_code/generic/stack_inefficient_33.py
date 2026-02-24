def count_valid_pairs(s):
    stack = []
    count = 0
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if stack:
                stack.pop()
                count += 1
    return count