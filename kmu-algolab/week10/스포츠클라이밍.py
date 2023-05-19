from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(input().split())
    cnt = [[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 'H':
                cnt[y][x] = -1

    cnt[n-1][0] = 1

    queue = deque([(n-1, 0)])

    while queue:
        i, j = queue.popleft()

        # rule 1
        if i-1 >= 0:
            if grid[i-1][j] == 'H' and cnt[i-1][j]  == -1:
                cnt[i-1][j] = cnt[i][j] + 1
                queue.append((i-1, j))
        if j+1 < n:
            if grid[i][j+1] == 'H' and cnt[i][j+1] == -1:
                cnt[i][j+1] = cnt[i][j] + 1
                queue.append((i, j+1))
        if i+1 < n:
            if grid[i+1][j] == 'H' and cnt[i+1][j] == -1:
                cnt[i+1][j] = cnt[i][j] + 1
                queue.append((i+1, j))
        if j-1 >= 0:
            if grid[i][j-1] == 'H' and cnt[i][j-1] == -1:
                cnt[i][j-1] = cnt[i][j] + 1
                queue.append((i, j-1))
        # rule 2
        if i-1 >= 0:
            if grid[i-1][j] == '.':
                for k in range(j+1, n):
                    if grid[i][k] != '.' or grid[i-1][k] != '.':
                        if grid[i][k] == 'H' and grid[i-1][k] == '.' and cnt[i][k] == -1:
                            cnt[i][k] = cnt[i][j] + 1
                            queue.append((i, k))
                        else:
                            break
        # rule 3
        if i-2 >= 0:
            if grid[i-1][j] == '.' and grid[i-2][j] == 'H' and cnt[i-2][j] == -1:
                cnt[i-2][j] = cnt[i][j] + 1
                queue.append((i-2, j))
        # rule 4
        if i-1 >= 0 and j-1 >=0:
            if grid[i-1][j-1] == 'H' and grid[i][j-1] == '.' and grid[i-1][j] == '.' and cnt[i-1][j-1] == -1:
                cnt[i-1][j-1] = cnt[i][j] + 1
                queue.append((i-1, j-1))
        # rule 5
        if i-1 >= 0 and j+1 < n:
            if grid[i-1][j+1] == 'H' and grid[i][j+1] == '.' and grid[i-1][j] == '.' and cnt[i-1][j+1] == -1:
                cnt[i-1][j+1] = cnt[i][j] + 1
                queue.append((i-1, j+1))

    for line in cnt:
        print(' '.join(map(str, line)))
