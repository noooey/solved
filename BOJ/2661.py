import sys
input = sys.stdin.readline

def isGoodArr(arr):
    l = len(arr)
    tmp = l // 2
    for i in range(1, tmp+1):
        if arr[l-i:l] == arr[l-2*i:l-i]:
            return False
    return True

def makeArr(arr, n):
    for i in range(1, 4):
        arr.append(i)
        if isGoodArr(arr):
            if len(arr) == n:
                return arr
            arr = makeArr(arr, n)
            if len(arr) == n:
                return arr
        arr.pop()
    return arr

N = int(input())
if N == 1:
    print(1)
else:
    arr = [1]
    print(''.join(map(str, makeArr(arr, N))))
