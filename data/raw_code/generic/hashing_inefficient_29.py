def group_by_first_letter(words):
    buckets = {}
    for w in words:
        first = w[0]
        if first in buckets:
            buckets[first].append(w)
        else:
            buckets[first] = [w]
    result = []
    for key in buckets:
        result.extend(buckets[key])
    return result