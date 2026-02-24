def all_combinations(chars):
    if not chars:
        return [""]
    result = []
    for combo in all_combinations(chars[1:]):
        result.append(combo)
        result.append(chars[0] + combo)
    return result