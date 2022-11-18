from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque([])

def command(com_list, queue):
    # push
    if len(com_list) > 1:
        if com_list[0] == 'push':
            queue.append(int(com_list[1]))
    # size, empty, pop, front, back
    else:
        if com_list[0] == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif com_list[0] == 'size':
            print(len(queue))
        elif com_list[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif com_list[0] == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif com_list[0] == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)

    return queue

for i in range(N):
    com = list(input().split())
    q = command(com, q)
