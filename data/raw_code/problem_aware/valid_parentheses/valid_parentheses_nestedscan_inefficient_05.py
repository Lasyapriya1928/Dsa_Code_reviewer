def is_valid(s):
    pairs = ["()", "{}", "[]"]

    while True:
        found = False
        for pair in pairs:
            if pair in s:
                s = s.replace(pair, "")
                found = True
        if not found:
            break

    return s == ""
"""num_loops = 2
max_loop_depth = 2
uses_list = 1
"""