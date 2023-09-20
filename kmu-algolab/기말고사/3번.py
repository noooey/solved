import sys
input = sys.stdin.readline

from collections import deque

def canMove(y, x, grid):
    n = len(grid)
    if n > y >= 0 and n > x >= 0:
        grid[y][x] != 'X'
        return True
    else:
        return False

t = int(input())
for _ in range(t):
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(str, input().split())))
    visit = [[-1]*n for _ in range(n)]
    visit[n-1][0] = 1

    queue = deque()
    queue.append((n-1, 0))

    while queue:
        i, j = queue.popleft()
        # rule 1
        dxs = [1, -1, 0, 0]
        dys = [0, 0, 1, -1]
        for dx, dy in zip(dxs, dys):
            if canMove(i+dy, j+dx, grid):
                if grid[i+dy][j+dx] == 'H':
                    queue.append((i+dy, j+dx))
                    visit[i+dy][j+dx] += 1

        # rule 2_ +2칸
        dxs = [1, 0, 1, 2]
        dys = [0, 1, 1, 1]
        if canMove(i, j+2, grid):
            if grid[i][j+2] == 'H':
                for dx, dy in zip(dxs, dys):
                    if canMove(i+dy, j+dx, grid):
                        if grid[i+dy][j+dx] == '.':
                            queue.append((i, j+2))
                            visit[i][j+2] += 1
        # rule 2_ -2칸
        dxs = [-1, 0, -1, -2]
        dys = [0, 1, 1, 1]
        if canMove(i, j-2, grid):
            if grid[i][j-2] == 'H':
                for dx, dy in zip(dxs, dys):
                    if canMove(i+dy, j+dx, grid):
                        if grid[i+dy][j+dx] == '.':
                            queue.append((i, j-2))
                            visit[i][j-2] += 1

        # rule 2_ +3칸
        dxs = [2, 1, 0, 1, 2, 3]
        dys = [0, 0, 1, 1, 1, 1]
        if canMove(i, j+3, grid):
            if grid[i][j+3] == 'H':
                for dx, dy in zip(dxs, dys):
                    if canMove(i+dy, j+dx, grid):
                        if grid[i+dy][j+dx] == '.':
                            queue.append((i, j+3))
                            visit[i][j+3] += 1

        # rule 2_ -3칸
        dxs = [-2, -1, 0, -1, -2, -3]
        dys = [0, 0, 1, 1, 1, 1]
        if canMove(i, j-3, grid):
            if grid[i][j-3] == 'H':
                for dx, dy in zip(dxs, dys):
                    if canMove(i+dy, j+dx, grid):
                        if grid[i+dy][j+dx] == '.':
                            queue.append((i, j-3))
                            visit[i][j-3] += 1

        # rule 3
        if canMove(i+2, j, grid):
            if grid[i+2][j] == 'H' and grid[i+1][j] == '.':
                queue.append((i+2, j))
                visit[i+2][j] += 1

        # rule 4
        if canMove(i+1, j-1, grid):
            if grid[i+1][j-1] == 'H' and grid[i][j-1] == '.' and grid[i+1][j] == '.':
                queue.append((i+1, j-1))
                visit[i+1][j-1] += 1
        if canMove(i+1, j-1, grid):
            if grid[i+1][j+1] == 'H' and grid[i+1][j] == '.' and grid[i][j+1] == '.':
                queue.append((i+1, j-1))
                visit[i+1][j-1] += 1

    for line in visit:
        print(' '.join(map(str, line)))
