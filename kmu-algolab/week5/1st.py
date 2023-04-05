# two pointer

def solutions():
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    i = 0
    j = 1
    min_m = nums[-1]
    while n > j > i >= 0:
        if (nums[j] - nums[i]) == m:
            min_m = m
            break
        elif (nums[j] - nums[i]) > m:
            min_m = min(min_m, nums[j] - nums[i])
            if i+1 == j:
                j += 1
            else:
                i += 1
        else:
            j += 1
    return min_m

t = int(input())
for _ in range(t):
    print(solutions())
