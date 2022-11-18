N = int(input())
for i in range(1, N + 1):
    s = '*' * i + ' ' * (N - i)
    print(s[::-1])
