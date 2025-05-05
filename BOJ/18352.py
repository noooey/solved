from collections import deque

def bacon(n, graph):
    table = [[float('inf')]*(n+1) for _ in range(n+1)]
    for key, values in graph.items():
        for i in values:
            table[key][i] = 1

    for root in range(1, n+1):
        queue = deque([(root, root, 0)])
        while queue:
            root, cur, cnt = queue.popleft()

            table[root][cur] = min(table[root][cur], cnt)

            for friend in graph[cur]:
                queue.append((root, friend, cnt+1))

    return

n, m = map(int, input().split())
graph = {}
for _ in range(m):
    a, b = map(int, input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

print(graph)
