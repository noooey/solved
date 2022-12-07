from collections import deque
import sys
input = sys.stdin.readline


def solutions(N, A, B, M):
    graph = {}
    for _ in range(M):
        n1, n2 = map(int, input().split())
        if n1 in graph:
            graph[n1].append(n2)
        else:
            graph[n1] = [n2]
        if n2 in graph:
            graph[n2].append(n1)
        else:
            graph[n2] = [n1]


    visited = []
    queue = deque([(A, 0)])
    while queue:
        root = queue.pop()
        if root[0] == B:
            return root[1]
        if root[0] not in visited:
            visited.append(root[0])
            tmp = list(set(graph[root[0]]) - set(visited))
            queue += [(item, root[1]+1) for item in tmp]
    return -1

n = int(input())
a, b = map(int, input().split())
m = int(input())
print(solutions(n, a, b, m))
