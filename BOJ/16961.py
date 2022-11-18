N = int(input())
day = [[0]*2 for i in range(366)]
long_time = 0

for i in range(N):
    c, s, e = input().split()
    if c == 'T':
        for j in range(int(s)-1, int(e)):
            day[j][0] += 1
    else:
        for j in range(int(s)-1, int(e)):
            day[j][1] += 1
    if (int(e)-int(s)+1) > long_time:
        long_time = (int(e)-int(s)+1)


over0 = 0
max = day[0][0] + day[0][1]
no_fight = 0
no_fight_max = 0
for i in range(366):
    if day[i][0]+day[i][1] > 0:
        over0 += 1
    if day[i][0] + day[i][1] > max:
        max = day[i][0] + day[i][1]
    if day[i][0] == day[i][1] and day[i][0] > 0:
        # 아무도 숙박하지 않은 경우는 제외
        no_fight += 1
        if day[i][0] + day[i][1] > no_fight_max:
            no_fight_max = day[i][0] + day[i][1]


print(over0)
print(max)
print(no_fight)
print(no_fight_max)
print(long_time)