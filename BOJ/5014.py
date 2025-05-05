F, S, G, U, D = map(int, input().split())
dp = [0]*(F+1)

for i in range(S, F):
    print(dp)
    if i-U > 0 and i+D <= F:
        dp[i] = min(dp[i-U], dp[i+D]) + 1
    elif i-U > 0:
        dp[i] = dp[i-U] + 1
    elif i+D <= F:
        dp[i] = dp[i+D] + 1

print(dp[G])
