import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
m.sort()

i = 0
j = len(m)-1
best = (m[i], m[j])
while i < j:
    tmp = (m[i], m[j])
    if abs(sum(tmp)) <= abs(sum(best)): # 0이랑 차가 가장 작은지
        best = tmp
    if sum(tmp) == 0:
        break
    elif sum(tmp) > 0:
        j -= 1
    else:
        i += 1

print(best[0], best[1])
