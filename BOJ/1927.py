import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x > 0: # x가 자연수라면 배열에 x 추가
        heapq.heappush(h, x)
    elif x == 0: # x가 0이라면 배열에서 가장 작은 값 출력하고 제거
        if h:
            pop = heapq.heappop(h)
            print(pop)
        else:
            print(0)
