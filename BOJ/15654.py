from itertools import combinations, permutations
import sys
input = sys.stdin.readline

def solutions(N, M):
    nums = sorted(list(map(int, input().split())))
    arr = []
    for com in combinations(nums, m):
        for per in permutations(com):
            arr.append(per)
    arr.sort()
    for a in arr:
        print(' '.join([str(c) for c in a]))

n, m = map(int, input().split())
# print(solutions(n, m))
solutions(m, n)
