t = int(input())

dxs = [-1, -1, -1, 0, 1, 1, 1, 0]
dys = [1, 0, -1, -1, -1, 0, 1, 1]

for _ in range(t):
    n, c, k, p = map(int, input().split())

    # ground
    gmap = []
    for _ in range(n):
        gmap.append(list(map(int, input().split())))

    # tree location
    tree_map = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(c):
        y, x, age = map(int, input().split())
        tree_map[y][x].append(age)

    # simulation
    for _ in range(p):
        for i in range(n):
            for j in range(n):
                # if len(tree_map[i][j]) >= 1:
                    # tree_map[i][j] = sorted(tree_map[i][j])
                tmp = 0
                for l in range(len(tree_map[i][j])-1, -1, -1):
                    if gmap[i][j] >= tree_map[i][j][l]:
                        gmap[i][j] -= tree_map[i][j][l]
                        tree_map[i][j][l] += 1
                    else:
                        tmp += (tree_map[i][j][l] // 2)
                        # delete
                        tree_map[i][j][l] = -1
                gmap[i][j] += tmp
                tree_map[i][j] = [item for item in tree_map[i][j] if item != -1]

        for i in range(n):
            for j in range(n):
                for t in tree_map[i][j]:
                    # bunsik
                    if t % 5 == 0:
                        for dy, dx in zip(dys, dxs):
                            if 0 <= i+dy < n and 0 <= j+dx < n:
                                tree_map[i+dy][j+dx].append(1)
                gmap[i][j] += k
        # print('------tree_map-------')
        # print(tree_map)
        # print('--------gmap---------')
        # print(gmap)

    total = 0
    for line in tree_map:
        for cell in line:
            total += len(cell)

    print(total)
