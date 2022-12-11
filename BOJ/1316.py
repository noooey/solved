import sys
input = sys.stdin.readline

def solutions(N):
    cnt = 0
    for _ in range(N):
        string = str(input())
        exist = []
        pre = ''
        group_word = True
        for chr in string:
            if chr not in exist:
                exist.append(chr)
            elif pre != chr:
                group_word = False
                break
            pre = chr
        if group_word:
            cnt += 1
    return cnt

if __name__ == "__main__":
    n = int(input())
    print(solutions(n))
