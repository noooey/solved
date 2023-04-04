i = int(input())

def solutions(n, cnt):
    nstr = str(n)
    if n < 10:
        nstr = '0' + nstr
    t = int(nstr[0]) + int(nstr[1])
    tstr = str(t)
    if t < 10:
        tstr = '0' + tstr
    new = int(nstr[1] + tstr[1])

    cnt += 1

    if new == i:
        print(cnt)
        exit(0)

    return solutions(new, cnt)

solutions(i, 0)
