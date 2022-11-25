import sys
input = sys.stdin.readline

dol = [0, 1, 2, 1]
def game(num):
    if n >= len(dol):
        for i in range(len(dol), num+1):
            dol.append(min(dol[i-1],dol[i-3])+1)
    if dol[num] % 2 == 0:
        return 'CY'
    else:
        return 'SK'

n = int(input())
print(game(n))
