import sys
input = sys.stdin.readline

def solutions(N, M):
    address = {}
    for _ in range(N):
        ad, pw = input().split()
        address[ad] = pw

    for _ in range(M):
        print(address[input().rstrip()])

if __name__ == "__main__":
    n, m = map(int, input().split())
    solutions(n, m)
