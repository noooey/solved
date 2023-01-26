from math import sqrt
import sys
input = sys.stdin.readline

def is_sosu(M):
    if M == 1:
        return False
    for j in range(2, int(sqrt(M))+1):
        if M % j == 0:
            return False
    return True

memo = []
for k in range(2, 246912):
    if is_sosu(k):
        memo.append(k)

def solutions(N):
    # N < 소수 <= 2N
    cnt = 0
    for i in memo:
        if N < i <= 2*N:
            cnt += 1
    return cnt

if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            exit()
        else:
            print(solutions(n))
