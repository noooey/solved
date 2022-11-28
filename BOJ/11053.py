import sys
input = sys.stdin.readline

n = int(input())
seq = [0]
seq += list(map(int, input().split()))
cnt = [0] + [1 for _ in range(n)]

for i in range(2, n+1):
    j = i-1
    while j > 0:
        if seq[i] > seq[j]:
            cnt[i] = max(cnt[j]+1, cnt[i])
            j -= 1
        else:
            j -= 1

print(max(cnt))
