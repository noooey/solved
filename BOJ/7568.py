import sys
input = sys.stdin.readline
N = int(input())

# 리스트 생성
lst = []
for i in range(N):
    tmp = list(map(int, input().split()))
    lst.append(tmp)

idx = [1 for i in range(N)]
for i in range(N):
    cnt = 0
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    idx[i] += cnt

idx_str = (' ').join([str(i) for i in idx])
print(idx_str)
