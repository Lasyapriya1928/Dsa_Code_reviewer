def count_down(n):
    if n <= 0:
        return []
    result = [n]
    result.extend(count_down(n - 1))
    return result