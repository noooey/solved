import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []
for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(heap, (x, y))

x_sorted = []
while heap:
    tmp = heapq.heappop(heap)
    x_sorted.append((tmp[0], tmp[1]))

x_sorted.sort(key=lambda x:x[1])

for x in x_sorted:
    print(x[0], x[1])
