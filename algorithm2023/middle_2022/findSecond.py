def findSecond(values, start, end):
    mid = (start+end) // 2
    if start == end:
        return values[start], float('-inf')
    else:
        left_1, left_2 = findSecond(values, start, mid)
        right_1, right_2 = findSecond(values, mid+1, end)

    tmp_list = sorted([left_1, left_2, right_1, right_2])

    return tmp_list[3], tmp_list[2]

t = int(input())
for _ in range(t):
    n, *values = map(int, input().split())
    first, second = findSecond(values, 0, n-1)
    print(second)
