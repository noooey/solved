def LCS(memo, X, Y, m, n):
    if m == 0 or n == 0:
        return 0

    if memo[m][n] != -1:
        return memo[m][n]

    if X[m-1] == Y[n-1]:
        memo[m][n] = LCS(memo, X, Y, m-1, n-1) + 1
    else:
        memo[m][n] = max(LCS(memo, X, Y, m-1, n), LCS(memo, X, Y, m, n-1))

    return memo[m][n]

def main():
    t = int(input())
    for _ in range(t):
        x, y = input().split()
        memo = [[-1] * (len(y)+1) for _ in range(len(x)+1)]
        result = LCS(memo, x, y, len(x), len(y))
        print(result)

if __name__ == "__main__":
    main()



"""
abcdefghijklmnopqrstuvwxyz
zyxwvutsrqponmlkjihgfedcba
"""
