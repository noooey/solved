import math
import sys
sys.setrecursionlimit(10**6)

dict = {0: 1}

def recursive(i):
    if i in dict:
        return dict[i]
    else:
        dict[i] = recursive(math.floor(i-math.sqrt(i)))+recursive(math.floor(math.log(i)))+recursive(math.floor(i*math.sin(i)*math.sin(i)))
        return dict[i]


while(True):
    i = int(sys.stdin.readline())
    if i == -1:
        break
    else:
        print(recursive(i) % 1000000)