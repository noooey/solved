import sys
input = sys.stdin.readline

def solutions(N, A):
    dp = [0 for _ in range(N)]
    dp[0] = A[0]
    for i in range(1, N):
        dp[i] = max(A[i] + dp[i-1], A[i])
    return max(dp)

n = int(input())
arr = list(map(int, input().split()))
print(solutions(n, arr))
