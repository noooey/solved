def exchange(coins, k):
    n = len(coins)
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, k+1):
            # 해당 동전 미포함
            exclude_coin = dp[i-1][j]
            # 해당 동전 포함
            include_coin = dp[i][j-coins[i-1]] if j - coins[i-1] >= 0 else 0

            dp[i][j] = exclude_coin + include_coin

    print(dp)
    return dp[n][k]

coins = list(map(int, input().split()))
k = int(input())
print(exchange(coins, k))
