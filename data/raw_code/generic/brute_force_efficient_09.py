def check_palindrome_pairs(words):
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                combined = words[i] + words[j]
                if combined == combined[::-1]:
                    return True
    return False