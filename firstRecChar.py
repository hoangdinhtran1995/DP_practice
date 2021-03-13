
def first_rec_char(input_string):
    memo = {}
    for i in range(len(input_string)):
        if input_string[i] in memo:
            return input_string[i]
        else:
            memo[input_string[i]] = 1

    return None