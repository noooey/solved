import sys
input = sys.stdin.readline
import heapq

n, l = map(int, input().split())
leaky = list(map(int, input().split()))
heapq.heapify(leaky) # min heap

cnt = 0
# pre = heapq.heappop(leaky)
while leaky:
    pre = heapq.heappop(leaky)
    tmp = 1
    while tmp < l and leaky:
        next = heapq.heappop(leaky)
        tmp += (next - pre)
        pre = next
    if tmp <= l:
        cnt += 1
    else: # tmp가 l을 초과해버린경우
        heapq.heappush(leaky, pre)
        cnt += 1

print(cnt)

"""
반례
4 3
1 4 7 10
-> 4

6 3
1 2 4 5 6 7
-> 3
"""
