def collect_word_lengths(words):
    bucket = {}
    for w in words:
        length = len(w)
        if length not in bucket:
            bucket[length] = []
        bucket[length].append(w)
    flattened = []
    for key in bucket:
        flattened.extend(bucket[key])
    return flattened