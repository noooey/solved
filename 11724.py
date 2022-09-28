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
                queue += tmp

    return visited

n, m = map(int, input().split())

# 반례 주의~
# 노드 n개, 간선 0개
# 노드 0개, 간선 0개
if m == 0:
    if n == 0:
        print(0)
    else:
        print(n)
else:
    graph = {}
    for i in range(m):
        n1, n2 = map(int, input().split())
        if n1 not in graph:
            graph[n1] = [n2]
        else:
            graph[n1].append(n2)
        if n2 not in graph:
            graph[n2] = [n1]
        else:
            graph[n2].append(n1)

    cnt = 0
    keys = list(graph.keys())
    # 반례 주의~
    # 혼자 있는 노드 개수 고려~
    cnt += (n-len(keys))
    while keys and graph:
        keys = list(set(keys) - set(BFS(keys[0], graph)))
        cnt += 1
    print(cnt)
