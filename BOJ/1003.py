import sys
input = sys.stdin.readline

zero = [1, 0, 1] # 0, 1, 2는 바로 리턴
one = [0, 1, 1]

def fibo(n):
    if n >= len(zero):
        for i in range(len(zero), n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(f'{zero[n]} {one[n]}')

t = int(input())
for _ in range(t):
    fibo(int(input()))
