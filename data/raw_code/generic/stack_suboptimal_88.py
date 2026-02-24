def check_stack_palindrome(s):
    stack = []
    for ch in s:
        stack.append(ch)
    for ch in s:
        if ch != stack.pop():
            return False
    return True