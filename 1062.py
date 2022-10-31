# fail...

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
word_list = [list(input().rstrip()[4:-4]) for _ in range(n)]
word_list = sorted(word_list, key=len)
# print(word_list)

start_end = set(list('anta')) | set(list('tica'))
word_set = start_end

w = 0
if k < 5: # antic 는 읽을 줄 알아야함
    print(w)
else:
    k -= 5
    for word in word_list:
        need = 0
        tmp = set(list(word))
        if len(tmp-start_end) != 0:
            need = len(tmp-start_end)
            if k >= need:
                k -= need
                w += 1
            else:
                break
            word_set |= tmp
        else:
            w += 1

print(w)
