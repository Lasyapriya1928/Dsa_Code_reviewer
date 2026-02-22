def group_by_frequency(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    result = []
    for key in freq:
        result.append((key, freq[key]))

    return result


nums = [1, 2, 2, 3, 3, 3]
print(group_by_frequency(nums))