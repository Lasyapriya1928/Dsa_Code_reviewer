def first_pair_product_negative(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] * nums[j] < 0:
                    return (nums[i], nums[j])
    return None