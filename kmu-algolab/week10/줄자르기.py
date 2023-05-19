"""
p = q + m
m = p - q
n = p + q
n - m = 2*q
(n - m) / 2 = q
"""
def solution():
    n, m = map(int, input().split())
    if n == 1:
        return 1

    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[n] = smu()

    for item in n_list:
        if item > m:

        elif item % 2 == 0:

        elif (item + m) % 2 == 0:

        cnt += 1
    return cnt % 10007

t = int(input())
for _ in range(t):
    print(solution())
