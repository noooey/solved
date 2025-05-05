n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(2)]
dp[0][0], dp[1][0] = s

cannot = False
for i in range(1, n+1):
    up = dp[0][i-1]+v[i-1]
    down = dp[i-1]-v[i-1]
    if up > m and down < 0:
        cannot = True
        break
    elif up <= m and down < 0:
        dp[i] = up
    elif up > m and down >= 0:
        dp[i] = down
    else:
        dp[i] = max(up, down)

print(dp)

if cannot:
    print(-1)
else:
    print(dp[n])
