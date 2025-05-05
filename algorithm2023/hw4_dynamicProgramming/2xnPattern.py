def pattern(n):
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 2
    if n <= 2:
        return dp[n]

    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]

    return dp[n]

n = int(input())
print(pattern(n))



"""
2x2
11 =

2x3
111 =1 1=

2x4
1111 11= =11 == 1=1
"""
