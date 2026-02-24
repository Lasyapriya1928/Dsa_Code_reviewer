def word_count(sentence):
    words = sentence.split()
    counter = {}
    for word in words:
        if word not in counter:
            counter[word] = 0
        counter[word] += 1
    return counter