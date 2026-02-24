def house_robber_circular(nums):
    def rob(arr):
        prev = curr = 0
        for num in arr:
            prev, curr = curr, max(curr, prev + num)
        return curr
    if len(nums) == 1:
        return nums[0]
    return max(rob(nums[:-1]), rob(nums[1:]))