n, m = map(int, input().split())
k = int(input())
road = []
for _ in range(k):
    road.append(list(map(int, input().split())))

dp = [[0]*(n+1) for _ in range(m+1)]
dp[0][0] = 1

def check(cur, a, b, c, d):
    if cur == [a, b, c, d] or cur == [c, d, a, b]:
        return True
    else:
        False

for i in range(m+1):
    for j in range(n+1):
        if i > 0:
            for a, b, c, d in road:
                if check([j, i-1, j, i], a, b, c, d):
                    break
            else:
                dp[i][j] += dp[i-1][j]
        if j > 0:
            for a, b, c, d in road:
                if check([j-1, i, j, i], a, b, c, d):
                    break
            else:
                dp[i][j] += dp[i][j-1]

print(dp[-1][-1])
