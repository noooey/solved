# 073. Set Matrix Zeroes

## Code (Python)
```python3
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        cols, rows = [0] * m, [0] * n
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    cols[j] = 1
                    rows[i] = 1

        for i in range(m):
            if cols[i] == 1:
                for j in range(n):
                    matrix[j][i] = 0

        for i in range(n):
            if rows[i] == 1:
                for j in range(m):
                    matrix[i][j] = 0
```

## Complexity
- Time: O(nm)

## Notes
- Indexing
