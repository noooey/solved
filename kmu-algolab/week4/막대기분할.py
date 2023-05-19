from collections import deque

t = int(input())

for _ in range(t):
    chrs = deque(list(input().strip()))
    height = 0
    cnt = 0
    pre = ''
    while chrs:
        cur = chrs.popleft()
        if cur == ')':
            if pre == '(':
                # no 'add pipe'
                height -= 1
                # cut
                cnt += height
            else:
                # pipe end
                cnt += 1
                height -= 1
        else:
            # add pipe
            height += 1
        # update
        pre = cur

    print(cnt)
