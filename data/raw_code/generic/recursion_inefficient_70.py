def generate_binary(n):
    if n == 0:
        return [""]
    smaller = generate_binary(n - 1)
    result = []
    for s in smaller:
        result.append("0" + s)
        result.append("1" + s)
    return result