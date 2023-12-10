import heapq

INF = float('inf')

def createGraph(n):
    graph = {}
    for _ in range(n):
        k, m, *vw = map(int, input().split())
        graph[k] = []
        for i in range(m):
            graph[k].append((vw[2*i], vw[2*i+1]))

    return graph


def dijkstra(graph, start):
    n = len(graph)
    distance = [INF]*(n+1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    edges = {i:[] for i in range(1, n+1)}

    while queue:
        dist, cur = heapq.heappop(queue)

        if distance[cur] < dist:
            continue

        for v, w in graph[cur]:
            if dist + w < distance[v]:
                distance[v] = dist + w
                edges[v] = edges[cur] + [(cur, v, w)]
                heapq.heappush(queue, (dist + w, v))

    edge_list = []
    for edge, weights in edges.items():
        edge_list += weights

    d_sum = 0
    for tup in set(edge_list):
        d_sum += tup[2]

    return d_sum

t = int(input())
for _ in range(t):
    n = int(input())
    graph = createGraph(n)
    print(dijkstra(graph, 1))
