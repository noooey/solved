class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_b] = root_a

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    dsu = DisjointSet(n)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


edges = [
    (0, 1, 1), (0, 2, 3), (1, 2, 2), (1, 3, 4), (2, 3, 5)
]

mst, weight = kruskal(4, edges)
print("크루스칼 MST:", mst)  # 최소 신장 트리 간선들
print("총 비용:", weight)  # 최소 비용
