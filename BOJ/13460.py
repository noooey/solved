from collections import deque
import sys
input = sys.stdin.readline

# 보드 입력
n, m = map(int, input().split())
board = []
for i in range(n):
    tmp = list(input().rstrip())
    # R과 B, 구멍 위치
    if 'R' in tmp:
        R_location = (i, tmp.index('R'))
        tmp[tmp.index('R')] = '.'
    if 'B' in tmp:
        B_location = (i, tmp.index('B'))
        tmp[tmp.index('B')] = '.'
    if 'O' in tmp:
        O_location = (i, tmp.index('O'))
    board.append(tmp)

# 좌표 체크
rx, ry = R_location[1], R_location[0]
bx, by = B_location[1], B_location[0]
ox, oy = O_location[1], O_location[0]

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 좌, 하, 우, 상
visited = [] # 방문 여부 체크

def move(x, y, dx, dy):
    cnt = 0
    nx, ny = x, y
    while board[ny+dy][nx+dx] != '#' and board[ny][nx] != 'O':
        nx += dx
        ny += dy
        cnt += 1
    return nx, ny, cnt


def solutions():
    queue = deque([(0, rx, ry, bx, by)])
    visited.append((rx, ry))

    while queue:
        cnt, rrx, rry, bbx, bby = queue.popleft()

        # 횟수가 10이 넘어가면 리턴 -1
        if cnt >= 10:
            return -1

        for dx, dy in dxy:
            rtx, rty, rcnt = move(rrx, rry, dx, dy)
            btx, bty, bcnt = move(bbx, bby, dx, dy)

            if board[bty][btx] != 'O': # b가 구멍이 닿지 않았을 때
                if rtx == ox and rty == oy: # r이 구멍에 도달했다면
                    return cnt + 1

                # 둘이 같은 선상에 존재했을 경우 -> 둘이 겹쳐짐
                if (rtx, rty) == (btx, bty):
                    if rcnt > bcnt: # r이 더 많이 이동, 겹친거 한 칸 뒤로 돌려놔줌
                        rtx, rty = rtx-dx, rty-dy
                    else: # b가 더 많이 이동
                        btx, bty = btx-dx, bty-dy

                if (rtx, rty, btx, bty) in visited:
                    continue
                else:
                    visited.append((rtx, rty, btx, bty))
                    queue.append((cnt+1, rtx, rty, btx, bty))

    # 갈 곳 없으면 -1
    return -1

print(solutions())
