import sys
input = sys.stdin.readline

def solutions(X):
    x_set = sorted(set(X))
    idx = [i for i in range(len(x_set))]
    dic = {}
    for i, s in zip(idx, x_set):
        dic[s] = i
    cnt = 0
    w = [0 for _ in range(len(X))]
    for i in range(len(X)):
        w[i] = dic[X[i]]

    return ' '.join(str(e) for e in w)

n = int(input())
x = list(map(int, input().split()))
print(solutions(x))
