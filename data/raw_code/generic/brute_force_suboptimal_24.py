def count_smaller_after(nums):
    result = []
    for i in range(len(nums)):
        c = 0
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                c += 1
        result.append(c)
    return result