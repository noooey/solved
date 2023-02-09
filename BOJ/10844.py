n = int(input())
dp = [[0]*10 for _ in range(n+1)]

for k in range(1, 10):
    dp[1][k] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


print(sum(dp[n])%1000_000_000)
