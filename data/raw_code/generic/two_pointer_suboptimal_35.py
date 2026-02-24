def find_triplet_sum(nums, target):
    nums.sort()
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == target:
                return True
            if s < target:
                left += 1
            else:
                right -= 1
    return False