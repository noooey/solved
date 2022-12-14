from collections import deque
import sys
input = sys.stdin.readline

def solutions(N, M):
    miro = []
    cnt = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        miro.append(list(input().rstrip()))

    dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]
    queue = deque([((0, 0), 1)])
    cnt[0][0] = 1
    while queue:
        cur = queue.popleft()
        y, x = cur[0][0], cur[0][1]
        cnt[y][x] = cur[1]
        if miro[y][x] == '1':
            miro[y][x] = '0'
            for dy, dx in zip(dys, dxs):
                if N > y+dy and y+dy >= 0 and M > x+dx and x+dx >= 0:
                    if miro[y+dy][x+dx] == '1':
                        queue.append(((y+dy, x+dx), min(cnt[y][x]+1, cur[1]+1)))

    return cnt[-1][-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(solutions(n, m))
