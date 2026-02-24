def invert_dict(d):
    inverted = {}
    for key in d:
        value = d[key]
        inverted[value] = key
    return inverted