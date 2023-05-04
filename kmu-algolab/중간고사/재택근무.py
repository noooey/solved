# 100점!

t = int(input())
for _ in range(t):
    i, j, k, l = map(int, input().split()) # i 팀개수, j 재택가능개수, k 재택 불가능개수, l 사원수
    ables = list(input().split())
    unables = list(input().split())
    total = {o:[] for o in range(1, i+1)}
    home_mem = {p:[] for p in range(1, i+1)}
    for mem in range(1, l+1):
        n, m = map(int,input().split())
        m_list = list(input().split())
        home = True
        for work in m_list:
            if work in unables:
                home = False
        if home:
            home_mem[n].append(mem)

        total[n].append(mem)

    # print(total)
    # print(home_mem)

    for q in range(1, i+1):
        if len(total[q]) == len(home_mem[q]):
            home_mem[q] = sorted(home_mem[q], reverse=True)[:-1]

    result = []
    for item in home_mem.items():
        result += item[1]

    if result:
        print(' '.join(map(str, sorted(result))))
    else:
        print(-1)
