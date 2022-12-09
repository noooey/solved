import sys
input = sys.stdin.readline

def solutions(N):
    if N < 100:
        return N
    else:
        cnt = 99
        for j in range(100, N+1):
            tmp = list(map(int, list(str(j))))
            term = (tmp[-1] - tmp[0]) // (len(tmp)-1)
            hansu = True
            for i in range(1, len(tmp)):
                if (tmp[i] - tmp[i-1]) != term:
                    hansu = False
                    break
            if hansu:
                cnt += 1
        return cnt

n = int(input())
print(solutions(n))
