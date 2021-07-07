import copy

lst = []
N = int(input())
lst.append([0 for i in range(N)])
M = int(input())
idx_list = list(map(int, input().split()))
dir_str = input()
result = 1

for i in range(M):
    tmp = copy.deepcopy(lst[i])
    if dir_str[i] == '+':
        tmp[idx_list[i]-1] += 1
        if tmp in lst:
            result = 0
            break
        lst.append(tmp)
    else:
        tmp[idx_list[i] - 1] -= 1
        if tmp in lst:
            result = 0
            break
        lst.append(tmp)

print(result)