import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

total = sum(a[:k])
max_total = total
for i in range(k, len(a)):
    total -= a[i-k]
    total += a[i]
    max_total = max(max_total, total)

print(max_total)
