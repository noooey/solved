# O(N * log(N))
from collections import Counter

def solution(A):
    dic = Counter(A)
    exist = False
    for item in dic.items():
        if item[1] == 1:
            exist = True
            return item[0]
    if not exist:
        return -1
