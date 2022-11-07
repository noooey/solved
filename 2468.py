import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
area = []
height = set([])
for _ in range(n):
    tmp = list(map(int, input().split()))
    area.append(tmp)
    height |= set(tmp)

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]
visited = [[0]*n for _ in range(n)]

def search(y, x, h):
    for dx, dy in zip(dxs, dys):
        if n > y+dy and y+dy >= 0 and n > x+dx and x+dx >= 0:
            if area[y+dy][x+dx] > h and visited[y+dy][x+dx] != 1:
                visited[y+dy][x+dx] = 1
                search(y+dy, x+dx, h)

cnt = 0
for h in height:
    visited = [[0]*n for _ in range(n)]
    c_tmp = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > h and visited[i][j] != 1:
                visited[i][j] = 1
                search(i, j, h)
                c_tmp += 1
    cnt = max(cnt, c_tmp)

if cnt == 0:
    cnt += 1
print(cnt)
