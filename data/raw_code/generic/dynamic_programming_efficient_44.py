def max_product_subarray(nums):
    dp_max = nums[0]
    dp_min = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        temp = dp_max
        dp_max = max(nums[i], nums[i]*dp_max, nums[i]*dp_min)
        dp_min = min(nums[i], nums[i]*temp, nums[i]*dp_min)
        result = max(result, dp_max)
    return result