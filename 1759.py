from itertools import combinations
import sys
input = sys.stdin.readline

l, c = map(int, input().split())
letters = list(input().split())
letter_vow = []
letter_con = []
answer = []
vows = ['a', 'e', 'i', 'o', 'u']

for letter in letters: # 자모음 분리
    if letter in vows:
        letter_vow.append(letter)
    else:
        letter_con.append(letter)

def combis(r):
    for i in range(1, r):
        for vow_combi in combinations(letter_vow, i):
            for con_combi in combinations(letter_con, l-i):
                tmp = list(vow_combi) + list(con_combi)
                tmp = sorted(tmp)
                answer.append(''.join(tmp))

if l - len(letter_vow) >= 2:
    combis(len(letter_vow)+1)
else:
    combis(l-2+1)

for a in sorted(answer):
    print(str(a))
