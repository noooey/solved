N = int(input())
edges = list(map(int, input().split()))
costs = list(map(int, input().split()))

cur = costs[0]
total = edges[0] * cur
for i in range(1, N-1):
    if costs[i] < cur:
        cur = costs[i]
    total += edges[i] * cur

print(total)
