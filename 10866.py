from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
d = deque([])

def command(com_list, deque):
    # push_front, push_back
    if len(com_list) > 1:
        if com_list[0] == 'push_front':
            deque.appendleft(int(com_list[1]))
        elif com_list[0] == 'push_back':
            deque.append(int(com_list[1]))
    # size, empty, pop_front, pop_back, front, back
    else:
        if com_list[0] == 'pop_front':
            if deque:
                print(deque.popleft())
            else:
                print(-1)
        if com_list[0] == 'pop_back':
            if deque:
                print(deque.pop())
            else:
                print(-1)
        elif com_list[0] == 'size':
            print(len(deque))
        elif com_list[0] == 'empty':
            if deque:
                print(0)
            else:
                print(1)
        elif com_list[0] == 'front':
            if deque:
                print(deque[0])
            else:
                print(-1)
        elif com_list[0] == 'back':
            if deque:
                print(deque[-1])
            else:
                print(-1)

    return deque

for i in range(N):
    com = list(input().split())
    d = command(com, d)
