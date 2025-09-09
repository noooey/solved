# 064. Minimum Path Sum

## Code (Python)
```python3
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if j > 0 and i > 0:
                    dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])
                elif j > 0:
                    dp[i][j] += dp[i][j - 1]
                elif i > 0:
                    dp[i][j] += dp[i - 1][j]
                dp[i][j] += grid[i][j]

        return dp[-1][-1]
```

## Complexity
- Time: O(nm)

## Notes
- DP
