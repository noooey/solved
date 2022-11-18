import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

jewels = []

for i in range(N):
    # M: 무게, V: 가격
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(jewels, (M, V))

bags = []
for i in range(K):
    # C: 가방의 최대 수용 무게
    C = int(sys.stdin.readline())
    heapq.heappush(bags, C)

sorted_bags = []
for i in range(K):
    sorted_bags.append(heapq.heappop(bags))

tmp = []
total = 0
for b in sorted_bags:
    while jewels and b >= jewels[0][0]:
        j = heapq.heappop(jewels)
        heapq.heappush(tmp, (-j[1]))
    if tmp:
        total -= heapq.heappop(tmp)
    elif not jewels:
        break

print(total)
