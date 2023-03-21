t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    sizes = sorted(list(map(int, input().split())))

    i = 0
    j = n-1
    while n > j > i >= 0:
        if sizes[i] + sizes[j] == p:
            print(sizes[i], sizes[j])
            break
        else:
            if sizes[i+1] + sizes[j] > p:
                j -= 1
            else:
                i += 1
