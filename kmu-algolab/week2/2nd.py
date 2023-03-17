def solution(n, m, d, sadari):
    y, x = (m-1, (d-1)*2)
    # end = sadari[m-1][(d-1)*2]
    move = False
    while m > y >= 0 and (n-1)*2 >= x >= 0:
        if (n-1)*2 >= x+2 and move == False:
            if sadari[y][x+1] == '+': # right
                x += 2
                move = True
                continue
        if x-2 >= 0 and move == False:
            if sadari[y][x-1] == '+': # left
                x -= 2
                move = True
                continue
        y -= 1
        move = False

    return (x+2) // 2

t = int(input())
for _ in range(t):
    n, m, d = map(int, input().split())
    sadari = []
    for _ in range(m):
        sadari.append(input().rstrip())
    print(solution(n, m, d, sadari))
