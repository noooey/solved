import sys
input = sys.stdin.readline

def solutions(n, arr):
    arr = [0] + arr
    dp = [0] + [1]*n

    for i in range(2, n+1):
        j = i-1
        while j > 0:
            if arr[i] > arr[j]:
                dp[i] = max(dp[j] + 1, dp[i])
            j -= 1
    return max(dp)

N = int(input())
A = list(map(int, input().split()))
print(solutions(N, A))
