def subSeq(values):
    l = 1
    last = values[0]
    best = 1

    for i in range(1, len(values)):
        if values[i] >= last:
            last = values[i]
            l += 1
        else:
            best = max(best, l)
            l = 1
            last = values[i]
    return max(best, l)

t = int(input())
for _ in range(t):
    n, *values = map(int, input().split())
    print(subSeq(values))
