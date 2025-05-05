import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    n = int(input())
    if n != 0:
        # insert
        heapq.heappush(heap, n)
    else:
        # pop
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
