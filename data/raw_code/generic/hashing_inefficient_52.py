def swap_key_value(d):
    result = {}
    for key, value in d.items():
        result[value] = key
    return result