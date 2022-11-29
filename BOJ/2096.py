import sys
input = sys.stdin.readline

dp_max = [0 for _ in range(3)]
dp_min = [0 for _ in range(3)]
tmp_max = [0 for _ in range(3)]
tmp_min = [0 for _ in range(3)]

n = int(input())

for _ in range(n):
    line = list(map(int, input().split()))

    dp_max[0] = max(tmp_max[0], tmp_max[1]) + line[0]
    dp_max[1] = max(tmp_max[0], tmp_max[1], tmp_max[2]) + line[1]
    dp_max[2] = max(tmp_max[1], tmp_max[2]) + line[2]


    dp_min[0] = min(tmp_min[0], tmp_min[1]) + line[0]
    dp_min[1] = min(tmp_min[0], tmp_min[1], tmp_min[2]) + line[1]
    dp_min[2] = min(tmp_min[1], tmp_min[2]) + line[2]

    for j in range(3):
        tmp_max[j] = dp_max[j]
        tmp_min[j] = dp_min[j]

print(max(dp_max), min(dp_min))
