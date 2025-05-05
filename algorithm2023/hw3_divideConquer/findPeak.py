def findPeak(valeus, start, end):
    if start == end:
        return values[start]

    mid = (start + end) // 2

    if values[mid] < values[mid + 1]:
        return findPeak(values, mid+1, end)
    else:
        return findPeak(values, start, mid)

n, *values = map(int, input().split())
print(findPeak(values, 0, n-1))
