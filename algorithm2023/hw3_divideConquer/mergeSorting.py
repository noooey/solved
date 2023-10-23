def merge(values, low, mid, high):
    tmp = [0]*len(values)
    for i in range(low, high+1):
        tmp[i] = a[i]
    i = low
    k = low
    j = mid+1
    while (i <= mid) and (j <= high):
        if tmp[i] <= tmp[j]:
            a[k+1] = tmp[i+1]
            k += 1
            i += 1
        else:
            a[k+1] = tmp[j+1]
            k += 1
            j += 1
        cnt += 1   # 비교 후 cnt +=1
    while i <= mid:
        a[k+1] = tmp[i+1]
        k += 1
        i += 1
    while j <= high:
        a[k+1] = tmp[j+1]
        k += 1
        j += 1
    return cnt

def mergeSort(values, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    mergeSort(values, low, mid)
    mergeSort(values, mid+1, high)
    merge(values, low, mid, high)

t = int(input())
for _ in range(t):
    n, *values = map(int, input().split())
    print(merge(values, 0, 9))
