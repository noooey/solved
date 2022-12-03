import sys
input = sys.stdin.readline

def solutions(S, CAL):
    C = CAL[0].rstrip()
    if len(CAL) > 1:
        N = int(CAL[1])
    if C == 'add':
        if S[N] == 0:
            S[N] = 1
    elif C == 'remove':
        if S[N] == 1:
            S[N] = 0
    elif C == 'check':
        if S[N] == 1:
            print(1)
        else:
            print(0)
    elif C == 'toggle':
        if S[N] == 1:
            S[N] = 0
        else:
            S[N] = 1
    elif C == 'all':
        for i in range(1, len(S)):
            S[i] = 1
    elif C == 'empty':
        for i in range(1, len(S)):
            S[i] = 0

m = int(input())
s = [0]*21
for _ in range(m):
    cal = list(input().split())
    solutions(s, cal)
