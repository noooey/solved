def topological_sort(n, edges):
    graph = {i: [] for i in range(n)}
    indegree = {i: 0 for i in range(n)}

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([node for node in range(n) if indegree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result

# 예제 그래프 (강의 순서)
edges = [
    (0, 1),  # 자료구조 → 알고리즘
    (1, 2),  # 알고리즘 → 인공지능
    (3, 0)   # 컴퓨터 기초 → 자료구조
]

sorted_order = topological_sort(4, edges)
print("위상 정렬 결과:", sorted_order)  # ✅ [3, 0, 1, 2]
