def invert_mapping(d):
    result = {}
    for key in d:
        value = d[key]
        result[value] = key
    return result