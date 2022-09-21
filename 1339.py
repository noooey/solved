import heapq
import sys
input = input = sys.stdin.readline

N = int(input())

al_dic = {}
for i in range(N):
    words = list(input().rstrip('\n'))
    length = len(words)
    for w in words:
        if w in al_dic:
            al_dic[w] += pow(10, length-1)
        else:
            al_dic[w] = pow(10, length-1)
        length -= 1

al_heap = []
for al in al_dic.items():
    heapq.heappush(al_heap, (-al[1], al[0]))

num = 9
total = 0
while al_heap:
    total += -heapq.heappop(al_heap)[0] * num
    num -= 1

print(total)
