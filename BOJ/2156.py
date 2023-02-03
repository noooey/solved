import sys
input = sys.stdin.readline

def solution(N):
    podos = [0]
    for _ in range(N):
        podos.append(int(input()))

    # dp, 3연속되지 않도록
    dp = [0]*(N+1)
    dp[1] = podos[1]
    if N > 1:
        dp[2] = podos[1]+podos[2]
    for i in range(3, N+1):
        dp[i] = max(dp[i-1], dp[i-3]+podos[i-1]+podos[i], dp[i-2]+podos[i])

    return max(dp)

if __name__ == "__main__":
    print(solution(int(input())))
