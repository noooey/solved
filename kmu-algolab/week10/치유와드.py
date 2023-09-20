import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split()) # 맵 크기, 시간
    a, b = map(int, input().split())
    poison = []
    heal = []
    for _ in range(a):
        poison.append(list(map(int, input().split())))
    for _ in range(b):
        heal.append(list(map(int, input().split())))

    location = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for p in poison:
                r, c = p
                p_dist = max(abs(r - i), abs(c - j))
                location[i][j] += max(m - p_dist + 1, 0)
            for h in heal:
                r, c = h
                h_dist = abs(r - i) + abs(c - j)
                location[i][j] += max(m - h_dist + 1, 0)
        for p in poison:
            r, c = p
            location[r][c] += 1
        for h in heal:
            r, c = h
            location[r][c] -= 1
        for i in location:
            print(" ".join(map(str, i)))
