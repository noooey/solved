import sys
input = sys.stdin.readline

n = int(input())
stairs = [0]*301
for i in range(1, n+1):
    stairs[i] = int(input())

score = [0]*301
score[1] = stairs[1]
score[2] = stairs[1] + stairs[2]
score[3] = max(stairs[1], stairs[2]) + stairs[3]

for i in range(4, n+1):
    score[i] = max(score[i-3] + stairs[i-1], score[i-2]) + stairs[i]

print(score[n])
