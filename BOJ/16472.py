n = int(input())
string = input()

length = 0
pre = ''
# 하나씩 확인하면서
# 이전거랑 같다면 tmp개수 늘리고
# 달라지면 tmp 0으로 초기화
#
tmp = 0
for chr in string:
    if chr == pre:
        tmp += 1
    else:
        print(f'chr!!!: {tmp}')
        pre = chr
        tmp = 1
print(f'chr!!!: {tmp}')
