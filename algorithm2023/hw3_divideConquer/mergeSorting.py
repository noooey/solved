def merge(a, low, mid, high):
    global cnt
    tmp = [0]*len(a)
    for i in range(low, high+1):
        tmp[i] = a[i]
    i = low
    k = low
    j = mid+1
    while (i <= mid) and (j <= high):
        if tmp[i] <= tmp[j]:
            a[k] = tmp[i]
            k += 1
            i += 1
        else:
            a[k] = tmp[j]
            k += 1
            j += 1
        cnt += 1   # 비교 후 cnt +=1
    while i <= mid:
        a[k] = tmp[i]
        k += 1
        i += 1
    while j <= high:
        a[k] = tmp[j]
        k += 1
        j += 1

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
    cnt = 0
    mergeSort(values, 0, n-1)
    print(cnt)
