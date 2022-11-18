from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            return visited[x]
        for nx in [x-1, x+1, x*2]:
            if 0 <= nx < 100001 and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)

visited = [0]*100001
n, k = map(int, input().split())
print(bfs())
