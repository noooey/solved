import sys
input = sys.stdin.readline


t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    lst = [[i for i in range(1, n+1)]]*k

    for j in range(k):
        for l in range(1, n):
            lst[j][l] += lst[j][l-1]

    print(lst[-1][-1])
