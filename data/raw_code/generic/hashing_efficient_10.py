def longest_consecutive(nums):
    numbers = set(nums)
    longest = 0
    for n in numbers:
        if n - 1 not in numbers:
            length = 1
            while n + length in numbers:
                length += 1
            if length > longest:
                longest = length
    return longest