import math
exp = 0.000000
T = int(input())

for i in range(T):
    N = int(input())
    for j in range(N):
        X1, Y1, X2, Y2 = map(int, input().split())
        if (X1 == -X2 and Y1 == -Y2) or (X1 == 0 and Y1 == 0) or (X2 == 0 and Y2 == 0):
            break
        else:
            exp += math.acos((X1*X2 + Y1*Y2)/math.sqrt((X1*X1 + Y1*Y1)*(X2*X2 + Y2*Y2)))
    print("{:.5f}".format(round(exp/(math.pi*2), 5)))
    exp = 0.00000