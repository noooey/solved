import sys
input = sys.stdin.readline

def getMcnt(times, cut):
    m_cnt = 1
    tmp = 0
    for time in times:
        if tmp + time > cut:
            m_cnt += 1
            tmp = time
        else:
            tmp += time
    return m_cnt

N, M = map(int, input().split())
times = list(map(int, input().split()))

i = 0
j = len(times)-1
while i <= j:
    k = (i + j) // 2
    cut = sum(times[k:])
    print(cut)
    if getMcnt(times, cut) < M:
        # 개당 사이즈 더 작게
        j = k - 1
    elif getMcnt(times, cut) > M:
        # 개당 사이즈 더 크게
        i = k + 1
    else:
        print(k, cut)
        break

print(getMcnt(times,cut))


# if M == 1:
#     print(sum(times))
# else:
#     start = 1
#     end = sum(times)
#
#     while start <= end:
#         cut = (start + end) // 2
#         if getMcnt(times, cut)[0] < M:
#             # 개당 사이즈 더 작게
#             end = cut - 1
#         elif getMcnt(times, cut)[0] > M:
#             # 개당 사이즈 더 크게
#             start = cut + 1
#         else:
#             print(cut)
#             break
#
#     print(getMcnt(times,cut)[1])
