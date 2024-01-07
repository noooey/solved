import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def update(stack, pre, n, m):
    for i in range(pre, n+1):
        stack.append(i)
        if len(stack) == m:
            print(' '.join(map(str, stack)))
        else:
            stack = update(stack, i, n, m)
        stack.pop()
    return stack

stack = []
update(stack, 1, N, M)
# if M == 1:
#     stack = []
#     for i in range(1, N+1):
#         stack.append(i)
#         print(stack)
#         stack.pop()
#     exit(0)
#
# if M == 2:
#     stack = []
#     for i in range(1, N+1):
#         stack.append(i)
#         for j in range(i, N+1):
#             stack.append(j)
#             print(stack)
#             stack.pop()
#         stack.pop()
#     exit(0)
#
# if M == 3:
#     stack = []
#     for i in range(1, N+1):
#         stack.append(i)
#         for j in range(i, N+1):
#             stack.append(j)
#             for k in range(j, N+1):
#                 stack.append(k)
#                 print(stack)
#                 stack.pop()
#             stack.pop()
#         stack.pop()
#     exit(0)
