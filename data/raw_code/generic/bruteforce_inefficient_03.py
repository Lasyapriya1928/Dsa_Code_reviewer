def brute_force_string_match(s, pattern):
    for i in range(len(s)):
        match = True
        for j in range(len(pattern)):
            if i + j >= len(s) or s[i + j] != pattern[j]:
                match = False
                break
        if match:
            return True
    return False

#Pattern: bruteforce
