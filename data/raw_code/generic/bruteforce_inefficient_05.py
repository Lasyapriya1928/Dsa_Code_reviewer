def brute_force_palindrome(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                return True
    return False

#Pattern: bruteforce
