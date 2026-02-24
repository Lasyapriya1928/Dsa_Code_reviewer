def group_by_length(words):
    result = {}
    for word in words:
        l = len(word)
        if l not in result:
            result[l] = []
        result[l].append(word)
    final = []
    for key in result:
        final.append(result[key])
    return final