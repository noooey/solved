from collections import deque

t = int(input())

for _ in range(t):
    facs = {'A': deque([]), 'B': deque([])}
    total_A = 0
    total_B = 0
    n = int(input())
    for _ in range(n):
        order = list(input().rstrip().split())
        if order[0] == 'ORDER':
            fac = order[2]
            if fac == 'A':
                facs['A'].append(int(order[1]))
                total_A += int(order[1])
            elif fac == 'B':
                facs['B'].append(int(order[1]))
                total_B += int(order[1])
            else:
                if total_A > total_B:
                    facs['B'].append(int(order[1]))
                    total_B += int(order[1])
                else:
                    facs['A'].append(int(order[1]))
                    total_A += int(order[1])
        else:
            fac = order[1]
            if fac == 'A':
                total_A -= facs[fac].popleft()
            else:
                total_B -= facs[fac].popleft()

    print(total_A, total_B)
