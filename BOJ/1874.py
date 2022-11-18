from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    stack.append(int(input()))

cnt = 0
nums = deque([])
answer = []

try:
    for s in stack:
        while s > cnt:
            cnt += 1
            nums.append(cnt)
            answer.append('+')

        tmp  = nums.pop()
        answer.append('-')

        while tmp != s:
            tmp = nums.pop()
            answer.append('-')
    for a in answer:
        print(a)
except:
    print('NO')
