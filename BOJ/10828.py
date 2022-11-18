import sys
input = sys.stdin.readline

N = int(input())
s = []

def command(com_list, stack):
    # push
    if len(com_list) > 1:
        if com_list[0] == 'push':
            stack.append(int(com_list[1]))
    # top, size, empty, pop
    else:
        if com_list[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif com_list[0] == 'size':
            print(len(stack))
        elif com_list[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif com_list[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)

    return stack

for i in range(N):
    com = list(input().split())
    s = command(com, s)
