from collections import deque
import sys
input = sys.stdin.readline

def solutions(N, M, DOCS):
    cnt = 0
    # 주어진 문서 큐
    queue = deque(DOCS)

    while queue:
        tmp = queue[0]
        if tmp[0] == max([i[0] for i in queue]):
            queue.popleft()
            cnt += 1
            if tmp[1] == M:
                return cnt
        else:
            queue.append(queue.popleft())
    return cnt

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        imps = list(map(int, input().split()))
        docs = []
        for imp, idx in zip(imps, [i for i in range(n)]):
            docs.append((imp, idx))
        print(solutions(n, m, docs))
