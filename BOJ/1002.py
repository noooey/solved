import sys
import math
input = sys.stdin.readline

def distance(X1, Y1, X2, Y2):
    return math.sqrt((X2-X1)**2 + (Y1-Y2)**2)

def solutions(T):
    for i in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        # 중심 좌표 동일
        if (x1 == x2) and (y1 == y2) and (r1 == r2):
            print(-1)
        elif (x1 == x2) and (y1 == y2) and (r1 != r2):
            print(0)
        elif distance(x1, y1, x2, y2) < max(r1, r2):
            # 종속
            if distance(x1, y1, x2, y2) + min(r1, r2) < max(r1, r2):
                print(0)
            elif distance(x1, y1, x2, y2) + min(r1, r2) == max(r1, r2):
                print(1)
            elif distance(x1, y1, x2, y2) + min(r1, r2) > max(r1, r2):
                print(2)
        elif distance(x1, y1, x2, y2) > max(r1, r2):
            # 종속 X
            if distance(x1, y1, x2, y2) > (r1 + r2):
                print(0)
            elif distance(x1, y1, x2, y2) == (r1 + r2):
                print(1)
            elif distance(x1, y1, x2, y2) < (r1 + r2):
                print(2)
        elif distance(x1, y1, x2, y2) ==  max(r1, r2):
            print(2)

if __name__ == "__main__":
    t = int(input())
    solutions(t)

# 두 원의 크기가 같고 중심 좌표가 같다면, 개수 무한: -1
# 두 원이 맞닿는다면 개수 1
# 두 원이 겹치는 부분이 있다면 개수 2
# 겹치는 부분이 없다면 개수 0
## 한 원이 다른 한 원에 종속 되어 있다면 -> 0
## 두 원이 따로 있고 그 중심 좌표 사이의 거리가 두 반지름 합보다 크다면 -> 0
## 두 중심 좌표 사이 거리 + 작은 원 반지름 < 큰원 반지름 -> 0
