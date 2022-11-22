import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
m.sort()

best = (m[0], m[1], m[2])
for i in range(n-2):
    j = i+1
    k = n-1
    while j < k:
        tmp = (m[i], m[j], m[k])
        if abs(sum(tmp)) < abs(sum(best)): # 0이랑 차가 가장 작은지
            best = tmp
        if sum(tmp) == 0:
            break
        elif sum(tmp) > 0:
            k -= 1
        else:
            j += 1

print(best[0], best[1], best[2])
