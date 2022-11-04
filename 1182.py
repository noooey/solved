from itertools import combinations
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
num = list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
    for combi in combinations(num, i):
        if sum(combi) == s:
            cnt += 1
print(cnt)
