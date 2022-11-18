import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def search(x, y):
    if x < 0 or x >=m or y < 0 or y >= n:
        return

    if loca[y][x] == 0:
        return

    loca[y][x] = 0

    search(x+1, y)
    search(x, y+1)
    search(x-1, y)
    search(x, y-1)


t = int(input())
for _ in range(t):
    # 지렁이 수
    count = 0

    # 가로, 세로, 배추 개수
    m, n, k = map(int, input().split())

    loca = [[0]*m for _ in range(n)]
    for _ in range(k):
        # 배추 위치
        x, y = map(int, input().split())
        loca[y][x] = 1

    for i in range(n): # 세로
        for j in range(m): # 가로
            if loca[i][j] == 1:
                search(j, i)
                count += 1

    print(count)
