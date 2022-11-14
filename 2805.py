import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

end = max(trees)
start = 0

while end >= start:
    height = (start + end) // 2
    tmp = 0
    for tree in trees:
        if tree >= height:
            tmp += (tree - height)
    if tmp >= m:
        start = height + 1
    else:
        end = height - 1

print(end)

# 시간초과
# height = max(trees)
# tmp = 0
# while m > tmp:
#     tmp = 0
#     for tree in trees:
#         if tree > height:
#             tmp += (tree - height)
#     if tmp >= m:
#         break
#     height -= 1
#
# print(height)
