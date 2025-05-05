def floyd_warshall(graph):
    INF = float('inf')
    nodes = list(graph.keys())
    n = len(nodes)

    dist = {u: {v: INF for v in nodes} for u in nodes}
    for u in nodes:
        dist[u][u] = 0
        for v, w in graph[u].items():
            dist[u][v] = w

    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

graph = {
    1: {2: 2, 3: 5},
    2: {1: 2, 3: 3},
    3: {1: 5, 2: 3}
}

distances = floyd_warshall(graph)
for key in distances:
    print(f"{key}: {distances[key]}")
