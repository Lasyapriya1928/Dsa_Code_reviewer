def count_smaller_elements(nums):
    n = len(nums)
    result = []

    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] < nums[i]:
                count += 1
        result.append(count)

    return result


nums = [8, 1, 2, 2, 3]
print(count_smaller_elements(nums))