def is_valid(s):
    count = 0
    for ch in s:
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0
"""num_loops = 1
uses_list = 0
uses_dict = 0
"""