def pair_product_equals(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        product = nums[left] * nums[right]
        if product == target:
            return True
        if product < target:
            left += 1
        else:
            right -= 1
    return False