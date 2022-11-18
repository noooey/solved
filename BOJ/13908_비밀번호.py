import math

def combination(a, b):
    return math.factorial(a) / (math.factorial((a - b)) * math.factorial(b))

n, m = map(int, input().split())
lst = list(map(int, input().split()))

sum = 0
for i in range(m+1):
    sum += ((-1)**i) * ((10-i)**n) * combination(m, i)
print(int(sum))
