def LCS(X, Y):
    m, n = len(X), len(Y)
    memo = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 1
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

    return memo[m][n]

t = int(input())
for _ in range(t):
    x, y = input().split()
    result = LCS(x, y)
    print(result)



"""
abcdefghijklmnopqrstuvwxyz
zyxwvutsrqponmlkjihgfedcba
"""
