"""
2n, 2n+1 우선순위 차이가 큰것부터 sort해서 우선권 사용
"""
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())), reverse=True)
    diff = []
    total = 0
    for i in range(n // 2):
        diff.append(nums[2*i] - nums[2*i+1])
        total += nums[2*i+1]
    if n % 2 == 1:
        diff.append(nums[-1])
    sorted_diff = sorted(diff, reverse=True)
    total += sum(sorted_diff[:m])

    print(total)


"""
# false
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())), reverse=True)
    total = 0
    for i in range(n // 2):
        if nums[i*2] == nums[i*2+1]:
            total += nums[i*2]
        else:
            if m > 0:
                total += max(nums[i*2], nums[i*2+1])
                m -= 1
            else:
                total += min(nums[i*2], nums[i*2+1])
    if n % 2 != 0:
        if m > 0:
            total += nums[-1]
            m -= 1

    print(total)
"""

"""
m = 1
9 9
8 6
6 1
"""
#


# 9 8 1 18
# 9 6 6 21
