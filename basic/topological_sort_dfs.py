def topological_sort_dfs(n, edges):
    graph = {i: [] for i in range(n)}
    visited = set()
    stack = []

    for u, v in edges:
        graph[u].append(v)

    def dfs(node):
        if node in visited:
            return
        visited.append(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        stack.append(node)

    for node in range(n):
        if node not in visited:
            dfs(node)

    return stack[::-1]


# 예제 그래프 (강의 순서)
edges = [
    (0, 1),  # 자료구조 → 알고리즘
    (1, 2),  # 알고리즘 → 인공지능
    (3, 0)   # 컴퓨터 기초 → 자료구조
]
sorted_order_dfs = topological_sort_dfs(4, edges)
print("위상 정렬 결과 (DFS):", sorted_order_dfs)  # ✅ [3, 0, 1, 2]
