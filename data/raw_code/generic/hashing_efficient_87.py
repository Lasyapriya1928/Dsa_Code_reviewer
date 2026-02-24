def longest_consecutive_sequence(nums):
    values = set(nums)
    longest = 0
    for n in values:
        if n - 1 not in values:
            current = n
            length = 1
            while current + 1 in values:
                current += 1
                length += 1
            if length > longest:
                longest = length
    return longest