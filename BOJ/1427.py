import sys
input = sys.stdin.readline

def solutions(N):
    nums = sorted([int(c) for c in str(N)], reverse=True)
    return ''.join([str(m) for m in nums])


if __name__ == "__main__":
    n = int(input())
    print(solutions(n))
