t = int(input())

for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))

    cnt = 1
    right = heights[-1]
    for i in range(n-1, -1, -1):
        if heights[i] > right:
            cnt += 1
            right = heights[i]

    print(cnt)
