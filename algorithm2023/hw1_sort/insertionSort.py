def insertionSort():
    ops = 0
    swaps = 0

    line = list(map(int, input().split()))
    n = line[0]
    nums = line[1:]

    for i in range(1, n):
        tmp = nums[i]
        idx = 0
        for j in range(i, 0, -1):
            ops += 1
            if nums[j-1] <= tmp:
                idx = j
                break
            else:
                swaps += 1
            nums[j] = nums[j-1]
        nums[idx] = tmp

    return ops, swaps

t = int(input())
for _ in range(t):
    print(' '.join(map(str, insertionSort())))
