import sys
input = sys.stdin.readline

def max_dp(num, lines, dp):
    dp = [[0]*3 for _ in range(num)]
    dp[0][0] = lines[0][0]
    dp[0][1] = lines[0][1]
    dp[0][2] = lines[0][2]

    for i in range(1, num):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + lines[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + lines[i][1]
        dp[i][2] = max(dp[i-1][1], dp[i-1][2]) + lines[i][2]

    return max(dp[n-1][0], dp[n-1][1], dp[n-1][2])

def min_dp(num, lines, dp):
    dp = [[0]*3 for _ in range(num)]
    dp[0][0] = lines[0][0]
    dp[0][1] = lines[0][1]
    dp[0][2] = lines[0][2]

    for i in range(num):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + lines[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + lines[i][1]
        dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + lines[i][2]

    return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])

n = int(input())
n_list = []
for _ in range(n):
    n_list.append(list(map(int, input().split())))

dp_table = [[0]*3 for _ in range(n)]
print(max_dp(n, n_list, dp_table), min_dp(n, n_list, dp_table))
