from collections import deque

def solution(graph):
    queue = deque([1])
    visited = set()
    visited.add(1)

    while queue:
        root = queue.popleft()
        for neighbor in graph.get(root, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return len(visited) - 1

if __name__ == "__main__":
    node = int(input())
    edge = int(input())
    graph = {}
    for _ in range(edge):
        a, b = map(int, input().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)

        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)

    print(solution(graph))
