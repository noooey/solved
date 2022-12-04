import sys
input = sys.stdin.readline

def solutions(N, M):
    dmd = []
    qh = []
    for _ in range(N):
        dmd.append(input())
    for _ in range(M):
        qh.append(input())
    p_set = sorted(set(dmd) & set(qh))

    print(len(p_set))
    for person in p_set:
        print(person.rstrip())

n, m = map(int, input().split())
solutions(n, m)
