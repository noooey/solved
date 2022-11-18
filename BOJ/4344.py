import sys
input = sys.stdin.readline

c = int(input())

for _ in range(c):
    tmp = list(map(int, input().split()))
    n = tmp[0]
    scores = tmp[1:]
    avg = sum(scores)/n
    cnt = 0
    for s in scores:
        if s > avg:
            cnt += 1
    answer = '%.3f' %(cnt/n*100)
    print(str(answer) + '%')
