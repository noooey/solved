def kadane(nums):
    cur_max = nums[0]
    max_sum = nums[0]
    cur_start = 0
    cur_end = 0
    start = 0
    end = 0

    for i in range(1, len(nums)):
        if cur_max + nums[i] > nums[i]:
            cur_max += nums[i]
            cur_end = i
        else:
            cur_max = nums[i]
            cur_start = i
            cur_end  = i
        if cur_max > max_sum:
            max_sum = cur_max
            start = cur_start
            end = cur_end

    return max_sum, start, end

t = int(input())
for _ in range(t):
    n, *nums = map(int, input().split())
    max_sum, s_idx, e_idx = kadane(nums)
    if max_sum <= 0:
        print(0, -1, -1)
    else:
        print(max_sum, s_idx, e_idx)
