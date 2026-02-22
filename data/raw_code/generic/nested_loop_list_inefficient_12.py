def count_frequency(nums):
    result = []

    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        result.append((nums[i], count))

    return result


nums = [1, 2, 1, 3, 2]
print(count_frequency(nums))