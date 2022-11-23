import sys
input = sys.stdin.readline
# 1과 2로 n을 만드는 경우의 수 구하기

memo = [0, 1, 2]
def cal(num):
    if num >= len(memo):
        for i in range(len(memo), num+1):
            memo.append(memo[i-1] + memo[i-2])
    return memo[num]

n = int(input())
print(cal(n)%10007)
