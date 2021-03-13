
def fib(n):
    # initial table
    tabl = [0 for x in range(n+1)]
    tabl[1] = 1

    for i in range(n):
        tabl[i+1] += tabl[i]
        if i < n-1:
            tabl[i+2] += tabl[i]
    print(tabl)
    return tabl[n]