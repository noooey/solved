import sys
input = sys.stdin.readline
from itertools import product

"""
하 ((N-2, -1, -1), (0, N, 1))
좌 ((0, N, 1), (1, N, 1))
상 ((1, N, 1), (0, N, 1))
우 ((0, N, 1), (N-2, -1, -1))
"""

# dir: 0, 1, 2, 3
def direction(N, B, dir):
    # 하0 좌1 상2 우3
    d = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}
    dirs = [((N-2, -1, -1), (0, N, 1)), ((0, N, 1), (1, N, 1)), ((1, N, 1), (0, N, 1)), ((0, N, 1), (N-2, -1, -1))]
    S = [[False for i in range(N)] for j in range(N)] # 상태 저장

    dy, dx = d[dir][0], d[dir][1]
    for i in range(dirs[dir][0][0], dirs[dir][0][1], dirs[dir][0][2]):
        for j in range(dirs[dir][1][0], dirs[dir][1][1], dirs[dir][1][2]):
            t1, t2 = 0, 0
            # 0은 움직일 필요 없음
            if B[i][j] != 0:
                while True: # 앞으로 안 쓰자...
                    # 벽
                    if not i+t1+dy in range(0, N) or not j+t2+dx in range(0, N):
                        break
                    elif S[i+t1+dy][j+t2+dx] == True:
                        break

                    elif B[i+t1+dy][j+t2+dx] == 0:
                        B[i+t1+dy][j+t2+dx] = B[i+t1][j+t2]
                        B[i+t1][j+t2] = 0
                        t1 += dy
                        t2 += dx
                    # 오른쪽이랑 값 똑같애 -> 더해줭
                    elif B[i+t1+dy][j+t2+dx] == B[i+t1][j+t2] and S[i+t1+dy][j+t2+dx] != True:
                        B[i+t1+dy][j+t2+dx] += B[i+t1][j+t2]
                        B[i+t1][j+t2] = 0
                        S[i+t1+dy][j+t2+dx] = True

                        break

                    else:
                        break # 오늘의 교훈... 남는거 break 시켜주자...

# # x +1 오른쪽 한 칸 이동
# def right(N, board):
#     B = board
#     S = [[False for i in range(N)] for j in range(N)] # 상태 저장
#     for i in range(N):
#          for j in range(N-2, -1, -1):
#              # 오른쪽에 아무것도 없을 때 계속 ㄱㄱ
#              t = 0
#              while S[i][j+t+1] != True and B[i][j+t+1] == 0 and B[i][j+t] != 0:
#                  B[i][j+t+1] = B[i][j+t]
#                  B[i][j+t] = 0
#                  t += 1
#                  if j+t+1 >= N: # 벽
#                     print('byuck')
#                     break
#
#              if B[i][j+t] != 0 and j+t+1 < N:
#                  if B[i][j+t+1] == B[i][j+t] and S[i][j+t+1] != True: # 오른쪽이랑 값 똑같애 -> 더해줭
#                     B[i][j+t+1] += B[i][j+t]
#                     S[i][j+t+1] = True
#                     B[i][j+t] = 0
#                 # 오른쪽이랑 값 다르면 냅도
#
#     return B
#
# # y -1 아래쪽 한 칸 이동
# def down(N, board):
#     B = board
#     S = [[False for i in range(N)] for j in range(N)] # 상태 저장
#     for i in range(N-2, -1, -1):
#          for j in range(N):
#              # 아래쪽에 아무것도 없을 때 계속 ㄱㄱ
#              t = 0
#              while S[i+t+1][j] != True and B[i+t+1][j] == 0 and B[i+t][j] != 0:
#                  B[i+t+1][j] = B[i+t][j]
#                  B[i+t][j] = 0
#                  t += 1
#                  if i+t+1 >= N: # 벽
#                     print('byuck')
#                     break
#
#              if B[i+t][j] != 0 and i+t+1 < N:
#                  if B[i+t+1][j] == B[i+t][j] and S[i+t+1][j] != True: # 오른쪽이랑 값 똑같애 -> 더해줭
#                     B[i+t+1][j] += B[i+t][j]
#                     S[i+t+1][j] = True
#                     B[i+t][j] = 0
#                 # 오른쪽이랑 값 다르면 냅도
#
#     return B

def solutions(N):
    board = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        board[i] = list(map(int, input().split()))

    answer = 0

    for case in product(range(4), range(4), range(4), range(4), range(4)):
        tmp = [item[:] for item in board]
        for c in case:
            direction(N, tmp, c)
        answer = max(max(map(max, tmp)), answer)
    return answer

if __name__ == "__main__":
    print(solutions(int(input())))
