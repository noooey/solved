import sys
input = sys.stdin.readline

n, x, y = map(int, input().split())

round = 0

while x != y:
    x -= x // 2
    y -= y // 2
    round += 1

print(round)
