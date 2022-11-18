from collections import deque
import sys
input = sys.stdin.readline

# 보드 입력
n, m = map(int, input().split())
board = []
for i in range(n):
    tmp = list(input().rstrip())
    # R과 B의 위치를 받아오기
    if 'R' in tmp:
        R_location = (i, tmp.index('R'))
    if 'B' in tmp:
        B_location = (i, tmp.index('B'))
    if 'O' in tmp:
        O_location = (i, tmp.index('O'))
    board.append(tmp)

ox, oy = O_location[1], O_location[0]

dxs = [1, 0, -1, 0] # 오른쪽, 위, 왼쪽, 아래
dys = [0, -1, 0, 1]
visited = [[False]*m for _ in range(n)]
R_cnt_map = [[0]*m for _ in range(n)]
B_cnt_map = [[0]*m for _ in range(n)]

def move(dxy, red, blue): # 이동
    red_location, blue_location = red, blue
    rx, ry = red[1], red[0]
    bx, by = blue[1], blue[0]
    dx, dy = dxy[1], dxy[0]
    R_tmp_cnt = R_cnt_map[ry][rx] + 1
    B_tmp_cnt = B_cnt_map[by][bx] + 1

    visited[ry][rx] = True

    R_moving = True
    B_moving = True
    while R_moving or B_moving:
        if (bx, by) == (rx+dx, ry+dy) or (bx+dx, by+dy) == (rx, ry): # B랑 R이 붙어있다면
            if board[by+dy][bx+dx] == '#' or board[ry+dy][rx+dx] == '#': # RB# 배치
                R_moving = False
                B_moving = False
        else:
            if board[ry+dy][rx+dx] == '#': # R# 배치
                R_moving = False
            if board[by+dy][bx+dx] == '#': # B# 배치
                B_moving = False

        if R_moving:
            rx += dx
            ry += dy
        if B_moving:
            bx += dx
            by += dy

        # 이동하는 동안 cnt_map 갱신해주기
        R_cnt_map[ry][rx] = R_tmp_cnt
        B_cnt_map[by][bx] = B_tmp_cnt

    return (ry, rx), (by, bx)

def BFS(red, blue):
    queue = deque([(red, blue)])
    while queue:
        cur = queue.popleft() # 현재 상태 pop
        red_location, blue_location = cur[0], cur[1]
        x, y = red_location[1], red_location[0] # R의 위치
        if visited[y][x] is False:
            visited[y][x] == True
            for dx, dy in zip(dxs, dys):
                if board[y+dy][x+dx] != '#': # 벽만 아니면 일단 이동 가능하다고 치자
                    queue.append(move((dy, dx), red_location, blue_location))
        print(R_cnt_map)

BFS(R_location, B_location)

if B_cnt_map[oy][ox] > R_cnt_map[oy][ox] and R_cnt_map[oy][ox] > 0:
    if R_cnt_map[oy][ox] > 10:
        print(-1)
    else:
        print(R_cnt_map[oy][ox])
elif B_cnt_map[oy][ox] == 0 and R_cnt_map[oy][ox] > 0:
    print(R_cnt_map[oy][ox])
else:
    print(-1)
