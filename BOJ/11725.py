import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = {}

# make tree
for _ in range(n-1):
    n1, n2 = map(int, input().split())
    if n1 in tree:
        tree[n1].append(n2)
    else:
        tree[n1] = [n2]

    if n2 in tree:
        tree[n2].append(n1)
    else:
        tree[n2] = [n1]

# dfs
visited = [0 for _ in range(n+1)]
def dfs(r):
    for node in tree[r]:
        if visited[node] == 0:
            visited[node] = r
            dfs(node)

dfs(1)

for j in range(2, len(visited)):
    print(visited[j])
