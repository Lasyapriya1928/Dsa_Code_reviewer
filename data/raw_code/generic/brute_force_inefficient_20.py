def longest_increasing_pair(nums):
    best = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] > nums[i]:
                length = j - i
                if length > best:
                    best = length
    return best