
def gridtraveler(m,n):
    tabl = [[0 for _ in range(n+1)] for _ in range(m+1)]
    tabl[1][1] = 1
    for M in range(m+1):
        for N in range(n+1):
            if M < m:
                tabl[M+1][N] += tabl[M][N]
            if N < n:
                tabl[M][N+1] += tabl[M][N]
    return tabl[m][n]