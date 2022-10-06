import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

day = 0
day += (v - b) // (a - b)
v = (v - b) % (a - b)

if v > 0:
    day += 1
print(day)
