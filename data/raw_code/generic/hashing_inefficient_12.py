def duplicate_values(nums):
    tracker = {}
    duplicates = []
    for val in nums:
        tracker[val] = tracker.get(val, 0) + 1
    for key, value in tracker.items():
        if value > 1:
            duplicates.append(key)
    return duplicates