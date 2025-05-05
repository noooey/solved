def exchange(k, coins, memo=None):
    if memo == None:
        memo = [k+1] * (k+1)
    if memo[k] <= k:
        return memo[k]
    if k == 0:
        return 0
    elif k < 0:
        return float('inf')

    min_cnt = k+1
    for coin in coins:
        min_cnt = min(min_cnt, exchange(k-coin, coins, memo)+1)

    memo[k] = min_cnt
    return min_cnt

t = int(input())
for _ in range(t):
    k = int(input())
    n, *coins = map(int, input().split())
    print(exchange(k, coins))
