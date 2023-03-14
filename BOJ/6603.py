from itertools import combinations

while 1:
    tmp = list(map(int, input().split()))
    if len(tmp) == 1 and tmp[0] == 0:
        exit()
    k  = tmp[0]
    S = tmp[1:]

    for com in combinations(S, 6):
        print(' '.join(map(str, com)))
    print('')
