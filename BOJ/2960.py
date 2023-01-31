import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = []

cnt = 0
for p in range(2, n+1):
    tmp = 1
    while p*tmp <= n:
        if p*tmp not in nums:
            nums.append(p*tmp)
            k -= 1
            if k == 0:
                print(p*tmp)
                exit()
            tmp += 1
        else:
            tmp += 1
