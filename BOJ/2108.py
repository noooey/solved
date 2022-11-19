import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort()

cnt = 1
dic = {}
max_cnt = 1
for i in range(1, n+1):
    dic[i]= []
for i in range(1, n):
    if a[i] == a[i-1]:
        cnt += 1
    else:
        dic[cnt].append(a[i-1])
        max_cnt = max(cnt, max_cnt)
        cnt = 1
    if i == n-1:
        dic[cnt].append(a[i-1])
        max_cnt = max(cnt, max_cnt)

if n == 1:
    dic[1].append(a[0])
print(round(sum(a)/n))
print(a[n//2])
if len(dic[max_cnt]) > 1:
    print(dic[max_cnt][1])
else:
    print(dic[max_cnt][0])
print(max(a)-min(a))
