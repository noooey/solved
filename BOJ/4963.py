from collections import deque
import sys
input = sys.stdin.readline

d = [(1, 0), (0, -1), (-1, 0), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1)] # 하 좌 상 우, 우하, 좌하, 좌상, 우상

def solutions(W, H):
    m = []
    for _ in range(H):
        m.append(list(map(int, input().split())))

    cnt = 0
    for i in range(H):
        for j in range(W):
            if m[i][j] == 1:
                # bfs
                cnt += 1
                m[i][j] = 0
                queue = deque([(i, j)])
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in d:
                        if 0 <= y+dy < H and 0 <= x+dx < W:
                            if m[y+dy][x+dx] == 1:
                                m[y+dy][x+dx] = 0
                                queue.append((y+dy, x+dx))
    return cnt

if __name__ == "__main__":
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        print(solutions(w, h))
