'''
3
9 1 2 3 4 5 6 7 8 9
9 9 8 7 6 5 4 3 2 1
9 9 6 3 1 2 4 5 7 8

29 0
29 6
37 7
'''
from math import floor

def combSort(nums, n):
    ops = 0
    swaps = 0
    shrinkRatio = 1.3
    gap = n
    sorted = False

    while not sorted:
        gap = floor(gap / shrinkRatio)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            ops += 1
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swaps += 1
                sorted = False
            i += 1

    return ops, swaps

t = int(input())
for _ in range(t):
    line = list(map(int, input().split()))
    n = line[0]
    nums = line[1:]
    print(' '.join(map(str, combSort(nums, n))))
