def LCS(X, Y, m, n):
    if m >= 0 and n >= 0:
        if X[m] == Y[n]:
            return LCS(X, Y, m-1, n-1) + 1
        else:
            return max(LCS(X, Y, m-1, n), LCS(X, Y, m, n-1))
    else:
        return 0

t = int(input())
for _ in range(t):
    x, y = input().split()
    print(LCS(x, y, len(x)-1, len(y)-1))
