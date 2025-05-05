import heapq
import sys
input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

upper = max(budgets)
down = 1

if M >= sum(budgets):
    print(upper)
else:
    max_budget = 0
    total = 0
    while upper >= down:
        limit = (upper + down) // 2
        cur = 0
        heap = []
        for budget in budgets:
            if budget > limit:
                heapq.heappush(heap, -limit)
                cur += limit
            else:
                heapq.heappush(heap, -budget)
                cur += budget
        if cur == M:
            total = max(total, cur)
            max_budget = -heapq.heappop(heap)
            break
        elif cur < M:
            total = max(total, cur)
            max_budget = -heapq.heappop(heap)
            down = limit + 1
        else:
            upper = limit - 1
    print(max_budget)
