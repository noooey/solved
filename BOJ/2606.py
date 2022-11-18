from collections import deque
import sys
input = sys.stdin.readline

def BFS(root, graph):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort()
                queue += tmp
    return len(visited)

n = int(input())
e = int(input())
graph = {}
for _ in range(e):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    else:
        graph[n1].append(n2)
    if n2 not in graph:
        graph[n2] = [n1]
    else:
        graph[n2].append(n1)

print(BFS(1, graph)-1)
