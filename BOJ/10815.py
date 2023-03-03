n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

p_idx = [0]*10_000_001
n_idx = [0]*10_000_001
answer = []

for ni in n_list:
    if ni >= 0:
        p_idx[ni] += 1
    else:
        n_idx[ni] += 1

for mi in m_list:
    if mi >= 0:
        if p_idx[mi] != 0:
            answer.append(1)
        else:
            answer.append(0)
    else:
        if n_idx[mi] != 0:
            answer.append(1)
        else:
            answer.append(0)

print(' '.join(map(str, answer)))


# """
# # time out
# for card in m_list:
#     if card in n_list:
#         answer.append(1)
#     else:
#         answer.append(0)
# """
