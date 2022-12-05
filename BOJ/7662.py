import heapq
import sys
input = sys.stdin.readline

def solutions():
    k = int(input())
    exist = [0] * k
    min_heap = []
    max_heap = []
    for i in range(k):
        c, n = input().split()
        if c == 'I':
            heapq.heappush(min_heap, (int(n), i))
            heapq.heappush(max_heap, (-int(n), i))
            exist[i] = 1
        elif c == 'D':
            if int(n) == -1: # 최솟값 삭제
                while min_heap and not exist[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    exist[heapq.heappop(min_heap)[1]] = 0
            else: # 최댓값 삭제
                while max_heap and not exist[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    exist[heapq.heappop(max_heap)[1]] = 0

    while min_heap and not exist[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not exist[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        return f'{-max_heap[0][0]} {min_heap[0][0]}'
    else:
        return 'EMPTY'

t = int(input())
for _ in range(t):
    print(solutions())
