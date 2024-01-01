"""
failed, 1퍼에서 틀렸다캄 예제 맞음
"""
n, m = map(int, input().split())
k = int(input())
road_info = {}
for _ in range(k):
    a, b, c, d = map(int, input().split())
    if (a + b) > (c + d):
        if (a, b) in road_info.keys():
            road_info[(a, b)].append((c, d))
        else:
            road_info[(a, b)] = [(c, d)]
    else:
        if (c, d) in road_info.keys():
            road_info[(c, d)].append((a, b))
        else:
            road_info[(c, d)] = [(a, b)]

dp = [[0]*(n+1) for _ in range(m+1)]

for i in range(1, n+1):
    if (i, 0) in road_info.keys():
        if road_info[(i, 0)][0] == (i-1, 0):
            break
    dp[0][i] = 1

for i in range(1, m+1):
    if (0, i) in road_info.keys():
        if road_info[(0, i)][0] == (0, i-1):
            break
    dp[i][0] = 1

for i in range(1, m+1):
    for j in range(1, n+1):
        if (j, i) in road_info.keys():
            if len(road_info[(j, i)]) == 2: # 둘 다 막힘
                dp[i][j] = 0
            else: # 한 쪽 막힘
                if road_info[(j, i)][0] == (j-1, i):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp)
print(dp[m][n])
