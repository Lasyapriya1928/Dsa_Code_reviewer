def generate_parentheses(n):
    if n == 0:
        return [""]
    result = []
    for i in range(n):
        for left in generate_parentheses(i):
            for right in generate_parentheses(n - i - 1):
                result.append("(" + left + ")" + right)
    return result