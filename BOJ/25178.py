from collections import Counter
import sys
input = sys.stdin.readline

def solutions(N, S1, S2):
    moeum = ['a', 'e', 'i', 'o', 'u']

    if Counter(S1) != Counter(S2):
        return 'NO'

    if (S1[0] != S2[0]) or (S1[-1] != S2[-1]):
        return 'NO'

    for m in moeum:
        S1 = S1.replace(m, '')
        S2 = S2.replace(m, '')

    if S1 != S2:
        return 'NO'

    return 'YES'

if __name__ == "__main__":
    n = int(input())
    s1 = input().rstrip()
    s2 = input().rstrip()
    print(solutions(n, s1, s2))
