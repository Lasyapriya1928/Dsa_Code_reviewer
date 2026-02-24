def contains_duplicate(nums):
    for idx in range(len(nums)):
        other = 0
        while other < len(nums):
            if idx != other:
                if nums[idx] == nums[other]:
                    return True
            other += 1
    return False