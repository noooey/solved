import sys
input = sys.stdin.readline

def solutions(S):
    cnt = 1
    pre = S[0]
    if pre == 'd':
        cnt *= 10
    else:
        cnt *= 26

    for chr in S[1:]:
        if chr == 'd': # 숫자
            tmp = cnt
            cnt *= 10
            if pre == chr:
                cnt -= tmp
            pre = chr
        else: # 문자
            tmp = cnt
            cnt *= 26
            if pre == chr:
                cnt -= tmp
            pre = chr
    return cnt

if __name__ == "__main__":
    print(solutions(list(input().rstrip())))
