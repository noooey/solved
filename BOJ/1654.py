import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

start, end = 1, max(lines)
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for line in lines:
        if line >= mid:
            cnt += (line // mid)
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
        cnt = 0

print(end)
