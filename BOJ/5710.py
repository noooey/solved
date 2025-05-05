import sys
input = sys.stdin.readline

def getFee(x):
    total = 0
    while x > 0:
        if x > 1_000_000:
            tmp = x - 1_000_000
            total += tmp * 7
            x -= tmp
        elif x > 10_000:
            tmp = x - 10_000
            total += tmp * 5
            x -= tmp
        elif x > 100:
            tmp = x - 100
            total += tmp * 3
            x -= tmp
        else:
            total += x * 2
            x -= x
    return total

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    start = 1
    end = 1_000_000_000
    cur = (start + end) // 2
    while end >= start:
        cur = (start + end) // 2
        if getFee(cur) > A:
            end = cur - 1
        elif getFee(cur) < A:
            start = cur + 1
        else:
            break

    """
    A = getFee(p1+p2)
    B = |getFee(p1) - getFee(p2)|
    cur = p1 + p2
    """

    start = 1
    end = (cur + start) // 2
    # |--|--|----|
    #   mid    cur
    mid = (start + end) // 2
    while end >= start:
        mid = (start + end) // 2
        if abs(getFee(cur-mid) - getFee(mid)) > B:
            start = mid + 1
        elif abs(getFee(cur-mid) - getFee(mid)) < B:
            end = mid - 1
        else:
            break

    print(getFee(mid))
