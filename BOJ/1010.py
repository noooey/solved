import math
import sys
input = sys.stdin.readline

def combi(n, k):
    return math.factorial(n) // (math.factorial(k)*math.factorial(n-k))

t = int(input())

for _ in range(t):
    i, j = map(int, input().split())
    print(combi(j, i))
