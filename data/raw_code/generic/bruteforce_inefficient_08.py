def max_difference(nums):
    n = len(nums)
    max_diff = float('-inf')

    for i in range(n):
        for j in range(n):
            if i != j:
                diff = nums[j] - nums[i]
                if diff > max_diff:
                    max_diff = diff

    return max_diff


nums = [7, 1, 5, 3, 6, 4]
print(max_difference(nums))