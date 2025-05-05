t = int(input())
for _ in range(t):
    n = int(input())
    string = list(map(int, input().split()))
    times = []
    for i in range(0, len(string)-1, 2):
        times.append((string[i], string[i+1]))

    times = sorted(times, key=lambda x: x[0])
    times = sorted(times, key=lambda x: x[1])

    cnt = 0
    last = 0
    for time in times:
        if time[0] > last:
            cnt += 1
            last = time[1]
            # print(time, last, cnt)
        else:
            pass

    print(cnt)
