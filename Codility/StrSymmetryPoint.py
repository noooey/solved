
def solution(S):
    l = len(S)
    if l % 2 == 0:
        return -1
    elif l == 1:
        return 0
    else:
        for i in range(l//2):
            if S[i] != S[-(i+1)]:
                return -1
        return l//2
