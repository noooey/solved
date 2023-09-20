from collections import deque
import sys

input = sys.stdin.readline
queue = deque()

def canMove(x, y, hold, visit):
    n = len(hold)
    if not (0 <= x <= n-1 and 0 <= y <= n-1):
        return False
    if visit[x][y] == -1:
        return True
    else:
        return False

def blank(tmps, hold):
    n = len(hold)
    for tmp in tmps:
        x, y = tmp
        if not (0 <= x <= n-1 and 0 <= y <= n-1):
            return False
        else:
            if hold[x][y] != '.':
                return False
    else:
        return True

t = int(input())
for _ in range(t):
    n = int(input())
    visit = [[-1]*n for i in range(n)]
    hold = []
    for _ in range(n):
        hold.append(input().split())
    for i in range(n):
        for j in range(n):
            if hold[i][j] == 'X' or hold[i][j] =='.':
                visit[i][j] = 0

    visit[n-1][0] = 1
    queue.append((n-1, 0, 1))

    while queue:
        r, c, count = queue.popleft()

        # rule 1
        dxs = [1, -1, 0, 0]
        dys = [0, 0, 1, -1]
        for dx, dy in zip(dxs, dys):
            x = r + dx
            y = c + dy
            if canMove(x, y, hold, visit):
                queue.append([x, y, count + 1])
                visit[x][y] = count + 1

        # rule 2
        x = r
        y = c + 2
        if canMove(x, y, hold, visit):
            temp = [[r - 1, c], [r - 1, c + 1], [r - 1, c + 2], [r, c + 1]]
            if blank(temp, hold):
                queue.append([x, y, count + 1])
                visit[x][y] = count + 1

        x = r
        y = c - 2
        if canMove(x, y, hold, visit):
            temp = [[r - 1, c], [r - 1, c - 1], [r - 1, c - 2], [r, c - 1]]
            if blank(temp, hold):
                queue.append([x, y, count + 1])
                visit[x][y] = count + 1

        x = r
        y = c + 3
        if canMove(x, y, hold, visit):
            temp = [[r - 1, c], [r - 1, c + 1], [r - 1, c + 2], [r - 1, c + 3], [r, c + 1], [r, c + 2]]
            if blank(temp, hold):
                queue.append([x, y, count + 1])
                visit[x][y] = count + 1

        x = r
        y = c - 3
        if canMove(x, y, hold, visit):
            temp = [[r - 1, c], [r - 1, c - 1], [r - 1, c - 2], [r - 1, c - 3], [r, c - 1], [r, c - 2]]
            if blank(temp, hold):
                queue.append([x, y, count + 1])
                visit[x][y] = count + 1

        x = r - 2
        y = c
        if canMove(x, y, hold, visit):
            temp = [[r - 1, c]]
            if blank(temp, hold):
                queue.append([x, y, count + 1])
                visit[x][y] = count + 1

        # rule 4
        x = r - 1
        y = c - 1
        if canMove(x, y, hold, visit):
            temp = [[r - 1, c], [r, c - 1]]
            if blank(temp, hold):
                queue.append([x, y, count + 1])
                visit[x][y] = count + 1

        # rule 5
        x = r - 1
        y = c + 1
        if canMove(x, y, hold, visit):
            temp = [[r - 1, c], [r, c + 1]]
            if blank(temp, hold):
                queue.append([x, y, count + 1])
                visit[x][y] = count + 1

    for line in visit:
        print(' '.join(map(str, line)))
