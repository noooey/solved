def binarySearch(n, K, A):
    if n == 1:
        if A[0] == K:
            return 0
        else:
            return -1

    if K == A[n//2]:
        return n//2
    elif K >= A[n//2]:
        bs = binarySearch(n-n//2, K, A[n//2:])
        if bs == -1:
            return -1
        else:
            return n//2 + bs
    else:
        return binarySearch(n//2, K, A[:n//2])

t = int(input())
for _ in range(t):
    n, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(binarySearch(n, K, A))
