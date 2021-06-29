import math
import sys
sys.setrecursionlimit(10**5)

def recursive(i):
    if i == 0:
        return 1
    elif i == 1:
        return 3
    else:
        x = recursive(math.floor(i-math.sqrt(i)))+recursive(math.floor(math.log(i)))+recursive(math.floor(i*math.sin(i)*math.sin(i)))
        return x


while(True):
    i = int(sys.stdin.readline())
    if i == -1:
        break
    else:
        print(recursive(i) % 1000000)