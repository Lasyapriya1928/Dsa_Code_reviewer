def count_by_category(nums):
    categories = {}
    for value in nums:
        key = value % 3
        if key not in categories:
            categories[key] = 0
        categories[key] += 1
    return categories