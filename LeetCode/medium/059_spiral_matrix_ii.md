# 059. Spiral Matrix II

## Code (Python)
```python3
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right = 0, n - 1
        top, bottom = 0, n - 1

        output = [[0] * n for _ in range(n)]
        cur = 1
        while left <= right and top <= bottom and cur <= n * n:
            for i in range(left, right + 1):
                output[top][i] = cur
                cur += 1
            top += 1

            if not (left <= right and top <= bottom):
                break

            if top <= bottom:
                for i in range(top, bottom + 1):
                    output[i][right] = cur
                    cur += 1
                right -= 1

            if left <= right:
                for i in range(right, left - 1, -1):
                    output[bottom][i] = cur
                    cur += 1
                bottom -= 1

            if top <= bottom:
                for i in range(bottom, top - 1, -1):
                    output[i][left] = cur
                    cur += 1
                left += 1

        return output
```

## Complexity
- Time: O(n^2)

## Notes
- Indexing
