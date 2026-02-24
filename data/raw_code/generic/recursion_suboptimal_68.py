def reverse_words(words, i=0):
    if i == len(words):
        return []
    rest = reverse_words(words, i + 1)
    rest.append(words[i])
    return rest