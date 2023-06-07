t = int(input())
for _ in range(t):
    N = int(input())
    total = N*(N+1) // 2
    nums = list(map(int, input().split()))
    print(total -sum(nums))
