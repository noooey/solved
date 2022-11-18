from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

loca = []
for _ in range(r):
    line = list(input().rstripe())
    loca.append(line)

pipe = 0
for i in range(r):
    tmp = 0
    for j in range(c):
        if i + tmp > r:
            break
        if loca[i+tmp][j] != '.':
            if tmp == 0:
                if loca[i+tmp+1][j] == '.':
                    tmp += 1
                    loca[i+tmp][j] = 'x'
            elif r > tmp + i and tmp > 0:
                if loca[i+tmp-1][j] == '.':
                    tmp -= 1
                    loca[i+tmp][j] = 'x'
                elif loca[i+tmp][j] == '.':
                    loca[i+tmp][j] = 'x'
                elif loca[i+tmp+1][j] == '.':
                    tmp += 1
                    loca[i+tmp][j] = 'x'
            elif r <= tmp + i:
                break
        # j 가 음 끝에 다달았을때..?
