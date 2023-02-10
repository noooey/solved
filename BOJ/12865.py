import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = {}
for _ in range(N):
    W, V = map(int, input().split())
    items[W] = V

# 가치 내림차순 정렬
# 크기 오름차순 정렬

items = sorted(items.items(), key = lambda x : x[1], reverse=True)

heap = []
for item in items:
    heapq.heappush(heap, item)


total = 0
while K > 0:
    w, v = heapq.heappop(heap)
    total += v
    K -= w

print(total)
