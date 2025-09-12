# 079. Word Search

## Code (Python)
```python3
from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        if n * m < len(word):
            return False

        starts = []
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    starts.append((i, j))
        if not starts:
            return False

        for a, b in starts:
            queue = deque([(a, b, [(a, b)])])
            dxs = [1, 0, -1, 0]
            dys = [0, 1, 0, -1]
            while queue:
                y, x, path = queue.popleft()
                cur_len = len(path)
                if cur_len == len(word):
                    return True
                target = word[cur_len]

                for dy, dx in zip(dys, dxs):
                    ay, ax = y + dy, x + dx
                    if 0 <= ay < n and 0 <= ax < m and (ay, ax) not in path:
                        if board[ay][ax] == target:
                            queue.append((ay, ax, path + [(ay, ax)]))

        return False
```

## Complexity
- Time: O(n·m·L·3^L)

## Notes
- BFS
- Back-tracking(recommended)
