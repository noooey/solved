# import sys
# sys.setrecursionlimit(5000)  # or another higher value

def fastExp(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        b = fastExp(a, (n-1)//2) % 1000
        return a * b * b
    else:
        b = fastExp(a, n//2) % 1000
        return b * b

t = int(input())
for _ in range(t):
    a, n = map(int, input().split())
    print(fastExp(a, n) % 1000)
