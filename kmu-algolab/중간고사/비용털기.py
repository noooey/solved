# 100점!

t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    n_list = sorted(list(map(int, input().split())))

    i = 0
    j = n-1
    while True:
        if n_list[i] + n_list[j] == p:
            break
        elif n_list[i] + n_list[j] < p:
            i += 1
        else:
            j -= 1

    print(n_list[i], n_list[j])
