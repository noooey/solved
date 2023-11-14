def LCS(memo, X, Y, m, n):
    if m > 0 and n > 0:
        if X[m-1] == Y[n-1]:
            if memo[m-1][n-1] != 0:
                memo[m][n] = memo[m-1][n-1] + 1
            else:
                memo[m][n] = LCS(memo, X, Y, m-1, n-1) + 1
            return memo[m][n]
        else:
            if memo[m-1][n] != 0 or memo[m][n-1] != 0:
                memo[m][n] = max(memo[m-1][n], memo[m][n-1])
                return memo[m][n]
            return max(LCS(memo, X, Y, m-1, n), LCS(memo, X, Y, m, n-1))
    else:
        return 0

t = int(input())
for _ in range(t):
    x, y = input().split()
    memo = [[0]*(len(y)+1) for _ in range(len(x)+1)]
    print(LCS(memo, x, y, len(x), len(y)))


"""
abcdefghijklmnopqrstuvwxyz
zyxwvutsrqponmlkjihgfedcba
"""
