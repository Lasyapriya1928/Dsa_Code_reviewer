def count_unique_values(nums):
    visited = set()
    for n in nums:
        visited.add(n)
    return len(visited)