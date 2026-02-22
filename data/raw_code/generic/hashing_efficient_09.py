def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            length = 1
            current = num

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


print(longest_consecutive([100, 4, 200, 1, 3, 2]))