import sys
from itertools import combinations
input = sys.stdin.readline

def dist(loc1, loc2):
    return abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])

n, m = map(int, input().split())
city = []
house = []
chicken = []
for i in range(n):
    tmp = list(map(int, input().split()))
    city.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == 1:
            house.append((i, j))
        elif tmp[j] == 2:
            chicken.append((i, j))

chicken_dist = 2*(n-1)*len(house) # 최대 치킨 거리 * 집 개수
for combi in combinations(chicken, m):
    total_dist = 0
    for h in house:
        one_dist = 2*(n-1) # 최대 치킨 거리
        for c in combi:
            one_dist = min(one_dist, dist(c, h))
        total_dist += one_dist
    chicken_dist = min(chicken_dist, total_dist)

print(chicken_dist)
