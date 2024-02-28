from collections import deque

# 북서 -> 북동 -> 남동 -> 남서
dys = [-1, -2, -2, -1, 1, 2, 2, 1]
dxs = [-2, -1, 1, 2, 2, 1, -1, -2]

def move(l, iy, ix, ey, ex):
    visited = [[0]*l for _ in range(l)]
    queue = deque([(iy, ix, 0)])
    visited[iy][ix] = 1

    while queue:
        y, x, c = queue.popleft()
        if (y, x) == (ey, ex):
            return c
        for dy, dx in zip(dys, dxs):
            if (l > y + dy >= 0) and (l > x + dx >= 0):
                if visited[y+dy][x+dx] == 0:
                    queue.append((y+dy, x+dx, c+1))
                    visited[y+dy][x+dx] = 1

n = int(input())
for _ in range(n):
    l = int(input())
    iy, ix = map(int, input().split())
    ey, ex = map(int, input().split())
    print(move(l, iy, ix, ey, ex))
