import sys
input = sys.stdin.readline

n = int(input())

h = [0] * 10001
for _ in range(n):
    h[int(input())] += 1

for i in range(len(h)):
    if h[i] != 0:
        for j in range(h[i]):
            print(i)
