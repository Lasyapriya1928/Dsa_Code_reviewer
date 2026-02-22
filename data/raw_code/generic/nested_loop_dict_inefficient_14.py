def match_dict_values(dict1, dict2):
    matches = []

    for key1 in dict1:
        for key2 in dict2:
            if key1 == key2:
                matches.append((key1, dict1[key1], dict2[key2]))

    return matches


d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 4, "c": 5, "d": 6}
print(match_dict_values(d1, d2))