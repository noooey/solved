def getSeq(dp, x, y, m, n):
    seq = []
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            seq.append(x[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(seq))

def LCS(x, y):
    m = len(x)
    n = len(y)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n], getSeq(dp, x, y, m, n)

def main():
    t = int(input())
    for _ in range(t):
        x, y = input().split()
        value, seq = LCS(x, y)
        print(value, seq)

if __name__ == "__main__":
    main()
