from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
stack = deque([])
for _ in range(k):
    tmp = int(input())
    if tmp != 0:
        stack.append(tmp)
    else:
        stack.pop()
print(sum(stack))
