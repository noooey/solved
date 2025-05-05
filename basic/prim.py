import heapq

def prim(n, graph, start=0):
    visited = set()
    pq = [(0, start)]
    mst = []
    total_weight = 0

    while len(visited) < n:
        weight, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        total_weight += weight

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor))

    return total_weight

graph = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (2, 2), (3, 4)],
    2: [(0, 3), (1, 2), (3, 5)],
    3: [(1, 4), (2, 5)]
}

print("프림 MST 총 비용:", prim(4, graph))
