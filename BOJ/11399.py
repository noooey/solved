import sys
input = sys.stdin.readline
import heapq

n = int(input())
p_list = list(map(int, input().split()))
heapq.heapify(p_list)

time = [0]*n

time[0] = heapq.heappop(p_list)
for i in range(1, n):
    time[i] = (time[i-1] + heapq.heappop(p_list))

print(sum(time))
