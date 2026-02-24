def contains_nearby_duplicate(nums, k):
    last_seen = {}
    for i in range(len(nums)):
        val = nums[i]
        if val in last_seen:
            if i - last_seen[val] <= k:
                return True
        last_seen[val] = i
    return False