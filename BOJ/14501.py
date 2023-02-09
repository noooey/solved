N = int(input())

T = [0]
P = [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

e = [0 for _ in range(N+2)]

for i in range(N, 0, -1):
    if i+T[i]-1 > N:
        e[i] = e[i+1]
    else:
        e[i] = max(P[i] + e[i+T[i]], e[i+1])

print(max(e))
