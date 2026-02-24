def first_pair_product(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                if nums[i] * nums[j] == target:
                    return (nums[i], nums[j])
    return None