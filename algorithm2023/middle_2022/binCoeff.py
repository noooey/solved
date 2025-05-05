def binCoeff(n, k):
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp[n][k]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(binCoeff(n, k)%1000)
