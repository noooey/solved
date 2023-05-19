t = int(input())

for _ in range(t):
    n, p = map(int, input().split())

    dp = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        if i == p:
            dp[i] = n
        else:
            dp[i] = min(dp[i-1], dp[i-2]) + 1

    print(dp[n])
