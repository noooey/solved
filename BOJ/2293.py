import sys
input = sys.stdin.readline

def solutions(n, coins, k):
    dp = [0]*(k+1)

    for coin in coins:
        dp[coin] = 1
        com[coin].append([coin])

    for i in range(1, k+1):
        for coin in coins:
            if i - coin > 0:
                dp[i] += dp[i-coin]
    return dp[k]

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

print(solutions(n, coins, k))
