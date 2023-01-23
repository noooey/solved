from itertools import permutations
import sys
input = sys.stdin.readline

def solutions(N, M):
    nums = [i for i in range(1, N+1)]
    for combi in permutations(nums, M):
        print(' '.join(str(x) for x in list(combi)))



if __name__ == "__main__":
    n, m = map(int, input().split())
    solutions(n, m)
