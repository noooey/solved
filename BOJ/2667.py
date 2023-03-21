from collections import deque
import sys
input = sys.stdin.readline

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

n = int(input())
gido = []
dangis = {}
dangi_idx = 0
for _ in range(n):
    gido.append(input().rstrip())

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if gido[i][j] == '1' and visited[i][j] != 1:
            cnt = 0
            dangi_idx += 1
            queue = deque([(i, j)])
            visited[i][j] = 1
            while queue:
                y, x = queue.popleft()
                cnt += 1
                for dy, dx in zip(dys, dxs):
                    if n > y + dy >= 0 and n > x + dx >= 0:
                        if gido[y+dy][x+dx] == '1' and visited[y+dy][x+dx] != 1:
                            queue.append((y+dy, x+dx))
                            visited[y+dy][x+dx] = 1
            dangis[dangi_idx] = cnt

print(dangi_idx)
for d in sorted(dangis.values()):
    print(d)
