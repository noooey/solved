N = int(input())

n = [0 for i in range(N+1)]
n[1] = 1

for j in range(2, N+1):
    n[j] = n[j-2] + n[j-1]

# print(n)
print(n[N])

# 2^(n-1)
#
# 1
#
# 10
#
# 101
# 100
#
# 1000
# 1001
# 1010
#
# 10000
# 10001
# 10010
# 10100
# 10101
# 10
#
# 112358
