from collections import deque
import sys
input = sys.stdin.readline


q = deque([])
N, T, W = map(int, input().split())
for _ in range(N):
    p, t = map(int, input().split())
    q.append((p, t))

waiting_q = deque([])
M = int(input())
for _ in range(M):
    p, t, c = map(int, input().split())
    waiting_q.append((p, t, c))

print(q)

time = 0


while qq:
    hi = False
    pp, tt, cc = qq.popleft()

    while time < cc:
        cus = q.popleft()
        if len(cus) == 2: # 시작 전
            p, t = cus
            if t > T:
                time += T
                t -= T
                for _ in range(T):
                    print(p)
                if time >= cc:
                    q.append((pp, tt))
                    hi = True
                    q.append((p, t))
                else:
                    q.append((p, t))
            else:
                time += t
                for _ in range(t):
                    print(p)

    if not hi:
        q.append((pp, tt))

print(q)

# while q:
#     if len(cus) == 2: # 시작 전
#         p, t = cus
#         if t > T:
#             time += T
#             t -= T
#             for _ in range(T):
#                 print(p)
#             q.append((p, t))
#         else:
#             time += t
#             for _ in range(t):
#                 print(p)
#     else: # 시작 후
#         p, t, c = cus
#         if time > c:
#             if t > T:
#                 time += T
#                 t -= T
#                 for _ in range(T):
#                     print(p)
#                 q.append((p, t))
#             else:
#                 time += t
#                 for _ in range(t):
#                     print(p)
#         else:
#             time = c
#             if t > T:
#                 time += T
#                 t -= T
#                 for _ in range(T):
#                     print(p)
#                 q.append((p, t))
#             else:
#                 time += t
#                 for _ in range(t):
#                     print(p)
