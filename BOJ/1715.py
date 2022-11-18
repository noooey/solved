import heapq # heapqueue

N = int(input())
num_list = []
for i in range(N):
  heapq.heappush(num_list, int(input()))

sum = 0
for i in range(N-1):
  tmp = heapq.heappop(num_list) + heapq.heappop(num_list)
  heapq.heappush(num_list, tmp)
  sum += tmp
print(sum)
