def max_subarray(nums):
    max_sum = float('-inf')
    n = len(nums)

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)

    return max_sum
#Pattern: BruteForce
#Time: O(n²)
#Space: O(1)