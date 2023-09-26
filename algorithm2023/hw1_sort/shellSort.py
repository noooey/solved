def shellSort(nums, n):
    ops = 0
    swaps = 0
    shrinkRatio = 2
    gap = n // shrinkRatio

    while gap > 0:
        for i in range(gap, n):
            tmp = nums[i]
            j = i
            while j >= gap:
                ops += 1
                if nums[j-gap] > tmp:
                    nums[j], nums[j-gap] = nums[j-gap], nums[j]
                    swaps += 1
                    j -= gap
                else:
                    break
            nums[j] = tmp
        gap //= shrinkRatio

    return ops, swaps
    
t = int(input())
for _ in range(t):
    line = list(map(int, input().split()))
    n = line[0]
    nums = line[1:]
    print(' '.join(map(str, shellSort(nums, n))))
