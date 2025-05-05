def makeTeam(values):
    checked = [0]*(len(values))
    teams = 0
    for j in range(1, len(values)):
        if checked[j] == 0:
            i = j
            teams += 1
            while True:
                if checked[i] == 0:
                    checked[i] = 1
                    i = values[i]
                else:
                    break
    return teams

t = int(input())
for _ in range(t):
    values = list(map(int, input().split()))
    print(makeTeam(values))


"""
1부터 n까지 각 학생이 뽑은 수

3
11 4 5 6 11 10 9 2 8 3 7 1
5 1 2 3 4 5
7 5 7 2 6 3 1 4
"""

    # for i in range(1, len(values)):
    #     team = []
    #     if i == values[i]:
    #         teams.append([i])
    #     else:
    #         if check[i] == 0 and check[values[i]] == 0:
    #             team.append(i)
    #             check[i] = 1
    #             team.append(values[i])
    #             check[values[i]] = 1
    #             if len(team) > 0:
    #                 teams.append(team)
