import sys
input = sys.stdin.readline

dp = [1, 1, 1, 2, 2]

def padovan(N):
    for i in range(len(dp), N):
        dp.append(dp[i-1] + dp[i-5])

def solution(n):
    padovan(n)
    return dp[n-1]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solution(int(input())))
