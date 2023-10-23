def max_sum(nums, start, half, end):
    left_max = 0
    tmp = 0
    for i in range(half, start-1, -1):
        tmp += nums[i]
        if tmp > left_max:
            left_max = tmp

    right_max = 0
    tmp = 0
    for i in range(half+1, end+1):
        tmp += nums[i]
        if tmp > right_max:
            right_max = tmp

    return left_max + right_max

def max_subseq_sum(nums, start, end):
    if start == end:
        return nums[start]
    half = (start + end) // 2
    return max(max_subseq_sum(nums, start, half), max_subseq_sum(nums, half+1, end), max_sum(nums, start, half, end))

t = int(input())
for _ in range(t):
    n, *nums = map(int, input().split())
    answer = max_subseq_sum(nums, 0, n-1)
    if answer > 0:
        print(answer)
    else:
        print(0)
