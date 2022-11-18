import sys
input = sys.stdin.readline

# 열, 행
n, m = map(int, input().split())

tensor = []
for _ in range(2):
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, list(str(input()))[:-1])))
    tensor.append(matrix)

def dzipgi(tensor, i, j):
    # 3*3 matrix
    dx = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    dy = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    for k in range(9):
        tensor[0][i+dy[k]][j+dx[k]] = 1 - tensor[0][i+dy[k]][j+dx[k]]

    return tensor

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if tensor[0][i][j] == tensor[1][i][j]:
            pass
        else:
            cnt += 1
            tensor = dzipgi(tensor, i, j)

for l in range(n):
    for m1, m2 in zip(tensor[0][l], tensor[1][l]):
        if m1-m2 != 0:
            print(-1)
            exit(0)

print(cnt)
