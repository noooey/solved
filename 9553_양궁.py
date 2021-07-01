import math
exp = 0.000000
T = int(input())

for i in range(T):
    N = int(input())
    for j in range(N):
        X1, Y1, X2, Y2 = map(int, input().split())
        aa = X1**2 + Y1**2
        bb = X2**2 + Y2**2
        cc = (X1-X2)**2 + (Y1-Y2)**2
        if aa == 0 or bb == 0:
            exp += math.pi*2
        else:
            exp += math.acos((aa + bb - cc)/(2*math.sqrt(aa)*math.sqrt(bb)))
    print("{:.5f}".format(round(exp/(math.pi*2), 5)))
    exp = 0.00000