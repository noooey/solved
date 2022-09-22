from collections import deque

N, K = map(int, input().split())

queue = deque([i for i in range(1, N+1)])

answer = []

while queue:
    for i in range(K-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print(f'<{str(answer)[1:-1]}>')
