def generate_range(start, end):
    if start > end:
        return []
    return [start] + generate_range(start + 1, end)