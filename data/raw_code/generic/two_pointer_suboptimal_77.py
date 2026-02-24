def count_palindromes_simple(s):
    left = 0
    right = len(s) - 1
    count = 0
    while left <= right:
        if s[left] == s[right]:
            count += 1
        left += 1
        right -= 1
    return count