def exchange(coins, k):
    dp = [k+1] * (k+1)
    dp[0] = 0
    for i in range(1, k+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[k] if dp[k] <= k else -1

coins = list(map(int, input().split()))
k = int(input())
print(exchange(coins, k))


"""
1, 5, 10, 21, 25
"""
