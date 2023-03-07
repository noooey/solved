from collections import deque

pipe = input().rstrip()

stack = deque([])
h = 0
total = 0
pre = ''

for p in pipe:
    if p == '(':
        stack.append('(')
        h += 1
    else:
        tmp = stack.pop()
        if pre == '(':
            # cut
            h -= 1
            total += h
        else:
            total += 1
            h -= 1
    pre = p

print(total)
