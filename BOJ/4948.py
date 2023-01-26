from math import sqrt
import sys
input = sys.stdin.readline

def is_prime_number(M):
    for j in range(2, int(sqrt(M))+1):
        if M % j == 0:
            return False
    return True

def solutions(N):
    # N < 소수 <= 2N
    cnt = 0
    for i in range(N+1, 2*N+1):
        if is_prime_number(i):
            cnt += 1
    return cnt

if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            exit()
        else:
            print(solutions(n))
