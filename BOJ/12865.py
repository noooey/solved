import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = {}
for _ in range(N):
    W, V = map(int, input().split())
    items[W] = V

dp = [0 for _ in range(K+1)]
for t in items.items():
    dp[t[0]] = t[1]

for i in range(K, 0, -1):
    for item in items.items():
        if 0 < i - item[0] <= K:
            dp[i] = max(dp[i-item[0]] + item[1], dp[i])
            print('******')
            print(dp)

print(dp)
print(max(dp))
