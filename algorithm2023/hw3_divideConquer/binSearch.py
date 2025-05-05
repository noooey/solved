def binarySearch(x, values, start, end):
    if start == end:
        if values[start] == x:
            return x
        else:
            return -1

    mid = (start + end) // 2

    if values[mid] == x:
        return mid
    elif values[mid] > x:
        return binarySearch(x, values, start, mid)
    else:
        return binarySearch(x, values, mid+1, end)

x = int(input())
n, *values = map(int, input().split())
print(binarySearch(x, values, 0, n-1))
