import heapq

def dijkstra(graph, start):
    INF = float('inf')
    distances = {node: INF for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
    1: {2: 2, 3: 5},
    2: {1: 2, 3: 3},
    3: {1: 5, 2: 3}
}

print(dijkstra(graph, 1))
