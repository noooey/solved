dxs = [-1, -1, -1, 0, 1, 1, 1, 0]
dys = [1, 0, -1, -1, -1, 0, 1, 1]

def simulate_forest(n, c, k, p, power, trees):
    forest = [[[] for _ in range(n)] for _ in range(n)]
    for r, c, age in trees:
        forest[r][c].append(age)

    print(forest)
    for _ in range(p):
        # step 1, 2
        for r in range(n):
            for c in range(n):
                if len(forest[r][c]) >= 1:
                    forest[r][c] = sorted(forest[r][c])
                    tmp = 0
                    for l in range(len(forest[r][c])):
                        if forest[r][c][l] > 0:
                            p = min(forest[r][c][l], power[r][c])
                            forest[r][c][l] += 1
                            power[r][c] -= p
                            if p < forest[r][c][l]:
                                tmp += ((forest[r][c][l]-1) // 2)
                                forest[r][c][l] = -1 # mark as dead

                    power[r][c] += tmp
                    forest[r][c] = [item for item in forest[r][c] if item != -1]

        # step 3
        for r in range(n):
            for c in range(n):
                for t in forest[r][c]:
                    if t % 5 == 0:
                        for dy, dx in zip(dys, dxs):
                            if 0 <= r+dy < n and 0 <= c+dx < n:
                                forest[r+dy][c+dx].append(1)
                    power[r][c] += k

    print(forest)
    remaining_trees = sum([len(forest[r][c]) for r in range(n) for c in range(n) if len(forest[r][c]) > 0])

    return remaining_trees

t = int(input())
for _ in range(t):
    n, c, k, p = map(int, input().split())
    power = [list(map(int, input().split())) for _ in range(n)]
    trees = [tuple(map(int, input().split())) for _ in range(c)]
    remaining_trees = simulate_forest(n, c, k, p, power, trees)
    print(remaining_trees)
