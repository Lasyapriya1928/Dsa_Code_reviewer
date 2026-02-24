def pair_product_exists(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and nums[i] * nums[j] == target:
                return True
    return False