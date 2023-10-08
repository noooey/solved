from itertools import combinations
from math import factorial

def calc_weight(s):
    return sum(ord(s[i]) - ord('a') for i in range(0, len(s)))

def permutate(s):
    cnt = 0
    n = len(s)

    for odd_combi in combinations(s, n//2):
        even_combi = [chr for chr in s if chr not in odd_combi]
        w = calc_weight(even_combi) - calc_weight(odd_combi)
        if w > 0:
            cnt += 1

    return cnt * factorial(n//2) * factorial(n-n//2)

t = int(input())
for _ in range(t):
    s = list(str(input()).rstrip())
    print(permutate(s))

"""
timeout code...

def permutateString(s, begin, end, w, cnt):
    if begin == end - 1:
        if begin % 2 == 0:
            w += (ord(s[-1])-ord('a'))
        else:
            w -= (ord(s[-1])-ord('a'))
        if w > 0:
            cnt[0] += 1
        return
    else:
        for i in range(begin, end):
            s[i], s[begin] = s[begin], s[i]
            tmp = 0
            if begin % 2 == 0:
                tmp += (ord(s[begin])-ord('a'))
            else:
                tmp -= (ord(s[begin])-ord('a'))
            permutateString(s, begin+1, end, w+tmp, cnt)
            s[i], s[begin] = s[begin], s[i]

def permutate(s):
    cnt = [0]
    permutateString(s, 0, len(s), 0, cnt)
    return cnt[0]
"""
