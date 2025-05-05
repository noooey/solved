n = int(input())

if n % 2 == 1:
    print(0)
else:
    dp = [0]*(n+1)
    dp[0] = 1
    dp[2] = dp[0] + 2
    # dp[4] = dp[2]*dp[2] + 2
    # dp[6] = dp[2]**3 + dp[2]*dp[4]*2 + 2 = 27 + 54 + 2 = 83
    # dp[8] = dp[2]**4 + dp[2]*dp[4]*3 + dp[4]*dp[4] + 2
    # dp[10] = dp[2]**5 + dp[2]

    for i in range(4, n+1, 2):
        tmp = i // 2
        dp[i] = dp[i-2]*2 + dp[i-2]
    print(dp[n])


"""
- n이 짝수여야 완전히 채울 수 있음
- 가로타일은 필수고, 세로 타일의 유무가 중요
"""
