def categorize_numbers(nums):
    categories = {}
    for n in nums:
        key = n % 5
        if key not in categories:
            categories[key] = []
        categories[key].append(n)
    return categories