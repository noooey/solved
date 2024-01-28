from collections import deque
import sys
input = sys.stdin.readline

def solutions(n, arr):
    if n == 1:
        return 0
    visited = [0]*n
    visited[0] = 1
    cnt = 0
    loc = 0
    queue = deque([])
    queue.append((0, 0))
    while queue:
        loc, cnt = queue.popleft()
        step = arr[loc]
        if step == 0:  # 못 움직임
            continue
        for i in range(step):
            if loc + i + 1 < n - 1:
                if visited[loc + i + 1] == 0:
                    queue.append((loc + i + 1, cnt + 1))
                    visited[loc + i + 1] = 1
            else:
                return cnt + 1

    return -1

N = int(input())
arr = list(map(int, input().split()))
print(solutions(N, arr))
