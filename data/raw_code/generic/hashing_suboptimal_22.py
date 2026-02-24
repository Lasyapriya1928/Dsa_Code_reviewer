def has_duplicate_values(data):
    memory = set()
    for value in data:
        if value in memory:
            return True
        else:
            memory.add(value)
    return False