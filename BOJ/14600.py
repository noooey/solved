k = int(input())
x, y = map(int, input().split())

baesu = [[1]*(2**k) for _ in range(2**k)]
if k == 1:
    baesu = [[1]*2 for _ in range(2)]
    baesu[2-y][x-1] = -1
    for line in baesu:
        print(' '.join(map(str, line)))
else: #k == 2
    baesu = [
    [4, 4, 5, 5],
    [4, 3, 3, 5],
    [1, 3, 3, 2],
    [1, 1, 2, 2]
    ]
    baesu[4-y][x-1] = -1
    for line in baesu:
        print(' '.join(map(str, line)))
