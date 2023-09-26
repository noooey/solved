def bubbleSort(nums, n):
    ops = 0
    swaps = 0

    for i in range(1, n):
        for j in range(1, n-i+1):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                swaps += 1
            ops += 1

    return ops, swaps

def bubbleSortImproved1(nums, n):
    ops = 0
    swaps = 0

    for i in range(1, n):
        swapped = False;
        for j in range(1, n-i+1):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                swaps += 1
                swapped = True;
            ops += 1
        if(swapped == False):
            break;

    return ops, swaps

def bubbleSortImproved2(nums, n):
    ops = 0
    swaps = 0

    lastSwappedPos = n
    while(lastSwappedPos > 0):
        swappedPos = 0;
        for j in range(1, lastSwappedPos):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                swaps += 1
                swappedPos = j
            ops += 1
        lastSwappedPos = swappedPos;

    return ops, swaps

t = int(input())
for _ in range(t):
    line = list(map(int, input().split()))
    n = line[0]
    nums = line[1:]
    print(' '.join(map(str, bubbleSort(nums.copy(), n))) + ' ' + ' '.join(map(str, bubbleSortImproved1(nums.copy(), n)))+ ' ' + ' '.join(map(str, bubbleSortImproved2(nums.copy(), n))))
