from collections import deque

def solutions(r, c, k, map_info):
    cnt = 0
    queue = deque([(r-1, 0, [(r-1, 0)])])
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        y, x, cur_list = queue.popleft()
        # print('-----------')
        # print(cur_list)
        # for i in range(R):
        #     line = ''
        #     for j in range(C):
        #         if i == y and x == j:
        #             line += 'x'
        #         else:
        #             line += '.'
        #     print(line)
        if len(cur_list) == k and y == 0 and x == c-1:
            cnt += 1
            continue

        for dy, dx in dir:
            if (y+dy, x+dx) not in cur_list:
                if r > y+dy >= 0 and c > x+dx >= 0:
                    if map_info[y+dy][x+dx] != 'T':
                        next_list = cur_list+[(y+dy, x+dx)]
                        queue.append((y+dy, x+dx, next_list))

    return cnt

R, C, K = map(int, input().split())
map_info = []
for _ in range(R):
    map_info.append(input())
print(solutions(R, C, K, map_info))
