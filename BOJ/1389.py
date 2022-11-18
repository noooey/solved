from collections import deque
import sys
input = sys.stdin.readline

# 한 사람의 베이컨 수를 계산하는 함수 ->  BFS
def bacon(graph, root):
    bacon = [0]*(len(graph)+1) # 베이컨수 저장하는 리스트, 인덱스 1부터 셀거라 1더해줌
    visited = [False]*(len(graph)+1) # 방문 여부 표시 리스트
    visited[root] = True # root는 방문처리
    queue = deque([root])

    while queue:
        cur = queue.popleft() # 현재
        for friend in graph[cur]: # 현재 사람의 친구들을 순회하면서
            if visited[friend] is False: # 방문한 적이 없다면
                bacon[friend] = bacon[cur] + 1 # 현재 사람의 베이컨 수 + 1
                visited[friend] = True # 방문 표시
                queue.append(friend) # 큐에 방문해야할 친구 추가

    return sum(bacon)

# n: user의 수, m: 친구 관계의 수
n, m = map(int, input().split())

# user 관계 그래프 생성
users = {}
for i in range(1, n+1):
    users[i] = []
for _ in range(m):
    u1, u2 = map(int, input().split())
    if u2 not in users[u1]:
        users[u1].append(u2)
    if u1 not in users[u2]:
        users[u2].append(u1)

# 1부터 n까지 순회하며 베이컨의 수가 가장 작은 사람을 갱신
min_people = 0 # 베이컨의 수가 가장 작은 사람
for i in range(1, n+1):
    if i == 1:
        min_bacon = bacon(users, i)
        min_people = i
    if min_bacon > bacon(users, i):
        min_bacon = min(min_bacon, bacon(users, i))
        min_people = i

print(min_people)
