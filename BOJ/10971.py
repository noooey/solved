from itertools import permutations
import sys
input = sys.stdin.readline

def solutions(N, W):
    cost = sys.maxsize
    for p in permutations([i for i in range(N)]):
        tmp = 0
        all = True
        for j in range(N):
            if W[p[j-1]][p[j]] == 0:
                all = False
                break
            tmp += W[p[j-1]][p[j]]
        if all:
            cost = min(tmp, cost)
    return cost

n = int(input())
w = []
for _ in range(n):
    w.append(list(map(int, input().split())))

print(solutions(n, w))
