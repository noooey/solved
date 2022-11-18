from collections import deque
import sys
input = sys.stdin.readline

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort(reverse=True)
                stack += tmp
    return ' '.join(str(i) for i in visited)

def BFS(graph, root):
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
    return ' '.join(str(i) for i in visited)


graph = {}
node, edge, start = map(int, input().split())
# 그래프에 노드 추가
for i in range(edge):
    node_1, node_2 = map(int, input().split())
    if node_1 not in graph:
        graph[node_1] = [node_2]
    elif node_2 not in graph[node_1]:
        graph[node_1].append(node_2)

    if node_2 not in graph:
        graph[node_2] = [node_1]
    elif node_1 not in graph[node_2]:
        graph[node_2].append(node_1)

print(DFS(graph, start))
print(BFS(graph, start))
