# 063. Unique Paths II

## Code (Python)
```python3
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for y in range(n):
            for x in range(m):
                if obstacleGrid[y][x] == 1:
                    dp[y][x] = 0
                    continue
                if y > 0:
                    dp[y][x] += dp[y - 1][x]
                if x > 0:
                    dp[y][x] += dp[y][x - 1]

        return dp[-1][-1]
```

## Complexity
- Time: O(nm)

## Notes
- DP
