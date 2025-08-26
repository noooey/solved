# 054. Spiral Matrix

## Code (Python)
```python3
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                spiral.append(matrix[top][i])
            top += 1

            for j in range(top, bottom + 1):
                spiral.append(matrix[j][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for j in range(bottom, top - 1, -1):
                    spiral.append(matrix[j][left])
                left += 1

        return spiral
```

## Complexity
- Time: O(n)

## Notes
- Indexing
