import sys
input = sys.stdin.readline

def solution(n, m):
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(1, n+1):

        if i % 2 == 0:
            dp[i] += dp[i//2]*dp[i//2]
            if i//2 == m:
                continue
        if i > m:
            dp[i] += dp[i-m]*dp[m]
        if i > m and i-m > 1 and (i-m)%2 == 0:
            if (i-m)//2 == m and (i+m)//2 == i-m:
                continue
            dp[i] += dp[(i-m)//2]*dp[(i+m)//2]
        if dp[i] == 0:
            dp[i] = 1

    return dp[n]


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solution(n, m) % 10007)
