def max_pair_sum(nums):
    maximum = float("-inf")
    for x in nums:
        for y in nums:
            if x != y:
                s = x + y
                if s > maximum:
                    maximum = s
    return maximum