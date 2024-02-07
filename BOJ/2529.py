from collections import deque

def solutions(k, k_list):
    queue = deque([(i, 0, [i]) for i in range(10)])
    results = []

    while queue:
        cur, idx, cur_list = queue.popleft()

        if idx+1 >= k+1:
            results.append(''.join(list(map(str, cur_list))))
            continue

        com = k_list[idx]

        if com == '>':
            if cur == 0:
                continue
            for i in range(0, cur):
                if i in cur_list:
                    continue
                next_list = cur_list +[i]
                queue.append((i, idx+1, next_list))
        else:
            if cur == 9:
                continue
            for i in range(cur+1, 10):
                if i in cur_list:
                    continue
                next_list = cur_list +[i]
                queue.append((i, idx+1, next_list))

    return f'{max(results)}\n{min(results)}'

k = int(input())
k_list = list(input().split())
print(solutions(k, k_list))
