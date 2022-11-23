import sys
input = sys.stdin.readline

memo = [0, 1, 2, 4]

def cal(n):
    if n >= len(memo):
        for i in range(len(memo), n+1):
            memo.append(memo[i-1] + memo[i-2] + memo[i-3])
    print(memo[n])

t = int(input())
for _ in range(t):
    cal(int(input()))
