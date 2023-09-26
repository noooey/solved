def matrix_mult(A, B):
    tmp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                tmp[i][j] += (A[i][k] * B[k][j]) % 1000
                tmp[i][j] %= 1000
    return tmp

def matrix_pow(n, M):
    if n == 0:
        return [[1, 0], [0, 1]] 
    if n % 2 == 0:
        tmp = matrix_pow(n//2, M)
        return matrix_mult(tmp, tmp)
    else:
        tmp = matrix_pow(n-1, M)
        return matrix_mult(M, tmp)

A = [[1, 1], [1, 0]]
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        print(matrix_pow(n-1, A)[0][0] % 1000)
