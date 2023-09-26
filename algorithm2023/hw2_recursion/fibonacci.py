def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

t = int(input())
for _ in range(t):
    n = int(input())
    print(fibonacci(n))
