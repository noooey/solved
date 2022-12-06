import sys
input = sys.stdin.readline

def cut(y, x, B, W, L, total):
    start = total[y][x]
    if L == 1: # 크기가 1*1 일 때
        if start == 1:
            return B+1, W
        else:
            return B, W+1

    cutting = False
    for i in range(y, y+L):
        for j in range(x, x+L):
            if total[i][j] != start: # 전체가 한 색깔X -> 자르기
                cutting = True

    if cutting:
        for dy, dx in zip([0, 1, 0, 1], [0, 0, 1, 1]):
            B, W = cut(y+L//2*dx, x+L//2*dy, B, W, L//2, total)
    else:
        if start == 1: # 전체가 한 색깔일 때
            return B+1, W
        else:
            return B, W+1
    return B, W

def solutions(N):
    t = []
    for _ in range(N):
        t.append(list(map(int, input().split())))

    blue, white = cut(0, 0, 0, 0, N, t)
    return f'{white}\n{blue}'

n = int(input())
print(solutions(n))
