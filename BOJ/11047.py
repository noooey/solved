import sys
input = sys.stdin.readline

n, k = map(int, input().split())

h = []
for _ in range(n):
    x = int(input())
    h.append(x)

tmp = 0
i = len(h) - 1
while k != 0:
    m = h[i]
    while k >= m :
        tmp += k // m
        k = (k % m)
    i -= 1

print(tmp)
