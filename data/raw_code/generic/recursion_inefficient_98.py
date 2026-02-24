def generate_permutations(chars):
    if len(chars) <= 1:
        return [chars]
    result = []
    for i in range(len(chars)):
        rest = chars[:i] + chars[i+1:]
        for p in generate_permutations(rest):
            result.append(chars[i] + p)
    return result