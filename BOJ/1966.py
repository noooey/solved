import sys
input = sys.stdin.readline
import heapq
from collections import deque

test_case = int(input())
answer = []
heap = []
for _ in range(test_case):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    for idx in range(len(docs)):
        heapq.heappush(heap, (-(docs[idx]+(0.1**(idx+1))), idx))

    ranked_docs = deque([])
    while heap:
        tmp = heapq.heappop(heap)
        ranked_docs.append((-int(tmp[0]), tmp[1]))

    cnt = 1
    for doc in docs:
        print(ranked_docs[0][1])
        if ranked_docs[0][0] > doc:
            docs.pop(0)
            docs.append(doc)
        else:
            docs.pop(0)
            ranked_docs.popleft()
        cnt += 1

    print(cnt)


    while cnt
