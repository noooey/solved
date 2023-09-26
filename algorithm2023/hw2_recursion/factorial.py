import sys
sys.setrecursionlimit(5000)  # or another higher value

def result(m):
    if m % 10 == 0:
        return result(m // 10)
    else:
        return m

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

t = int(input())
for _ in range(t):
    n = int(input())
    print(result(factorial(n)) % 1000)
