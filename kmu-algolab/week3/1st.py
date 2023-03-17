def solution(n, p, sizes):
    sizes = sorted(sizes)
    i = 0
    j = n-1
    while j > i >= 0 and n > j:
        if sizes[i] + sizes[j] == p:
            return sizes[i], sizes[j]
        else:
            if sizes[i+1] + sizes[j] > p:
                j -= 1
            else:
                i += 1

t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    sizes = list(map(int, input().split()))
    print(' '.join(map(str, solution(n, p, sizes))))
