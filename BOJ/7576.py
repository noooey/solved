from collections import deque
import heapq
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(tmt, q):
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if len(tmt[0]) > nx >= 0 and len(tmt) > ny >= 0 and tmt[ny][nx] == 0:
                tmt[ny][nx] = tmt[y][x] + 1
                q.append([ny, nx])

# 가로 세로
m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))

queue = deque([])
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])

bfs(tomato, queue)
max = 0
h = []
for i in range(n):
    for j in range(m):
        heapq.heappush(h, (-tomato[i][j], tomato[i][j])) # max heap
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
print(heapq.heappop(h)[1]-1)
