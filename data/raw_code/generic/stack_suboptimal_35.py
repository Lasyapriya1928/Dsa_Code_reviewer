def compare_strings(a, b):
    def build(x):
        stack = []
        for ch in x:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
    return build(a) == build(b)
