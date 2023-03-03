from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n+1)])

answer = []
while queue:
    cnt = 0
    while cnt != k-1:
        tmp = queue.popleft()
        cnt += 1
        queue.append(tmp)
    answer.append(queue.popleft())


print('<' + str(answer)[1:-1] + '>')
