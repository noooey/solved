import sys
from itertools import combinations
input = sys.stdin.readline

chars = {'a', 'c', 'i', 'n', 't'}
n, k = map(int, input().split())
word_list = [set(input().rstrip())-chars for _ in range(n)]

answer = 0
if k < 5: # k가 5보다 작으면 배울 수 있는 단어가 없음
    print(answer)
else:
    k -= 5 # a c i n t

    # 입력된 단어에 있는 char들 집합을 길이 26짜리 리스트로 표현
    alpha = [0]*26

    # 입력 단어에 포함된 알파벳 인덱싱
    for j in range(len(word_list)):
        w_bit = 0
        for w in word_list[j]:
            idx = ord(w) - ord('a')
            w_bit |= (1 << idx)
            if alpha[idx] == 0:
                alpha[idx] = 1
        word_list[j] = w_bit

    input_chars = []
    for i in range(len(alpha)):
        bit = 0
        if alpha[i] == 1:
            bit |= (1 << i)
            input_chars.append(bit)

    if k >= len(input_chars):
        answer = n

    for combi in combinations(input_chars, k):
        c = sum(combi)
        cnt = 0
        for word in word_list:
            if word & c == word:
                cnt += 1
        answer = max(answer, cnt)

    print(answer)
