# def solution(d, values):
#     benefit = 0
#     high = values[-1]
#     for v in values[::-1][1:]:
#         if v > high:
#             high = v
#         else:
#             benefit += (high - v)
#     return benefit
#
# t = int(input())
# for _ in range(t):
#     d = int(input())
#     values = list(map(int, input().split()))
#     print(solution(d, values))


# 4번
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
