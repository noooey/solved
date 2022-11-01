import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())

# 단어 리스트 인풋
word_list = [set(input().rstrip()) for _ in range(n)]

# k가 5보다 작거나 26일 경우
if k < 5:
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

# 알파벳 5개는 알고있어야함
start_end = set(list('anta')) | set(list('tica'))

# 가능한 알파벳 조합
word_set = set()
for word in word_list:
    word -= start_end
    word_set |= word
combi_list = list(combinations(word_set, k-5))

max = 0
for combi in combi_list:
    w = 0
    for word in word_list:
        if len(word-set(combi)) == 0:
            w += 1
    if w > max:
        max = w
    if max == n:
        break

print(max)
