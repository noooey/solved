# 289. Game of Life

## Code (Python)
```python3
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n, m = len(board), len(board[0])
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        changes = [[0] * m for _ in range(n)]

        for y in range(n):
            for x in range(m):
                lives = 0
                for ay, ax in neighbors:
                    ny, nx = y + ay, x + ax
                    if 0 <= ny < n and 0 <= nx < m:
                        if board[ny][nx] == 1:
                            lives += 1

                if lives < 2 or lives > 3:
                    if board[y][x] == 1:
                        changes[y][x] = 1
                else:
                    if lives == 3 and board[y][x] == 0:
                        changes[y][x] = 1

        for i in range(n):
            for j in range(m):
                if changes[i][j] == 1:
                    board[i][j] = 1 if board[i][j] == 0 else 0
```

## Complexity
- Time: O(n*m)

## Notes
- Simulation
