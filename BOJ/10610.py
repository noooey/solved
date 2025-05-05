import sys
input = sys.stdin.readline

n = str(int(input()))
zeros = ''
others = []
for chr in n:
    if chr != '0':
        others.append(chr)
    else:
        zeros += '0'

others_sum = sum(list(map(int, others)))

if len(zeros) != 0 and others_sum % 3 == 0:
    answer = ''
    for o in sorted(others, reverse=True):
        answer += o
    print(int(answer + zeros))
else:
    print(-1)
