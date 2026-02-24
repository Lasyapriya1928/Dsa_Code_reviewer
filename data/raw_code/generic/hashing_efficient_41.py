def find_all_indices(nums):
    positions = {}
    for idx, value in enumerate(nums):
        if value not in positions:
            positions[value] = []
        positions[value].append(idx)
    return positions