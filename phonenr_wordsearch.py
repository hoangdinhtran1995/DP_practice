
def phonenr_wordsearch(numberstr, words):
    # convert words into numberstrings
    interpretor = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
    output_list = []
    for word in words:
        word2nums = ''
        for i in range(len(word)):
            word2nums += str(interpretor[ord(word[i])-97])
        if word2nums in numberstr:
            output_list.append(word)
    return output_list

