def reverse_words_stack(sentence):
    stack = []
    word = ""
    for ch in sentence:
        if ch == " ":
            stack.append(word)
            word = ""
        else:
            word += ch
    stack.append(word)
    result = []
    while stack:
        result.append(stack.pop())
    return " ".join(result)