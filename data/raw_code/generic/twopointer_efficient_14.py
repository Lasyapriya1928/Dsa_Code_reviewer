def pair_with_difference(nums, k):
    left = 0
    right = 1

    while right < len(nums):
        diff = nums[right] - nums[left]

        if diff == k:
            return True
        elif diff < k:
            right += 1
        else:
            left += 1
            if left == right:
                right += 1

    return False


print(pair_with_difference([1,3,5,7,9], 4))