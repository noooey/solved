def findingMax(nums, i, j):
    if i == j:
        return nums[i]
    else:
        half = (i + j) // 2
        return max(findingMax(nums, i, half), findingMax(nums, half+1, j))

t = int(input())
for _ in range(t):
    n, *nums = map(int, input().split())
    print(findingMax(nums, 0, n-1))
