def contains_duplicate(arr):
    visited = set()
    i = 0
    while i < len(arr):
        if arr[i] in visited:
            return True
        visited.add(arr[i])
        i += 1
    return False