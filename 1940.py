import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = list(map(int, input().split()))
s.sort()

cnt = 0
i, j = 0, len(s)-1
while j > i:
    if s[i] + s[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif s[i] + s[j] > m:
        j -= 1
    else:
        i += 1

print(cnt)
