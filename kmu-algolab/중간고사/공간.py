# time outㅠㅠ

def gcd(n, m):
    max_gcd = 0
    for i in range(2, n):
        if m % i == 0 and n % i == 0:
            max_gcd = max(max_gcd, i)
    return max_gcd

def gcds(arr):
    max_gcd = 0
    for i in range(len(arr)-1):
        max_gcd = max(max_gcd, gcd(arr[i], arr[i+1]))
    return max_gcd

def yaksu(n):
    yaksu = []
    for i in range(1, n+1):
        if n % i == 0:
            yaksu.append(i)
    return yaksu

t = int(input())
for _ in range(t):
    n, T = map(int, input().split())
    cost = {}
    cost_by_time = {}
    max_time = 0
    for _ in range(n):
        t, f = map(int, input().split())
        max_time = max(max_time, t)
        if f in cost:
            cost[f].append(t)
        else:
            cost[f] = [t]
        cost_by_time[t] = f
    # print(cost)

    min_term = 1
    for item in cost.items():
        if len(item[1]) > 1:
            term = max(item[1]) - min(item[1])
            min_term = max(min_term, term)
    # print(min_term)

    max_cost = gcds(list(cost.keys()))
    result = []
    for y in yaksu(max_cost):
        for x in range(min_term, max_time):
            term = x
            time = 0
            c_tmp = y
            tmp = {}
            while time <= max(T, max_time):
                tmp[time] = c_tmp
                time += 1
                if time % term == 0:
                    c_tmp += y
            # print(tmp)
            for item in cost_by_time.items():
                ok = True
                if tmp[item[0]] != item[1]:
                    ok = False
                    break
            if ok:
                result.append(tmp[T])
    if result:
        print(min(result), max(result))
    else:
        print(-1)
