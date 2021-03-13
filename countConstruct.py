
def countConstruct(targ_word, words):
    tabl = [0 for _ in range(len(targ_word)+1)]
    tabl[0] = 1

    for i in range(len(targ_word)):

        for word in words:
            if i + len(word) <= len(targ_word):
                if targ_word[i:i+len(word)] == word:
                    tabl[i+len(word)] += tabl[i]

    print(tabl)
    return tabl[-1]
