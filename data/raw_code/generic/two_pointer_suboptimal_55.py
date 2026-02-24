def find_triplet_zero(nums):
    nums.sort()
    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                return True
            if total < 0:
                l += 1
            else:
                r -= 1
    return False