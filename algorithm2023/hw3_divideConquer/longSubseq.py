def longSubseq(nums):
    cur_len = 1
    max_len = 1
    cur_start = nums[0]

    for i in range(1, len(nums)):
        if nums[i] >= cur_start:
            cur_len += 1
        else:
            max_len = max(max_len, cur_len)
            cur_len = 1
            cur_start = nums[i]
    max_len = max(max_len, cur_len)
    return max_len

t = int(input())
for _ in range(t):
    n, *nums = map(int, input().split())
    print(longSubseq(nums))
