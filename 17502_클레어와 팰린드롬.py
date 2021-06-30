import random
import string
N = int(input())
lst = list(input())
string_pool = string.ascii_lowercase

for i in range(N//2):
    if lst[i] == "?":
        if lst[-1-i] != "?":
            lst[i] = lst[-1-i]
        else:
            lst[i] = random.choice(string_pool)
            lst[-1-i] = lst[i]
    else:
        if lst[-1-i] == "?":
            lst[-1-i] = lst[i]

if N % 2 != 0:
    if lst[(N//2)] == "?":
        lst[(N//2)] = random.choice(string_pool)

print(''.join(lst))
