import math

exp = 0

T = int(input())
for i in range(T):
    N = int(input())
    for j in range(N):
        X1, Y1, X2, Y2 = map(int, input().split())
        if X1 != 0 and Y1 != 0 and X2 != 0 and Y2 != 0:
            exp += abs(math.atan(Y1 / X1) - math.atan(Y2 / X2))
        elif (X1 == 0 and Y2 == 0) or (Y1 == 0 and X2 == 0):
            exp += math.pi/2
        elif X1 == 0 and X2 != 0:
            exp += abs(math.atan(X2 / Y2))
        elif X2 == 0 and X1 != 0:
            exp += abs(math.atan(X1 / Y1))
        elif Y1 == 0 and Y2 != 0:
            exp += abs(math.atan(Y2 / X2))
        elif Y2 == 0 and Y1 != 0:
            exp += abs(math.atan(Y1 / X1))
        else:
            exp += 0


    print("{:.5f}".format(exp/(math.pi*2)))
    exp = 0