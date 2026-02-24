def find_triplet_closest(nums, target):
    nums.sort()
    closest = float("inf")
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if abs(s - target) < abs(closest - target):
                closest = s
            if s < target:
                left += 1
            else:
                right -= 1
    return closest