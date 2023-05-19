def solution(n, heights):
    cnt = 1
    right = heights[-1]
    for i in range(n-1, -1, -1):
        cur = heights[i]
        if cur > right:
            cnt += 1
            right = cur
    return cnt

t = int(input())
for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))
    print(solution(n, heights))
