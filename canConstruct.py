
def canConstruct_tab(targ_word, words):
    tabl = [False for _ in range(len(targ_word)+1)]
    tabl[0] = True

    for i in range(len(targ_word)):
        if tabl[i]:
            for word in words:
                if targ_word[i:i+len(word)] == word:
                    if i+len(word) <= len(targ_word):
                        tabl[i+len(word)] = True

    return tabl[-1]
