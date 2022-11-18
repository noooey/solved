from itertools import combinations
import sys
input = sys.stdin.readline

def total(combis):
    tmp = 0
    for c in combinations(combis, 2):
        tmp += (power[c[0]][c[1]] + power[c[1]][c[0]])
    return tmp

n = int(input())
teams = set([i for i in range(n)])
power = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    power.append(tmp)

team_s = 0
team_l = 0
diff = 1000000
for combi in combinations(teams, int(n/2)):
    team_s = total(combi)
    team_l = total(teams - set(combi))
    diff = min(diff, abs(team_s-team_l))

print(diff)
