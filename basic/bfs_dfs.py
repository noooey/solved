from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

def dfs_stack(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

graph = {
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5],
    5: [2, 4, 6],
    6: [3, 5]
}

print("----")
# bfs(graph, 1)
dfs(graph, 1)
