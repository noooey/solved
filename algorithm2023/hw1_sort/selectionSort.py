def selectionSort():
    ops = 0
    swaps = 0

    line = list(map(int, input().split()))
    n = line[0]
    nums = line[1:]

    for i in range(n-1):
        j_min = i

        for j in range(i+1, n):
            ops += 1
            if nums[j] < nums[j_min]:
                j_min = j

        if j_min != i:
            tmp = nums[j_min]
            nums[j_min] = nums[i]
            nums[i] = tmp
            swaps += 1

    return ops, swaps

t = int(input())
for _ in range(t):
    print(' '.join(map(str, selectionSort())))
