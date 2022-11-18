import sys
import heapq

input = sys.stdin.readline

N = int(input())

pos = [] # 양수 heap
neg = [] # 음수 heap
z = [] # 0 list
for i in range(N):
    num = int(input())
    # num > 0이라면 양수 heap에 push
    if num > 0:
        heapq.heappush(pos, (-num, num)) # max heap
    elif num < 0:
        heapq.heappush(neg, (num, num)) # min heap
    else:
        z.append(num) # 0

# 최대 X 최대 = 최대
def cal(total, heap, zeros):
    while len(heap) > 1:
        max_1 = heapq.heappop(heap)
        max_2 = heapq.heappop(heap)
        tmp = max_1[1] * max_2[1]
        if tmp == max_1[1]: # 1 1
            total += (max_1[1] + max_2[1])
        else:
            total += tmp
    # 나머지
    if heap:
        last = heapq.heappop(heap)[1]
        # pos heap
        if last > 0:
            total += last
        # neg heap
        else:
            if not zeros:
                total += last

    return total

print(cal(0, pos, z) + cal(0, neg, z))
