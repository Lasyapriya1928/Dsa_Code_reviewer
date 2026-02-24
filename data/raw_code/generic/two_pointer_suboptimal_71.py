def count_triplets(nums, target):
    nums.sort()
    count = 0
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == target:
                count += 1
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    return count