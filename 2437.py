import sys
input = sys.stdin.readline

n = int(input())
w_list = list(map(int, input().split()))
w_list.sort()

tmp = 1
for w in w_list:
    if tmp < w:
        break

    tmp += w

print(tmp)


"""
1 - > 1
1, 1 -> 1, 2
1, 1, 2 -> 1, 2, 3, 4
1, 1, 2, 3 -> 1, 2, 3, 4, 5, 6, 7
1, 1, 2, 3, 6 -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
1, 1, 2, 3, 6, 7 -> 1, 2, 3, ~, 13, 14, 15, 16, 17, 18, 19
1, 1, 2, 3, 6, 7, 30 ->
"""
