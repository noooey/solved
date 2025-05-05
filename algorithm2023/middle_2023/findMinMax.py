def findMinMax(values, start, end):
    global cnt
    cnt += 1

    if start == end: # 원소 하나
        return values[start], values[end]
    elif start + 1 == end: # 원소 두 개
        return max(values[start], values[end]), min(values[start], values[end])
    else:
        mid = (start + end) // 2
        max1, min1 = findMinMax(values, start, mid)
        max2, min2 = findMinMax(values, mid+1, end)
        return max(max1, max2), min(min1, min2)


t = int(input())
for _ in range(t):
    n, *values = map(int, input().split())
    cnt = 0
    max_v, min_v = findMinMax(values, 0, n-1)
    print(max_v, min_v, cnt)


"""
정수 절대값 100 이하
"""
