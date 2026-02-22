def max_product(nums):
    max_so_far = nums[0]
    min_so_far = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        temp_max = max(nums[i], max_so_far * nums[i], min_so_far * nums[i])
        min_so_far = min(nums[i], max_so_far * nums[i], min_so_far * nums[i])
        max_so_far = temp_max
        result = max(result, max_so_far)

    return result


print(max_product([2,3,-2,4]))