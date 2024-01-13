import sys
input = sys.stdin.readline

def solutions(n, board):
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            if i == n-1 and j == n-1: # 가장 오른쪽 아래칸 도달
                return dp[i][j]
            dist = board[i][j]
            if i + dist < n:
                dp[i + dist][j] += dp[i][j]
            if j + dist < n:
                dp[i][j+dist] += dp[i][j]

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

print(solutions(N, board))


"""
def solutions(N, B):
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            if i == N-1 and j == N-1:
                return dp[i][j]
            d = B[i][j]
            if j + d < N:
                dp[i][j+d] += dp[i][j]
            if i + d < N:
                dp[i+d][j] += dp[i][j]
"""
