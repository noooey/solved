from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
values = deque(list(map(int, input().split())))
stack = []
answer = [-1]*len(values)

stack.append(values[0])
for i in ragnge(len(values)-1):
    stack.append(values[i])
    if stack[0] < values[i]:
        answer[i] = values[0]

print(*answer)


"""
# timeout
for i in range(len(values)):
    exist = False
    for j in range(i+1, len(values)):
        if values[i] < values[j]:
            if i == len(values)-1:
                print(values[j])
            else:
                print(values[j], end=" ")
            exist = True
            break
    if not exist:
        if i == len(values)-1:
            print(-1)
        else:
            print(-1, end=" ")
"""
