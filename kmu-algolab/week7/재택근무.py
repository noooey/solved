t = int(input())
for _ in range(t):
    i, j, k, l = map(int, input().split()) # i: n of team
    able = list(input().split()) # j
    unable = list(input().split()) # k
    all_members = {n:[] for n in range(1, i+1)}
    home_members = {n:[] for n in range(1, i+1)}
    for q in range(1, l+1):
        team, m = map(int, input().split())
        works = list(input().split())
        home = True
        for work in works:
            if work in unable:
                home = False
        all_members[team].append(q)
        if home:
            home_members[team].append(q)

    homes = []
    for n in range(1, i+1):
        if len(home_members[n]) == len(all_members[n]):
            homes += [mem for mem in home_members[n] if not mem == min(home_members[n])]
        else:
            homes += home_members[n]

    if homes:
        print(' '.join(map(str, sorted(homes))))
    else:
        print(-1)
