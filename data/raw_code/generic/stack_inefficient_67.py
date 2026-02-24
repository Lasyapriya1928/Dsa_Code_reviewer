def build_number(expr):
    stack = []
    current = ""
    for ch in expr:
        if ch.isdigit():
            current += ch
        else:
            if current:
                stack.append(int(current))
                current = ""
            stack.append(ch)
    if current:
        stack.append(int(current))
    return stack