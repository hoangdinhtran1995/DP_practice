
def allConstruct(target_word, words):
    tabl = [[] for _ in range(len(target_word)+1)]
    tabl[0] = [[]]

    for i in range(len(target_word)):
        for word in words:
            if i+len(word) <= len(target_word):
                if target_word[i:i+len(word)] == word:
                    for w in tabl[i]:
                        tabl[i+len(word)].extend([w + [word]])

    return tabl[-1]