def stack_reverse_string(s):
    stack = []

    for char in s:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string
