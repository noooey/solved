def findMax(values, start, end):
    if start == end:
        return values[start]
    mid = (start + end) // 2
    return max(findMax(values, start, mid), findMax(values, mid+1, end))

n, *values = map(int, input().split())
print(findMax(values, 0, n-1))
