def binCoeff(n, k):
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i+1, k+1)):
            if (j == 0) or (i == j):
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    return dp[n][k]

n, k = map(int, input().split())
print(binCoeff(n, k))
