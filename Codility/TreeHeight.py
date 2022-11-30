from extratypes import Tree  # library with types used in the task
from collections import deque

def solution(T):
    # write your code in Python 3.8.10
    queue = deque([(T, 0)])
    visited = []
    height = 0
    while queue:
        tmp = queue.pop()
        root = tmp[0]
        height = max(height, tmp[1])
        if root not in visited:
            visited.append(root)
            if root.l != None:
                queue.append((root.l, tmp[1] + 1))
            if root.r != None:
                queue.append((root.r, tmp[1] + 1))

    return height
