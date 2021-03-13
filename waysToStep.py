
def ways_to_step(number_of_steps, possible_steps):

    tabl = [0 for _ in range(number_of_steps+1)]
    tabl[0] = 1

    for i in range(number_of_steps):
        for j in possible_steps:
            if i+j <= number_of_steps:
                tabl[i+j] += tabl[i]

    print(tabl)
    return tabl[-1]