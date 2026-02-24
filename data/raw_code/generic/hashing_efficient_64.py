def first_duplicate_index(nums):
    visited = {}
    for i in range(len(nums)):
        if nums[i] in visited:
            return i
        visited[nums[i]] = True
    return -1