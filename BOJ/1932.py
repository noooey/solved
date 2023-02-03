import sys
input = sys.stdin.readline

def solution(N):
    trg = []
    dp = []
    for _ in range(N):
        line = list(map(int, input().split()))
        trg.append(line)
        dp.append([0]*len(line))

    dp[0][0] = trg[0][0]

    for i in range(1, N):
        for j in range(0, i+1):
            if j == 0:
                dp[i][j] += dp[i-1][j] + trg[i][j]
            elif j == i:
                dp[i][j] += dp[i-1][j-1] + trg[i][j]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j]) + trg[i][j]

    return max(dp[-1])

if __name__ == "__main__":
    n = int(input())
    print(solution(n))
